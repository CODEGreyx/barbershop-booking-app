# Live Demo
https://barbershop-booking-app.onrender.com
# Barbershop Booking App

A simple full-stack booking system built using Flask and SQLite.  
Users can create, edit, and delete barbershop appointments through a clean web interface.

---

## Features

- Create bookings (barber, service, time)
- Prevent duplicate bookings (same barber + same time)
- Edit existing bookings
- Delete bookings
- Dropdown-based time selection (no invalid inputs)
- Clean UI using HTML + CSS

---

## Tech Stack

- Python (Flask)
- SQLite
- HTML (Jinja2 templates)
- CSS

---

## Project Structure

```
booking-app/
│
├── app.py
├── bookings.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── edit.html
│   ├── booking_taken.html
│   └── error.html
│
└── static/
    └── style.css
```

---

## How to Run

1. Install dependencies:

```
pip install flask
```

2. Run the app:

```
python app.py
```

3. Open in browser:

```
http://127.0.0.1:5000
```

---

## How It Works

- Flask handles routes:
  - `/` → show bookings
  - `/book` → create booking
  - `/edit/<id>` → edit page
  - `/update/<id>` → update booking
  - `/delete/<id>` → delete booking

- SQLite stores booking data

- Jinja templates render dynamic content

---

## Key Concepts Learned

- CRUD operations
- Flask routing
- Form handling
- Database integration (SQLite)
- Template rendering with Jinja
- Basic validation (frontend + backend)

---

## Future Improvements

- User authentication (login/signup)
- Real-time booking availability
- Deploy to cloud (Render / AWS)
- Convert to REST API + frontend (React)

---

## Author

Hassan Naveed Khan
Computer Science Student
