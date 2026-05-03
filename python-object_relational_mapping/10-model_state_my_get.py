#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_by_name():
    """
    Retrieves the ID of a state based on the name argument.
    """
    # Database connection and search arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_to_search = sys.argv[4]

    # Initialize the engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, passwd, db_name
        ),
        pool_pre_ping=True
    )

    # Create session factory and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the exact name provided
    # SQLAlchemy's .filter() handles input safely to prevent SQL injection
    state = session.query(State).filter(State.name == state_to_search).first()

    # Output the state ID or "Not found"
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    get_state_by_name()
