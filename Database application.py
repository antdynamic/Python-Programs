from tkinter import *
from tkinter import ttk
import mysql.connector
import tkinter.messagebox as MessageBox


def insert():
    id = str(entry_id.get())
    name = str(entry_name.get())
    address = str(entry_address.get())
    email = str(entry_email.get())
    DOB = str(f'{combo_day.get()}/{combo_month.get()}/{combo_year.get()}')
    phone_no = str(entry_mobno.get())
    print(id, name, address, email, DOB, phone_no)
    if name == "" or address == "" or email == "" or DOB == "" or phone_no == "" or id =="":
        MessageBox.showinfo("Insert Status", "All fields are required!")

    else:
        con = mysql.connector.connect(host="localhost", user="root", passwd="@nkit2004", database="Student")
        cursor = con.cursor()
        cursor.execute("insert into student values ('" + str(id) + "','" + name + " ',' " + address + "','" + email + "', '" + DOB + "', '" + phone_no + "')")
        cursor.execute("commit")
        show()

        MessageBox.showinfo("Insert status", "Inserted Successfully")
        con.close()
        entry_id.delete(0, END)
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        entry_address.delete(0, END)
        entry_mobno.delete(0, END)
        combo_day.delete(0, END)
        combo_month.delete(0, END)
        combo_year.delete(0, END)


def delete():
    if entry_id.get() == "":
        MessageBox.showinfo("Delete Status", "ID is compulsory to delete!")

    else:
        con = mysql.connector.connect(host="localhost", user="root", passwd="@nkit2004", database="Student")
        cursor = con.cursor()
        cursor.execute("delete from student where id='" + entry_id.get() + "'")
        cursor.execute("commit")
        show()

        MessageBox.showinfo("Delete status", "Deleted Successfully")
        con.close()
        entry_id.delete(0, END)
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        entry_address.delete(0, END)
        entry_mobno.delete(0, END)
        combo_day.delete(0, END)
        combo_month.delete(0, END)
        combo_year.delete(0, END)


def cancel():
    if entry_id == "" or entry_name == "" or entry_address == "" or entry_email == "" or entry_mobno == "" or combo_day == "" or combo_month == "" or combo_year == "":
        MessageBox.showinfo("Cancel Status", "Entry widget are empty")

    # elif combo_day.get() == "Select day" or combo_month.get() == "Select Month" or combo_year.get() == "Select Year":
    #     MessageBox.showinfo("Cancel Status", "Entry widget are empty")

    # elif combo_day.get != "Select day":
    #     combo_day.delete(0, END)
    #
    # elif combo_month.get != "Select Month":
    #     combo_month.delete(0, END)
    # elif combo_year.get() != "Select Year":
    #     combo_year.delete(0, END)
    else:
        entry_id.delete(0, END)
        entry_name.delete(0, END)
        entry_email.delete(0, END)
        entry_address.delete(0, END)
        entry_mobno.delete(0, END)
        combo_day.delete(0, END)
        combo_month.delete(0, END)
        combo_year.delete(0, END)
        combo_day.insert(str(day[0]))
        combo_month.insert(str(month[0]))
        combo_year.insert(str(year[0]))


def fetch():
    if entry_id.get() == "":
        MessageBox.showinfo("Fetch Status", "ID is compulsory to fetch data!")

    else:
        con = mysql.connector.connect(host="localhost", user="root", passwd="@nkit2004", database="Student")
        cursor = con.cursor()
        cursor.execute("select * from student where id='" + entry_id.get() + "'")
        rows = cursor.fetchall()
        combo_day.delete(0, END)
        combo_month.delete(0, END)
        combo_year.delete(0, END)
        show()

        for row in rows:
            entry_name.insert(0, row[1])
            entry_address.insert(0, row[2])
            entry_email.insert(0, row[3])
            combo_day.insert(0, row[4])
            combo_month.insert(0, row[4])
            combo_year.insert(0, row[4])
            entry_mobno.insert(0, row[5])
        print(cursor.fetchall())

        MessageBox.showinfo("fetch status", "fetched Successfully")
        con.close()


