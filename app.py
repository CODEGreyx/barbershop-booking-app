from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barber TEXT NOT NULL,
            service TEXT NOT NULL,
            time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, barber, service, time FROM bookings")
    bookings = cursor.fetchall()

    conn.close()
    success = request.args.get("sucess")
    return render_template("index.html", bookings=bookings, success=success)


@app.route("/book", methods=["POST"])
def book():
    service = request.form.get("service")
    time = request.form.get("time", "").strip()
    barber = request.form.get("barber")

    # validation
    if not barber or not service or not time:
        return render_template("error.html", message="Please fill all fields properly.")

    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    # check duplicate booking
    cursor.execute(
        "SELECT * FROM bookings WHERE barber = ? AND time = ?",
        (barber, time)
    )
    existing = cursor.fetchone()

    if existing:
        conn.close()
        return render_template("booking_taken.html")

    # insert booking
    cursor.execute(
        "INSERT INTO bookings (barber, service, time) VALUES (?, ?, ?)",
        (barber, service, time)
    )

    conn.commit()
    conn.close()

    return redirect("/?sucess=1")

@app.route("/edit/<int:booking_id>")
def edit(booking_id):
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, barber, service, time FROM bookings WHERE id = ?",
        (booking_id,)
    )
    booking = cursor.fetchone()

    conn.close()

    return render_template("edit.html", booking=booking)

@app.route("/update/<int:booking_id>", methods=["POST"])
def update(booking_id):
    barber = request.form.get("barber")
    service = request.form.get("service")
    time = request.form.get("time", "").strip()

    if not barber or not service or not time:
        return render_template("error.html", message="Please fill all fields properly.")

    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM bookings WHERE barber = ? AND time = ? AND id != ?",
        (barber, time, booking_id)
    )
    existing = cursor.fetchone()

    if existing:
        conn.close()
        return render_template("booking_taken.html")

    cursor.execute(
        "UPDATE bookings SET barber = ?, service = ?, time = ? WHERE id = ?",
        (barber, service, time, booking_id)
    )

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/delete/<int:booking_id>")
def delete(booking_id):
    conn = sqlite3.connect("bookings.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)