from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base, TodoItem

engine = create_engine("sqlite:///tasks.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
s = Session()


for desc in ("1 задача", "2 задача",
"3 задача", "4 задача"):
    t = TodoItem(desc)
    s.add(t)

s.commit()
