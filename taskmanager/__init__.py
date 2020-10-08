import os
from petisco import Petisco

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def petisco_setup():
    petisco = Petisco.from_filename(ROOT_PATH + "/petisco.yml")
    petisco.configure_events(ROOT_PATH + "/petisco.events.yml")
