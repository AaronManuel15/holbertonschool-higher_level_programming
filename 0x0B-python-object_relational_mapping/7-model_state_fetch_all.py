#!/usr/bin/python3
""" Project 0x0B. Python - Object-relational mapping
    Task 7
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """ Prints all State objects from database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for id, name in session.query(State.id, State.name):
        print("{}: {}".format(id, name))
