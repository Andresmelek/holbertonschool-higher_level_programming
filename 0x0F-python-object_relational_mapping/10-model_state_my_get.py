#!/usr/bin/python3
"""
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).filter(
               State.name.like(argv[4])).all()
    if state:
        for i in session.query(State).order_by(State.id).filter(
               State.name.like(argv[4])):
            print(i.id)
    else:
        print("Not found")
