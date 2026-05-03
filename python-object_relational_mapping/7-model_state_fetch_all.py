#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa using SQLAlchemy.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_all_states():
    """
    Connects to the database and retrieves all State objects.
    """
    # Capture arguments for database connection
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    # Format: mysql+mysqldb://user:password@host:port/database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, passwd, db_name
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    # Display results in the format "id: name"
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    fetch_all_states()
