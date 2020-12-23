from tkinter import *
import random
root=Tk()
root.title("List")
root.geometry("500x500")
def put_things():

    random_number=random.randint(0, 6)
    item_wanted["text"]="Put Item no ["+str(random_number)+"] In bag" 
listed=Label(root)
listed["text"]="Listed Items : ['Bottle','Tiffin','ID Card','Chocolates','Chips','Tickets','Hanky']"

listed.place(relx=0.5,rely=0.4,anchor=CENTER)
btn1=Button(root,text="Which item to put in bag?",command=put_things,bg="gold")
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)
item_wanted=Label(root)
item_wanted.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()