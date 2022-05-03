from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="small",
    rating=5,
    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDLE3I46XP9ycAFqDkxcR120Zu2XMgriO1huaWuhcarrDovmf0ARNU83nTQU2AOf0_lwc&usqp=CAU"
)

c2 = Cupcake(
    flavor="chocolate",
    size="large",
    rating=5,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="mint",
    size="small",
    rating=7,
    image="https://thumbs.dreamstime.com/b/vector-cupcake-cake-maffin-mint-chocolate-dessert-print-illustration-vector-cupcake-cake-maffin-mint-chocolate-dessert-154600335.jpg"
)

c4 = Cupcake(
    flavor="red velvet",
    size="small",
    rating=9,
    image="https://i.pinimg.com/originals/f9/6d/4c/f96d4c93f9d988451ce0c5c403c14566.jpg"
)

db.session.add_all([c1, c2, c3, c4])
db.session.commit()