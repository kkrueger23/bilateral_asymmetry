import unittest
from get_data import *
from demographics import Demographics

class TestDemographics(unittest.TestCase):
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
