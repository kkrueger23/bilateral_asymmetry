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
