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

        self.assertEqual({"rlsd":{"ankle_flexion": [31.80302, 33.81476],"knee_flexion" : [74.38065, 78.46692],
                                  "knee_displacement": [0.05599, 0.05317],"hip_flexion": [69.10696, 60.16306],
                                  "ankle_power":[10.31173960310218, 18.047827590237784],"knee_power": [45.03117354457981, 49.893285437348446],
                                  "hip_power": [44.65708685231801, 32.058886972413774]},
                          "bwsq": {"ankle_flexion": [25.69942, 23.20493], "knee_flexion": [80.75887, 83.69199],
                                   "knee_adduction": [14.16273, 5.89156], "knee_displacement": [-0.01337, -0.01413],
                                   "hip_flexion": [74.21773, 81.18118], "hip_adduction": [3.09391, -14.0808],
                                   "foot_weight": [398.67337, 312.75476], "ankle_power": [8.964519330372989, 3.529233537272964],
                                   "knee_power": [48.60714940452276, 42.54304517372706],
                                   "hip_power": [42.42833126510425, 53.92772128899996]},
                          "rllun": {"ankle_flexion": [26.65927, 25.8274],"knee_flexion":[103.05579, 104.97586],
                                   "knee_displacement": [0.04431, 0.04441],"hip_flexion":[82.87424, 79.07224],
                                   "ankle_power":[17.69417799951346, 27.024233000782523],"knee_power":[48.146637527229124, 47.745653464403375],
                                   "hip_power":[34.15918447325741, 25.23011353481411],
                                   "foot_weight":[48.067803737682645, 43.43463214407068]}}, subject1.get_asymmetry_pairs())

        self.assertEqual({"rlsd":{"ankle_flexion": 0,"knee_flexion" : 0,
                                  "knee_displacement": 0,"hip_flexion": 0,
                                  "ankle_power":0,"knee_power": 0,
                                  "hip_power": 0},
                          "bwsq": {"ankle_flexion": 0, "knee_flexion": 0,
                                   "knee_adduction": 0, "knee_displacement": 0,
                                   "hip_flexion": 0, "hip_adduction": 0,
                                   "foot_weight": 0, "ankle_power": 0,
                                   "knee_power": 0,
                                   "hip_power": 0},
                          "rllun": {"ankle_flexion": 0,"knee_flexion":0,
                                   "knee_displacement": 0,"hip_flexion":0,
                                   "ankle_power":0,"knee_power":0,
                                   "hip_power":0,
                                   "foot_weight":0}},subject1.calculate_asymmetry(percent_bilat_asymmetry))

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

