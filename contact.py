import sqlite3

def id_exists(x):
    cursor.execute("SELECT 1 FROM contacts WHERE id = ?", (x,))
    return cursor.fetchone() is not None

def add_contact():
    first= input("\nEnter the first name:")
    last= input("Enter the last name:")
    email= input("Enter the email:")
    phone= int(input("Enter the Phone number:"))
    cursor.execute("INSERT INTO contacts(first,last, email, phone) VALUES(?,?,?,?)", (first, last, email, phone))
    conn.commit()

def view_contact():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    for row in rows:
        print(f'\nID:{row[0]}, First:{row[1]}, last:{row[2]}, Email:{row[3]}, Phone:{row[4]}')

def update_contact():
    UserID= input("Which ID do u want to update?:\t")
    cursor.execute("SELECT * FROM contacts WHERE id=(?)", (UserID))
    if not id_exists(UserID):
        print(f"No contact found with ID {UserID}")
    else:
        print("You can change the details here:\n")
        new_first= input("Enter the first name:")
        new_last= input("\nEnter the last name:")
        new_email= input("\nEnter the new email:")
        new_phone= int(input("\nEnter the new Number:"))
        cursor.execute("UPDATE contacts SET first=(?), last= (?), email=(?), phone=(?) WHERE id=(?)",(new_first,new_last,new_email,new_phone, UserID))
        conn.commit()
        print("\nYour contact has been updated successfully")

        
def delete_contact():
    print("Which contact do you want to delete?")
    try:
        w= int(input("Enter the ID no.:"))
    except ValueError:
        print("Please Enter an ID")
    cursor.execute(f"DELETE FROM contacts WHERE id=?",(w,))
    conn.commit()
    print(f"Contact with ID {w} deleted (if it existed).")


conn= sqlite3.connect("contact.db")
cursor= conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY NOT NULL,
    first TEXT,
    last TEXT,
    email TEXT, 
    phone INTEGER
    )
''')
print("Welcome to the contact list\n")

while True:
    print("-----CONTACT MANAGEMENT-----")
    print("\n1. Add contact \n 2.View contact \n3.Update contact \n 4. Delete contact \n5.Exit ")
    i=int(input("What do you want to do ?"))
    if i==1:
      add_contact()
    elif i==2:
        view_contact()
    elif i==3:
        update_contact()
    elif i==4:
        delete_contact()
    else:
      break
            

