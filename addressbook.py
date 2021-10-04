import sqlite3


from prettytable import PrettyTable
from prettytable import from_db_cursor

addressbookmenu = PrettyTable([' By : Omid Mohajerani '])
addressbookmenu.add_row(['omid.mohajerani@gmail.com'])
print(addressbookmenu.get_string(title="Welcome to Address Book Program"))



while True:
    addressbookmenu = PrettyTable(['Option', 'Action'])
    addressbookmenu.add_row(['1','List all contacts'])
    addressbookmenu.add_row(['2','Search in contacts'])
    addressbookmenu.add_row(['3','Edit a contact   '])
    addressbookmenu.add_row(['4','Delete a contact '])
    addressbookmenu.add_row(['5','Exit             '])
    # print(addressbookmenu)
    print(addressbookmenu.get_string(title=" Main Menu "))
    userinput = input("Please select an option: ")
    menuoptions = ['1','2','3','4','5']
    if userinput not in menuoptions:
        print("You can choose between options 1 to 5 - Exiting ...")
        exit()
    elif userinput == '1':
        print("List of all contacts in you addressbook")
        connection = sqlite3.connect("addressbook.db")
        cursor = connection.cursor()
        mytable = from_db_cursor(cursor)
        cursor.execute(
        "SELECT id, name, phone FROM contacts"
        )
        addressbooktable = from_db_cursor(cursor)
        print(addressbooktable.get_string(title=" Contact list  "))
        connection.commit()
        connection.close()
    elif userinput == '2':
        searchinput = input("Please enter name or phone number:  ")
        connection = sqlite3.connect("addressbook.db")
        cursor = connection.cursor()
        select_query = f'SELECT id, name, phone FROM contacts WHERE name = "{searchinput}" or phone = "{searchinput}"'
        rows = cursor.execute(select_query).fetchall()
        if len(rows) == 0:
            print("\nNo contact Found!!!\n")
        else:
            print("\nContact Found:")
            addressbooktable = PrettyTable(['id', 'Name', 'Phone'])
            for row in rows:
                id = row[0]
                name = row[1]
                phone = row[2]
                addressbooktable.add_row([id, name, phone])
            print(addressbooktable.get_string(title=" Search list  "))
    elif userinput == '3':
        editinput = input("Please enter id to edit or back to go to the main menu:  ")
    elif userinput == '4':
        editinput = input("Please enter id to delete or back to go to the main menu:  ")






    elif userinput == '5':
        exit()



# cursor.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, phone TEXT)")
# #
# cursor.execute("INSERT INTO contacts (name,phone) VALUES ('Amin Mohajerani', '0175641214')")
# cursor.execute("INSERT INTO contacts (name,phone) VALUES ('Mahboob Maleki', '0175641111')")
# #
#
# name = 'Mahboob Maleki'
#

#
# mytable = from_db_cursor(cursor)
#
# # rows = cursor.execute(
# #     "SELECT id, name, phone FROM contacts"
# # ).fetchall()
#
# cursor.execute(
#     "SELECT id, name, phone FROM contacts"
# )
#
# addressbooktable = from_db_cursor(cursor)

# print(rows)
#
# addressbooktable = PrettyTable(['id', 'Name', 'Phone'])
# for row in rows:
#     id = row[0]
#     name = row[1]
#     phone = row[2]
#     addressbooktable.add_row([id, name, phone])
# print(addressbooktable)

# print(addressbooktable)

#
#
# phone = "0175649737"
# name = "Omid Mohajerani"
# cursor.execute(
#     "UPDATE contacts SET phone = ? WHERE name = ?",
#     (phone, name)
# )
#
# #
# name = "Omid Mohajerani"
# cursor.execute(
#     "DELETE FROM contacts WHERE name = ?",
#     (name,)
# )
