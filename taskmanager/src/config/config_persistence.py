import os
from typing import Callable

from petisco.persistence.sqlalchemy.sqlalchemy_persistence_config import (
    SqlAlchemyPersistenceConfig,
)
from petisco.persistence.sqlalchemy.sqlalchemy_persistence_connector import (
    SqlAlchemyPersistenceConnector,
)


def config_persistence(import_database_models: Callable):

    config = sql_alchemy_persistence_config_provider()

    persistence_connector = SqlAlchemyPersistenceConnector(
        config=config, import_database_models=import_database_models
    )
    persistence_connector.execute()


def sql_alchemy_persistence_config_provider():
    return SqlAlchemyPersistenceConfig(
        server=os.environ.get("SQL_SERVER"),
        database=os.environ.get("SQL_DATABASE")
        if os.environ.get("SQL_DATABASE")
        else os.environ.get("MYSQL_DATABASE"),
        driver=os.environ.get("MYSQL_DRIVER", "pymysql"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        host=os.environ.get("MYSQL_HOST"),
        port=os.environ.get("MYSQL_PORT"),
    )
