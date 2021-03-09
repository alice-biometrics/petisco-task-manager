import os
import pytest

from tests.modules.fixtures import *
from petisco.fixtures import *
from petisco.persistence.sql.sqlite.sqlite_connection import SqliteConnection
from petisco.persistence.sql.sqlite.sqlite_database import SqliteDatabase

ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def test_persistence_setup():
    sql_database = SqliteDatabase(
        name="taskmanager",
        connection=SqliteConnection.create("sqlite", "tasmanager.db"),
        model_filename=f"{ROOT_PATH}/taskmanager/petisco.sql.models.yml",
    )
    persistence = Persistence()
    persistence.add(sql_database)


if not os.environ.get("END2END_TEST"):
    from taskmanager import petisco_setup

    petisco_setup()

    test_persistence_setup()
