import tkinter as tk
import csv

passwords=[["Username", "Note", "Password"]]

def initialization():
    #read csv file and show in window and sync passwords list
    try:
        with  open('localPasswordManagerData.csv', newline='') as file:
            reader=csv.reader(file, delimiter=' ', quotechar='|')
            for row in reader:
                rowList=row[0].split(',')   
                if rowList != passwords[0]:
                    passwords.append(rowList)
                    labeledPasswordEntry="Username: " + rowList[0] + " | " + "Note: " + rowList[1] + " | " + "Password: " + rowList[2]
                    textOutput.insert(tk.END, labeledPasswordEntry)
                    textOutput.insert(tk.END, "\n")
        return
    except:
        return

def addToPasswordsList():
    item=[userNameVar.get(), notesVar.get(), passwordVar.get()]
    for i in passwords:
        if item == i:
            return
    passwords.append(item)
    labeledPasswordEntry="Username: " + userNameVar.get() + " | " + "Note: " + notesVar.get() + " | " + "Password: " + passwordVar.get()
    textOutput.insert(tk.END, labeledPasswordEntry)
    textOutput.insert(tk.END, "\n")

    #write and encrypt password data to csv file
    with open('localPasswordManagerData.csv', 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerows(passwords)

def job():
    window.after(2000, job)


#GUI
window=tk.Tk()
textOutput = tk.Text(window, height = 33, width = 127)
window.title("Password Manager")
window.geometry("900x500")
window.resizable(False, False)


#variables
userNameVar=tk.StringVar()
notesVar=tk.StringVar()
passwordVar=tk.StringVar()  

#label and buttons
entryLabelUsername=tk.Label(window, text="Username: ")
entryInputUsername=tk.Entry(window, textvariable=userNameVar)
entryLabelNote=tk.Label(window, text="Note: ")
entryInputNote=tk.Entry(window, textvariable=notesVar)
entryLabelPassword=tk.Label(window, text="Password: ")
entryInputPassword=tk.Entry(window, textvariable=passwordVar)
#button does not work
addButton=tk.Button(window, text="Add", command=addToPasswordsList)

#place tkinter widgets
textOutput.place(x=0,y=0)
entryLabelUsername.place(x=20, y=450)
entryInputUsername.place(x=90, y=450)
entryLabelNote.place(x=300, y=450)
entryInputNote.place(x=340, y=450)
entryLabelPassword.place(x=550, y=450)
entryInputPassword.place(x=620, y=450)
addButton.place(x=830, y=450)
window.update()

initialization()

window.after(2000, job)

while True:
    window.update()


"""
links:
https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
"""

"""
functions include:
generating strong passwords
hashing and encrypting given passwords
exporting passwords to csv
checking weak passwords database to warn against weak passwords
"""