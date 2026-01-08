class Rental(db.Model):
    __tablename__ = "rental"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    rent_price = db.Column(db.Float)
    billing_date = db.Column(db.String(20))
    status = db.Column(db.String(20))
