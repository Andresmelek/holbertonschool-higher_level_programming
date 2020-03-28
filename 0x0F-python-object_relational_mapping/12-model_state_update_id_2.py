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

    change_state = session.query(State).filter_by(id=2).first()
    change_state.name = "New Mexico"
    session.commit()
