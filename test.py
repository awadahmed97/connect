from app import db, Venue, Show, Genre
db.session.rollback()
venue = Venue.query.get(1)
g6 = Genre.query.filter(Genre.name=='Alternative').first()
g7 = Genre.query.filter(Genre.name=='Blues').first()
g8 = Genre.query.filter(Genre.name=='Country').first()
g9 = Genre.query.filter(Genre.name=='Electonic').first()
g10 = Genre.query.filter(Genre.name=='Heavy Metal').first()
venue.genres= [g6, g7, g8, g9, g10]
db.session.add(venue)
db.session.commit()