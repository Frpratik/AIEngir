# 🔐 Django Authentication System (Email + OTP + Session)

A simple **Django + DRF authentication system** that supports **registration with OTP verification**, login, logout, CSRF-protected API calls, and a minimal **HTML UI** for testing.  

---

## 📌 Features
- ✅ **User Registration** – Users register with email & password  
- ✅ **Email OTP Verification** – Email is verified via a 6-digit OTP  
- ✅ **Login with Session** – Secure login using Django sessions  
- ✅ **CSRF Protection** – All API calls require CSRF token  
- ✅ **Get Logged-in User** – `/api/me/` endpoint to fetch current user  
- ✅ **Logout** – Secure logout with CSRF protection  
- ✅ **Minimal Frontend UI** – Simple HTML + CSS interface to test the APIs easily  

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework (DRF)  
- **Frontend:** Plain HTML, CSS, JavaScript (no external lib)  
- **Database:** SQLite (can be replaced with PostgreSQL/MySQL)  
- **Email:** Console backend (can be configured for SMTP)  

---

## 📂 Project Structure
```
📦 your_project/
┣ 📂 Authentication_app/
┃ ┣ 📜 models.py # Custom User model with email login + OTP
┃ ┣ 📜 serializers.py # DRF serializers for register, verify, login
┃ ┣ 📜 views.py # API Views for Register, Verify, Login, Me, Logout
┃ ┗ 📜 urls.py # Authentication-related API routes
┣ 📂 templates/
┃ ┗ 📜 auth.html # Simple UI for Register → Verify → Login → Actions
┣ 📜 settings.py # Config (AUTH_USER_MODEL, EMAIL_BACKEND, CSRF, etc.)
┗ 📜 README.md # Project Documentation
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repo
- git clone [https://github.com/Frpratik/AIEngir.git](https://github.com/Frpratik/AIEngir.git)
- cd your-repo


### 2️⃣ Create Virtual Environment & Install Dependencies
- python -m venv venv
- source venv/bin/activate # Linux / Mac
- venv\Scripts\activate # Windows
- pip install -r requirements.txt


### 3️⃣ Run Migrations
- python manage.py makemigrations
- python manage.py migrate


### 4️⃣ Run Server
- python manage.py runserver


---

## 🔗 API Endpoints

| Endpoint              | Method | Auth Required | Description                         |
|-----------------------|--------|---------------|-------------------------------------|
| `/api/register/`      | POST   | ❌ No         | Register new user (email, password) |
| `/api/register/verify/` | POST | ❌ No         | Verify email using OTP              |
| `/api/login/`         | POST   | ❌ No         | Login user (sets session + CSRF)    |
| `/api/me/`            | GET    | ✅ Yes        | Get logged-in user's details        |
| `/api/logout/`        | POST   | ✅ Yes        | Logout user (delete session)        |
| `/api/get_csrf/`      | GET    | ❌ No         | Get CSRF token for frontend use     |

---

## 🎨 Frontend UI
- Located at `templates/auth.html`  
- Provides a tab-based interface for **Register → Verify → Login → Actions**  
- Uses `fetch()` with `credentials: "include"` to maintain sessions  
- Handles CSRF token fetching automatically  

---

## 🧪 Testing Flow
1. **Register** – Enter email + password → You will see *"OTP Sent"*  
2. **Check Console** – OTP will appear in terminal (console email backend)  
3. **Verify** – Enter email + OTP → You will see *"Verified"*  
4. **Login** – Enter email + password → You will see *"Logged in"*  
5. **Get Me** – Click *Get Me* to see logged-in user details  
6. **Logout** – Click *Logout* to end the session  

---

## ⚙️ Settings Highlights
- AUTH_USER_MODEL = "Authentication_app.User"
- EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

✅ Replace `EMAIL_BACKEND` with SMTP in production.

---

## 👨‍💻 Author
**Pratik Ghuge**  
💼 Software Developer | 💻 Python Backend Engineer  
🔗 [LinkedIn](https://www.linkedin.com/in/pratik-ghuge1926)  
📍 Mumbai, India  


---
