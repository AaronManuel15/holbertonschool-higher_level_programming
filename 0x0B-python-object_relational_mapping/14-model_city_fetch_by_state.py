#!/usr/bin/python3
""" Project 0x0B. Python - Object-relational mapping
    Task 14
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sqlalchemy import insert


if __name__ == "__main__":
    """ prints all City objects from the database
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    for state_name, city_id, city_name in session.query(
            State.name, City.id, City.name).filter(
            City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state_name, city_id, city_name))
