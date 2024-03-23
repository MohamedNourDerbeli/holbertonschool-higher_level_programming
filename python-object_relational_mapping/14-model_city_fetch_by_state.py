#!/usr/bin/python3
"""
This script lists all City objects
from the database `hbtn_0e_6_usa`.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main(username, password, db_name):
    """
    This script prints all City objects
    from the database `hbtn_0e_14_usa`.
    """
    # Create the database connection
    cnt = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    # Create the engine
    engine = create_engine(cnt)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the states
    query = session.query(City, State).join(State)
    # print the states
    for city, state in query.all():
        print(f"{state.name}: ({city.id}) {city.name}")
    # Close the session
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    main(username, password, db_name)
