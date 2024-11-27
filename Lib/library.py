from tkinter import*


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6 )
        lbltitle.pack(side=TOP,fill =X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",12,"bold"),padx=2,pady=6 )
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",bd=12,relief=RIDGE,font=("arial",12,"bold"),padx=2 )
        DataFrameRight.place(x=870,y=5,width=580,height=350)


        #=========================Buttons Frame ===================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        #=========================Information Frame ===================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        


if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
        