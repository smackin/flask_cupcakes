"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, jsonify

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "oh_so_secret"

connect_db(app)

@app.route('/')
def root():
    """displays homepage with cupcake form"""
    return render_template("index.html")

@app.route('/api/cupcakes')
def list_all_cupcakes():
    """return a list of all cupcakes in db
        as JSON 
        {cupcake: [{id, flvaor, rating, size, image}]}
    """
    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)
    
    
@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """return data on cupcake of id passed in
    as JSON """
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.to_dict())
    
    
@app.route('/api/cupcakes/', methods=["POST"])
def create_cupcake():
    """add new cupcake and returnd the data in JSON
    {cupcake: [{id, flavor, rating, size, image}]}
    """  
    
    data = request.json
    
    cupcake = Cupcake(
        flavor = data['flavor'], 
        rating = data['rating'], 
        size = data['size'], 
        image = data['image'] or None)
    
    db.session.add(cupcake)
    db.session.commit()
    
    # POST requests should return HTTP status of 201 Created
    return (jsonify(cupcake=cupcake.to_dict()), 201)
    
    
@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """update cupcake from db in request and return updated info"""
    
    data = request.json
    
    cupcake = Cupcake.query.get_or_404(id)
    
    cupcake.flavor = data['flavor'], 
    cupcake.rating = data['rating'], 
    cupcake.size = data['size'], 
    cupcake.image = data['image']
    
    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.to_dict()))

