# 🔐 Smart Password Generator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

<br/>

**A modern, secure, and customizable password generator with real-time strength analysis, SQLite history tracking, and Streamlit Cloud support.**

[Key Features](#-features) • [Streamlit Deployment](#-how-to-deploy-to-streamlit-cloud) • [Local Setup](#-local-setup) • [Project Structure](#-project-structure) • [Database](#-database-schema)

</div>

---

## 📖 Overview

**Smart Password Generator** provides an interactive and secure way to create cryptographically random passwords tailored to any complexity requirement. It comes equipped with both a **Streamlit Web App** (ready for one-click cloud deployment) and a classic **Flask Web App**.

---

## ✨ Features

- ⚙️ **Customizable Character Sets**: Toggle Alphabets (Uppercase & Lowercase), Numbers, and Special Characters.
- 📏 **Adjustable Password Length**: Configure length easily via sliders (4 to 32 characters).
- 🎚️ **Difficulty Presets**: Simple, Hard, Difficult, and Very Difficult quick presets.
- 📊 **Live Strength Meter**: Real-time evaluation (Weak, Moderate, Strong, Very Strong).
- 📋 **One-Click Copy**: Instant clipboard copying.
- 💾 **SQLite History Tracking**: Automatically stores generated passwords with timestamps and metadata.
- ☁️ **Streamlit Cloud Ready**: Zero-config deployment via GitHub and Streamlit Community Cloud.

---

## 🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Core application logic & password generation engine |
| **Streamlit** | Interactive modern data/web application UI |
| **Flask** | Classic lightweight backend server alternative |
| **SQLite3** | Embedded database for storing password generation logs |

---

## ☁️ How to Deploy to Streamlit Cloud

You can host and upload this app to **Streamlit Community Cloud** completely free in 3 simple steps:

### Step 1: Push Code to GitHub
1. Create a new repository on [GitHub](https://github.com).
2. Push your project files to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Streamlit Password Generator"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   git push -u origin main
   ```

### Step 2: Connect to Streamlit Community Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.
2. Click **"New app"** (or **"Create app"**).

### Step 3: Configure and Deploy
1. **Repository**: Select your newly created repository.
2. **Branch**: `main`
3. **Main file path**: `streamlit_app.py`
4. Click **Deploy!** 🚀

Streamlit Cloud will read `requirements.txt`, install dependencies, and give you a live shareable URL!

---

## 🚀 Local Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run with Streamlit (Recommended)

```bash
streamlit run streamlit_app.py
```

### 3. (Alternative) Run with Flask

```bash
pip install flask
python app.py
```

---

## 📁 Project Structure

```bash
website tanish/
│
├── 📄 streamlit_app.py    # Streamlit interactive application & UI
├── 📄 requirements.txt    # Project dependencies for Streamlit Cloud
├── 🗄️ passwords.db         # SQLite database storing generation history
│
├── 📄 app.py              # Flask server alternative
├── 📂 templates/
│   └── 📄 index.html      # Flask HTML template
├── 📂 static/
│   └── 📄 style.css       # Flask CSS stylesheet
│
└── 📄 README.md           # Documentation & deployment guide
```

---

## 🗄️ Database Schema

The SQLite database (`passwords.db`) contains the table `generated_passwords`:

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | `INTEGER PRIMARY KEY` | Auto-incremented unique ID |
| `difficulty` | `TEXT` | Difficulty level classification |
| `length` | `INTEGER` | Length of generated password |
| `password` | `TEXT` | Generated password string |
| `created_at` | `TEXT` | Timestamp when password was created |

---

## 👤 Author

Developed with ❤️ by **Tanish**.
