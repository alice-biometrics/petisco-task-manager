from petisco.persistence.persistence import Persistence
from sqlalchemy import Column, Integer


Base = Persistence.get_base("taskmanager")


class TasksCountModel(Base):
    __tablename__ = "TasksCount"

    count = Column("count", Integer, primary_key=True)
