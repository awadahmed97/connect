from app import db, Venue, Show, Genre
import pytest

@pytest.fixture
def venue_genres():
    venue = Venue.query.get(1)
    jazz = Genre.query.filter(Genre.name=='Jazz').first()
    venue.genres= [jazz]
    db.session.add(venue)
    db.session.commit()
    yield
    venue.genres=[]
    db.session.add(venue)
    db.session.commit()

def test_venue_genres(venue_genres):
    venue = Venue.query.get(1)
    genres = [g.name for g in venue.genres]
    assert ['Jazz'] == genres

    
