# ReadSQ3

SQLite .sq3 file reader in Python

## Background

SQLite is becoming more popular as a lightweight, RDBMS for embedding databases into applications. However, not every database tool can open the .sq3/.db files for them, and in some cases, you may not want to use the available SQLite online browsers to view them. This script uses the sqlite3 library to enable you to view them.

## How to use

*  Syntax

  ```python
  python ReadSQ3 (database) "(query)"
  ```
  
*  You must specify a .sq3 or .db databse name when you execute the script. 

*  You can optionally pass a sql query within quotations. If you leave this blank, it uses a default query that reads from the sqlite_sequence table to return all tables and the number of records in each table. Hint: this is actually a good place to start if you're looking to map or probe a table. 

*  Example

  ```python
  python ReadSQ3 chinook.db "SELECT * FROM GENRES"
  ```


