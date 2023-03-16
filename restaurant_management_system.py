#import tkinter modules
from tkinter import *
from tkinter import messagebox
import random
from datetime import date
root=Tk()

#window
root.title("Food Billing System")
root.geometry("1250x650")
root.configure(bg="yellow")

#label for name of restaurant
name=Label(root,text="Frecious\n Restaurant ",fg="red",font=("cursive",25,"bold"),bg="yellow",padx=20,pady=150)
name.pack()

#creating new window for menu
def menu_wind() :
    menu_wind=Toplevel()
    menu_wind.title("Menu")
    menu_wind.configure(bg="green")
    
    #label for menu
    menu=Label(menu_wind,bg="green",fg="white",text="Menu\n\n \tsnacks\t\tfrom the bread basket\n1)coca cola =40 rs\t\t11)tawa roti = 25 rs\n 2) lays= 20 rs\t\t12)butter roti = 35 rs\n 3) samosa = 15 rs\t\t13)tandoori roti = 50 rs\n4) chowmein= 30 rs\t\t14)naan = 70 rs\n 5) burger = 30 rs\t\t15)butter naan = 85 rs\n6) sandwich = 20 rs\t\t16)aloo naan = 100 rs\n\nchef's special\n7) shahi paneer = 215 rs\n8) malai kofta = 250 rs\n9) mixed veg = 180 rs\n10)soya chap = 170 rs" )
    menu.pack()
    
#menu button    
Menu_button=Button(root,text="Menu",bg="black",fg="white",activebackground="red",relief="groove",command=menu_wind)
Menu_button.place(x=390,y=380)

#creating new window for about us
def about_us_wind() :
    about_us_wind=Toplevel()
    about_us_wind.title("About us")
    about_us_wind.configure(bg="green")
    
    #label for about us
    About_us=Label(about_us_wind,text="Welcome, \nRestaurant Frecious is one of the oldest restaurant in Cannaught Place,Delhi, which offers\n traditional food specialties which you can enjoyed in the\n pleasant air conditioned ambience.\nWe believe customer satisfaction is important.That's why we try our best to \nget no complaints from you",bg="green",fg="white")
    About_us.pack()

#about us button
About_us_button=Button(root,text="About us",bg="black",fg="white",activebackground="red",relief="groove",command=about_us_wind)
About_us_button.place(x=550,y=380)

#creating new window for contact us
def contact_us_wind() :
    contact_us_wind=Toplevel()
    contact_us_wind.title("About us")
    contact_us_wind.configure(bg="green")
    
    #label for contact us
    Contact_us=Label(contact_us_wind,text="Contact us : \n 1)+91-9582xxxxxx \n 2)+91-9210xxxxxx\n 3)+91140xxxxxxx\n4)+912248xxxxxx",bg="green",fg="white")
    Contact_us.pack()

#contact us button
Contact_us_button=Button(root,text="Contact us",bg="black",fg="white",activebackground="red",relief="groove",command=contact_us_wind)
Contact_us_button.place(x=750,y=380)

