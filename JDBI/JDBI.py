def dbConnect(drv, dbname, host, user, password):
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
    
    def mysql_connect(dbname, host, user, password):
        import mysql.connector
        mysql.connector.connect(host=host,
                                user=user,
                                password=password)
    
    def sqlite_connect(dbname, host, user, password):
        import sqlite3
        con = sqlite3.connect(host = host,
                              user=user,
                              password=password)
    
    match drv:
        case "mysql":
            mysql_connect(host=host, user=user, password=password)
        case "sqlite":
            sqlite_connect(host=host, user=user, password=password)

def dbListTables():
    ""