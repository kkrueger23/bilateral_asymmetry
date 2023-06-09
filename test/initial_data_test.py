import unittest
from initial_data.get_data import *
from initial_data.demographics import Demographics
from initial_data.rlsd import StepDown
from initial_data.bwsq import Squat
from initial_data.rllun import Lunge

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
        self.assertEqual([31.80302, 33.81476], subject_object.ankle_flexion)
        self.assertEqual([74.38065, 78.46692], subject_object.knee_flexion)
        self.assertEqual([0.05599, 0.05317], subject_object.knee_displacement)
        self.assertEqual([69.10696, 60.16306], subject_object.hip_flexion)
        self.assertEqual([10.31173960310218, 18.047827590237784], subject_object.ankle_power)
        self.assertEqual([45.03117354457981, 49.893285437348446], subject_object.knee_power)
        self.assertEqual([44.65708685231801, 32.058886972413774], subject_object.hip_power)

        self.assertEqual({"ankle_flexion": [31.80302, 33.81476],"knee_flexion" : [74.38065, 78.46692], "knee_displacement": [0.05599, 0.05317],
                          "hip_flexion": [69.10696, 60.16306], "ankle_power":[10.31173960310218, 18.047827590237784],
                          "knee_power": [45.03117354457981, 49.893285437348446], "hip_power": [44.65708685231801, 32.058886972413774]},
                         subject_object.get_rlsd_pairs())

    def test_bwsq(self):
        bwsq_dict = get_dict_data('bwsq.xlsx', 'bwsq_data')
        subject1 = bwsq_dict[1]
        subject_object = Squat(subject1)

        # test class using first subject
        self.assertEqual(-57.96778,subject_object.rotational_pelvic_tilt)
        self.assertEqual([25.69942, 23.20493], subject_object.ankle_flexion)
        self.assertEqual([80.75887, 83.69199], subject_object.knee_flexion)
        self.assertEqual([14.16273, 5.89156],subject_object.knee_adduction)
        self.assertEqual([-0.01337, -0.01413], subject_object.knee_displacement)
        self.assertEqual([74.21773, 81.18118], subject_object.hip_flexion)
        self.assertEqual([3.09391, -14.0808],subject_object.hip_adduction)
        self.assertEqual([398.67337, 312.75476],subject_object.foot_weight)
        self.assertEqual([8.964519330372989, 3.529233537272964], subject_object.ankle_power)
        self.assertEqual([48.60714940452276, 42.54304517372706], subject_object.knee_power)
        self.assertEqual([42.42833126510425, 53.92772128899996], subject_object.hip_power)

        self.assertEqual({"ankle_flexion": [25.69942, 23.20493], "knee_flexion": [80.75887, 83.69199], "knee_adduction": [14.16273, 5.89156],
                          "knee_displacement": [-0.01337, -0.01413], "hip_flexion": [74.21773, 81.18118], "hip_adduction": [3.09391, -14.0808],
                          "foot_weight": [398.67337, 312.75476], "ankle_power": [8.964519330372989, 3.529233537272964],
                          "knee_power": [48.60714940452276, 42.54304517372706], "hip_power": [42.42833126510425, 53.92772128899996]},
                         subject_object.get_bwsq_pairs())

    def test_rllun(self):
        rllun_dict = get_dict_data('rllun.xlsx', 'rllun_data')
        subject1 = rllun_dict[1]
        subject_object = Lunge(subject1)

        # test class using first subject
        self.assertEqual([26.65927, 25.8274], subject_object.ankle_flexion)
        self.assertEqual([103.05579, 104.97586], subject_object.knee_flexion)
        self.assertEqual([0.04431, 0.04441], subject_object.knee_displacement)
        self.assertEqual([82.87424, 79.07224], subject_object.hip_flexion)
        self.assertEqual([17.69417799951346, 27.024233000782523], subject_object.ankle_power)
        self.assertEqual([48.146637527229124, 47.745653464403375], subject_object.knee_power)
        self.assertEqual([34.15918447325741, 25.23011353481411], subject_object.hip_power)
        self.assertEqual([48.067803737682645, 43.43463214407068], subject_object.foot_weight)

        self.assertEqual({"ankle_flexion": [26.65927, 25.8274],"knee_flexion":[103.05579, 104.97586], "knee_displacement": [0.04431, 0.04441],
                          "hip_flexion":[82.87424, 79.07224], "ankle_power":[17.69417799951346, 27.024233000782523],
                          "knee_power":[48.146637527229124, 47.745653464403375], "hip_power":[34.15918447325741, 25.23011353481411],
                          "foot_weight":[48.067803737682645, 43.43463214407068]},subject_object.get_rllun_pairs())
