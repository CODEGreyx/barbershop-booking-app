# Barbershop Booking System

A simple full-stack web application built using Python (Flask) that allows users to book appointments with different barbers.

## Live Demo

https://barbershop-booking-app.onrender.com

## Overview

This project simulates a real-world barbershop booking system where users can:

- Choose a barber
- Select a service
- Pick a time slot
- Create bookings
- Prevent duplicate bookings for the same barber and time
- Delete existing bookings

## Features

- Multiple barbers (Marco, Hassan, Gwen)
- Service selection (Haircut, Beard, Combo)
- Time slot selection
- Booking validation (no duplicate time slots per barber)
- Input validation (prevents empty submissions)
- Delete booking functionality
- Clean dark-themed UI

## Tech Stack

- Python
- Flask
- HTML (embedded in Flask)
- CSS (inline styling)

## Project Structure

app.py          # Main Flask application  
requirements.txt  # Dependencies (Flask, gunicorn)

## Running Locally

1. Clone the repository:
git clone https://github.com/CODEGreyx/barbershop-booking-app.git

2. Navigate into the project:
cd barbershop-booking-app

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
python app.py

5. Open in browser:
http://127.0.0.1:5000

## Deployment

This project is deployed on Render:
https://barbershop-booking-app.onrender.com

## Limitations

- Data is stored in memory and resets when the server restarts
- No database integration yet
- No authentication system

## Future Improvements

- Add a database such as SQLite or PostgreSQL
- Add user authentication
- Add an admin dashboard
- Improve booking management and availability tracking
- Separate templates and styling into dedicated files

## Author

Hassan Naveed Khan  
Computer Science Student
