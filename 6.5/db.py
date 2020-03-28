from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()


class TodoItem(Base):
    __tablename__ = "tasks"

    uid = Column(Integer, primary_key=True)
    description = Column(String(255))
    is_completed = Column(Boolean, default=False)

    def __init__(self, description):
        self.description = description

    def __str__(self):

        return self.description.lower()


class LogEntry(Base):
    __tablename__ = "logs"
    uid = Column(Integer, primary_key=True)
    ip_addr = Column(String(16))
    timestamp = Column(DateTime)

    def __init__(self, ip_addr, timestamp):
        self.ip_addr = ip_addr
        self.timestamp = timestamp

    def __str__(self):
        return "'%s' on %s" % (self.ip_addr, self.timestamp)
