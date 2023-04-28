import unittest
from get_data import *
from demographics import Demographics
from rlsd import StepDown

class TestInitialData(unittest.TestCase):
    def test_demographic(self):
        dem_dict = get_dict_data('Demographics.xlsx','Demographics')
        subject1 = dem_dict[0]
        subject_object = Demographics(subject1)

        # test class using first subject
        self.assertEqual('74', subject_object.id)
        self.assertEqual(21, subject_object.age)
        self.assertEqual('M',subject_object.sex)
        self.assertEqual(69,subject_object.height)
        self.assertEqual(150,subject_object.weight)
        self.assertEqual('Lt',subject_object.limb_dominance)
        self.assertEqual('',subject_object.injury)
        self.assertEqual('',subject_object.injury_date)

        subject2 = dem_dict[31]
        subject2_object = Demographics(subject2)
        self.assertEqual(['Stress facture',' avulsion fracture'], subject2_object.injury)
        self.assertEqual(['2021 (3mo)',' 2021 (5mo)'], subject2_object.injury_date)

    def test_rlsd(self):
        rlsd_dict = get_dict_data('rlsd.xlsx', 'rlsd_data')
        subject1 = rlsd_dict[1]
        subject_object = StepDown(subject1)

        # test class using first subject
        self.assertEqual((31.80302, 33.81476), subject_object.ankle_flexion)
        self.assertEqual((74.38065, 78.46692), subject_object.knee_flexion)
        self.assertEqual((0.05599, 0.05317), subject_object.knee_displacement)
        self.assertEqual((69.10696, 60.16306), subject_object.hip_flexion)
        self.assertEqual((10.31173960310218, 18.047827590237784), subject_object.ankle_power)
        self.assertEqual((45.03117354457981, 49.893285437348446), subject_object.knee_power)
        self.assertEqual((44.65708685231801, 32.058886972413774), subject_object.hip_power)