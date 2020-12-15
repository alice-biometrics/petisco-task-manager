import os
import pytest

from tests.modules.fixtures import *
from petisco.fixtures import *


def test_persistence_setup():
    ROOT_PATH = (
        "/Users/acosta/Software/alice/open_source/petisco-task-manager/taskmanager"
    )
    sql_database = SqliteDatabase(
        name="taskmanager",
        connection=SqliteConnection.create("sqlite", "tasmanager.db"),
        model_filename=f"{ROOT_PATH}/petisco.sql.models.yml",
    )
    persistence = Persistence()
    persistence.add(sql_database)


if not os.environ.get("END2END_TEST"):
    from taskmanager import petisco_setup

    petisco_setup()

    test_persistence_setup()
