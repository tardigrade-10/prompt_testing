import os
import yaml
from pathlib import Path


CONFIG_FILE = "config.yaml"
ROOT_DIR = os.path.dirname(Path(__file__).parent.parent)
config_path = ROOT_DIR + "/" + CONFIG_FILE

if os.path.exists(config_path):
    with open(config_path, "r") as file:
        config_data = yaml.safe_load(file)

else:
    config_data = {'OPENAI_API_KEY': ""}
    config_data['OPENAI_API_KEY'] = input("Enter OPENAI_API_KEY:")


class Config:
    OPENAI_API_KEY = config_data["OPENAI_API_KEY"]