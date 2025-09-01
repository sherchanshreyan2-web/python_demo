import sqlite3

conn=sqlite3.connect('bipson_contact.db')

cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS contact
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL)''')
conn.commit()

def addContact():
    name=input("Enter name: ")
    email=input("Enter email: ")
    phone=int(input("Enter phone: "))
    cursor.execute("INSERT INTO contact (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    print("Contact added successfully!")
def ViewContact():
    cursor.execute("SELECT * FROM contact")
    rows=cursor.fetchall()
    for row in rows:
        print(f'ID: {row[0]} Name: {row[1]} Email: {row[2]} Phone: {row[3]}')
def UpdateContact():
    try:
        id=int(input("Enter the id of the contact you want to update: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    # check here if the id exists
    if checkExist(id)!=None:
        name=input("Enter new name: ")
        email=input("Enter new email: ")
        phone=int(input("Enter new phone: "))
        cursor.execute("UPDATE contact SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, id))
        conn.commit()
        print("Contact updated successfully!")
    else:
        print("Contact with this id does not exist.")
def DeleteContact():
    try:
        id=int(input("Enter the id of the contact you want to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if checkExist(id)!=None:
        cursor.execute("DELETE FROM contact WHERE id=?", (id,))
        conn.commit()
        print("Contact deleted successfully!")
    else:
        print("Contact With this id does not exist.")
def checkExist(id):
    cursor.execute("SELECT * FROM contact WHERE id=?", (id,))
    row=cursor.fetchone()
    return row
    ####


while True:
    print("Contact Management System")
    print("1.Add contact ")
    print("2.View contact ")
    print("3.Update contact ")
    print("4.Delete contact ")
    print("5.Exit ")
    try :
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    else:
        if (choice in (1,2,3,4,5)):
            if choice==1:
                addContact()
            elif choice==2:
                ViewContact()
            elif choice==3:
                UpdateContact()
            elif choice==4:
                DeleteContact()
            elif choice==5:
                break
            else:
                print("Invalid choice. Please try again.")
                continue
        else:
            print("Invalid choice. Please try again.")
print("Thank you for using the Contact Management System!")

