from initial_data.bwsq import *
from initial_data.demographics import *
from initial_data.rllun import *
from initial_data.rlsd import *

class Subject:
    def __init__(self,demographics_dict,rlsd_dict,rllun_dict,bwsq_dict):
        self.id = demographics_dict['Subject ']
        self.demographics = Demographics(demographics_dict)
        self.rlsd = StepDown(rlsd_dict)
        self.rllun = Lunge(rllun_dict)
        self.bwsq = Squat(bwsq_dict)




