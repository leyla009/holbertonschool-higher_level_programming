#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_a():
    """
    Connects to the database and deletes states containing the letter 'a'.
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

    # Query all states containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Iterate through the list and delete each object from the session
    for state in states_to_delete:
        session.delete(state)

    # Commit all deletions to the database
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
