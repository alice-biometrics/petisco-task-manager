from petisco import Petisco

from taskmanager.petisco_loader import load

load()

app = Petisco.get_instance().get_app()
