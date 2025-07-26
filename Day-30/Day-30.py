
import sqlite3
import hashlib
import getpass


# =====================================>>

# Database se connection h

# =====================================>>

conn = sqlite3.connect("users.db")
current_user = None
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        is_logged_in INTEGER DEFAULT 0
    )
''')
conn.commit()

# ==========================================>>

#  USER  REGIStration

# ===========================================>>

def register():
    username = input("Enter your NAme:\n")
    password = input("Enter your password:\n")

    # CHECK USER Already h ya nhi

    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cur.fetchone():
        print("❌ Username already exists. Try another.")
        return
    else:
        print("Registration Pending.......:\n")
        print("You are almost here.....\n")

    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

    cur.execute(
        "INSERT INTO users (username, password, is_logged_in) VALUES (?, ?, 0)",
        (username, hashed_pwd)
    )
    conn.commit()

    print("Registration Successful!")


# ================================================>>

#   User Login function create kerna

# ================================================>>

def login():
    global current_user

    username = input("Enter your Name:\n")
    password = input("Enter your Password:\n")

    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cur.fetchone()

    if not row:
        print("User doesn't exist. Please register first.")
        return
    db_password = row[1]
    is_logged_in = row[2]

    hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
    if hashed_pwd != db_password:
        print("Password incorrect.")
        return
    if is_logged_in == 1:
        print("You are already logged in.")
        current_user = username
    cur.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
    conn.commit()

    current_user = username
    print("Login Successful!")


# =========================================================>>

#  LOGOUT KO DEFINE KERNA

# ==========================================================>>

def logout():
    global current_user

    if not current_user:
        print("You are not log in this website....\n")
    else:
        cur.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (current_user,))
        conn.commit()
        print(f"{current_user} successfully logged out.")
        current_user = None

# ============================================================>>

# Pass change kerna

# ============================================================>>

def change_password():
    global current_user
    if not current_user:
        print("❌ Pehle login karo.")
        return

    current_pwd = input("Current password: ")
    cur.execute("SELECT password FROM users WHERE username = ?", (current_user,))
    stored_pwd = cur.fetchone()[0]

    if hashlib.sha256(current_pwd.encode()).hexdigest() != stored_pwd:
        print("❌ Galat password.")
        return

    new_pwd = input("Naya password: ")
    confirm_pwd = input("Confirm password: ")

    if new_pwd != confirm_pwd:
        print("❌ Password match nahi kar rahe.")
        return

    hashed_new = hashlib.sha256(new_pwd.encode()).hexdigest()
    cur.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_new, current_user))
    conn.commit()
    print("✅ Password change ho gaya.")




# ================================================================>>

#  Main  function ko call kerna

# =================================================================>>

def menu():
    while True:
        print("\n===== USER MANAGEMENT MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Change Password")
        print("5. Exit")
        choice = input("Choose any option (1-5): ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            change_password()
        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("Invalid Choice  Try Again!\n")

menu()