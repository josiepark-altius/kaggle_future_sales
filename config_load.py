import os
from dotenv import load_dotenv
import json

def load_environment():
    '''
    Function that defines the names of configuration and data files

    Returns:
        environment_dict (dictionary) : 
    '''

    # load environment variables
    
    data_folder = os.environ.get("DATA_FOLDER")
    config_folder = os.environ.get("MODEL_CONFIG_FOLDER")

    # define environment dictionary

    environment_dict = {
        "TRAIN_FILE" : os.path.join(data_folder, "sales_train.csv"),
        "TEST_FILE" : os.path.join(data_folder, "test.csv"),
        "ITEM_CATS_FILE" : os.path.join(data_folder, "item_categories.csv"),
        "ITEMS_FILE" : os.path.join(data_folder, "items.csv"),
        "SHOPS_FILE" : os.path.join(data_folder, "shops.csv"),
        "SUBMISSION_FILE" : os.path.join(data_folder, "submission.csv"),
        "CONFIG_FILE" : os.path.join(config_folder, "dev.yaml"),
        "MODEL_CONFIG_FILE" : os.path.join(config_folder, "model_config.json"),
        "GROUPED_TRAIN_FILE" : os.path.join(data_folder, "grouped_train.csv"),
        "PREPROCESSED_TRAIN_FILE" : os.path.join(data_folder, "preprocessed_train.csv")
    }

    return environment_dict

def load_model_config():

    with open(env['MODEL_CONFIG_FILE']) as json_file:
        model_config = json.load(json_file)
    
    return model_config

load_dotenv('.env')
env = load_environment()
config = load_model_config()