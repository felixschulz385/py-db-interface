def dbConnect(drv, host, user=None, password=None, port=None, dbname=None):
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
    
    def mysql_connect(host, user=None, password=None, port=None, dbname=None):
        import mysql.connector
        return mysql.connector.connect(host=host,
                                       user=user,
                                       password=password, 
                                       port=port, 
                                       database=dbname)
    
    def sqlite_connect(database):
        import sqlite3
        return sqlite3.connect(database = host)
    
    match drv:
        case "mysql":
            return mysql_connect(host=host, user=user, password=password, port=port, dbname=dbname)
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
    
    def mysql_list_tables(con):
        cursor = con.cursor()
        cursor.execute("SELECT `TABLE_NAME` FROM information_schema.tables " +
                       "WHERE `TABLE_SCHEMA` = '" + con.database + "'")
        out = [item[0] for item in cursor.fetchall()]
        cursor.close()
        return out
    
    def sqlite_list_tables(con):
        from itertools import chain
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master where type='table'")
        out = list(chain.from_iterable(cursor.fetchall()))
        cursor.close()
        return out
    
    match str(type(con)):
        case "<class 'mysql.connector.connection.MySQLConnection'>":
            return mysql_list_tables(con)
        case "<class 'sqlite3.Connection'>":
            return sqlite_list_tables(con)
        
def dbListFields(con, table):
    """
    Lists all fields of a table
    Args:
        con (Connection): the connection to the database
        table (String): the name of the table
    Returns:
        An array containing the names of the fields in the table
    """

    def mysql_list_fields(con, table):
        cursor = con.cursor()
        cursor.execute("SELECT `COLUMN_NAME` FROM information_schema.columns " +
                       "WHERE `TABLE_SCHEMA` = '" + con.database + "' AND `TABLE_NAME` = '" + table + "'")
        out = [item[0] for item in cursor.fetchall()]
        cursor.close()
        return out
    
    def sqlite_list_fields(con, table):
        cursor = con.cursor()
        cursor.execute("PRAGMA table_info('" + table + "')")
        out = [item[1] for item in cursor.fetchall()]
        cursor.close()
        return out
    
    match str(type(con)):
        case "<class 'mysql.connector.connection.MySQLConnection'>":
            return mysql_list_fields(con, table)
        case "<class 'sqlite3.Connection'>":
            return sqlite_list_fields(con, table)
        
def dbReadTable(con, table):
    """
    Reads a database table to a Pandas DataFrame
    Args:
        con (Connection): the connection to the database
        table (String): the name of the table
    Returns:
        A Pandas DataFrame containing the entire data of the chosen table
    """
    
    from pandas import DataFrame
    
    def mysql_read_table(con, table):
        cursor = con.cursor()
        cursor.execute("SELECT * FROM `" + table + "`")
        out = DataFrame(cursor.fetchall(), columns = [item[0] for item in cursor.description])
        cursor.close()
        return out
    
    def sqlite_read_table(con, table):
        cursor = con.cursor()
        cursor.execute("SELECT * FROM '" + table + "'")
        out = DataFrame(cursor.fetchall(), columns = [item[0] for item in cursor.description])
        cursor.close()
        return out
    
    match str(type(con)):
        case "<class 'mysql.connector.connection.MySQLConnection'>":
            return mysql_read_table(con, table)
        case "<class 'sqlite3.Connection'>":
            return sqlite_read_table(con, table)
        
def dbGetQuery(con, query):
    """
    Executes query and returns results in a Pandas DataFrame
    Args:
        con (Connection): the connection to the database
        query (String): the query to be evaluated
    Returns:
        A Pandas DataFrame containing the result of the query
    """
    
    from pandas import DataFrame
    
    def mysql_get_query(con, query):
        cursor = con.cursor()
        cursor.execute(query)
        out = DataFrame(cursor.fetchall(), columns = [item[0] for item in cursor.description])
        cursor.close()
        return out
    
    def sqlite_get_query(con, query):
        cursor = con.cursor()
        cursor.execute(query)
        out = DataFrame(cursor.fetchall(), columns = [item[0] for item in cursor.description])
        cursor.close()
        return out
    
    match str(type(con)):
        case "<class 'mysql.connector.connection.MySQLConnection'>":
            return mysql_get_query(con, query)
        case "<class 'sqlite3.Connection'>":
            return sqlite_get_query(con, query)
        
def dbDisconnect(con):
    """
    Closes the connection
    Args:
        con (Connection): the connection to the database
    Returns:
        None
    """
    
    def mysql_disconnect(con):
        con.close()
    
    def sqlite_disconnect(con):
        con.close()
    
    match str(type(con)):
        case "<class 'mysql.connector.connection.MySQLConnection'>":
            return mysql_disconnect(con)
        case "<class 'sqlite3.Connection'>":
            return sqlite_disconnect(con)
    