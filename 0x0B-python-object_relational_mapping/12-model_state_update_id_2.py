#!/usr/bin/python3
""" Project 0x0B. Python - Object-relational mapping
    Task 11
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, state
from sqlalchemy import (create_engine)
from sqlalchemy import insert


if __name__ == "__main__":
    """ Prints the State object with the named passed
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_grab = session.get(State, 2)

    state_grab.name = "New Mexico"

    session.commit()
