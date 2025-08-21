name = input("Enter your name: ")
notes = input("Enter your notes: ")
with open('MyNotes.txt','w') as f:
    f.write("Name : " +name+ "\n")
    f.write("The note :" + notes + "\n")
with open('MyNotes.txt','r') as f: 
    print ("the content of the file is :", f.read())   