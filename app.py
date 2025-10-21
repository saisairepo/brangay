from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100), nullable=False)
    fullname = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    details = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Create DB tables
with app.app_context():
    db.create_all()

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    service_type = request.form.get("service_type")
    fullname = request.form.get("fullname")
    address = request.form.get("address")
    details = request.form.get("details")

    new_request = ServiceRequest(
        service_type=service_type,
        fullname=fullname,
        address=address,
        details=details
    )
    db.session.add(new_request)
    db.session.commit()

    return redirect(url_for("success"))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
