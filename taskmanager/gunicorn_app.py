from taskmanager import petisco_setup, persistence_setup
from petisco import Petisco

petisco_setup()
persistence_setup()
app = Petisco.get_instance().get_app()
