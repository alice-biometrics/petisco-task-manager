from taskmanager import petisco_setup
from petisco import Petisco

petisco_setup()
app = Petisco.get_instance().get_app()
