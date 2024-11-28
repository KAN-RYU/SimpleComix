from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
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

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/list/{rest_of_path:path}")
def get_file_list(rest_of_path: str):
    directory = os.path.join(data_folder, rest_of_path)
    if os.path.isfile(directory):
        raise HTTPException(status_code=404, detail="It is not directory")
    file_list = []
    directory_list = []
    for thing in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, thing)):
            file_list.append(thing)
        else:
            directory_list.append(thing)
    file_list = utils.sorted_alphanumeric(file_list)
    directory_list = utils.sorted_alphanumeric(directory_list)
    return {"file_list" : file_list, "directory_list" : directory_list}

@app.get("/file/{rest_of_path:path}")
def get_file(rest_of_path: str):
    directory = os.path.join(data_folder, rest_of_path)
    file_name = os.path.basename(directory)
    if not os.path.isfile(directory):
        raise HTTPException(status_code=404, detail="file not found")
    return FileResponse(path=directory, filename=file_name)