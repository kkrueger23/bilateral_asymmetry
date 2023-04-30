class Lunge:
    def __init__(self,rllun_dict):
        self.id = rllun_dict['Subject ']
        self.ankle_flexion = [float(rllun_dict['plantar_dorsiflexion_R_ankle']),float(rllun_dict['plantar_dorsiflexion_L_ankle'])]
        self.knee_flexion = [float(rllun_dict['flexion_R_Knee']),float(rllun_dict['flexion_L_Knee'])]
        self.knee_displacement = [float(rllun_dict['M_L_disp_R_knee']),float(rllun_dict['M_L_disp_L_knee'])]
        self.hip_flexion = [float(rllun_dict['flexion_R_hip']),float(rllun_dict['flexion_L_hip'])]
        self.hip_flexion = [float(rllun_dict['flexion_R_hip']), float(rllun_dict['flexion_L_hip'])]
        self.foot_weight = [float(rllun_dict['perc_r_wt_front_foot']),float(rllun_dict['perc_l_wt_front_foot'])]
        self.hip_power = [float(rllun_dict['perc_R_HIP_POWER']), float(rllun_dict['perc_L_HIP_POWER'])]
        self.knee_power = [float(rllun_dict['perc_R_KNEE_POWER']), float(rllun_dict['perc_L_KNEE_POWER'])]
        self.ankle_power = [float(rllun_dict['perc_R_ANKLE_POWER']), float(rllun_dict['perc_L_ANKLE_POWER'])]

    def get_rllun_pairs(self):
        """
        :return: a dictionary with all data pairs
        """