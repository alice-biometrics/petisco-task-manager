import os
from petisco import Petisco

def petisco_setup():
    Petisco.from_filename(os.path.dirname(os.path.abspath(__file__)) + "/petisco.yml")
