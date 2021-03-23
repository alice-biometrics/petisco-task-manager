import os

from petisco import (
    AppServices,
    MySqlConnection,
    MySqlDatabase,
    Persistence,
    Petisco,
    Repositories,
    SqliteConnection,
    SqliteDatabase,
)

from taskmanager.src.config.app_services import app_services_provider
from taskmanager.src.config.repositories import repositories_provider

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def load(testing: bool = False):
    load_petisco()
    if testing:
        load_persistence_testing()
    else:
        load_persistence()
    load_repositories()
    load_app_services()


def load_petisco():
    petisco = Petisco.from_filename(ROOT_PATH + "/petisco.yml")
    petisco.configure_events(ROOT_PATH + "/petisco.events.yml")


def load_persistence():
    def create_admin_mysql_database():
        connection = MySqlConnection.from_environ()
        return MySqlDatabase(
            name="taskmanager",
            connection=connection,
            model_filename=ROOT_PATH + "/petisco.sql.models.yml",
        )

    persistence = Persistence()
    persistence.add(create_admin_mysql_database())
    persistence.create()


def load_persistence_testing():
    def create_admin_sqlite_database():
        return SqliteDatabase(
            name="taskmanager",
            connection=SqliteConnection.create("sqlite", "taskmanager-test.db"),
            model_filename=f"{ROOT_PATH}/petisco.sql.models.yml",
        )

    persistence = Persistence()
    persistence.add(create_admin_sqlite_database())
    persistence.create()


def load_repositories():
    Repositories.from_provider(repositories_provider)


def load_app_services():
    AppServices.from_provider(app_services_provider)
