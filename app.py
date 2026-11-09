from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.config["SECRET_KEY"] = "replace-this-with-a-long-random-secret"
DB_PATH = Path(__file__).with_name("estovia.db")


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS enquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                interest TEXT,
                location TEXT,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        interest = request.form.get("interest", "").strip()
        location = request.form.get("location", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email:
            flash("Please provide your name and email address.", "error")
            return redirect(url_for("home") + "#contact")

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                INSERT INTO enquiries (name, email, phone, interest, location, message)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, email, phone, interest, location, message))

        flash("Thank you! Your enquiry has been received. Our team will contact you.", "success")
        return redirect(url_for("home") + "#contact")

    return render_template("index.html", current_year=datetime.now().year)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
