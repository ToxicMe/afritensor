import os, re, secrets
from flask import Flask, render_template, request, session, abort, redirect, url_for, flash
from data import COMPANY, SERVICES, DIRECTORS, VALUES

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-me-in-production")

@app.context_processor
def inject_globals():
    return {"company": COMPANY, "services": SERVICES}

def csrf_token():
    if "_csrf" not in session:
        session["_csrf"] = secrets.token_hex(16)
    return session["_csrf"]
app.jinja_env.globals["csrf_token"] = csrf_token

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", directors=DIRECTORS, values=VALUES)

@app.route("/services")
def services_page():
    return render_template("services.html")

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate(form):
    errors, v = {}, {k: form.get(k, "").strip() for k in
                     ("name", "email", "phone", "organization", "service", "message")}
    if len(v["name"]) < 2: errors["name"] = "Enter your full name."
    if not EMAIL_RE.match(v["email"]): errors["email"] = "Enter a valid email address."
    if v["phone"] and not re.match(r"^[0-9+()\-\s]{7,20}$", v["phone"]):
        errors["phone"] = "Enter a valid phone number, or leave this blank."
    if v["service"] not in [s["title"] for s in SERVICES] + ["Other"]:
        errors["service"] = "Select the service you need."
    if len(v["message"]) < 10: errors["message"] = "Describe your enquiry in at least 10 characters."
    return v, errors

def send_enquiry(data):
    """Hook for email delivery (e.g. smtplib or a transactional email API). Currently a no-op."""
    app.logger.info("Enquiry received from %s <%s>", data["name"], data["email"])

@app.route("/contact", methods=["GET", "POST"])
def contact():
    values, errors = {}, {}
    if request.method == "POST":
        if request.form.get("_csrf") != session.get("_csrf"):
            abort(400)
        if request.form.get("website"):  # honeypot
            return redirect(url_for("contact"))
        values, errors = validate(request.form)
        if not errors:
            send_enquiry(values)
            session["sent"] = True
            return redirect(url_for("contact"))
    sent = session.pop("sent", False)
    return render_template("contact.html", values=values, errors=errors, sent=sent)

@app.route("/privacy-policy")
def privacy():
    return render_template("legal.html", title="Privacy Policy")

@app.route("/terms-and-conditions")
def terms():
    return render_template("legal.html", title="Terms & Conditions")

if __name__ == "__main__":
    app.run(debug=True)
