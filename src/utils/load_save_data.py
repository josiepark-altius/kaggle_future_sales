import pandas as pd
import os

def load_environment():
    
    data_folder = os.environ.get("DATA_FOLDER")
    config_folder = os.environ.get("MODEL_CONFIG_FOLDER")

    environment_dict = {
        "TRAIN_FILE" : os.path.join(data_folder, "sales_train.csv"),
        "TEST_FILE" : os.path.join(data_folder, "test.csv"),
        "ITEM_CATS_FILE" : os.path.join(data_folder, "item_categories.csv"),
        "ITEMS_FILE" : os.path.join(data_folder, "items.csv"),
        "SHOPS_FILE" : os.path.join(data_folder, "shops.csv"),
        "SUBMISSION_FILE" : os.path.join(data_folder, "submission.csv"),
        "CONFIG_FILE" : os.path.join(config_folder, "dev.yaml")
    }

    return environment_dict

def load_static_files():

    static_files = {}
    env = load_environment()

    return