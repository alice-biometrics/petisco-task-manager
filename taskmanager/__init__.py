import os
from petisco import Petisco, Persistence, SqliteDatabase, SqliteConnection

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def create_sql_database():
    # sql_database = MySqlDatabase(name="taskmanager", connection=MySqlConnection.create_local(), model_filename=f"{ROOT_PATH}/petisco.sql.models.yml")
    sql_database = SqliteDatabase(
        name="taskmanager",
        connection=SqliteConnection.create("sqlite", "tasmanager.db"),
        model_filename=f"{ROOT_PATH}/petisco.sql.models.yml",
    )
    return sql_database


def petisco_setup():
    petisco = Petisco.from_filename(f"{ROOT_PATH}/petisco.yml")
    petisco.configure_events(f"{ROOT_PATH}/petisco.events.yml")


def persistence_setup():
    persistence = Persistence()
    database = create_sql_database()
    persistence.add(database)
    persistence.create()
