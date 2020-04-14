import os
import pytest

from tests.modules.fixtures import *
from sqlalchemy import create_engine
from petisco import SqlAlchemyPersistence, Petisco
from taskmanager import petisco_setup

petisco_setup()
app = Petisco.get_instance().get_app()


@pytest.fixture
def client():
    with app.app.test_client() as c:
        yield c


@pytest.fixture
def database():

    connection = "sqlite:///petisco.db"
    engine = create_engine(connection)

    Base = SqlAlchemyPersistence.get_instance().base
    Session = SqlAlchemyPersistence.get_instance().session

    Base.metadata.create_all(engine)

    yield

    session = Session()
    session.rollback()
    session.close()
    Base.metadata.drop_all(bind=engine)
    os.remove("taskmanager.db")
