import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import simpledialog
from tkinter import messagebox


global img
global img2
global img3
global img4
global img5
global img6
global bgimg
global bck
root=tk.Tk()
root.geometry('2000x2000')
root.title('Login page')

f1=open("info.txt","w")
f1.close()

#------------------------------------------------------------------------------------------------------------------------
name_var=tk.StringVar()
passw_var=tk.IntVar()


show_face='🐵'
hide_face='🙈'
def show_hide_password():
    if password_entry['show'] == '*':
        password_entry.configure(show='')
        show_hide_btn.configure(text=show_face)
    else:
        password_entry.configure(show='*')
        show_hide_btn.configure(text=hide_face)



page_frame=tk.Frame(root,width=500,highlightbackground='blue',highlightthickness=5)
def back():
    global bgimg
    global bck
    bgimg= Image.open(r"C:\Users\91868\OneDrive\Pictures\Screenshot 2022-11-28 174024.png")
   
    bck=ImageTk.PhotoImage(bgimg)
    limg= Label(page_frame,image=bck)
    limg.place(x=0,y=0)
back()
    
user_name_lb=tk.Label(page_frame,text='User Name',font=('Bold',15),fg='white',bg='black')
user_name_lb.pack(pady=20)



img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\91868\OneDrive\Desktop\python project\login.png"))
label_lb = Label(page_frame, image = img1)
label_lb.place(x=50,y=50)
                    
hr_user_line=tk.Label(page_frame,text='_______________________________',font=('Bold',10),bd=0,fg='#d6d6d6')
hr_user_line.place(x=607.5,y=100)


user_name_entry=tk.Entry(page_frame,textvariable=name_var,font=('Bold',15),bd=0)
user_name_entry.pack(pady=20)


user_name_entry.bind('<FocusIn>', lambda e: hr_user_line.configure(fg='#158aff'))
user_name_entry.bind('<FocusOut>', lambda e: hr_user_line.configure(fg='#d6d6d6'))


password_lb=tk.Label(page_frame,text='Mobile Number',font=('Bold',15),fg='white',bg='black')
password_lb.pack(pady=10)

show_hide_btn=tk.Button(root,text=hide_face,font=('Bold',15),bd=0,command=show_hide_password)
show_hide_btn.place(x=833,y=225)

hr_password_line=tk.Label(page_frame,text='_______________________________',font=('Bold',10),bd=0,fg='#d6d6d6')
hr_password_line.place(x=607.5,y=213)

password_entry=tk.Entry(page_frame,textvariable=passw_var,font=('Bold',15),bd=0,show='*')
password_entry.pack(pady=20)


password_entry.bind('<FocusIn>',lambda e:hr_password_line.configure(fg='#158aff'))
password_entry.bind('<FocusOut>',lambda e: hr_password_line.configure(fg='#d6d6d6'))