#creating new window for billing
def new_wind() :
    new_wind=Toplevel()
    new_wind.title("Bill")
    new_wind.configure(bg="blue")
    new_wind.geometry("1250x650")
    #label for main heading
    heading=Label(new_wind,text="Billing",font=("arial",15,"bold"),bg="black",fg="yellow")
    heading.pack()
    
    #variable
    coca_cola=IntVar()
    lays=IntVar()
    samosa=IntVar()
    chowmein=IntVar()
    burger=IntVar()
    sandwich=IntVar()
    shahi_paneer=IntVar()
    malai_kofta=IntVar()
    mixed_veg=IntVar()
    soya_chap=IntVar()
    tawa_roti=IntVar()
    butter_roti=IntVar()
    tandoori_roti=IntVar()
    naan=IntVar()
    butter_naan=IntVar()
    aloo_naan=IntVar()
    
    #variables for check button color
    off_color="white" ;
    on_color="yellow" ;
    
    #functions for check button color
    def check_on1_1() :
     if check_var1_1.get()=="1" :
      Item1_1["fg"]=on_color
     else :
      Item1_1["fg"]=off_color
    
    def check_on1_2() :
     if check_var1_2.get()=="1" :
      Item1_2["fg"]=on_color
     else :
      Item1_2["fg"]=off_color
    
    def check_on1_3() :
     if check_var1_3.get()=="1" :
      Item1_3["fg"]=on_color
     else :
      Item1_3["fg"]=off_color
    
    def check_on1_4() :
     if check_var1_4.get()=="1" :
      Item1_4["fg"]=on_color
     else :
      Item1_4["fg"]=off_color
    
    def check_on1_5() :
     if check_var1_5.get()=="1" :
      Item1_5["fg"]=on_color
     else :
      Item1_5["fg"]=off_color
    
    def check_on1_6() :
     if check_var1_6.get()=="1" :
      Item1_6["fg"]=on_color
     else :
      Item1_6["fg"]=off_color
    
    def check_on2_1() :
     if check_var2_1.get()=="1" :
      Item2_1["fg"]=on_color
     else :
      Item2_1["fg"]=off_color
    
    def check_on2_2() :
     if check_var2_2.get()=="1" :
      Item2_2["fg"]=on_color
     else :
      Item2_2["fg"]=off_color

    def check_on2_3() :
     if check_var2_3.get()=="1" :
      Item2_3["fg"]=on_color
     else :
      Item2_3["fg"]=off_color
    
    def check_on2_4() :
     if check_var2_4.get()=="1" :
      Item2_4["fg"]=on_color
     else :
      Item2_4["fg"]=off_color
    
    def check_on3_1() :
     if check_var3_1.get()=="1" : 
      Item3_1["fg"]=on_color
     else :
      Item3_1["fg"]=off_color
    
    def check_on3_2() :
     if check_var3_2.get()=="1" :
      Item3_2["fg"]=on_color
     else :
      Item3_2["fg"]=off_color
    
    def check_on3_3() :
     if check_var3_3.get()=="1" :
      Item3_3["fg"]=on_color
     else :
      Item3_3["fg"]=off_color
    
    def check_on3_4() :
     if check_var3_4.get()=="1" :
      Item3_4["fg"]=on_color
     else :
      Item3_4["fg"]=off_color
    
    def check_on3_5() :
     if check_var3_5.get()=="1" :
      Item3_5["fg"]=on_color
     else :
      Item3_5["fg"]=off_color
    
    def check_on3_6() :
     if check_var3_6.get()=="1" :
      Item3_6["fg"]=on_color
     else :
      Item3_6["fg"]=off_color
    #gh

    #variable for check button
    check_var1_1=StringVar(root)
    check_var1_1.set(0)
    
    check_var1_2=StringVar(root)
    check_var1_2.set(0)
    
    check_var1_3=StringVar(root)
    check_var1_3.set(0)
    
    check_var1_4=StringVar(root)
    check_var1_4.set(0)
    
    check_var1_5=StringVar(root)
    check_var1_5.set(0)
    
    check_var1_6=StringVar(root)
    check_var1_6.set(0)
    
    check_var2_1=StringVar(root)
    check_var2_1.set(0)
    
    check_var2_2=StringVar(root)
    check_var2_2.set(0)
    
    check_var2_3=StringVar(root)
    check_var2_3.set(0)
    
    check_var2_4=StringVar(root)
    check_var2_4.set(0)
    
    check_var3_1=StringVar(root)
    check_var3_1.set(0)
    
    check_var3_2=StringVar(root)
    check_var3_2.set(0)
    
    check_var3_3=StringVar(root)
    check_var3_3.set(0)
    
    check_var3_4=StringVar(root)
    check_var3_4.set(0)
    
    check_var3_5=StringVar(root)
    check_var3_5.set(0)
    
    check_var3_6=StringVar(root)
    check_var3_6.set(0)
    
    #Items snacks
    Category1=Label(new_wind,text="Snacks",font=("arial",10,"bold"), bg="red",fg="white")
    Category1.place(x=0,y=85)
    
    Item1_1=Checkbutton(new_wind,text="Coca Cola",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on1_1,variable=check_var1_1)
    Item1_1.place(x=0,y=150)
    Item1_2=Checkbutton(new_wind,text="Lays",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on1_2,variable=check_var1_2)
    Item1_2.place(x=0,y=200)
    Item1_3=Checkbutton(new_wind,text="Samosa",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on1_3,variable=check_var1_3)
    Item1_3.place(x=0,y=250)
    Item1_4=Checkbutton(new_wind,text="Chowmein",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on1_4,variable=check_var1_4)
    Item1_4.place(x=0,y=300)
    Item1_5=Checkbutton(new_wind,text="Burger",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on1_5,variable=check_var1_5)
    Item1_5.place(x=0,y=350)
    Item1_6=Checkbutton(new_wind,text="Sandwich",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on1_6,variable=check_var1_6)
    Item1_6.place(x=0,y=400)
    
    #entry for quantity of item
    Entry_coca_cola=Entry(new_wind,width=5,textvariable=coca_cola)
    Entry_coca_cola.place(x=250,y=150)
    Entry_lays=Entry(new_wind,width=5,textvariable=lays)
    Entry_lays. place(x=250,y=200)
    Entry_samosa=Entry(new_wind,width=5,textvariable=samosa)
    Entry_samosa.place(x=250,y=250)
    Entry_chowmein=Entry(new_wind,width=5,textvariable=chowmein)
    Entry_chowmein.place(x=250,y=300)
    Entry_burger=Entry(new_wind,width=5,textvariable=burger)
    Entry_burger.place(x=250,y=350)
    Entry_sandwich=Entry(new_wind,width=5,textvariable=sandwich)
    Entry_sandwich.place(x=250,y=400)
    
    #items chef's special
    Category2=Label(new_wind,text="Chef's Special",font=("arial",10,"bold"),bg="red",fg="white")
    Category2.place(x=400,y=85)
    
    Item2_1=Checkbutton(new_wind,text="Shahi Paneer",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on2_1,variable=check_var2_1)
    Item2_1.place(x=400,y=150)
    Item2_2=Checkbutton(new_wind,text="Malai Kofta",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on2_2,variable=check_var2_2)
    Item2_2.place(x=400,y=200)
    Item2_3=Checkbutton(new_wind,text="Mixed Veg",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on2_3,variable=check_var2_3)
    Item2_3.place(x=400,y=250)
    Item2_4=Checkbutton(new_wind,text="Soya Chap",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on2_4,variable=check_var2_4)
    Item2_4.place(x=400,y=300)
    
    #entry for quantity of item
    Entry_shahi_paneer=Entry(new_wind,width=5,textvariable=shahi_paneer)
    Entry_shahi_paneer.place(x=700,y=150)
    Entry_malai_kofta=Entry(new_wind,width=5,textvariable=malai_kofta)
    Entry_malai_kofta.place(x=700,y=200)
    Entry_mixed_veg=Entry(new_wind,width=5,textvariable=mixed_veg)
    Entry_mixed_veg.place(x=700,y=250)
    Entry_soya_chap=Entry(new_wind,width=5,textvariable=soya_chap)
    Entry_soya_chap.place(x=700,y=300)
    
    #items bread basket
    Category3=Label(new_wind,text="From The Bread Basket",font=("aerial",10,"bold"),bg="red",fg="white")
    Category3.place(x=830,y=85)
    
    Item3_1=Checkbutton(new_wind,text="Tawa Roti",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on3_1,variable=check_var3_1)
    Item3_1.place(x=830,y=150)
    Item3_2=Checkbutton(new_wind,text="Butter Roti",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on3_2,variable=check_var3_2)
    Item3_2.place(x=830,y=200)
    Item3_3=Checkbutton(new_wind,text="Tandoori Roti",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on3_3,variable=check_var3_3)
    Item3_3.place(x=830,y=250)
    Item3_4=Checkbutton(new_wind,text="Naan",fg="white",bg="black", activebackground="black",activeforeground="white",selectcolor="grey",command=check_on3_4,variable=check_var3_4)
    Item3_4.place(x=830,y=300)
    Item3_5=Checkbutton(new_wind,text="Butter Naan",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on3_5,variable=check_var3_5)
    Item3_5.place(x=830,y=350)
    Item3_6=Checkbutton(new_wind,text="Aloo Naan",fg="white",bg="black",activebackground="black",activeforeground="white",selectcolor="grey",command=check_on3_6,variable=check_var3_6)
    Item3_6.place(x=830,y=400)
    
    #entry for quantity of items
    Entry_tawa_roti=Entry(new_wind,width=5,textvariable=tawa_roti)
    Entry_tawa_roti.place(x=1155,y=150)
    Entry_butter_roti=Entry(new_wind,width=5,textvariable=butter_roti)
    Entry_butter_roti.place(x=1155,y=200)
    Entry_tandoori_roti=Entry(new_wind,width=5,textvariable=tandoori_roti)
    Entry_tandoori_roti.place(x=1155,y=250)
    Entry_naan=Entry(new_wind,width=5,textvariable=naan)
    Entry_naan.place(x=1155,y=300)
    Entry_butter_naan=Entry(new_wind,width=5,textvariable=butter_naan)
    Entry_butter_naan.place(x=1155,y=350)
    Entry_aloo_naan=Entry(new_wind,width=5,textvariable=aloo_naan)
    Entry_aloo_naan.place(x=1155,y=400)
    
    #function for sub total
    def sub_total() :
        Sub_total=(coca_cola.get()*40) + (lays.get()*20) + (samosa.get()*15) + (chowmein.get()*30) + (burger.get()*30) + (sandwich.get()*20) + (shahi_paneer.get()*215) + (malai_kofta.get()*250) + (mixed_veg.get()*180) + (soya_chap.get()*170) + (tawa_roti.get()*25) + (butter_roti.get()*35) + (tandoori_roti.get()*50) + (naan.get()*70) + (butter_naan.get()*85) + (aloo_naan.get()*100)
        Entry_sub_total.delete(0,END)
        Entry_sub_total.insert(0,Sub_total)

    #button for sub-total
    sub_total=Button(new_wind,text="Sub-total",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=sub_total)
    sub_total.place(x=0,y=470)
    Entry_sub_total=Entry(new_wind,width=10)
    Entry_sub_total.place(x=230,y=500)
    
    #function for tax
    def tax() :
        Tax= (5/100)*int(Entry_sub_total.get())
        Entry_tax.delete(0,END)
        Entry_tax.insert(0,Tax)
            
    #button for tax
    tax=Button(new_wind,text="tax",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=tax) 
    tax.place(x=480,y=470)
    Entry_tax=Entry(new_wind,width=10)
    Entry_tax.place(x=630,y=500)
    
    #function for total
    def total() :
        Total=float(Entry_sub_total.get()) + float( Entry_tax.get())
        Entry_total.delete(0,END)
        Entry_total.insert(0,Total)
        
    #button for total
    total=Button(new_wind,text="total",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=total) 
    total.place(x=880,y=470)
    Entry_total=Entry(new_wind,width=10)
    Entry_total.place(x=1050,y=500)
    
    #function for clear all
    def clear_all() :
        Entry_coca_cola.delete(0,END)
        Entry_coca_cola.insert(0,0)
        Entry_lays.delete(0,END)
        Entry_lays.insert(0,0)
        Entry_samosa.delete(0,END)
        Entry_samosa.insert(0,0)
        Entry_chowmein.delete(0,END)
        Entry_chowmein.insert(0,0)
        Entry_burger.delete(0,END)
        Entry_burger.insert(0,0)
        Entry_sandwich.delete(0,END)
        Entry_sandwich.insert(0,0)
        Entry_shahi_paneer.delete(0,END)
        Entry_shahi_paneer.insert(0,0)
        Entry_malai_kofta.delete(0,END)
        Entry_malai_kofta.insert(0,0)
        Entry_mixed_veg.delete(0,END)
        Entry_mixed_veg.insert(0,0)
        Entry_soya_chap.delete(0,END)
        Entry_soya_chap.insert(0,0)
        Entry_tawa_roti.delete(0,END)
        Entry_tawa_roti.insert(0,0)
        Entry_butter_roti.delete(0,END)
        Entry_butter_roti.insert(0,0)
        Entry_tandoori_roti.delete(0,END)
        Entry_tandoori_roti.insert(0,0)
        Entry_naan.delete(0,END)
        Entry_naan.insert(0,0)
        Entry_butter_naan.delete(0,END)
        Entry_butter_naan.insert(0,0)
        Entry_aloo_naan.delete(0,END)
        Entry_aloo_naan.insert(0,0)
        Entry_sub_total.delete(0,END)
        Entry_sub_total.insert(0,"")
        Entry_tax.delete(0,END)
        Entry_tax.insert(0,"")
        Entry_total.delete(0,END)
        Entry_total.insert(0,"")
        
        
    #button for clear
    clear_all=Button(new_wind,text="clear all",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=clear_all) 
    clear_all.place(x=120,y=570)
    
    #creating new  window for receipt
    def receipt_wind() :
        receipt_wind=Toplevel()
        receipt_wind.title("Receipt")
        receipt_wind.configure(bg="white")
        
        #function for receipt
        def receipt() :
            receipt_text.delete(1.0,END)
            receipt_text.insert(END,"\tFrecious\n\tRestaurant\n")
            receipt_text.insert(END,"_______\n") 
            x=random.randint(100,1000)
            receiptnumber="Receipt No.\t\t" + str(x)
            receipt_text.insert(END,receiptnumber)
            x=date.today()
            Date=x.strftime("%d-%m-%y")
            receipt_text.insert(END,f"\nDate\t{Date}")
            receipt_text.insert(END,"\n_______\n")        
            if Entry_coca_cola.get() !="0" :
             receipt_text.insert(END,(f"coca cola\t\t{int(Entry_coca_cola.get())*40}\n") )
            if Entry_lays.get() !="0" :
             receipt_text.insert(END,(f"lays\t\t{int(Entry_lays.get())*20}\n"))
            if Entry_samosa.get() !="0" :
             receipt_text.insert(END,(f"samosa\t\t{int(Entry_samosa.get())*15}\n"))
            if Entry_chowmein.get() !="0" :
             receipt_text.insert(END,(f"chowmein\t\t{int(Entry_chowmein.get())*30}\n"))
            if Entry_burger.get() !="0" :
             receipt_text.insert(END,(f"burger\t\t{int(Entry_burger.get())*40}\n"))
            if Entry_sandwich.get() !="0" :
             receipt_text.insert(END,(f"sandwich\t\t{int(Entry_sandwich.get())*20}\n"))
            if Entry_shahi_paneer.get() !="0" :
             receipt_text.insert(END,(f"shahi paneer\t\t{int(Entry_shahi_paneer.get())*215}\n"))
            if Entry_malai_kofta.get() !="0" :
             receipt_text.insert(END,(f"malai kofta\t\t{int(Entry_malai_kofta.get())*250}\n"))
            if Entry_mixed_veg.get() !="0" :
             receipt_text.insert(END,(f"mixed veg\t\t{int(Entry_mixed_veg.get())*180}\n"))
            if Entry_soya_chap.get() !="0" :
             receipt_text.insert(END,(f"soya chap\t\t{int(Entry_soya_chap.get())*170}\n")) 
            if Entry_tawa_roti.get() !="0" :
             receipt_text.insert(END,(f"tawa roti\t\t{int(Entry_tawa_roti.get())*25}\n")) 
            if Entry_butter_roti.get() !="0" :
             receipt_text.insert(END,(f"butter roti\t\t{int(Entry_butter_roti.get())*35}\n")) 
            if Entry_tandoori_roti.get() !="0" :
             receipt_text.insert(END,(f"tandoori roti\t\t{int(Entry_tandoori_roti.get())*50}\n")) 
            if Entry_naan.get() !="0" :
             receipt_text.insert(END,(f"naan\t\t{int(Entry_naan.get())*70}\n")) 
            if Entry_butter_naan.get() !="0" :
             receipt_text.insert(END,(f"butter naan\t\t{int(Entry_butter_naan.get())*85}\n")) 
            if Entry_aloo_naan.get() !="0" :
             receipt_text.insert(END,(f"aloo naan\t\t{int(Entry_aloo_naan.get())*100}\n")) 
            receipt_text.insert(END,"_______\n")
            receipt_text.insert(END,(f"Sub total\t\t{Entry_sub_total.get()}\n"))
            receipt_text.insert(END,(f"Tax\t\t{Entry_tax.get()}\n"))
            receipt_text.insert(END,(f"Total\t\t{Entry_total.get()}\n"))
                                        
        #text box for receipt
        receipt_text=Text(receipt_wind, height=20,width=30)
        receipt_text.pack()
        
        #get receipt button
        get_receipt=Button(receipt_wind,text="Get receipt",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=receipt) 
        get_receipt.place(x=100,y=580)
        
        #message box function for print
        def message() :
         messagebox.showinfo("", "your receipt has successfully printed") 
        
        #print receipt button
        print=Button(receipt_wind,text="print",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=message) 
        print.place(x=350,y=580)
        
    #button for receipt
    receipt=Button(new_wind,text="Receipt",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=receipt_wind) 
    receipt.place(x=500,y=570)
    
    #creating new window for lucky draw
    def lucky_draw_wind() :
         lucky_draw_wind=Toplevel()
         lucky_draw_wind.title("Lucky Draw")
         lucky_draw_wind.geometry("1250x650")
         lucky_draw_wind.configure(bg="yellow")
         title=Label(lucky_draw_wind,text="Lucky Draw",font=("arial",15,"bold"),bg="red",fg="yellow")
         title.pack()
         #label for rules
         rules=Label(lucky_draw_wind,text="RULES : - You have to guess the number between 1-100.If you guess the number correctly\n, you can stand the chance to get one time meal for free. You can order anything. ",bg="yellow",fg="black")
         rules.place(x=0,y=100)
    
         #label for input
         input=Label(lucky_draw_wind, text="Enter the number :-", bg="yellow", fg="black") 
         input.place(x=0,y=200)
          
         #entry for input
         Entry_input=Entry(lucky_draw_wind) 
         Entry_input.place(x=300,y=200)
         
         #function for lucky draw
         def lucky_draw() :
          Entry_result.delete(0,END)
          if Entry_input.get() == "73" :
           Entry_result.insert(0,"Winner")
          else :
           Entry_result.insert(0,"Sorry, you Loose")
           
         #entry to display result
         Entry_result=Entry(lucky_draw_wind, bg="yellow") 
         Entry_result.place(x=300,y=400) 
         
         #function for reset
         def reset() :
          Entry_input.delete(0,END)
          Entry_input.insert(0,0)
          Entry_result.delete(0,END)
          Entry_result.insert(0,"" )
         
         #button for result
         result=Button(lucky_draw_wind, text="Check", fg="white", bg="blue", activebackground="grey", activeforeground="white", command=lucky_draw) 
         result.place(x=300,y=300) 
         
         #button for reset
         reset=Button(lucky_draw_wind, text="Reset", fg="white", bg="blue", activebackground="grey", activeforeground="white", command=reset) 
         reset.place(x=500,y=300)
                
    #button for lucky draw
    lucky_draw=Button(new_wind,text="Lucky Draw",fg="white",bg="green",activebackground="grey",activeforeground="white",bd=5,relief="groove",command=lucky_draw_wind) 
    lucky_draw.place(x=900,y=570)
                         
#button to go to new window
Button_calculate_bill=Button(root,text="calculate bill",bg="orange",relief="groove",bd=10,command=new_wind)
Button_calculate_bill.place(x=1000,y=570)

root.mainloop(