#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_first_state():
    """
    Retrieves and prints the first state from the database.
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

    # Query the first state record ordered by id
    # .first() is used to ensure we do not fetch all records
    first_state = session.query(State).order_by(State.id).first()

    # Output the result or "Nothing" if the table is empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()


if __name__ == "__main__":
    fetch_first_state()
