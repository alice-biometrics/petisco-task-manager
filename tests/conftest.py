import os

from taskmanager.petisco_loader import load

from tests.modules.fixtures import *  # noqa
from petisco.fixtures import *  # noqa

test_db_filename = "taskmanager-test.db"
if os.path.isfile(test_db_filename):
    os.remove(test_db_filename)

load(testing=True)
