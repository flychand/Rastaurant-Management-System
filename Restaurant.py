from Tkinter import*
import random
import time;

root = Tk()
root.geometry("1500x800+0+0")
root.title("Rastaurant Management System")

text_Input =StringVar()
operator=""

Tops = Frame(root, width =1600,height=50,bg="Dark Slate Gray", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width =800,height =700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width =300,height =700, relief=SUNKEN)
f2.pack(side=RIGHT)
#================================================Time===========================
localtime=time.asctime(time.localtime(time.time()))
#========================================info======================================


lblinfo = Label(Tops,font=('arial',50,'bold'),text="Rastaurant Management System",fg="Sea Green",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

lblDateTime = Label(Tops,font=('arial',10,'bold'),text=localtime,fg="Brown",bd=10,anchor='w')
lblDateTime.grid(row=1,column=0)
#=========================================calculator=====================================
def btnClick(numbers):
    global operator
    operator =operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x=random.randint(10908,500763)
    randomRef = str(x)
    rand.set(randomRef)


    CoF=float(Fries.get())
    CoD=float(Drinks.get())
    CoFilet= float(Filet.get())
    CoBurger= float(Burger.get())
    CoChiBurger=float(Chicken_Burger.get())
    CoCheese_Burger=float(Cheese_Burger.get())

    CostofFries = CoF * 0.99
    CostofDrinks = CoD *1.00
    CostofFilet = CoFilet * 2.00
    CostofBurger = CoBurger *3.65
    CostChicken_Burger = CoChiBurger * 3.00
    CostCheese_Burger = CoCheese_Burger *5.00

    CostofMeal ='$',str('%.2f' %(CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                 + CostChicken_Burger +CostCheese_Burger))

    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                 + CostChicken_Burger +CostCheese_Burger) * 0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                 + CostChicken_Burger +CostCheese_Burger)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                 + CostChicken_Burger +CostCheese_Burger) /99)
    Service = "$",str('%.2f' % Ser_Charge)
    OverAllCost = "$",str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = "$",str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")   

txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=15,insertwidth=4,
                   bg="Cadet Blue",justify='right')
txtDisplay.grid(columnspan=4)
#------------------------------------------1-Row---------------------------------------------
btn7=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue",command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue",command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue",command=lambda: btnClick(9)).grid(row=2,column=2)
Addition=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue",command=lambda: btnClick("+")).grid(row=2,column=3)
#--------------------------------------2-Row---------------------------------------------------



btn4=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue",command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue",command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue",command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue",command=lambda: btnClick("-")).grid(row=3,column=3)

#----------------------------------------3-Row--------------------------------------------------

btn1=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue",command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue",command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue",command=lambda: btnClick(3)).grid(row=4,column=2)

Multiplication=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue",command=lambda: btnClick("*")).grid(row=4,column=3)
#----------------------------------------4-Row---------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue",command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="C",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue",command=btEqualsInput).grid(row=5,column=2)

Devision=Button(f2,padx=16,pady=16,bd=5,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue",command=lambda: btnClick("/")).grid(row=5,column=3)
#---------------------------------------------Restaurent info 1----------------------------------------
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge =StringVar()
Drinks = StringVar()
Tax =StringVar()
Cost = StringVar()
Chicken_Burger =StringVar()
Cheese_Burger =StringVar()
TotalCost =StringVar()

lblReference = Label(f1,font=('arial',16,'bold'),text="Reference", bd=16,anchor='w')
lblReference.grid(row=0,column=0)

txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand, bd=5,insertwidth=4,
                    bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)
#---
lblFries = Label(f1,font=('arial',16,'bold'),text="Large Fries", bd=16,anchor='w')
lblFries.grid(row=1,column=0)

txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries, bd=5,insertwidth=4,
                    bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)
#--
lblBurger = Label(f1,font=('arial',16,'bold'),text="Burger Meal", bd=16,anchor='w')
lblBurger.grid(row=2,column=0)

txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger, bd=5,insertwidth=4,
                    bg="powder blue",justify='right')
