#!/usr/bin/python3
"""
changes the name of a State object
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(username, password, db_name):
    """
    changes the name of a State object
    """
    # Create the database connection
    cnt = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    # Create the engine
    engine = create_engine(cnt)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the states and print it
    update = session.query(State).filter_by(id=2).first()
    update.name = "New Mexico"
    session.commit()
    # Close the session
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    main(username, password, db_name)
