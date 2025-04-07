---

# 🏫 University Course Registration System

A full-featured Django web application that allows students to register, log in, enroll in courses, and manage academic data efficiently. Designed to simulate a real university registration portal with a secure, user-friendly interface.

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

![Screenshot 2025-04-06 220952](https://github.com/user-attachments/assets/1266b944-6ea3-49be-8196-28e5911d1deb)


## 🙌 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

