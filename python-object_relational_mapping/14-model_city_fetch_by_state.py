#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_state():
    """
    Retrieves and prints cities along with their corresponding state names.
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

    # Query both State and City, joining them on state_id
    # Results are sorted by cities.id
    results = session.query(State, City).join(City).order_by(City.id).all()

    # Format: <state name>: (<city id>) <city name>
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
