import psycopg2

try:
    # Connect to the "chinook" database using the socket path for Gitpod
    connection = psycopg2.connect(
        database="chinook",
        user="gitpod",  # Use 'gitpod' instead of 'postgres'
        password="",  # No password required for Gitpod
        host="/home/gitpod/.pg_ctl/sockets",  # Use Gitpod-specific socket path
        port=""  # Leave port blank since we are using a Unix socket
    )

    # Build a cursor object of the database
    cursor = connection.cursor()

    # Query 1 - Select all records from the "Artist" table
    # cursor.execute('SELECT * FROM "Artist"')

    # Query 2 - Select only the "Name" column from the "Artist" table
    # cursor.execute('SELECT "Name" FROM "Artist"')

    # Query 3 - Select only "Queen" from the "Artist" table
    cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

    # Query 4 - Select only by "ArtistId" #51 from the "Artist" table
    # cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

    # Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
    # cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

    # Query 6 - Select all tracks where the composer is "Queen" from the "Track" table
    # cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

    # Fetch the results (multiple)
    results = cursor.fetchall()

    # Fetch the result (single)
    # results = cursor.fetchone()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    try:
        if connection:
            connection.close()
    except NameError:
        print("Connection was not established, so no need to close it.")

# Print results
for result in results:
    print(result)
