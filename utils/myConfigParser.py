import configparser
from pathlib import Path

cfgFile = 'pets_qa.ini'
cfgFileDir = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)

config.read(CONFIG_FILE)


def return_pet_api_url():
    return config['pet']['url']


def return_store_api_url():
    return config['store']['url']


print(return_pet_api_url())
print(return_store_api_url())