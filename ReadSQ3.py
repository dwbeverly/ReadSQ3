import sqlite3
from sys import argv

#take a sqlite database filename as the 1st command line argument, and optionally, a sql query  sa second argument. If no query is provided, it defaults to one that returns all table names and the number of records. 
if __name__ == "__main__":
    if len(argv) < 3:
        sqlite_file = argv[1]
        sql_query = "SELECT * FROM sqlite_sequence"
        print('No query provided: using default query to return all table names')
    elif len(argv) > 2:
        sqlite_file = argv[1]
        sql_query = argv[2]
    else:
        print('Error: must provide a sqlite database file as input')
        exit(1)

#validate file, open new file to dump results into
newfile = 'sqlite_results.csv'
try:
    infile = open(sqlite_file)
except EnvironmentError as e:
    print(e)
    sys.exit(1)
print("\nThe file ({}) is valid.".format(sqlite_file))
print("\n")
o = open(newfile, 'w')

#connect to database, run the below query. You can update this to whatever sql you need to execute on the databse. Stores results into all_rowsself.
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute(sql_query)
all_rows = c.fetchall()

#write all_rows to filename
o.write("{0},\n".format(all_rows))
o.close()

#close database connection
conn.close()

print("The script has finished running. The results have been stored in {0}\n".format(newfile))
