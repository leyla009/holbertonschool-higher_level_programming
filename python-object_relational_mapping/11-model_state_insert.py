#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state():
    """
    Adds a new state to the database and prints its new id.
    """
    # Database connection arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

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

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the object to the session and commit to the database
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print("{}".format(new_state.id))

    # Close the session
    session.close()


if __name__ == "__main__":
    add_state()