def show():
    con = mysql.connector.connect(host="localhost", user="root", passwd="@nkit2004", database="Student")
    cursor = con.cursor()
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    data_list.delete(0, data_list.size())

    for row in rows:
        insert_data = str(row[0]) + ' --- ' + row[1] + ' --- ' + row[2] + ' --- ' + row[3] + ' --- ' + row[4] + ' --- ' + row[5]
        data_list.insert(data_list.size()+1, insert_data)

    con.close()


root = Tk()
root.title("Database app")
root.iconbitmap('D:\Images\ICONS\Database.ico')
root.geometry("1920x1080")
canvas = Canvas(root, height=1080, width=1920, bg="light green")
canvas.grid(columnspan=50, rowspan=15)


# label_one = Label(root, text=" # Please Enter your Info. to Insert into Database:-", font=('Bahnschrift', 20))
# label_one.grid(row=0, column=0)
label_id = Label(root, text="ID", font=('Calibri', 15))
label_id.grid(row=1, column=0)
label_name = Label(root, text="Name: ", font=('Calibri', 15))
label_name.grid(row=2, column=0)
label_address = Label(root, text="Address: ", font=('Calibri', 15))
label_address.grid(row=3, column=0)
label_email = Label(root, text="E mail: ", font=('Calibri', 15))
label_email.grid(row=4, column=0)
lebel_DOB = Label(root, text="DOB: ", font=('Calibri', 15))
lebel_DOB.grid(row=5, column=0)
lebel_mobno = Label(root, text="Phone no: ", font=('Calibri', 15))
lebel_mobno.grid(row=6, column=0)
lebel_show = Label(root, text="Data in the Database.", font=('Bahnschrift', 20))
lebel_show.grid(row=8, column=10)


entry_id = Entry(root, font=("Consolas", 15))
entry_id.grid(row=1, column=1)
entry_name = Entry(root, font=("Consolas", 15))
entry_name.grid(row=2, column=1)
entry_address = Entry(root, font=("Consolas", 15))
entry_address.grid(row=3, column=1)
entry_email = Entry(root, font=("Consolas", 15))
entry_email.grid(row=4, column=1)
entry_mobno = Entry(root, font=("Consolas", 15))
entry_mobno.grid(row=6, column=1)


button_insert = Button(root, text="Insert",height=2, width=10, command=lambda: insert(), font=("Comic Sans MS", 16))
button_insert.grid(row=7, column=0)
# button_add = Button(root, text="Add", height=2, width=10, font=("Comic Sans MS", 16))
# button_add.grid(row=7, column=1)
button_cancel = Button(root, text="Clear", height=2, width=10, command=lambda: cancel(), font=("Comic Sans MS", 16))
button_cancel.grid(row=7, column=1)
button_Delete = Button(root, text="Delete", height=2, width=10, command=lambda: delete(), font=("Comic Sans MS", 16))
button_Delete.grid(row=7, column=2)
button_fetch = Button(root, text="Fetch", height=2, width=10, command=lambda: fetch(), font=("Comic Sans MS", 16))
button_fetch.grid(row=7, column=3)


day = ["Select day", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month = ["Select Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
year = ["Select Year", 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

combo_day = ttk.Combobox(root, values=day , font=("Consolas", 15) )
combo_day.grid(row=5, column=1)
combo_day.current(0)
combo_month = ttk.Combobox(root, values=month, font=("Consolas", 15))
combo_month.grid(row=5, column=2)
combo_month.current(0)
combo_year = ttk.Combobox(root, values=year, font=("Consolas", 15))
combo_year.grid(row=5, column=3)
combo_year.current(0)


data_list = Listbox(root, height=40, width=80, bg="yellow", )
data_list.grid(row=9, column=10)
show()


root.mainloop()