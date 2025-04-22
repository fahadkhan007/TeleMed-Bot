# 💬 TeleMed ChatBot

An AI-powered chatbot built with Flask that helps users schedule, view, and cancel telemedicine appointments. It uses a simple yet effective interface powered by Tailwind CSS and stores data in CSV and JSON files.

<!-- replace with actual path if needed -->
![AI_project_scnshot](https://github.com/user-attachments/assets/5ff6399b-9e5f-42a1-9394-fe6df67b45c7)

---

## 🚀 Features

- ✅ Book appointments with available doctors
- 🗓️ View your upcoming appointments
- ❌ Cancel existing bookings with a simple command
- 🤖 Intelligent command-based conversation
- 💾 Data stored in CSV (appointments) and JSON (doctors)
- 🎨 Clean and modern UI using Tailwind CSS

---

## 🛠️ Technologies Used

- **Python** 🐍
- **Flask** for backend
- **Tailwind CSS** for frontend UI
- **HTML + JS** for user interaction
- **CSV & JSON** for lightweight data handling

---

## 📁 Project Structure

telemed_bot/ │ ├── chatbot.py # Main Flask app ├── templates/ │ └── index.html # Frontend UI ├── static/ │ └── styles.css # Optional styling (Tailwind is CDN based) ├── data/ │ ├── doctors.json # List of doctors & slots │ └── appointments.csv # Booked appointments └── README.md



---

## 📦 Setup Instructions

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/telemed-chatbot.git
   cd telemed-chatbot
Install dependencies:

bash
Copy
Edit
pip install flask
Run the app:

bash
Copy
Edit
python chatbot.py
Open in browser: http://127.0.0.1:5000

🗨️ How to Use
Type any of the following in the chat box:

book, Dr. Sharma, 2025-06-03, 10:00

my appointments

cancel, Dr. Sharma, 2025-06-03, 10:00

📌 Future Improvements
Add authentication for users

Use a proper database (SQLite or MongoDB)

Real-time chat with WebSockets

Doctor availability auto-update

📸 Screenshots

<!-- Add screenshots here -->
💻 Simple UI with modern design
📆 Booked appointments list
🗑️ Cancel functionality with error handling

🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📃 License
MIT License © 2025 Fahad Khan


---

