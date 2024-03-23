#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(username, password, db_name):
    """
    Access to the database and get the states
    from the database.
    """
    # Create the database connection
    cnt = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    # Create the engine
    engine = create_engine(cnt)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the State object
    filter = session.query(State).filter(State.name.contains('a'))
    # delete  the States that contain an 'a'
    for state in filter:
        session.delete(state)
    # Commit the changes
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    main(username, password, db_name)
