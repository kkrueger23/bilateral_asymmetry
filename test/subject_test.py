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



