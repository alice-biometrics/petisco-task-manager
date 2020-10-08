from petisco.persistence.sqlalchemy.sqlalchemy_persistence import SqlAlchemyPersistence
from sqlalchemy import Column, Integer, String, JSON

Base = SqlAlchemyPersistence.get_instance().sources["petisco"]["base"]


class EventModel(Base):

    __tablename__ = "Event"

    id = Column("id", Integer, primary_key=True)
    event_id = Column("event_id", String(36))
    type = Column("type", String(100))
    data = Column("data", JSON)
