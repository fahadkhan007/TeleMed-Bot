from flask import Flask, render_template, request, jsonify
import json, csv, os

app = Flask(__name__)

DOCTOR_FILE = "data/doctors.json"
APPOINTMENT_FILE = "appointments.csv"
current_user = "fahad khan"  


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.json["msg"].strip()

    if "who made this chatbot" in user_msg.lower():
        return jsonify(reply="👨‍💻 I was created by Fahad, Akchhat and Lucky Here to help you book you doctor appointments\n Hi! I’m your Telemed Assistant. How can I help you today?\nYou can say 'show available doctors', 'book appointments', 'cancel appointment', or 'my appointments'.")
    if any(greet in user_msg.lower() for greet in ["hi", "hello", "hey"]):
        return jsonify(reply="👋 Hi! I’m your Telemed Assistant. How can I help you today?\nYou can say 'show available doctors', 'book appointments', 'cancel appointments', or 'my appointments'.")
    elif "show doctors" in user_msg.lower():
        return jsonify(reply=show_all_doctors())
    
    elif user_msg.lower().startswith("show"):
        return jsonify(reply=filter_doctors_by_speciality(user_msg))
    
    elif user_msg.lower().startswith("book"):
        return jsonify(reply="Please enter your booking details like: Name, Doctor, Date (YYYY-MM-DD), Time (HH:MM)")
    
    elif user_msg.lower().startswith("cancel") and user_msg.count(",") == 3:
        return jsonify(reply=cancel_appointment(user_msg))
    
    elif user_msg.lower().startswith("cancel"):
        return jsonify(reply="❌ Invalid cancel format. Use: cancel, Doctor, Date, Time")
    
    elif user_msg.count(",") == 3:
        return jsonify(reply=book_appointment(user_msg))
    
    elif "my appointments" in user_msg.lower():
        return jsonify(reply=show_user_appointments())
    
    else:
        return jsonify(reply="Sorry, I didn't get that. Try 'show doctors', 'book', 'cancel', or 'my appointments'.")



def load_doctors():
    with open(DOCTOR_FILE, "r") as f:
        return json.load(f)

def show_all_doctors():
    doctors = load_doctors()
    reply = "🩺 Available Doctors:\n"
    for d in doctors:
        reply += f"- {d['name']} ({d['speciality']}): {', '.join(d['available_slots'])}\n"
    return reply

def filter_doctors_by_speciality(msg):
    speciality = msg.split("show", 1)[1].strip()
    doctors = load_doctors()
    filtered = [d for d in doctors if speciality.lower() in d["speciality"].lower()]
    if not filtered:
        return f"No doctors found for speciality: {speciality}"
    reply = f"🔍 Doctors in {speciality}:\n"
    for d in filtered:
        reply += f"- {d['name']}: {', '.join(d['available_slots'])}\n"
    return reply

def book_appointment(details):
    try:
        name, doctor, date, time = [x.strip() for x in details.split(",")]
        if os.path.exists(APPOINTMENT_FILE):
            with open(APPOINTMENT_FILE, "r") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if row[1].lower() == doctor.lower() and row[2] == date and row[3] == time:
                        return f"❌ That slot is already booked with {doctor} at {time} on {date}."
        with open(APPOINTMENT_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, doctor, date, time])
        return f"✅ Appointment booked for {name} with {doctor} on {date} at {time}"
    except:
        return "❌ Invalid format. Use: Name, Doctor, Date, Time"

def cancel_appointment(user_msg):
    try:
        parts = user_msg.split(",")
        if len(parts) != 4:
            return "❌ Invalid cancel format. Use: cancel, Doctor, Date, Time"

        _, doctor_name, date, time = [p.strip().lower() for p in parts]

        updated_lines = []
        cancelled = False
        with open("appointments.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                name, doctor, appt_date, appt_time = [x.strip() for x in row]
                if (doctor.strip().lower() == doctor_name and 
                    appt_date.strip().lower() == date and 
                    appt_time.strip().lower() == time and 
                    name.strip().lower() == current_user.lower()):
                    cancelled = True
                    continue
                updated_lines.append(",".join([name, doctor, appt_date, appt_time]) + "\n")

        with open("appointments.csv", "w") as f:
            f.writelines(updated_lines)

        if cancelled:
            return f"🗑️ Appointment with {doctor_name} on {date} at {time} cancelled."
        else:
            return f"❌ No appointment found with {doctor_name} on {date} at {time} to cancel."
    except Exception as e:
        return f"❌ Error cancelling appointment: {str(e)}"




def show_user_appointments():
    if not os.path.exists(APPOINTMENT_FILE):
        return "📂 No appointments yet."
    with open(APPOINTMENT_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        data = list(reader)
        if not data:
            return "📂 No appointments yet."
        reply = "📅 Your Booked Appointments:\n"
        for row in data:
            reply += f"- {row[0]} with {row[1]} on {row[2]} at {row[3]}\n"
        return reply

if __name__ == "__main__":
    if not os.path.exists(APPOINTMENT_FILE):
        with open(APPOINTMENT_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Doctor", "Date", "Time"])
    app.run(debug=True)
