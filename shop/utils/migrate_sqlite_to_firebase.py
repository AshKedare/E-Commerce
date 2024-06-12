import sqlite3
from firebase_admin import auth, credentials, initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate('shop/credentials/ecom-firebse.json')
firebase_app = initialize_app(cred)

# Connect to SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Retrieve user data from SQLite database
cursor.execute('SELECT username, email, password FROM auth_user')
users = cursor.fetchall()

# Iterate over users and create accounts in Firebase Authentication
for user in users:
    username, email, password = user
    try:
        user_record = auth.create_user(
            email=email,
            password=password,
            display_name=username
        )
        print(f'User {email} created successfully')
    except Exception as e:
        print(f'Error creating user {email}: {e}')

# Close database connection
conn.close()
