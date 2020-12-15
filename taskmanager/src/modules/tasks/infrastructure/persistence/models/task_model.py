from petisco.persistence.persistence import Persistence
from sqlalchemy import Column, Integer, String, DateTime

Base = Persistence.get_base("taskmanager")


class TaskModel(Base):

    __tablename__ = "Task"

    id = Column("id", Integer, primary_key=True)
    task_id = Column("task_id", String(36))
    title = Column("title", String(40))
    description = Column("description", String(200))
    created_at = Column("created_at", DateTime)
