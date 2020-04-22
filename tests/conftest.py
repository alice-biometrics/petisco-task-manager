import os
import pytest

from tests.modules.fixtures import *
from petisco.fixtures import *

if not os.environ.get("END2END_TEST"):
    from taskmanager import petisco_setup

    petisco_setup()
