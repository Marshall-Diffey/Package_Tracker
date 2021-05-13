from flask import Flask, render_template, Config
from app.shipping_form import ShippingForm

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("package_tracker.html")


@app.route("/new_package", methods=["GET", "POST"])
def shipping_request():
    form = ShippingForm()
    return render_template("shipping_request.html", form=form)