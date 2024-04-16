#!/usr/bin/python3
"""to get all states"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.
                                  argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    printed = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print(state.id)
            printed = True
            break
    if printed is False:
        print("Not found")