def select_option():
    user_name_lb.destroy()
    hr_user_line.destroy()
    password_lb.destroy()
    user_name_entry.destroy()
    password_entry.destroy()
    hr_password_line.destroy()
    show_hide_btn.destroy()
    login_btn.destroy()
    label_lb.destroy()
    
    def city(city_name):
        for widgets in page_frame.winfo_children():
                widgets.destroy()
        back()
        f1=open("info.txt","a")
        f1.write(city_name)
        f1.write('\n')
        f1.close()
        def movi(theatre_name):
            for widgets in page_frame.winfo_children():
                        widgets.destroy()
            back()
            f1=open("info.txt","a")
            f1.write(theatre_name)
            f1.write('\n')
            f1.close()
            label_l= Label(page_frame, text= "SELECT MOVIE",width=50,bd=15, font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
            label_l.pack(side=TOP)

            global img
            global img2
            global img3
            global img4
            frame_for_posters=Frame(page_frame,bg='black')
            frame_for_posters.pack(side=TOP,fill='x',pady=100)

            frame_for_names=Frame(page_frame)
            frame_for_names.pack(side=TOP,fill='x',padx=15)

            img=Image.open(r"C:\Users\91868\OneDrive\Desktop\python project\Screenshot 2022-11-20 100056.png")
            resize_image = img.resize((300,300))
            img = ImageTk.PhotoImage(resize_image)
            label = Label(frame_for_posters, image = img)
            label.pack(side=LEFT,fill='both',expand=1)

            
            img2=Image.open(r"C:\Users\91868\OneDrive\Desktop\python project\Screenshot 2022-11-20 100201.png")
            resize_image = img2.resize((300,300))
            img2 = ImageTk.PhotoImage(resize_image)
            label2 = Label(frame_for_posters, image = img2)
            label2.pack(side=LEFT,fill='both',expand=1)
        
            
            img3=Image.open(r"C:\Users\91868\OneDrive\Desktop\python project\Screenshot 2022-11-20 100407.png")
            resize_image = img3.resize((300,300))
            img3 = ImageTk.PhotoImage(resize_image)
            label3 = Label(frame_for_posters, image = img3)
            label3.pack(side=LEFT,fill='both',expand=1)
            
            
            img4=Image.open(r"C:\Users\91868\OneDrive\Desktop\python project\Screenshot 2022-11-20 100824.png")
            resize_image = img4.resize((200,300))
            img4 = ImageTk.PhotoImage(resize_image)
            label4 = Label(frame_for_posters, image = img4)
            label4.pack(side=LEFT,fill='both',expand=1)
            
            def num_of_seats(movie_name):
                for widgets in frame_for_posters.winfo_children():
                    widgets.destroy()
                for widgets in frame_for_names.winfo_children():
                    widgets.destroy()
                back()
                frame_for_names.destroy()
                frame_for_posters.destroy()
                label_l.destroy()
                l2=Label(page_frame, text="Enter number of seats:", font=('Calibri 25'))
                l2.pack()
                global img5
                img5=Image.open(r"C:\Users\91868\OneDrive\Desktop\python project\Screenshot 2022-11-25 091045.png")
                resize_image = img5.resize((700,700))
                img5 = ImageTk.PhotoImage(resize_image)
                label5 = Label(page_frame, image = img5)
                label5.pack()
                list4=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
                        41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,
                        81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110]
                item=[]
                count=0
                b=simpledialog.askinteger("Input","Enter from which number:")
                c=simpledialog.askinteger("Input","Enter to which number:")
                for i in range(b,c):
                    item.append(list4[i])
                    count+=1
                t2=count*200
                    
                    
                def timing():
                    for widgets in page_frame.winfo_children():
                        widgets.destroy()
                    back()
                    def display(Time):
                        for widgets in page_frame.winfo_children():
                            widgets.destroy()
                        back()
                        f1=open("info.txt","a")
                        f1.write(Time)
                        f1.write('\n')
                        f1.close()
                        labe_2=Label(page_frame,text='DETAILS',width=50,bd=15, font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
                        labe_2.pack()
                        f1=open("info.txt","r")
                        l1=Label(page_frame,text='CITY  :'+f1.readline(),font=('Times new roman',25))
                        l1.pack()
                        l2=Label(page_frame,text='THEATRE :'+f1.readline(),font=('Times new roman',25))
                        l2.pack()
                        l3=Label(page_frame,text='MOVIE :'+f1.readline(),font=('Times new roman',25))
                        l3.pack()
                        l4=Label(page_frame,text='SEAT NUMBERS :'+f1.readline(),font=('Times new roman',25))
                        l4.pack()
                        l5=Label(page_frame,text='PRICE :'+f1.readline(),font=('Times new roman',25))
                        l5.pack()
                        l6=Label(page_frame,text='TIMING :'+f1.readline(),font=('Times new roman',25))
                        l6.pack()
                        f1.close()
                    lab=Label(page_frame,text='SELECT TIMING',bd=15,width=50,font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
                    lab.pack()
                    button1_btn=Button(page_frame,text='10:00AM - 1:00PM',bg='black',fg='white',font=('Bold',25),command=lambda : display('10:00AM - 1:00PM'))
                    button1_btn.pack(pady=10)
                    button2_btn=Button(page_frame,text='01:10PM - 4:10PM',bg='black',fg='white',font=('Bold',25),command=lambda :display('01:10PM - 4:10PM'))
                    button2_btn.pack(pady=10)
                    button3_btn=Button(page_frame,text='04:20PM - 7.20PM',bg='black',fg='white',font=('Bold',25),command=lambda :display('04:20PM - 7.20PM'))
                    button3_btn.pack(pady=10)
                    button4_btn=Button(page_frame,text='07:30PM - 10.30PM',bg='black',fg='white',font=('Bold',25),command=lambda :display('07:30PM - 10.30PM'))
                    button4_btn.pack(pady=10)
                    
                f1=open("info.txt","a")
                f1.write(movie_name)
                f1.write('\n')
                f1.write(str(item))
                f1.write('\n')
                f1.write(str(t2))
                f1.write('\n')
                f1.close()
                labe_1=Button(page_frame,text='NEXT',font=('Times new roman',25),bg='blue',fg='white',command=timing)
                labe_1.pack(side=BOTTOM)
                
                
                
            
            
            button1_lb=Button(frame_for_names,text='Ant man and the wasp Quantamania',width=len('Ant man and the wasp Quantamania'),bg='Yellow',fg='Black',font=('Bold',15),command=lambda : num_of_seats('Ant man and the wasp Quantamania'))
            button1_lb.pack(side=LEFT,anchor='w',padx=3)
            button2_lb=Button(frame_for_names,text='Wakanda forever',width=len('Ant man and the wasp Quantamania'),bg='Yellow',fg='Black',font=('Bold',15),command=lambda : num_of_seats('Wakanda forever'))
            button2_lb.pack(side=LEFT,anchor='w',padx=3)
            button3_lb=Button(frame_for_names,text='Avatar 2',width=len('Ant man and the wasp Quantamania'),bg='Yellow',fg='Black',font=('Bold',15),command=lambda : num_of_seats('Avatar 2'))
            button3_lb.pack(side=LEFT,anchor='w',padx=3)
            button4_lb=Button(frame_for_names,text='John Wick 4',width=25,bg='Yellow',fg='Black',font=('Bold',15),command=lambda : num_of_seats('John Wick 4'))
            button4_lb.pack(side=LEFT,anchor='w',padx=3)
        def image():
            global img6
            img6=Image.open(r"C:\Users\91868\OneDrive\Desktop\python project\Screenshot 2022-11-25 085857.png")
            resize_image = img6.resize((500,500))
            img6 = ImageTk.PhotoImage(resize_image)
            label7 = Label(page_frame, image = img6)
            label7.pack(side=LEFT,padx=10)    
        if(city_name=='Vijayawada'):
            image()
            label_lb= Label(page_frame, text= "SELECT THEATRE",bd=15,width=70,font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
            label_lb.pack()
            button_1=Button(page_frame,text='1.PVR Cinema Hall',width=len('2.Capital cinemas(Trendset mall)'),bg='Yellow',fg='Black',font=('Bold',20),command= lambda : movi("PVR Cinema Hall"))
            button_1.pack(pady=15)
            button_2=Button(page_frame,text='2.Capital cinemas(Trendset mall)',width=len('2.Capital cinemas(Trendset mall)'),bg='#58F',fg='red',font=('Bold',20),command= lambda : movi('2.Capital cinemas(Trendset mall)'))
            button_2.pack(pady=15)
            button_3=Button(page_frame,text='3.Cinepolis(PVP square)',width=len('2.Capital cinemas(Trendset mall)'),bg='violet',fg='white',font=('Bold',20),command= lambda : movi('3.Cinepolis(PVP square)'))
            button_3.pack(pady=15)
        elif(city_name=='Mangalagiri'):
            image()
            label_lb= Label(page_frame, text= "SELECT THEATRE",width=70,bd=15, font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
            label_lb.pack()
            button_1=Button(page_frame,text='1.Urvashi',width=len('3.Annapurna theatre'),bg='Yellow',fg='Black',font=('Bold',20),command= lambda : movi('Urvashi'))
            button_1.pack(pady=15)
            button_2=Button(page_frame,text='2.Venkateswara',width=len('3.Annapurna theatre'),bg='#58F',fg='red',font=('Bold',20),command= lambda : movi('Venkateswara'))
            button_2.pack(pady=15)
            button_3=Button(page_frame,text='3.Annapurna theatre',width=len('3.Annapurna theatre'),bg='violet',fg='white',font=('Bold',20),command= lambda : movi('Annapurna theatre'))
            button_3.pack(pady=15) 
        elif(city_name=='Guntur'):
            image()
            label_lb= Label(page_frame, text= "SELECT THEATRE",width=70,bd=15, font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
            label_lb.pack()
            button_1=Button(page_frame,text='1.Harihar cinemas',bg='Yellow',fg='Black',font=('Bold',20),command=lambda : movi('Harihar cinemas'))
            button_1.pack(pady=15)
            button_2=Button(page_frame,text='2.PVR cinemas',width=len('3.Bhaskar cinemas'),bg='#58F',fg='red',font=('Bold',20),command=lambda : movi('PVR cinemas'))
            button_2.pack(pady=15)
            button_3=Button(page_frame,text='3.Bhaskar cinemas',bg='violet',fg='white',font=('Bold',20),command= lambda : movi('Bhaskar cinemas'))
            button_3.pack(pady=15)
        else:
            image()
            label_lb= Label(page_frame, text= "SELECT THEATRE", width=70,bd=15, font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
            label_lb.pack()
            button_1=Button(page_frame,text='1.Lakshmi complex',width=len('4.Sangameswara Cinemas'),bg='Yellow',fg='Black',font=('Bold',20),command=lambda : movi('Lakshmi complex'))
            button_1.pack(pady=15)
            button_2=Button(page_frame,text='2.Priya complex',width=len('4.Sangameswara Cinemas'),bg='#58F',fg='red',font=('Bold',20),command=lambda : movi('Priya complex'))
            button_2.pack(pady=15)
            button_3=Button(page_frame,text='4.Sangameswara Cinemas',width=len('4.Sangameswara Cinemas'),bg='violet',fg='white',font=('Bold',20),command=lambda : movi('Sangameswara Cinemas'))
            button_3.pack(pady=15)
    
            
            
    label1=Label(page_frame,text='Select City',width=50,bd=15, font= ('Times new roman',35),relief=GROOVE,bg='black',fg='green')
    label1.pack(pady=0,side=TOP)
    
    
    button1=Button(page_frame,text='1.Vijayawada',width=len('2.Mangalagiri'),bg='Yellow',fg='Black',font=('Bold',20),command=lambda : city('Vijayawada'))
    button1.pack(pady=15)
    button2=Button(page_frame,text='2.Mangalagiri',width=len('2.Mangalagiri'),bg='#58F',fg='red',font=('Bold',20),command=lambda : city('Mangalagiri'))
    button2.pack(pady=15)
        
    button3=Button(page_frame,text='3.Guntur',width=len('2.Mangalagiri'),bg='violet',fg='white',font=('Bold',20),command=lambda : city('Guntur'))
    button3.pack(pady=15)
    button4=Button(page_frame,text='4.Tenali',width=len('2.Mangalagiri'),bg='green',fg='white',font=('Bold',20),command=lambda : city('Tenali'))
    button4.pack(pady=15)



def check_pass():
    f=open("customer.txt","a")
    p1=str(name_var.get())
    f.write(p1)
    f.write('\n')
    p2=int(password_entry.get())
    f.write(str(p2))
    f.write('\n')
    f.close()
    if(type(p2)==str):
        messagebox.showerror("showerror","Please enter mobile number as your password")
    elif(len(str(p2))==10):
        select_option()
    elif(len(str(p2))!=10):
        messagebox.showerror("showerror","Password must consist of 10 digits")
        
    

login_btn=tk.Button(page_frame,text='Login',font=('Bold',15),bd=0,bg='#158aff',fg='white',width=20,command=check_pass)
login_btn.pack(pady=20)

page_frame.pack(pady=20)
page_frame.pack_propagate(False)
page_frame.configure(width=2000,height=2000)


root.mainloop()