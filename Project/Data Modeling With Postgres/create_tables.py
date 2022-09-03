import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    Creates the Database to insert the data
    :return: cursor an connection
    """

    #connect to default database
    #connection
    try:
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password= 707707")

    except psycopg2.Error as e:
        print("Error: Could not make the conn.set_session(autocommit=True) connection to PostgreSQl Database")
        print(e)

    #cursor 
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: could not get curser to the Database")
        print(e)
    #autocommit
    conn.set_session(autocommit=True)



    #Create sparkify_db database with UTF8 encoding
    try:
        print("DROP sparkify_db database")
        cur.execute("DROP DATABASE IF EXISTS sparkify_db")
        print("CREATE sparkify_db database")
        cur.execute("CREATE DATABASE sparkify_db WITH ENCODING 'utf8' TEMPLATE template0")

    except psycopg2.Error as e:
        print("Error: Dropping Tables")
        print(e)
    # close connection to default database
    cur.close()
    conn.close()


    #connect to sparkify_db database
    #connection

    try:
        conn = psycopg2.connect("host=localhost dbname=sparkify_db user=postgres password= 707707")

    except psycopg2.Error as e:
        print("Error: Could not make theconn.set_session(autocommit=True) connection to PostgreSQl Database")
        print(e)
    

    #cursor
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: could not get curser to the Database")
        print(e)

    #autocommit
    conn.set_session(autocommit=True)

    return cur, conn



def drop_tables(cur, conn):
    """
    Drop all the tables.
    :param cur: cursor.
    :param conn: connection.
    """

    for query in  drop_table_queries:
        cur.execute(query)
        conn.commit()

    print("DROP ALL TABLES")    


def create_tables(cur, conn):
    """
    Create all the tables.
    :param cur: cursor.
    :param conn: connection.
    """

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

    print("CREATE ALL TABLES") 


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()