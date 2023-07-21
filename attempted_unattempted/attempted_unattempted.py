import json
from Config import config_main

def add_attempted_key(data):
    main_special = data.get("main_special", {})
    for module_list in main_special.values():
        print(module_list)
        for module in module_list:
            module_title = module.get("module_title", "")

            if module_title == "Games":
                categories = module.get("categories", [])
                for category in categories:
                    sub_categories = category.get("sub_cat", [])
                    for sub_category in sub_categories:
                        sub_category['attempted'] = {'level1':False,
                                                     'level2' : False,
                                                     'level3' : False}
            if module_title == "Flashcard":
                categories = module.get("categories", [])
                for category in categories:
                    category['attempted'] = False

            if module_title == "Education":
                categories = module.get("categories", [])
                for category in categories:
                    # category['attempted'] = False
                    levels = category.get("levels", [])
                    for level in levels:
                        level['attempted'] = False
    return data
    
# with open(config_main.main_module_assessment_flashcard_score_location) as f:
#     data = json.load(f)

# new_data = add_attempted_key(data)

# with open('D:/company/NEMA AI/attempted_unattempted/master.json', 'w') as file:
#     json.dump(new_data, file, indent=4)
