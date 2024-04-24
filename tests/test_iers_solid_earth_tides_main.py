# SPDX-FileCopyrightText: Aresys S.r.l. <info@aresys.it>
# SPDX-License-Identifier: MIT

"""Unittest for solid core functionalities"""

import datetime
import unittest

import numpy as np

from arepyextras.iers_solid_tides.wrapper.main import solid_earth_tides_core


class IERSSolidTidesTest(unittest.TestCase):
    """Testing iers_solid_tides core functionalities"""

    def setUp(self) -> None:
        # creating test data
        self.date = datetime.date(2021, 7, 5)
        self.lat_lon = (60, -32)

        # benchmarking values
        self.results = {
            "time": np.arange(0, 1441 * 60, 60),
            "north_first_10": np.array(
                [
                    -0.015825623193191092,
                    -0.015776041510506926,
                    -0.015725788756351514,
                    -0.015674868196914382,
                    -0.01562328316260679,
                    -0.015571037047455057,
                    -0.015518133308917409,
                    -0.015464575467705063,
                    -0.015410367107603677,
                    -0.015355511874798028,
                    -0.015300013478574508,
                ]
            ),
            "north_last_10": np.array(
                [
                    -0.01443196952059516,
                    -0.014427569594715035,
                    -0.014422307425932084,
                    -0.014416182630802687,
                    -0.014409194905818552,
                    -0.014401344027576646,
                    -0.014392629852808987,
                    -0.014383052318342512,
                    -0.014372611440315146,
                    -0.01436130731786553,
                ]
            ),
            "east_first_10": np.array(
                [
                    -0.006357325485034922,
                    -0.006372752295016878,
                    -0.00638771254767662,
                    -0.006402199054716194,
                    -0.006416204658214084,
                    -0.0064297222316781494,
                    -0.006442744680424984,
                    -0.006455264942339754,
                    -0.006467275988292951,
                    -0.00647877082321224,
                    -0.006489742484327297,
                ]
            ),
            "east_last_10": np.array(
                [
                    -0.002393388238819648,
                    -0.002421954240802441,
                    -0.0024505107760917876,
                    -0.0024790486791140924,
                    -0.002507558779122499,
                    -0.002536031901671232,
                    -0.0025644588684377093,
                    -0.0025928304989919077,
                    -0.002621137609309824,
                    -0.002649371019312525,
                ]
            ),
            "up_first_10": np.array(
                [
                    -0.11601492659493721,
                    -0.11608524317436182,
                    -0.11615598508277784,
                    -0.11622714587109889,
                    -0.11629871897764008,
                    -0.11637069773093842,
                    -0.11644307534905124,
                    -0.11651584494044266,
                    -0.11658899950329762,
                    -0.11666253192832363,
                    -0.11673643499779585,
                ]
            ),
            "up_last_10": np.array(
                [
                    -0.11936205377437703,
                    -0.1193710318799089,
                    -0.1193806438813301,
                    -0.1193908901419048,
                    -0.1194017708834717,
                    -0.11941328618811609,
                    -0.11942543599674635,
                    -0.11943822010892563,
                    -0.11945163818567663,
                    -0.11946568974162648,
                ]
            ),
        }

    def test_solid_earth_tides_core(self):
        """Testing solid earth tides core function"""
        out_df = solid_earth_tides_core(
            year=self.date.year,
            month=self.date.month,
            day_of_month=self.date.day,
            lat_deg=self.lat_lon[0],
            lon_deg=self.lat_lon[1],
        )

        # comparing data to benchmark
        TOLERANCE = 1e-12
        # time array
        np.testing.assert_array_almost_equal(self.results["time"], out_df["time_s"].to_numpy(), TOLERANCE)

        # first 10 data of each displacement
        np.testing.assert_array_almost_equal(self.results["north_first_10"], out_df["north"].to_numpy()[:11], TOLERANCE)
        np.testing.assert_array_almost_equal(self.results["east_first_10"], out_df["east"].to_numpy()[:11], TOLERANCE)
        np.testing.assert_array_almost_equal(self.results["up_first_10"], out_df["up"].to_numpy()[:11], TOLERANCE)

        # last 10 data of each displacement
        np.testing.assert_array_almost_equal(self.results["north_last_10"], out_df["north"].to_numpy()[-10:], TOLERANCE)
        np.testing.assert_array_almost_equal(self.results["east_last_10"], out_df["east"].to_numpy()[-10:], TOLERANCE)
        np.testing.assert_array_almost_equal(self.results["up_last_10"], out_df["up"].to_numpy()[-10:], TOLERANCE)


if __name__ == "__main__":
    unittest.main()
