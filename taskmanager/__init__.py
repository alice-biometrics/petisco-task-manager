import os
from petisco import Petisco

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

def petisco_setup():
    Petisco.from_filename(ROOT_PATH + "/petisco.yml")
