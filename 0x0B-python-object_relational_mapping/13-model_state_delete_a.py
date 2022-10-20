#!/usr/bin/python3
""" Project 0x0B. Python - Object-relational mapping
    Task 13
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, state
from sqlalchemy import (create_engine)
from sqlalchemy import insert


if __name__ == "__main__":
    """ deletes all State objects with a name containing an a
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.contains("a")).delete(
                                synchronize_session="fetch")
    session.commit()
