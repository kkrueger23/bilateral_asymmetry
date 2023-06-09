class StepDown:
    def __init__(self, rlsd_dict):
        self.id = rlsd_dict['subject']
        self.ankle_flexion = [float(rlsd_dict['plantar_dorsiflexion_R_ankle']), float(rlsd_dict['plantar_dorsiflexion_L_ankle'])]
        self.knee_flexion = [float(rlsd_dict['flexion_R_Knee']),float(rlsd_dict['flexion_L_Knee'])]
        self.knee_displacement = [float(rlsd_dict['M_L_disp_R_knee']),float(rlsd_dict['M_L_disp_L_knee'])]
        self.hip_flexion = [float(rlsd_dict['flexion_R_hip']),float(rlsd_dict['flexion_L_hip'])]
        self.hip_power = [float(rlsd_dict['perc_R_HIP_POWER']), float(rlsd_dict['perc_L_HIP_POWER'])]
        self.knee_power = [float(rlsd_dict['perc_R_KNEE_POWER']), float(rlsd_dict['perc_L_KNEE_POWER'])]
        self.ankle_power = [float(rlsd_dict['perc_R_ANKLE_POWER']), float(rlsd_dict['perc_L_ANKLE_POWER'])]

    def get_rlsd_pairs(self):
        """
        :return: a dictionary with all data pairs
        """
        return {"ankle_flexion": self.ankle_flexion,"knee_flexion" : self.knee_flexion, "knee_displacement": self.knee_displacement,
                          "hip_flexion": self.hip_flexion, "ankle_power":self.ankle_power,
                          "knee_power": self.knee_power, "hip_power": self.hip_power}