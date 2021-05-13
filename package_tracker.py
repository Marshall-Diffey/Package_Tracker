from flask import Flask, render_template, redirect, url_for
from app.shipping_form import ShippingForm
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
def index():
    return render_template("package_tracker.html")


@app.route("/new_package", methods=["GET", "POST"])
def shipping_request():
    form = ShippingForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template("shipping_request.html", form=form)
