#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
"""
import MySQLdb
import sys


def filter_cities():
    """
    Connects to the database and retrieves cities based on the state argument.
    """
    # Grab arguments: username, password, database, state name
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    cursor = db.cursor()

    # JOIN cities and states, filtering by the provided state name
    # Parameterized query (%s) handles SQL injection protection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all resulting rows
    rows = cursor.fetchall()

    # Format the output as a comma-separated string
    print(", ".join([row[0] for row in rows]))

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
