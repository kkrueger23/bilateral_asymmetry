import pandas as pd


def export_data(subjects_object):
    final = subjects_object.final_dict_format()
    for exercise in final:
        df = pd.DataFrame.from_dict(final[exercise], orient="index")
        df.to_csv(exercise + "_data.csv")
