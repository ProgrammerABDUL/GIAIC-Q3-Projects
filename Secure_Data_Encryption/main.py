import streamlit as st
from cryptography.fernet import Fernet
import hashlib

# -----------------------
# 🔧 Page Setup
# -----------------------
st.set_page_config(page_title="Secure Data Encryption", page_icon="🔐")

# Show intro message only once
if 'show_intro' not in st.session_state:
    st.session_state.show_intro = True

# -------------------- 📢 Intro Message --------------------
if st.session_state.show_intro:
    st.title("🔐 Secure Data Vault")
    st.markdown("""
    Welcome to **Secure Data Vault** – your private digital safe for confidential notes and information.  
    🔒 Encrypt your messages with a secret passkey.  
    🧠 Only you can decrypt it – even we can't peek inside.  
    👉🏻 Create an account or log in to get started!
    """)
    
    if st.button("Get Started"):
        st.session_state.show_intro = False
        st.session_state.page = "login"
        st.rerun()
    st.stop()  # Pause app here until user clicks "Get Started"

# -----------------------
# 🔐 Initialize Session State
# -----------------------
# Generate encryption key (used for encrypting data)
if 'fernet_key' not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()
fernet = Fernet(st.session_state.fernet_key)

# Store all encrypted data
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}

# Track failed decryption attempts
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

# Authorization flag to block retrieval after 3 failed attempts
if 'authorized' not in st.session_state:
    st.session_state.authorized = True

# Default landing page
if 'page' not in st.session_state:
    st.session_state.page = "login"

# Default user database (can be later connected with JSON persistence)
if 'users' not in st.session_state:
    st.session_state.users = {"admin": hashlib.sha256("admin".encode()).hexdigest()}

# Tracks currently logged-in user
if 'logged_user' not in st.session_state:
    st.session_state.logged_user = None

# -----------------------
# 🔑 Hashing Utility
# -----------------------
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# -----------------------
# 🔐 Login Page
# -----------------------
def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.warning("Please enter both username and password.")
        elif username in st.session_state.users and hash_passkey(password) == st.session_state.users[username]:
            st.session_state.logged_user = username
            st.session_state.authorized = True
            st.session_state.failed_attempts = 0
            st.session_state.page = "home"
            st.rerun()
        else:
            st.error("Invalid credentials.")

    if st.button("Don't have an account? Register"):
        st.session_state.page = "register"
        st.rerun()

# -----------------------
# 📝 Register Page
# -----------------------
def register():
    st.title("📝 Register")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Register"):
        if not username or not password:
            st.warning("Please enter both username and password.")
        elif username in st.session_state.users:
            st.warning("Username already exists.")
        else:
            st.session_state.users[username] = hash_passkey(password)
            st.success("Registered! Please log in.")
            st.session_state.page = "login"
            st.rerun()

    if st.button("Already have an account? Login"):
        st.session_state.page = "login"
        st.rerun()

# -----------------------
# 🏠 Home Page
# -----------------------
def home():
    st.title("🏠 Secure Data Encryption")

    st.write(f"Welcome, **{st.session_state.logged_user}**")

    # Show warning if redirected after failed attempts
    if st.session_state.get("logout_reason"):
        st.warning(st.session_state.logout_reason)
        del st.session_state.logout_reason

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Store Data"):
            st.session_state.page = "store"
            st.rerun()
    with col2:
        if st.button("🔍 Retrieve Data"):
            if st.session_state.failed_attempts >= 3:
                st.session_state.authorized = False
                st.session_state.page = "login"
            else:
                st.session_state.page = "retrieve"
            st.rerun()

    # Logout option
    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.logged_user = None
        st.session_state.page = "login"
        st.rerun()

# -----------------------
# 💾 Store Data Page
# -----------------------
def store_data():
    st.title("➕ Store Data")

    text = st.text_area("Enter the text you want to store")
    passkey = st.text_input("Enter a passkey to secure your data", type="password")
    identifier = st.text_input("Enter a unique identifier")

    if st.button("Encrypt & Store"):
        if not text or not passkey or not identifier:
            st.warning("Please fill all fields.")
        elif identifier in st.session_state.stored_data:
            st.warning("Identifier already exists.")
        else:
            encrypted = fernet.encrypt(text.encode()).decode()
            hashed_key = hash_passkey(passkey)
            st.session_state.stored_data[identifier] = {
                "encrypted_text": encrypted,
                "passkey": hashed_key,
                "owner": st.session_state.logged_user
            }
            st.success("Data encrypted and stored!")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# -----------------------
# 🔍 Retrieve Data Page
# -----------------------
def retrieve_data():
    st.title("🔍 Retrieve Data")

    identifier = st.text_input("Enter your data identifier")
    passkey = st.text_input("Enter your passkey", type="password")

    if st.button("Decrypt & Retrieve"):
        entry = st.session_state.stored_data.get(identifier)

        # Validate access
        if not entry or entry['owner'] != st.session_state.logged_user:
            st.error("No data found for this identifier.")
        else:
            if hash_passkey(passkey) == entry["passkey"]:
                decrypted = fernet.decrypt(entry["encrypted_text"].encode()).decode()
                st.success("Decryption successful!")
                st.text_area("Your data:", decrypted, height=150)
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                st.error(f"Incorrect passkey. Attempt {st.session_state.failed_attempts}/3.")

                # Lock out after 3 failed attempts
                if st.session_state.failed_attempts >= 3:
                    st.session_state.logout_reason = "⚠️ 3 failed attempts. You've been redirected to the vault for security reason."
                    st.session_state.authorized = False
                    st.session_state.page = "home"
                    st.rerun()

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()

# -----------------------
# 🔀 Page Controller
# -----------------------
if st.session_state.logged_user is None:
    if st.session_state.page == "login":
        if st.session_state.get("show_intro", False):
            st.title("🔐 Welcome to Secure Data Encryption App")
            st.markdown("This app allows you to safely store and retrieve sensitive data using encryption. Keep your secrets secure! 🔒")
            st.session_state.show_intro = False

        if "logout_reason" in st.session_state:
            st.warning(st.session_state.logout_reason)
            del st.session_state.logout_reason

        login()

    elif st.session_state.page == "register":
        register()
else:
    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "store":
        store_data()
    elif st.session_state.page == "retrieve":
        if st.session_state.authorized:
            retrieve_data()
        else:
            st.session_state.page = "login"
            st.rerun()
