from subject import *

class DatasetSummary:
    def __init__(self,demographics_dict,rlsd_dict,rllun_dict,bwsq_dict):
        self.all_subjects = []
        for i in range(len(demographics_dict)):
            self.all_subjects.append(Subject(demographics_dict[i],rlsd_dict[i+1],rllun_dict[i+1],bwsq_dict[i+1]))
        self.subject_count = len(demographics_dict)