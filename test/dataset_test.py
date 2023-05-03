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
                                   'knee_power': 10.797213374764175}},all_data.subject_asymmetries[0])

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

    ### test all_asymmetry_dict
        self.assertEqual([6.325625679573825, 2.8478949420568327, 11.642615842126233, 5.47903979075285,
                          7.209901838628187, 5.502830108442, 18.8176926679093, 4.567848257242821,
                          3.9471720285154617, 5.884086561748891, 2.7616159280767354, 0.66725779922702,
                          4.526056169941921, 2.999609031258363, 4.431173280482407, 7.104109592262884,
                          2.933433458980635, 7.190299313421178, 17.203414300195757, 7.76904253479208,
                          2.866093854866775, 13.980152458557562, 4.685222072103335, 35.237658358941474,
                          7.76904253479208, 2.866093854866775, 13.980152458557562, 4.685222072103335,
                          35.237658358941474],all_data.all_asymmetry_dict()['rlsd']['ankle_flexion'])

    ### test get_min and get_max:
        minimums = all_data.get_min()
        maximums = all_data.get_max()
        self.assertAlmostEqual(0.279016066,minimums['rllun']['hip_flexion'])
        self.assertAlmostEqual(0.11950387,minimums['bwsq']['ankle_flexion'])
        self.assertAlmostEqual(12.86486572, maximums['rllun']['hip_flexion'])
        self.assertAlmostEqual(18.80717594, maximums['bwsq']['ankle_flexion'])

    ### test_avg_demographics:
        self.assertAlmostEqual(19.68965517,all_data.avg_demographics()["age"])
        self.assertAlmostEqual(67.48275862, all_data.avg_demographics()["height"])
        self.assertAlmostEqual(154.8275862, all_data.avg_demographics()["weight"])

    ### test_avg_asymmetry:
        self.assertAlmostEqual(6.851139147,all_data.avg_asymmetry()["bwsq"]['ankle_flexion'])
        self.assertAlmostEqual(8.65924190, all_data.avg_asymmetry()["rlsd"]['ankle_flexion'])
        self.assertAlmostEqual(10.46344258, all_data.avg_asymmetry()["rllun"]['ankle_flexion'])

    ### test_sort_asymmetry:
        sorted_bwsq = (all_data.sort_asymmetry())["bwsq"]
        self.assertEqual(('knee_adduction', 188.32422155632767),list(sorted_bwsq)[0])
        self.assertEqual(('knee_flexion', 2.7762848704084586),list(sorted_bwsq)[-1])
        self.assertEqual([('knee_adduction', 188.32422155632767),
 ('hip_adduction', 61.904685148319835),
 ('ankle_power', 41.26268186435315),
 ('knee_displacement', 31.988213045601796),
 ('hip_power', 12.347952167667426),
 ('knee_power', 10.633869175732249),
 ('foot_weight', 8.55153998791356),
 ('ankle_flexion', 6.851139147038701),
 ('hip_flexion', 3.95818318254965),
 ('knee_flexion', 2.7762848704084586)],sorted_bwsq)



