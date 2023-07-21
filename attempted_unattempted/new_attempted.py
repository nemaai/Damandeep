from Config import config_main
import json
import pandas as pd


def csv_to_2d_list(csv):
    df = pd.read_csv(csv)
    df1 = df.iloc[:, 3:7]  # extracting moduleNum	moduleName	categoryId	level  from csv
    report_table_list = df1.values.tolist()
    return report_table_list


def add_status_key_main_module(csv):
    with open(config_main.main_module_assessment_flashcard_score_location) as f:
        data = json.load(f)   # loading main module

    report_table_list = csv_to_2d_list(csv)

    for row in report_table_list:
        module_data = data['main_special'][row[0].capitalize()]
        # print(module_data,"\n\n\n")
        if row[1] == "flashcard":
            flashcard_data = module_data[2]
            cat_data = flashcard_data["categories"]
            # print(cat_data)
            for cat in cat_data:
                if cat["name"] == row[2]:
                    cat["status"] = "attempted"
            # flashcard_data["status"] = "attempted"
            # flashcard_data[]
            # print(flashcard_data)
            # print(cat_data.keys())
            # print(cat_data)
        else:
            games_data = module_data[3]
            # print(games_data)
            level_lst = ["level1", "level2", "level3"]
            cat_data = games_data["categories"]
            for cat in cat_data:
                if cat["name"] == row[1].capitalize():
                    sub_cat = cat["sub_cat"]
                    for sub in sub_cat:
                        if sub["name"] == row[2].capitalize():
                            new_dict = {}
                            for lvl in level_lst:
                                if lvl == row[3]:
                                    new_dict[lvl] = "attempted"
                                else:
                                    new_dict[lvl] = "new"
                            sub["status"] = new_dict

                            # print(cat)
    
    with open(config_main.main_module_assessment_flashcard_score_location, 'w') as fp:
        json.dump(data, fp, indent=4)   # updating main module

    return "Completed"


# a = add_status_key_main_module(r"C:\Users\kapoo\OneDrive\Desktop\attempted_reports_table (1).csv")
# print(a)
