import os
from dotenv import load_dotenv

load_dotenv('.env')
print("data_folder = ", os.environ.get("DATA_FOLDER"))