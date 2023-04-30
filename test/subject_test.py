import unittest
from initial_data.get_data import *
from subject import *

class TestInitialData(unittest.TestCase):
    def test_subject(self):
        dem_dict = get_dict_data('Demographics.xlsx', 'Demographics')
        rlsd_dict = get_dict_data('rlsd.xlsx', 'rlsd_data')
        bwsq_dict = get_dict_data('bwsq.xlsx', 'bwsq_data')
        rllun_dict = get_dict_data('rllun.xlsx', 'rllun_data')
        subject1 = Subject(dem_dict[0],rlsd_dict[1],rllun_dict[1],bwsq_dict[1])

        self.assertEqual('74', subject1.id)
        self.assertEqual('74',subject1.rlsd.id)
        self.assertEqual('74', subject1.rllun.id)
        self.assertEqual('74', subject1.bwsq.id)
        # Could do more tests, but it would be reiterating what's already been done

    def test_percent_asymmetry(self):
        self.assertEqual(120,percent_asymmetry(8,2))
        self.assertEqual(-120,percent_asymmetry(2,8))
        self.assertEqual(ValueError,percent_asymmetry(0,0))
        self.assertEqual(0,percent_asymmetry(1,1))

    def test_percent_bilat_asymmetry(self):
        self.assertEqual(300,percent_bilat_asymmetry(8,2))
        self.assertEqual(300,percent_bilat_asymmetry(2,8))
        self.assertEqual(ValueError,percent_bilat_asymmetry(0,0))
        self.assertEqual(0,percent_bilat_asymmetry(1,1))

    def test_percent_gait_asymmetry1(self):
        self.assertEqual(75,percent_gait_asymmetry1(8,2))
        self.assertEqual(75,percent_gait_asymmetry1(2,8))
        self.assertEqual(ValueError,percent_gait_asymmetry1(0,0))
        self.assertEqual(0,percent_gait_asymmetry1(1,1))

    def test_percent_gait_asymmetry1(self):
        self.assertEqual(30,percent_gait_asymmetry2(8,2))
        self.assertEqual(30,percent_gait_asymmetry2(2,8))
        self.assertEqual(ValueError,percent_gait_asymmetry2(0,0))
        self.assertEqual(0,percent_gait_asymmetry2(1,1))