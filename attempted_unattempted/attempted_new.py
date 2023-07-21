import json
import csv
from attempted_unattempted import add_attempted_key
from Config import config_main

def add_space_to_module_number(module_number):
    module = ''.join(filter(str.isalpha, module_number))
    number = ''.join(filter(str.isdigit, module_number))
    return f"{module} {number}"


def attempted_new_user_traversel(master_json, user_id, list_of_list):
    for row in list_of_list:
        if row[2] == user_id:
            module_num = add_space_to_module_number(row[3])
            module_title = row[4]
            category_id = row[5]
            target_level = row[6]
            master_json = attempted_new_json_traversel(master_json,module_num,module_title,category_id,target_level)
    return master_json

def attempted_new_json_traversel(master_json,module_num,module_title,category_id,target_level):

    target_module = module_title.lower() if module_title.lower() in ["flashcard", "education"] else "games"

    desired_module_items = None
    for module in master_json["main_special"]:
        if module.lower() == module_num.lower():
            desired_module_items = master_json["main_special"][module]
            if target_module== "flashcard":
               print(12)
               for element in desired_module_items[2]['categories']:
                   if element['name_title'].lower() == category_id:
                       element['attempted'] = True

            if target_module == 'education':
               for element in desired_module_items[1]['categories']:
                   if element['name_title'].lower() == category_id:
                       for level in element['levels']:
                           if level['name_title'].lower() == target_level:
                               level['attempted'] = True
                
            if target_module == "games":
                for element in desired_module_items[3]['categories']:
                    if element['name_title'].lower() == module_title:  
                        for sub_cat in element['sub_cat']:
                            if sub_cat['name_title'].lower() == category_id:
                                sub_cat['attempted'][target_level] = True
                        
    return master_json

with open(config_main.main_module_assessment_flashcard_score_location) as f:
    data = json.load(f)


with open('D:/company/NEMA AI/attempted_unattempted/attempted_reports_table.csv', 'r') as f:
    list_of_list = list(csv.reader(f))  # Read all rows and convert to list

user_id = "1422e54f-2cdb-4874-bee1-43ba591622fa"


def main(data,user_id, list_of_list):
    master_json = add_attempted_key(data)
    new_master_json = attempted_new_user_traversel(master_json, user_id, list_of_list)
    return new_master_json