txtBurger.grid(row=2,column=1)
#--
lblFilet = Label(f1,font=('arial',16,'bold'),text="Large Fliet", bd=16,anchor='w')
lblFilet.grid(row=3,column=0)

txtFilet=Entry(f1,font=('arial',16,'bold'),textvariable=Filet, bd=5,insertwidth=4,
                    bg="powder blue",justify='right')
txtFilet.grid(row=3,column=1)
#--------
lblDrinks = Label(f1,font=('arial',16,'bold'),text="Soft Drinks", bd=16,anchor='w')
lblDrinks.grid(row=4,column=0)

txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks, bd=5,insertwidth=4,
                    bg="powder blue",justify='right')
txtDrinks.grid(row=4,column=1)
#-------
lblChicken_Burger = Label(f1,font=('arial',16,'bold'),text="Chicken_Burger", bd=16,anchor='w')
lblChicken_Burger.grid(row=5,column=0)

txtChicken_Burger=Entry(f1,font=('arial',16,'bold'),textvariable=Chicken_Burger, bd=5,insertwidth=4,
                    bg="powder blue",justify='right')
txtChicken_Burger.grid(row=5,column=1)

#-------------
lblCheese_Burger = Label(f1,font=('arial',16,'bold'),text="Cheese_Burger", bd=16,anchor='w')
lblCheese_Burger.grid(row=6,column=0)

txtCheese_Burger=Entry(f1,font=('arial',16,'bold'),textvariable=Cheese_Burger, bd=5,insertwidth=4,
                    bg="powder blue",justify='right')
txtCheese_Burger.grid(row=6,column=1)

#---------------------------------------------Restaurent info 2----------------------------------------
'''rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
subTotal = StringVar()
Total = StringVar()
Service_Charge =StringVar()
Drinks = StringVar()
Tax =StringVar()
Cost = StringVar()
Chicken_Burger =StringVar()
Chiese_Burger =StringVar()

lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks", bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)

txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks, bd=10,insertwidth=4,
                    bg="#ffffff",justify='right')
txtDrinks.grid(row=0,column=3)'''
#---
lblCost = Label(f1,font=('arial',16,'bold'),text="Cost Of Meal", bd=16,anchor='w')
lblCost.grid(row=1,column=2)

txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost, bd=5,insertwidth=4,
                    bg="#ffffff",justify='right')
txtCost.grid(row=1,column=3)
#--
lblservice = Label(f1,font=('arial',16,'bold'),text="Service Charge", bd=16,anchor='w')
lblservice.grid(row=2,column=2)

txtservice=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge, bd=5,insertwidth=4,
                    bg="#ffffff",justify='right')
txtservice.grid(row=2,column=3)
#--
lblStateTax = Label(f1,font=('arial',16,'bold'),text="State Tax", bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)

txtStateTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax, bd=5,insertwidth=4,
                    bg="#ffffff",justify='right')
txtStateTax.grid(row=3,column=3)
#--------
lblSubTotal = Label(f1,font=('arial',16,'bold'),text="Sub  Total", bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)

txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal, bd=5,insertwidth=4,
                    bg="#ffffff",justify='right')
txtSubTotal.grid(row=4,column=3)
#-------
lblTotalCost = Label(f1,font=('arial',16,'bold'),text="Total Cost", bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)

txtTotalCost=Entry(f1,font=('arial',16,'bold'),textvariable=Total, bd=5,insertwidth=4,
                    bg="#ffffff",justify='right')
txtTotalCost.grid(row=5,column=3)




#=======================================================Button===========================
btnTotal = Button(f1,padx=16,pady=8,bd=3,fg="black",font=('arial',10,'bold'),width=10,
                  text="Total",bg="Cadet Blue", command =Ref).grid(row =7,column=1)

btnReset = Button(f1,padx=16,pady=8,bd=3,fg="black",font=('arial',10,'bold'),width=10,
                  text="Reset",bg="Cadet Blue", command =Reset).grid(row =7,column=2)


btnExit = Button(f1,padx=16,pady=8,bd=3,fg="black",font=('arial',10,'bold'),width=10,
                  text="Exit",bg="Cadet Blue", command =qExit).grid(row =7,column=3 )





root.mainloop()
