# SPDX-FileCopyrightText: Aresys S.r.l. <info@aresys.it>
# SPDX-License-Identifier: MIT

"""Solid Earth Tides estimator precompiled libraries wrapper"""

import ctypes as ct
import datetime

import numpy as np
import pandas as pd

from arepyextras.iers_solid_tides import solid_earth_tide_lib_path

MINUTES_IN_DAY = 24 * 60


def load_solid_library(windows_mode: hex = 0x00000010) -> ct._CFuncPtr:
    """Loading and setup solid main function from the solid pre-compiled library.

    Parameters
    ----------
    windows_mode : hex, optional
        windows mode to load dll, ignored on Linux, by default 0x00000010
        to properly load this library in windows (.dll), the winmode should be 0x00000010 or 0x00000008
        these two values corresponds to the windows api .dll LoadLibraryExA function (libloaderapi.h) modes
        LOAD_IGNORE_CODE_AUTHZ_LEVEL and LOAD_WITH_ALTERED_SEARCH_PATH
        see: https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexa

    Returns
    -------
    ct._CFuncPtr
        solid core function already set up
    """

    # loading custom precompiled library
    custom_lib = ct.CDLL(str(solid_earth_tide_lib_path), winmode=windows_mode)
    solid_core = custom_lib.solid

    # defining function input/output types
    solid_core.argtypes = [
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_int),
        ct.POINTER(ct.c_int),
        ct.POINTER(ct.c_int),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
    ]
    solid_core.restype = None

    return solid_core


def solid_earth_tides_core(year: int, month: int, day_of_month: int, lat_deg: float, lon_deg: float) -> pd.DataFrame:
    """Solid Earth Tides pre-compiled .dll/.so wrapper of original Fortran code. This function uses the C-compiled
    library to extract solid earth tides displacements.

    Earth tides are estimated using an external tool (executable) called Solid, based on a fortran script, wrapped in
    arepyextras iers solid tides.

    Solid Earth Tide (SET) displacement estimator class based on Solid fortran executable by Dennis Milbert.

    Program Solid is based on an edited version of the dehanttideinelMJD.f source code provided by Professor V. Dehant.
    This code is an implementation of the Solid Earth Tide computation found in section 7.1.2 of the
    IERS Conventions (2003) , IERS Technical Note No. 32

    Program inputs: date (year, month of the year, day of the month), latitude (deg), longitude (deg).
    Program output: .txt file with solid earth tide (body tide) components [north, east, up] for each minute of the
    input date.

    Solid is driven by a pair of routines that compute low-precision geocentric coordinates for the Moon and the Sun.
    These routines were coded from the equations in "Satellite Orbits: Models, Methods, Applications" by
    Montenbruck & Gill (2000), section 3.3.2, pp.70-73

    Solid does not contain ocean loading, atmospheric loading, or deformation due to polar motion.

    Ref: 'http://geodesyworld.github.io/SOFTS/solid.htm'

    Parameters
    ----------
    year : int
        year of the date at which the displacement must be estimated, between 1901 and 2099
    month : int
        month of the date at which the displacement must be estimated, between 1 and 12
    day_of_month : int
        day of the month of the date at which the displacement must be estimated, between 1 and 31
    lat_deg : float
        latitude where the displacement should be evaluated, in deg
    lon_deg : float
        longitude where the displacement should be evaluated, in deg

    Returns
    -------
    pd.DataFrame
        pandas dataframe containing the data returned by the solid earth tides estimator

    Raises
    ------
    ValueError
        if the input date is not valid
    """

    # loading library
    solid_core = load_solid_library()

    # check year, month and day validity
    assert isinstance(year, int), f"year {year} is not of type int"
    assert 1900 < year < 2100, f"year {year} exceeds boundaries [1901-2099]"
    assert isinstance(month, int), f"month {month} is not of type int"
    assert 1 <= month <= 12, f"{month} is not a valid month"
    assert isinstance(day_of_month, int), f"day {day_of_month} is not of type int"
    assert 1 <= day_of_month <= 31, f"{day_of_month} is not a valid day of the month"

    # check datetime validity
    try:
        datetime.datetime(year=year, month=month, day=day_of_month)
    except Exception as err:
        raise ValueError(f"{year}-{month}-{day_of_month} [yy-mm-dd] is not a valid date") from err

    # check validity of latitude and longitude
    assert -90 <= lat_deg <= 90
    assert -360 <= lon_deg <= 360

    # instantiating output arrays
    time_array = np.empty(MINUTES_IN_DAY + 1, dtype="double")
    north_array = np.empty_like(time_array)
    east_array = np.empty_like(time_array)
    up_array = np.empty_like(time_array)

    # converting inputs to c types
    lat_c = ct.c_double(lat_deg)
    lon_c = ct.c_double(lon_deg)
    year_c = ct.c_int(year)
    month_c = ct.c_int(month)
    day_c = ct.c_int(day_of_month)

    # calling function from dll
    solid_core(
        ct.pointer(lat_c),
        ct.pointer(lon_c),
        ct.pointer(year_c),
        ct.pointer(month_c),
        ct.pointer(day_c),
        time_array.ctypes.data_as(ct.POINTER(ct.c_double)),
        north_array.ctypes.data_as(ct.POINTER(ct.c_double)),
        east_array.ctypes.data_as(ct.POINTER(ct.c_double)),
        up_array.ctypes.data_as(ct.POINTER(ct.c_double)),
    )

    # composing output dataframe
    df_out = pd.DataFrame(
        np.vstack([time_array, north_array, east_array, up_array]).T, columns=["time_s", "north", "east", "up"]
    )

    return df_out
