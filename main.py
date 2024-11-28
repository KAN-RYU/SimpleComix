from fastapi import FastAPI
import json
import os
from utils import utils

with open('config.json', encoding='utf-8') as f:
    config = json.load(f)
if not "data_folder" in config:
    data_folder = "./"
    print("Please set up data_folder configuration")
else:
    data_folder = config["data_folder"]

app = FastAPI()

@app.get("/list/{rest_of_path:path}")
def get_file_list(rest_of_path: str):
    directory = os.path.join(data_folder, rest_of_path)
    file_list = utils.sorted_alphanumeric(os.listdir(directory))
    return file_list
