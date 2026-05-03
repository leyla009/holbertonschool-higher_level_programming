#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_states_with_a():
    """
    Connects to the database and filters states containing the letter 'a'.
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

    # Query states containing 'a', ordered by id
    # .like() is used for pattern matching (%a% means 'a' anywhere)
    states = session.query(State).filter(State.name.like('%a%')) \
                                 .order_by(State.id).all()

    # Display results in the format "id: name"
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    filter_states_with_a()
