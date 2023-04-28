class Demographics:
    def __init__(self,demographic_dict):
        self.id = demographic_dict['Subject ']
        self.sex = demographic_dict['Sex']
        self.age = int(demographic_dict['Age'])
        self.height = int(demographic_dict['Ht (in)'])
        self.weight = int(demographic_dict['Wt (lbs)'])
        self.limb_dominance = demographic_dict['Dominant leg ']
        if demographic_dict["Injuries "] == '':
            self.injury = demographic_dict['Injuries ']
        else:
            self.injury = (demographic_dict['Injuries ']).split(',')
        if demographic_dict['Date of injury '] == '':
            self.injury_date = demographic_dict['Date of injury ']
        else:
            self.injury_date = (demographic_dict['Date of injury ']).split(',')