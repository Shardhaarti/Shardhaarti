import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database Setup
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Set your MySQL root password if any
    database="CrimeDB"
)
cursor = conn.cursor()

# Create Database and Tables if not exist
cursor.execute("""
CREATE DATABASE IF NOT EXISTS CrimeDB;
""")
cursor.execute("USE CrimeDB;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    role ENUM('Victim', 'Officer', 'Admin') NOT NULL,
    contact_info VARCHAR(100),
    address TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Crimes (
    crime_id INT AUTO_INCREMENT PRIMARY KEY,
    crime_type VARCHAR(50) NOT NULL,
    description TEXT,
    location VARCHAR(100),
    date_reported DATE,
    time_reported TIME,
    reporter_id INT,
    FOREIGN KEY (reporter_id) REFERENCES Users(user_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Suspects (
    suspect_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    status ENUM('Arrested', 'Wanted', 'Cleared') DEFAULT 'Wanted',
    associated_crime_id INT,
    FOREIGN KEY (associated_crime_id) REFERENCES Crimes(crime_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Witnesses (
    witness_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    contact_info VARCHAR(100),
    statement TEXT,
    crime_id INT,
    FOREIGN KEY (crime_id) REFERENCES Crimes(crime_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Evidence (
    evidence_id INT AUTO_INCREMENT PRIMARY KEY,
    evidence_type VARCHAR(100),
    description TEXT,
    storage_location VARCHAR(100),
    crime_id INT,
    date_collected DATE,
    FOREIGN KEY (crime_id) REFERENCES Crimes(crime_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CaseStatus (
    case_id INT AUTO_INCREMENT PRIMARY KEY,
    crime_id INT,
    officer_id INT,
    status ENUM('Open', 'Under Investigation', 'Closed') DEFAULT 'Open',
    last_updated DATE,
    FOREIGN KEY (crime_id) REFERENCES Crimes(crime_id),
    FOREIGN KEY (officer_id) REFERENCES Users(user_id)
);
""")

# Insert Sample Users if empty
cursor.execute("SELECT COUNT(*) FROM Users")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO Users (full_name, role, contact_info, address) VALUES
    ('Ali Khan', 'Victim', 'ali@email.com', 'Karachi'),
    ('Inspector Zara', 'Officer', 'zara@police.pk', 'Lahore'),
    ('Admin Ahmed', 'Admin', 'admin@system.com', 'Islamabad');
    """)
    conn.commit()

# GUI
root = tk.Tk()
root.title("Crime Reporting System")
root.geometry("400x500")

# Form Labels and Entry Widgets
tk.Label(root, text="Crime Type").pack()
crime_type = tk.Entry(root)
crime_type.pack()

tk.Label(root, text="Description").pack()
description = tk.Entry(root)
description.pack()

tk.Label(root, text="Location").pack()
location = tk.Entry(root)
location.pack()

tk.Label(root, text="Date Reported (YYYY-MM-DD)").pack()
date_reported = tk.Entry(root)
date_reported.pack()

tk.Label(root, text="Time Reported (HH:MM:SS)").pack()
time_reported = tk.Entry(root)
time_reported.pack()

tk.Label(root, text="Reporter ID").pack()
reporter_id = tk.Entry(root)
reporter_id.pack()

def add_crime():
    try:
        sql = """
        INSERT INTO Crimes (crime_type, description, location, date_reported, time_reported, reporter_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (
            crime_type.get(),
            description.get(),
            location.get(),
            date_reported.get(),
            time_reported.get(),
            reporter_id.get()
        )
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Success", "Crime Added Successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Submit Button
tk.Button(root, text="Add Crime", command=add_crime).pack(pady=20)

root.mainloop()

# Close connection on exit
cursor.close()
conn.close()
