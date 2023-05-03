from initial_data.get_data import *
from dataset_summary import *
import pandas as pd


def export_data(subjects_object):
    final = subjects_object.final_dict_format()
    for exercise in final:
        df = pd.DataFrame.from_dict(final[exercise], orient="index")
        df.to_csv(exercise + "_data.csv")

def main():
    dem_dict = get_dict_data('Demographics.xlsx', 'Demographics')
    rlsd_dict = get_dict_data('rlsd.xlsx', 'rlsd_data')
    bwsq_dict = get_dict_data('bwsq.xlsx', 'bwsq_data')
    rllun_dict = get_dict_data('rllun.xlsx', 'rllun_data')

    all_data = DatasetSummary(dem_dict, rlsd_dict, rllun_dict, bwsq_dict)
    export_data(all_data)

if __name__ == "__main__":
    main()