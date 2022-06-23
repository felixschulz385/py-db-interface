# PDBI

PDBI provides unified methods to access databases. It tries to mimic the functionalities of the R package {DBI}.

The creation of this package is tied to teaching at the University of Tübingen.

- [x] Establish backends for both sqlite and MySQL
- [x] Implement a basic set of functions allowing database connection, navigation and queries
- [x] Test the databases used in the lecture
- [ ] Test all existing exercises of the lecture

## What functions have been implemented?

- `dbConnect()`
- `dbDisconnect()`
- `dbListTables()`
- `dbListFields()`
- `dbReadTable()`
- `dbGetQuery()`

All have been tested with a local sqlite database and a hosted MySQL database

## How to install?

The package is thus far only uploaded on TestPyPI. Therefore, install by means of pip using:

```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple py-db-interface
```

## How to use?

The recommended way of importing the package is:
```
import py_db_interface.py_db_interface as pdbi
```

After this, create a connection object to database, run queries and close the connection:
```
con = pdbi.dbConnect("sqlite", host = "test.db")
result = pdbi.dbGetQuery(con, "SELECT * FROM tracks WHERE Milliseconds != 200000")
pdbi.dbDisconnect(con)
```
