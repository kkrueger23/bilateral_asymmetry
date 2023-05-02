import unittest
from initial_data.get_data import *
from dataset_summary import *

class TestInitialData(unittest.TestCase):
    def test_subject(self):
        dem_dict = get_dict_data('Demographics.xlsx', 'Demographics')
        rlsd_dict = get_dict_data('rlsd.xlsx', 'rlsd_data')
        bwsq_dict = get_dict_data('bwsq.xlsx', 'bwsq_data')
        rllun_dict = get_dict_data('rllun.xlsx', 'rllun_data')

        all_data = DatasetSummary(dem_dict,rlsd_dict,rllun_dict,bwsq_dict)
        self.assertEqual(29,all_data.subject_count)
        id_list = []
        for subject in all_data.all_subjects:
            id_list.append(subject.id)
        self.assertEqual(['74','75','76','80','81','82','83','86','87','88','89','90','91','92','93','94','95','96','97'
                             ,'98','99','100','101','102','104','105','106','107','108'], id_list)
        self.assertEqual({'bwsq': {'ankle_flexion': 10.749827730572765, 'ankle_power': 154.00754117563628,
                                   'foot_weight': 27.471559505601135,'hip_adduction': -121.9725441736265, 'hip_flexion': 9.382461576229822,
                                   'hip_power': 27.103092865105303,'knee_adduction': 140.39015133513024,
                                   'knee_displacement': -5.378627034677992,'knee_flexion': 3.6319477971893397,
                                   'knee_power': 14.2540436539805},
                          'rllun': {'ankle_flexion': 3.2208816992806035,'ankle_power': 52.72951928891872,
                                    'foot_weight': 10.666998579023174,'hip_flexion': 4.808261407543289,
                                    'hip_power': 35.39053015406532,'knee_displacement': 0.22568269013765724,
                                    'knee_flexion': 1.8631364622987174,'knee_power': 0.8398336471082162},
                          'rlsd': {'ankle_flexion': 6.325625679573825,'ankle_power': 75.02214257629508,
                                   'hip_flexion': 14.866098898560013, 'hip_power': 39.29705947291561,
                                   'knee_displacement': 5.303742712055663,'knee_flexion': 5.493727199211083,
                                   'knee_power': 10.797213374764175}},all_data.all_asymmetries[0])

    ### tests for find subject
        self.assertEqual(list(all_data.all_subjects)[0],all_data.find_subject('74'))
        self.assertEqual(ValueError, all_data.find_subject(74))
        self.assertEqual(None, all_data.find_subject('0'))

    ### test sort by sex and count
        male_list,female_list = all_data.sort_by_sex()
        self.assertEqual(list(all_data.all_subjects)[0],male_list[0])
        self.assertEqual(list(all_data.all_subjects)[1],female_list[0])
        self.assertEqual(len(male_list),all_data.count_by_sex()[0])
        self.assertEqual(len(female_list),all_data.count_by_sex()[1])

    ### test get_min and get_max:
        minimums = all_data.get_min()
        maximums = all_data.get_max()
        self.assertEqual(0.279016066,minimums.rllun.hip_flexion)
        self.assertEqual(0.11950387,minimums.bwsq.ankle_flexion)
        self.assertEqual(12.86486572, maximums.rllun.hip_flexion)
        self.assertEqual(18.80717594, maximums.bwsq.ankle_flexion)

    def test_avg_demographics(self):
        self.assertEqual(19.69,all_data.avg_demographics["age"])
        self.assertEqual(67.48275862, all_data.avg_demographics["height"])
        self.assertEqual(154.8275862, all_data.avg_demographics["weight"])

    def test_avg_asymmetry(self):
        self.assertEqual(6.851139147,all_data.avg_asymmetry["bwsq"]['ankle_flexion'])
        self.assertEqual(8.43167543, all_data.avg_asymmetry["rlsd"]['ankle_flexion'])
        self.assertEqual(10.46344258, all_data.avg_asymmetry["rllun"]['ankle_flexion'])

    def test_sort_asymmetry(self):
        sorted_bwsq = (all_data.sort_asymmetry())["bwsq"]
        self.assertEqual('percent_ankle_power',list(sorted_bwsq)[0])
        self.assertEqual('knee_flexion',list(sorted_bwsq)[-1])
        self.assertEqual({},sorted_bwsq)'''



