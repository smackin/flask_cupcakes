"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = 'https://i.etsystatic.com/21185388/r/il/4e3b57/2297821352/il_794xN.2297821352_opu8.jpg'


class Cupcake(db.Model):
    """cupcake model"""
    
    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def to_dict(self):
        """serialize cupcake to dict"""
        return {
        "id": self.id, 
        "flavor": self.flavor, 
        "size": self.size, 
        "image": self.image, 
        }


def connect_db(app):
    """connect to db.  call in app.py """
    
    db.app = app 
    db.init_app(app)


