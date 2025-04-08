---

# 🏫 University Course Registration System

A full-featured Django web application that allows students to register, log in, enroll in courses, and manage academic data efficiently. Designed to simulate a real university registration portal with a secure, user-friendly interface. visit my youtube channel on this link https://youtu.be/q6cwcvhQ4-U to check the overview.

## 🚀 Features

- 🔐 **User Authentication**  
  Secure registration, login, and logout functionality for students and admins.

- 📝 **Course Enrollment**  
  Students can view available courses and enroll or drop them with ease.

- 🎓 **Student Dashboard**  
  Personalized dashboard showing enrolled courses, profile details, and course history.

- 🧑‍💼 **Admin Panel**  
  Admins can manage users, courses, and enrollment records via Django's built-in admin interface.

- 📅 **Academic Term Support**  
  System supports multiple semesters and tracks enrollment accordingly.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap 
- **Database**: SQLite 
- **Other**: Django Admin, Django Auth

## 📂 Project Structure

```
registration_system/
├── varsity/               # Main app with models, views, and templates
├── templates/          # HTML templates
├── static/             # CSS, JS, and images
├── db.sqlite3          # Default database
└── manage.py
```

## 🧪 How to Run Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ven-Sib/registration_system.git
   cd registration_system
   ```

2. **Create a virtual environment & install dependencies:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run migrations & start the server:**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. **Access the site:**
   Open `http://127.0.0.1:8000` in your browser.

## 📸 Screenshots


![Screenshot 2025-04-06 220901](https://github.com/user-attachments/assets/31ac9bb2-74ba-4aa1-a812-8cb23eb41377)
![Screenshot 2025-04-06 220921](https://github.com/user-attachments/assets/83889461-c89e-4e55-9c2b-f8393e61fb8d)
![Screenshot 2025-04-06 220940](https://github.com/user-attachments/assets/5208fa24-ca81-435a-bfc9-81d46c1210eb)
![Screenshot 2025-04-06 221423](https://github.com/user-attachments/assets/4d19d76e-af82-4114-a743-717200bcb477)
![Screenshot 2025-04-06 221004](https://github.com/user-attachments/assets/30601160-c8d6-4ff3-82b8-7b33eba67adc)







## 🙌 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

