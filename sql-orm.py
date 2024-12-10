from sqlalchemy import create_engine, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session


# Step 1: Update the connection to use Gitpod-specific socket path
db = create_engine("postgresql+psycopg2://gitpod:@/chinook?host=/home/gitpod/.pg_ctl/sockets")

# Step 2: Use the modern SQLAlchemy 2.0 approach for the declarative base
base = declarative_base()


# Step 3: Create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# Step 4: Create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# Step 5: Create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# Step 6: Update the sessionmaker for SQLAlchemy 2.0
Session = sessionmaker(bind=db)  # Bind the engine to the sessionmaker

# Step 7: Create the database schema
try:
    # Ensure the database tables are created
    base.metadata.create_all(db)
    print("Database schema created successfully.")
except Exception as e:
    print(f"Error creating database schema: {e}")


# Step 8: Open a new session using the SQLAlchemy 2.0 syntax
try:
    # Open a new session
    with Session() as session:
        # Query 1 - select all records from the "Artist" table
        # artists = session.query(Artist)
        # for artist in artists:
        #     print(artist.ArtistId, artist.Name, sep=" | ")

        # Query 2 - select only the "Name" column from the "Artist" table
        # artists = session.query(Artist)
        # for artist in artists:
        #     print(artist.Name)

        # Query 3 - select only "Queen" from the "Artist" table
        # artist = session.query(Artist).filter_by(Name="Queen").first()
        # print(artist.ArtistId, artist.Name, sep=" | ")

        # Query 4 - select only by "ArtistId" #51 from the "Artist" table
        # artist = session.query(Artist).filter_by(ArtistId=51).first()
        # print(artist.ArtistId, artist.Name, sep=" | ")

        # Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
        # albums = session.query(Album).filter_by(ArtistId=51)
        # for album in albums:
        #     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

        # Query 6 - select all tracks where the composer is "Queen" from the "Track" table
        tracks = session.query(Track).filter_by(Composer="Queen")
        for track in tracks:
            print(
                track.TrackId,
                track.Name,
                track.AlbumId,
                track.MediaTypeId,
                track.GenreId,
                track.Composer,
                track.Milliseconds,
                track.Bytes,
                track.UnitPrice,
                sep=" | "
            )

except Exception as e:
    print(f"An error occurred: {e}")
