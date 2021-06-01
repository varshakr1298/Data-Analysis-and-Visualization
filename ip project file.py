# IP PROJECT FILE
#program to study US Supermarket sales data analysis 2019
import pandas as pd
import pyttsx3 as p
import matplotlib.pyplot as plt
import tkinter as Tk
from tkinter import *
from tkinter import messagebox
p.speak("Hello user! Please enter your name")
name=input("Hello user! Please enter your name: ")
df=pd.read_csv("C:\\Users\\hp\\Downloads\\superdata12.csv",encoding='windows-1252')
print("\n Welcome "+name+"! THIS PROJECT IS ABOUT A SUPERMARKET BASED IN THE UNITED STATES! WE WILL GRAPHICALLY AND STATISTICALLY PRESENT THE DIFFERENT TRANSACTIONS MADE BY VARIOUS CUSTOMERS IN THIS SUPERMARKET BY VISUALIZING THE DATASET.")
p.speak("\n Welcome "+name+"! THIS PROJECT IS ABOUT A SUPERMARKET BASED IN THE UNITED STATES! WE WILL GRAPHICALLY AND STATISTICALLY PRESENT THE DIFFERENT TRANSACTIONS MADE BY VARIOUS CUSTOMERS IN THIS SUPERMARKET BY VISUALIZING THE DATASET.")
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\tAnalysis of the dataset used in the project!")
p.speak("The analysis of the dataset used in our project is as follows")
print("\n Shape of the dataset=",df.shape)
p.speak("Shape of the dataset")
print("\n Number of columns in dataset=",df.columns)
p.speak("Number of columns")
print("\n Number of dimensions in dataset=",df.ndim)
p.speak("Number of dimensions")
print("\n Data type of each data=: \n",df.dtypes)
p.speak("Data type of each column")
print("----------------------------------------------------------------------------------------------------------------------------------")
ch='yes'
while(ch == 'yes'):
    print("***************** US SUPERMARKET SALES ********************")
    p.speak("Welcome to US Supermarket")
    print("\n Select from the menu displayed below:")
    p.speak("Select from the menu displayed below:")
    p.speak("Kindly press enter after each line to view the further options")
    print("\n 1.View all records:")
    q=input()
    print("\n 2.Get to know about:\n a)Product \n b)Customer \n c)Order")
    q1=input()
    print("\n 3.What do you want to find:\n a)Total Sales \n b)Average Sales \n c)Total Quantity \n d)Total Profit \n e)Average Profit")
    q2=input()
    print("\n 4.Cash Counter")
    q3=input()
    print("\n 5.Choose any category:\n a)Furniture:\n \t i)Bookcases \n \t ii)Chairs \n \t iii)Tables \n \t iv)Furnishings \n b)Office Supplies:\n \t i)Labels \n \t ii)Storage \n \t iii)Art \n \t iv)Binders \n \t v)Appliances \n \t vi)Paper \n \t vii)Envelopes \n \t viii)Fasteners \n \t ix)Supplies \n c)Technology: \n \t i)Phones \n \t ii)Accessories \n \t iii)Copiers \n \t iv)Machines")
    q4=input()
    print("\n 6.Details of products sold in a particular region:\n a)North \n b)South \n c)East \n d)West \n e)Central")
    q5=input()
    print("\n 7.Graphical analysis:\n a)Product Level \n b)Customer Level \n c)Order Level \n d)Profit and Sales analysis")
    q6=input()
    print("\n 8.Maximum and Minimum Calculation: \n a)Sales \n b)Quantity \n c)Discount \n d)Profit")
    q7=input()
    print("**********************************************")
    p.speak("Welcome back "+name+"! Please enter your choice from the above menu: ")
    a=int(input("Welcome back "+name+"! Please enter your choice from the above menu: "))
    if a==1:
        print("Viewing dataset")
        p.speak("Showing the dataset")
        print(df.head(31))
    elif a==2:
        p.speak("Enter your level of choice")
        c=input("a)Product \n b)Customer \n c)Order \n Enter your choice of level: ")
        if c=="a":
            p.speak("Showing product level records")
            print(df.loc[1:30,"Product ID":"Quantity"])
        elif c=="b":
            p.speak("Showing customer level records")
            print(df.loc[1:30,"Customer ID":"Region"])
        elif c=="c":
            p.speak("Showing order level records")
            print(df.loc[1:30,"Order ID":"Ship Mode"])
    elif a==3:
        p.speak("Enter your choice")
        d=input("Enter your choice \n a)Total Sales \n b)Average Sales \n c)Total Quantity \n d)Total Profit \n e)Average Profit : ")
        if d=="a":
            p.speak("Total sales of the supermarket")
            print("Total sales of the supermarket",df["Sales"].sum(skipna=True))
        elif d=="b":
            p.speak("Average sales of the supermarket")
            print("Average sales of the supermarket",df["Sales"].mean(skipna=True))
        elif d=="c":
            p.speak("Total quantity of the products")
            print("Total quantity of the products",df["Quantity"].sum(skipna=True))
        elif d=="d":
            p.speak("Profit earned by the supermarket")
            print("Profit earned by the supermarket",df["Profit"].sum(skipna=True))
        elif d=="e":
            p.speak("Average income by the supermarket")
            print("Average income by the supermarket",df["Profit"].sum(skipna=True))
    elif a==4:
        #df=pd.read_csv("C:\\Users\\HP\\Desktop\\superdata12.csv",encoding='windows-1252')
        wi=Tk()
        wi.title("LET'S MAKE YOUR BILL")
        wi.configure(bg='magenta')
        Label(wi,text="",font="arial 10 bold",bg='magenta').grid(row=3,column=1)
        Label(wi,text="",font="arial 28 bold",bg='magenta').grid(row=4,columnspan=3)
        Label(wi,text="",font="arial 10 bold",bg='magenta').grid(row=5,columnspan=3)
        Label(wi,text="{MONEY SAVING IS YOUR BIRTH RIGHT AND YOU SHALL HAVE IT}",font="arial 16 bold",bg='magenta',fg='blue').grid(row=6,columnspan=8)
        Label(wi,text="",font="arial 28 bold",bg='magenta').grid(row=7,columnspan=3)
        a=Label(wi,text="BILL CALCULATOR",font="arial 50 bold underline",fg="yellow",bg='magenta')
        a.place(x=0,y=0,relwidth=1)
        AA=Label (wi,text='Quantity :',font="arial 28 bold",fg="blue",bg='magenta')
        AA.grid(row=8,columnspan=3)
        BB=Label(wi,text='Category:',font="arial 28 bold",fg="blue",bg='magenta')
        BB.grid(row=9,columnspan=3)
        CC=Label(wi,text='Sub-Category1:',font="arial 28 bold",fg="blue",bg='magenta')
        CC.grid(row=10,columnspan=3)
        DD=Label(wi,text='Sub-Category2:',font="arial 28 bold",fg="blue",bg='magenta')
        DD.grid(row=11,columnspan=3)
        EE=Label(wi,text='Sub-Category3:',font="arial 28 bold",fg="blue",bg='magenta')
        EE.grid(row=12,columnspan=3)
        FF=Label(wi,text='Sub-Category4:',font="arial 28 bold",fg="blue",bg='magenta')
        FF.grid(row=13,columnspan=3)
        v1=StringVar()
        v2=StringVar()
        v3=StringVar()
        v4=StringVar()
        v5=StringVar()
        v6=StringVar()
        e1=Entry(wi,textvariable=v1,bg='cyan',font="arial 16 bold").grid(row=8,column=4)
        e2=Entry(wi,textvariable=v2,bg='cyan',font="arial 16 bold").grid(row=9,column=4)
        e3=Entry(wi,textvariable=v3,bg='cyan',font="arial 16 bold").grid(row=10,column=4)
        e4=Entry(wi,textvariable=v4,bg='cyan',font="arial 16 bold").grid(row=11,column=4)
        e5=Entry(wi,textvariable=v5,bg='cyan',font="arial 16 bold").grid(row=12,column=4)
        e6=Entry(wi,textvariable=v6,bg='cyan',font="arial 16 bold").grid(row=13,column=4)
        Label(wi,text=" ",font="arial 28 bold",bg='magenta').grid(row=11,columnspan=3)
        def calculate():
            q=int(v1.get())
            c=v2.get()
            sc=v3.get()
            sc1=v4.get()
            sc2=v5.get()
            sc3=v6.get()
            df1=df
            df1["Price"]=df["Sales"]/df["Quantity"]
            if((c=="Furniture" or c=="furniture") and (sc=="Bookcases" or sc=="bookcases")):
                x1=df1[df1["Category"]=="Furniture"]
                y1=x1[x1["Sub-Category"]=="Bookcases"]
                z1=y1["Price"].iloc[0]
                total_price=z1*q
            if((c=="Furniture" or c=="furniture") and (sc1=="Chairs" or sc1=="chairs")):
                x2=df1[df1["Category"]=="Furniture"]
                y2=x2[x2["Sub-Category"]=="Chairs"]     
                z2=y2["Price"].iloc[0]
                total_price1=z2*q
            if((c=="Furniture" or c=="furniture") and (sc2=="tables" or sc2=="Tables")):
                x3=df1[df1["Category"]=="Furniture"]
                y3=x3[x3["Sub-Category"]=="Tables"]
                z3=y3["Price"].iloc[0]
                total_price2=z3*q
            if((c=="Furniture" or c=="furniture") and (sc3=="Furnishings" or sc3=="furnishings")):
                x4=df1[df1["Category"]=="Furniture"]
                y4=x4[x4["Sub-Category"]=="Furnishings"]
                z4=y4["Price"].iloc[0]
                total_price3=z4*q
            if((c=="Office Supplies" or c=="office supplies") and (sc=="Labels" or sc=="labels")):
                x1=df1[df1["Category"]=="Office Supplies"]
                y1=x1[x1["Sub-Category"]=="Labels"]
                z1=y1["Price"].iloc[0]
                total_price=z1*q
            if((c=="Office Supplies" or c=="office supplies") and (sc1=="Storage" or sc1=="storage")):
                x2=df1[df1["Category"]=="Office Supplies"]
                y2=x2[x2["Sub-Category"]=="Storage"]
                z2=y2["Price"].iloc[0]
                total_price1=z2*q
            if((c=="Office Supplies" or c=="office supplies") and (sc2=="Art" or sc2=="art")):
                x3=df1[df1["Category"]=="Office Supplies"]
                y3=x3[x3["Sub-Category"]=="Art"]
                z3=y3["Price"].iloc[0]
                total_price2=z3*q
            if((c=="Office Supplies" or c=="office supplies") and (sc3=="Binders" or sc3=="binders")):
                x4=df1[df1["Category"]=="Office Supplies"]
                y4=x4[x4["Sub-Category"]=="Binders"]
                z4=y4["Price"].iloc[0]
                total_price3=z4*q
            if((c=="Technology" or c=="technology") and (sc=="Phones" or sc=="phones")):    
                x1=df1[df1["Category"]=="Technology"]
                y1=x1[x1["Sub-Category"]=="Phones"]
                z1=y1["Price"].iloc[0]
                total_price=z1*q
            if((c=="Technology" or c=="technology") and (sc1=="Accessories" or sc1=="accessories")):
                x2=df1[df1["Category"]=="Technology"]
                y2=x2[x2["Sub-Category"]=="Accessories"]
                z2=y2["Price"].iloc[0]
                total_price1=z2*q
            if((c=="Technology" or c=="technology") and (sc2=="Copiers" or sc2=="copiers")):    
                x3=df1[df1["Category"]=="Technology"]
                y3=x3[x3["Sub-Category"]=="Copiers"]
                z3=y3["Price"].iloc[0]
                total_price2=z3*q
            if((c=="Technology" or c=="technology") and (sc3=="Machines" or sc3=="machines")):
                x4=df1[df1["Category"]=="Technology"]
                y4=x4[x4["Sub-Category"]=="Machines"]
                z4=y4["Price"].iloc[0]
                total_price3=z4*qrket
            final_bill=total_price+total_price1+total_price2+total_price3
    
            win=Tk()
            win.title("LET'S CALCULATE YOUR BILL")
            win.configure(bg='yellow')
            Label(win,text="# Please Note:-",font="arial 20 bold underline",fg="red",bg='yellow').grid(row=12,column=1)
            aa=Label(win,text="1.There is no return policy at the supermarket",font="arial 12 bold",fg="green",bg='yellow')
            aa.grid(row=12,column=2)
            bb=Label(win,text="2.Please check your bill before you leave the supermarket \n 3.You  can choose only one category at once",font="arial 12 bold",fg="green",bg='yellow')
            bb.grid(row=13,column=2)
            Label(win,text="Quantity of the product 1",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=14,column=1)
            Label(win,text="Price of the product",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=14,column=2)
            Label(win,text="The amount you have to pay",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=14,column=3)
            Label(win,text=q,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=15,column=1)
            Label(win,text=z1,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=15,column=2)
            Label(win,text=total_price,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=15,column=3)
            
            Label(win,text="Quantity of the product 2",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=19,column=1)
            Label(win,text="Price of the product 2",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=19,column=2)
            Label(win,text="The amount you have to pay for product 2",width=33,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=19,column=3)
            Label(win,text=q,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=20,column=1)
            Label(win,text=z2,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=20,column=2)
            Label(win,text=total_price1,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=20,column=3)

            Label(win,text="Quantity of the product 3",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=24,column=1)
            Label(win,text="Price of the product 3",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=24,column=2)
            Label(win,text="The amount you have to pay for product 3",width=33,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=24,column=3)
            Label(win,text=q,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=25,column=1)
            Label(win,text=z3,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=25,column=2)
            Label(win,text=total_price2,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=25,column=3)

            Label(win,text="Quantity of the product 4",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=29,column=1)
            Label(win,text="Price of the product 4",width=25,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=29,column=2)
            Label(win,text="The amount you have to pay for product 4",width=33,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=29,column=3)
            Label(win,text=q,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=30,column=1)
            Label(win,text=z4,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=30,column=2)
            Label(win,text=total_price3,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=30,column=3)

            Label(win,text="Total amount that you have to pay",width=33,relief=GROOVE,font="arial 14 bold underline",fg="blue",bg='yellow').grid(row=34,column=2)
            Label(win,text=final_bill,width=25,relief=GROOVE,font="arial 18 bold",fg="red",bg='yellow').grid(row=34,column=3)
            
            Label(win,text=" ",font="arial 10 bold",bg='yellow').grid(row=16,columnspan=12)
            Label(win,text=" ",font="arial 10 bold",bg='yellow').grid(row=21,columnspan=12)
            Label(win,text=" ",font="arial 10 bold",bg='yellow').grid(row=26,columnspan=12)
            Label(win,text=" ",font="arial 10 bold",bg='yellow').grid(row=31,columnspan=12)
            def cut():
                win.destroy()
                wi.destroy()
            Button(win,text="EXIT",command=cut,width=15,font="arial 15 bold underline",fg="blue").grid(row=150,column=2)
        def clear():
            v1.set('')
            v2.set('')
            v3.set('')
        def close():
            wi.destroy()
        Button(wi,text="CALCULATE",command=calculate,width=10,font="arial 10 bold underline",fg="blue").grid(row=16,column=5)
        Button(wi,text="CLEAR",command=clear,width=10,font="arial 10 bold underline",fg="blue").grid(row=16,column=6)
        Button(wi,text="EXIT",command=close,width=10,font="arial 10 bold underline",fg="blue").grid(row=16,column=7)
        wi.mainloop()
    elif a==5:
        p.speak("Under which category,do you have your product")
        print("Under which category,do you have your product:\n i)Furniture \n ii)Office Supplies \n iii)Technology")
        p.speak("Select and enter your category")
        g=input("Enter your category(i,ii,iii): ")
        if g=="i":
            p.speak("Under which sub-category do you have your product: i one Bookcases i two Chairs i three Tables i four Furnishings")
            print("Under which sub-category do you have your product:\n i1)Bookcases \n i2)Chairs \n i3)Tables \n i4)Furnishings")
            p.speak("Choose your Sub-Category")
            h=input("Enter your Sub-Category: ")                   
            if h=="i1":
                df1=df.head(31)
                p.speak("Showing the data related to Bookcases")
                print(df1[df1["Sub-Category"]=="Bookcases"])
            elif h=="i2":
                p.speak("Showing the data related to chairs")
                df1=df.head(31)
                print(df1[df1["Sub-Category"]=="Chairs"])
            elif h=="i3":
                p.speak("Showing the data related to tables")
                df1=df.head(31)
                print(df1[df1["Sub-Category"]=="Tables"])
            elif h=="i4":
                p.speak("Showing the data related to furnishings")
                df1=df.head(31)
                print(df1[df1["Sub-Category"]=="Furnishings"])
        elif g=="ii":
            p.speak("Under which sub-category do you have your product:i i one Labels i i two Storage i i three Art  i i four Binders i i five Applainces  i i six Paper i i seven Envelope i i eigth Fasteners  i i nine Supplies")
            print("Under which sub-category do you have your product:\n ii1)Labels \n ii2)Storage \n ii3)Art \n ii4)Binders \n ii5)Appliances \n ii6)Paper \n ii7)Envelopes \n ii8)Fasteners \n ii9)Supplies")
            p.speak("Choose your Sub-Category")
            h=input("Enter your Sub-Category: ")
            if h=="ii1":
                df1=df.head(31)
                p.speak("Showing the data related to Labels")
                print(df1[df1["Sub-Category"]=="Labels"])
            elif h=="ii2":
                df1=df.head(31)
                p.speak("Showing the data related to Storage")
                print(df1[df1["Sub-Category"]=="Storage"])
            elif h=="ii3":
                df1=df.head(31)
                p.speak("Showing the data related to Art")
                print(df1[df1["Sub-Category"]=="Art"])
            elif h=="ii4":
                df1=df.head(31)
                p.speak("Showing the data related to Binders")
                print(df1[df1["Sub-Category"]=="Binders"])
            elif h=="ii5":
                df1=df.head(31)
                p.speak("Showing the data related to Appliances")
                print(df1[df1["Sub-Category"]=="Appliances"])
            elif h=="ii6":
                df1=df.head(31)
                p.speak("Showing the data related to Papers")
                print(df1[df1["Sub-Category"]=="Paper"])
            elif h=="ii7":
                df1=df.head(31)
                p.speak("Showing the data related to Envelope")
                print(df1[df1["Sub-Category"]=="Envelopes"])
            elif h=="ii8":
                df1=df.head(31)
                p.speak("Showing the data related to Fasterners")
                print(df1[df1["Sub-Category"]=="Fasteners"])
            elif h=="ii9":
                df1=df.head(31)
                p.speak("Showing the data related to Supplies")
                print(df1[df1["Sub-Category"]=="Supplies"])
        elif g=="iii":
            p.speak("Under which sub-category do you have your product:\n i i i one Phones i i i two Accessories i i i three Copiers i i i four Machines")
            print("Under which sub-category do you have your product:\n iii1)Phones \n iii2)Accessories \n iii3)Copiers \n iii4)Machines")
            p.speak("Choose your Sub-Category")
            h=input("Enter your Sub-Category: ")                          
            if h=="iii1":
                df1=df.head(31)
                p.speak("Showing the data related to Phones")
                print(df1[df1["Sub-Category"]=="Phones"])
            elif h=="iii2":
                df1=df.head(31)
                p.speak("Showing the data related to Accessories")
                print(df1[df1["Sub-Category"]=="Accessories"])
            elif h=="iii3":
                df1=df.head(31)
                p.speak("Showing the data related to Copiers")
                print(df1[df1["Sub-Category"]=="Copiers"])
            elif h=="iii4":
                df1=df.head(31)
                p.speak("Showing the data related to Machines")
                print(df1[df1["Sub-Category"]=="Machines"])
    elif a==6:
        p.speak("Details of products of which region you want to know: one North two South three  East four West five V)Central")
        print("Details of products of which region you want to know:\n I)North \n II)South \n III)East \n IV)West \n V)Central")
        p.speak("Choose your region")
        i=input("\n Enter your region(I,II,III,IV,V): ")
        if i=="I":
            df2=df.head(31)
            print(df2[df2["Region"]=="North"])
            northData=df[df["Region"]=="North"]
            p.speak("Sales of North Region")
            print("Sales of North Region= ",northData["Sales"].sum())
            northData1=df[df["Region"]=="North"]
            p.speak("Profit of North Region")
            print("Profit of North Region= ",northData1["Profit"].sum())
            northData2=df[df["Region"]=="North"]
            p.speak("Quantity of product sold in North Region")
            print("Quantity of products sold in North Region= ",northData2["Quantity"].sum())           
        elif i=="II":
            df2=df.head(31)
            print(df2[df2["Region"]=="South"])
            southData=df[df["Region"]=="South"]
            p.speak("Sales of South Region")
            print("Sales of South Region= ",southData["Sales"].sum())
            southData1=df[df["Region"]=="South"]
            p.speak("Profits of South Region")
            print("Profits of South Region= ",southData1["Profit"].sum())
            southData2=df[df["Region"]=="South"]
            p.speak("Quantity of product sold in South Region")
            print("Quantity of South Region= ",southData1["Quantity"].sum())           
        elif i=="III":
            df2=df.head(31)
            print(df2[df2["Region"]=="East"])
            eastData=df[df["Region"]=="East"]
            p.speak("Sales of East Region")
            print("Sales of East Region= ",eastData["Sales"].sum())
            eastData1=df[df["Region"]=="East"]
            p.speak("Profit of East Region")
            print("Profits of East Region= ",eastData1["Profit"].sum())
            eastData2=df[df["Region"]=="East"]
            p.speak("Quantity of product sold in East Region")
            print("Quantity of East Region= ",eastData1["Quantity"].sum())
        elif i=="IV":
            df2=df.head(31)
            print(df2[df2["Region"]=="West"])
            westData=df[df["Region"]=="West"]
            p.speak("Sales of West Region")
            print("Sales of West Region= ",westData["Sales"].sum())
            westData1=df[df["Region"]=="West"]
            p.speak("Profits of West Region")
            print("Profits of West Region= ",westData1["Profit"].sum())
            westData2=df[df["Region"]=="West"]
            p.speak("Quantity of product sold in West Region")
            print("Quantity of West Region= ",westData2["Quantity"].sum())
        elif i=="V":
            df2=df.head(31)
            print(df2[df2["Region"]=="Central"])
            centralData=df[df["Region"]=="South"]
            p.speak("Sales of Central Region")
            print("Sales of Central Region= ",centralData["Sales"].sum())
            centralData1=df[df["Region"]=="Cental"]
            p.speak("Profits of Central Region")
            print("Profit of Central Region= ",centralData1["Profit"].sum())
            centralData2=df[df["Region"]=="Cental"]
            p.speak("Quantity of product sold in Central Region")
            print("Quantity of Central Region= ",centralData1["Quantity"].sum())           
    elif a==7:
        p.speak("View analysis at:a part Product Level b part Customer Level c part Order Level d part Profit and Sales level")
        print("View analysis at:\n a)Product Level \n b)Customer Level \n c)Order Level \n d)Profit and Sales level")
        p.speak("which analysis you want to view")
        j=input("\nWhat analysis you want to view(a,b,c,d): ")
        if j=="a":
            p.speak("pie chart showing quantity of product per category")
            category=["Furniture","Office Supplies","Technology"]
            colors=["m","b","g"]
            explode=(0.1,0,0)
            furniture_qty=df[df["Category"]=="Furniture"]
            fqty=furniture_qty["Quantity"].sum()
            officesupplies_qty=df[df["Category"]=="Office Supplies"]
            oqty=officesupplies_qty["Quantity"].sum()
            technology_qty=df[df["Category"]=="Technology"]
            tqty=technology_qty["Quantity"].sum()
            qty=[fqty,oqty,tqty]
            print(plt.pie(qty,explode=explode,labels=category,colors=colors,autopct="%1.1f%%"))
            print(plt.title("Quantity of product per category"))
            print(plt.show())
        elif j=="b":
            p.speak("horizontal bar graph showing sales made by each customer")
            sample_graph_data=df.head(100)
            print(sample_graph_data["Customer Name"].unique())
            print(sample_graph_data["Customer Name"].count())
            print(plt.barh("Customer Name","Sales",data=sample_graph_data,color="m"))
            print(plt.xlabel("Sales of the Customer"))
            print(plt.ylabel("Names of custom)ers"))
            print(plt.title("Customer Level Analysis"))
            print(plt.show())
        elif j=="c":
            p.speak("bar graph showing profit earned on a particular date") 
            sample_graph_data=df.head(21)
            print(sample_graph_data["Order Date"].unique())
            print(sample_graph_data["Order Date"].count())
            print(plt.bar("Order Date","Profit",data=sample_graph_data,color="m",width=0.8))
            print(plt.xlabel("Order Date of the Customer"))
            print(plt.ylabel("Profit of customers"))
            print(plt.title("Order Level Analysis"))
            print(plt.show())
        elif j=="d":
            p.speak("line chart showing profits and sales made by the supermarket during an year")
            sample_graph_data=df.head(101)
            print(plt.plot("Sales",data=sample_graph_data,color="m",label="Sales"))
            print(plt.plot("Profit",data=sample_graph_data,color="g",Label="Profit"))
            print(plt.legend())
            print(plt.xlabel("Sales and Profit of the Customer"))
            print(plt.ylabel("Values of customers"))
            print(plt.title("Order Level nalysis"))
            print(plt.show())
    elif a==8:
            p.speak("Maximum and Minimum of a part Sales b part Quantity c part Discount d part Profit")
            k=input("\n Enter your choice[a)Sales,b)Quantity,c)Discount,d)Profit]:")
            if k=="a":
                maxSale=df[df["Sales"]==df["Sales"].max()]
                print(maxSale[["City","Order ID","Sales"]])
                print("Maximum Sales = ",df["Sales"].max())
                print("Minimum Sales= ",df["Sales"].min())
            if k=="b":
                maxquant=df[df["Quantity"]==df["Quantity"].max()]
                print(maxquant[["City","Order ID","Quantity"]])
                print("Maximum Quantity = ",df["Quantity"].max())
                minquant=df[df["Quantity"]==df["Quantity"].min()]
                print(minquant[["City","Order ID","Quantity"]])
                print("Minimum Quantity= ",df["Quantity"].min())                            
            if k=="c":
                maxdisc=df[df["Discount"]==df["Discount"].max()]
                print(maxdisc[["City","Order ID","Sales","Discount"]])
                print("Maximum Discount = ",df["Discount"].max())
                mindisc=df[df["Discount"]==df["Discount"].min()]
                print(mindisc[["City","Order ID","Sales","Discount"]])
                print("Minimum Discount= ",df["Discount"].min())                            
            if k=="d":
                maxpro=df[df["Profit"]==df["Profit"].max()]
                print(maxpro[["City","Order ID","Sales","Profit"]])
                print("Maximum Profit = ",df["Profit"].max())
                minpro=df[df["Profit"]==df["Profit"].min()]
                print(minpro[["City","Order ID","Sales","Profit"]])
                print("Minimum Profit= ",df["Profit"].min())
    print("*********************************************")
    ch=input("Do you wish to continue?(yes/no): ").lower()
    if(ch!='yes'):
        p.speak("Thank you for visiting our supermarket")
        print("Thank you for visiting our supermarket!!")
        break
