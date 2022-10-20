#!/usr/bin/python3
""" Project 0x0B. Python - Object-relational mapping
    Task 10
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """ Prints the State object with the named passed
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state_name = argv[4]
    matching_state = session.query(State.id, State.name).filter(State.name == state_name)
    if matching_state:
        print("{}".format(matching_state.id))
    else:
        print("Not found")
