import streamlit as st
import random
import string
import sqlite3
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Smart Password Generator",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Custom Styling ---
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .password-display {
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.4rem;
        font-weight: 600;
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid #3b82f6;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: #38bdf8;
        letter-spacing: 2px;
        word-break: break-all;
        margin-bottom: 15px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)


# --- Database Functions ---
def init_db():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS generated_passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            difficulty TEXT,
            length INTEGER,
            password TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()


def save_password(difficulty, length, password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO generated_passwords (difficulty, length, password, created_at)
        VALUES (?, ?, ?, ?)
    ''', (difficulty, length, password, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()


def fetch_history(limit=10):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT difficulty, length, password, created_at 
        FROM generated_passwords 
        ORDER BY id DESC 
        LIMIT ?
    ''', (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def clear_history():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM generated_passwords')
    conn.commit()
    conn.close()


init_db()


# --- Password Generation Logic ---
def generate_password(length, use_letters, use_numbers, use_special):
    chars = ""
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}"

    if not chars:
        return None

    return ''.join(random.choice(chars) for _ in range(length))


def calculate_strength(pwd):
    if not pwd:
        return 0, "No password", "#64748b"
    score = 0
    if len(pwd) >= 8:
        score += 1
    if len(pwd) >= 14:
        score += 1
    if any(c.islower() for c in pwd) and any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}" for c in pwd):
        score += 1

    if score <= 2:
        return 25, "Weak ⚠️", "#ef4444"
    elif score == 3:
        return 50, "Moderate 🟡", "#f59e0b"
    elif score == 4:
        return 75, "Strong 🟢", "#10b981"
    else:
        return 100, "Very Strong 🛡️", "#06b6d4"


# --- Header ---
st.markdown('<div class="main-title">🔐 Smart Password Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Generate cryptographically secure & customizable passwords instantly</div>', unsafe_allow_html=True)

# --- Configuration Section ---
with st.container():
    st.subheader("⚙️ Configuration")
    
    col_preset, col_length = st.columns([1, 1])
    with col_preset:
        difficulty = st.selectbox(
            "Difficulty Preset",
            ["Custom", "Simple", "Hard", "Difficult", "Very Difficult"],
            index=0
        )
    
    # Preset presets logic
    default_length = 12
    default_letters = True
    default_numbers = True
    default_special = True

    if difficulty == "Simple":
        default_length = 8
        default_letters = True
        default_numbers = False
        default_special = False
    elif difficulty == "Hard":
        default_length = 12
        default_letters = True
        default_numbers = True
        default_special = False
    elif difficulty == "Difficult":
        default_length = 16
        default_letters = True
        default_numbers = True
        default_special = True
    elif difficulty == "Very Difficult":
        default_length = 24
        default_letters = True
        default_numbers = True
        default_special = True

    with col_length:
        length = st.slider("Password Length", min_value=4, max_value=32, value=default_length)

    st.write("Included Character Sets:")
    c1, c2, c3 = st.columns(3)
    with c1:
        include_letters = st.checkbox("🔤 Alphabets (A-Z, a-z)", value=default_letters)
    with c2:
        include_numbers = st.checkbox("🔢 Numbers (0-9)", value=default_numbers)
    with c3:
        include_special = st.checkbox("✨ Special Symbols (!@#$)", value=default_special)

# --- Session State for Password ---
if "current_password" not in st.session_state:
    st.session_state.current_password = ""

st.divider()

# --- Generate Action ---
if st.button("🚀 Generate Password", type="primary"):
    if not (include_letters or include_numbers or include_special):
        st.error("⚠️ Please select at least one character type!")
    else:
        new_pwd = generate_password(length, include_letters, include_numbers, include_special)
        st.session_state.current_password = new_pwd
        save_password(difficulty, length, new_pwd)
        st.toast("New password generated and saved to history!", icon="🔑")

# --- Display Output ---
if st.session_state.current_password:
    st.markdown("### 🔑 Generated Password")
    st.code(st.session_state.current_password, language="")

    # Strength Indicator
    progress, label, color = calculate_strength(st.session_state.current_password)
    st.write(f"**Security Strength:** {label}")
    st.progress(progress / 100)

st.divider()

# --- History Section ---
with st.expander("📜 Password History (Recent 10)"):
    history = fetch_history(10)
    if history:
        for item in history:
            diff, lgth, pwd, dt = item
            st.markdown(f"**`{pwd}`** — *{diff} ({lgth} chars)* • `{dt}`")
        
        if st.button("🗑️ Clear History"):
            clear_history()
            st.rerun()
    else:
        st.info("No passwords generated yet.")
