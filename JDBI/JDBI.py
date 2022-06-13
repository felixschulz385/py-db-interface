def dbConnect(drv, host, user=None, password=None):
    """
    Connect to a SQL database
    Args:
        drv (str): the type of database
        dbname (str): a name for the connection object
        host (str): the path/URL to the database
        user (str): the username credential
        password (str): the password credential
    Returns:
        A Connection object
    """
    
    def mysql_connect(host, user, password):
        import mysql.connector
        return mysql.connector.connect(host=host,
                                       user=user,
                                       password=password)
    
    def sqlite_connect(database):
        import sqlite3
        return sqlite3.connect(database = host)
    
    match drv:
        case "mysql":
            return mysql_connect(host=host, user=user, password=password)
        case "sqlite":
            return sqlite_connect(database=host)

def dbListTables(con):
    """
    Lists all tables of a database
    Args:
        con (Connection): the connection to the database
    Returns:
        An array containing the names of the tables in the database
    """
    
    def sqlite_list_tables(con):
        from itertools import chain
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master where type='table'")
        return list(chain.from_iterable(cursor.fetchall()))
    
    match str(type(con)):
        case "<class 'sqlite3.Connection'>":
            return sqlite_list_tables(con)
        
def dbDisconnect(con):
    """
    Closes the connection
    Args:
        con (Connection): the connection to the database
    Returns:
        None
    """
    
    def sqlite_disconnect(con):
        con.close()
    
    match str(type(con)):
        case "<class 'sqlite3.Connection'>":
            return sqlite_disconnect(con)
    