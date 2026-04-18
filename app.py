from flask import Flask, request, redirect

app = Flask(__name__)

bookings = []

@app.route("/")
def home():
    booking_list = "".join(
        f"""
        <div class="booking-card">
            <span>{b['service']} with {b['barber']} at {b['time']}</span>
            <a class="delete-btn" href="/delete/{i}">Delete</a>
        </div>
        """
        for i, b in enumerate(bookings)
    )

    return f"""
    <html>
    <head>
        <title>Barbershop Booking</title>
        <style>
            body {{
                margin: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #0b0b0f;
                font-family: Georgia, serif;
                color: #eaeaea;
            }}

            .container {{
                width: 430px;
                background: #111116;
                border: 1px solid #3a2f2f;
                border-radius: 14px;
                padding: 24px;
                box-shadow: 0 0 30px rgba(0, 0, 0, 0.6);
            }}

            h1 {{
                text-align: center;
                margin-top: 0;
                margin-bottom: 20px;
                color: #d6c3a1;
                letter-spacing: 1px;
            }}

            form {{
                display: flex;
                flex-direction: column;
                gap: 12px;
                margin-bottom: 20px;
            }}

            select, input {{
                padding: 10px;
                border: 1px solid #3a2f2f;
                border-radius: 8px;
                background: #0d0d12;
                color: #f5f5f5;
            }}

            button {{
                padding: 10px;
                border: 1px solid #5a4343;
                border-radius: 8px;
                background: #1a1a22;
                color: #d6c3a1;
                cursor: pointer;
            }}

            button:hover {{
                background: #242430;
            }}

            h3 {{
                margin-bottom: 12px;
                color: #d6c3a1;
            }}

            .booking-card {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px;
                margin-bottom: 10px;
                border-radius: 10px;
                background: #1a1a22;
                border: 1px solid #2e2e38;
            }}

            .delete-btn {{
                color: #ff8a8a;
                text-decoration: none;
                font-size: 14px;
            }}

            .delete-btn:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Barbershop Booking</h1>

            <form action="/book" method="POST">
                <select name="barber" required>
                    <option value="" disabled selected>Choose your barber</option>
                    <option value="Marco">Marco</option>
                    <option value="Hassan">Hassan</option>
                    <option value="Gwen">Gwen</option>
                </select>

                <select name="service">
                    <option value="" disabled selected>Choose your service</option>
                    <option value="Haircut">Haircut</option>
                    <option value="Beard">Beard</option>
                    <option value="Haircut + Beard">Haircut + Beard</option>
                </select>

                <input name="time" placeholder="Enter time (e.g. 3 PM)">
                <button type="submit">Book</button>
            </form>

            <h3>Bookings</h3>
            {booking_list if booking_list else "<p>No bookings yet.</p>"}
        </div>
    </body>
    </html>
    """

@app.route("/book", methods=["POST"])
def book():
    service = request.form["service"]
    time = request.form["time"].strip()
    barber = request.form["barber"]

    for b in bookings:
        if b["time"].lower() == time.lower() and b["barber"] == barber:
            return """
            <html>
            <head>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background: #0b0b0f;
                        color: #eaeaea;
                        font-family: Georgia, serif;
                    }

                    .box {
                        background: #111116;
                        padding: 30px;
                        border-radius: 12px;
                        border: 1px solid #3a2f2f;
                        text-align: center;
                    }

                    a {
                        display: inline-block;
                        margin-top: 15px;
                        color: #d6c3a1;
                        text-decoration: none;
                    }

                    a:hover {
                        text-decoration: underline;
                    }
                </style>
            </head>
            <body>
                <div class="box">
                    <h2>This time slot is already booked for this barber.</h2>
                    <a href="/">Go back</a>
                </div>
            </body>
            </html>
            """

    bookings.append({
        "service": service,
        "time": time,
        "barber": barber
    })

    return redirect("/")

@app.route("/delete/<int:booking_id>")
def delete(booking_id):
    if 0 <= booking_id < len(bookings):
        bookings.pop(booking_id)
    return redirect("/")

if __name__ == "__main__":
    app.run()