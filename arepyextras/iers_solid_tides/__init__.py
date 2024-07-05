# SPDX-FileCopyrightText: Aresys S.r.l. <info@aresys.it>
# SPDX-License-Identifier: MIT

"""
IERS Solid Earth Tides package
------------------------------
"""

# import pkgutil
import platform
from pathlib import Path

from pkg_resources import resource_filename

__version__ = "1.0.2"

# Get the extension for the library, depending on which OS we're on
LIB_EXT = ".dll" if platform.system() == "Windows" else ".so"

solid_earth_tide_lib_path = resource_filename("arepyextras.iers_solid_tides.resources", "solid" + LIB_EXT)
