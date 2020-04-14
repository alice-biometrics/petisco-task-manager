from petisco.persistence.sqlalchemy.sqlalchemy_persistence import SqlAlchemyPersistence
from sqlalchemy import Column, Integer, String, DateTime

Base = SqlAlchemyPersistence.get_instance().base


class TaskModel(Base):

    __tablename__ = "Task"

    id = Column("id", Integer, primary_key=True)
    task_id = Column("task_id", String(16))
    title = Column("title", String(40))
    description = Column("description", String(200))
    created_at = Column("created_at", DateTime)
