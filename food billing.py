from tkinter import*
import math,random,os
from tkinter import messagebox
class bill_app:
    def __init__(self, root):
        self.root = root    # self is to indecate peticular varible
        self.root.geometry("1355x700+0+0")
        self.root.title("billing software")
        bg_color = "#074463"
        title= Label(self.root, text="billng software", bd=12, relief=GROOVE, bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        #==================================variable=====================================
        #==================================vegetable variable===========================
        self.mix_veg=IntVar()
        self.chhole=IntVar()
        self.pav_bhaji=IntVar()
        self.veg_kolhapuri=IntVar()
        self.paneer=IntVar()
        self.rajma=IntVar()

        # ==================================dal and rice variable===========================
        self.black_gal = IntVar()
        self.dal_fry = IntVar()
        self.kadhi = IntVar()
        self.biryani = IntVar()
        self.pulav = IntVar()
        self.jeera_rice = IntVar()

        # ==================================soth indian variable===========================
        self.sambhar = IntVar()
        self.dusha = IntVar()
        self.idlli = IntVar()
        self.coconut_chatney = IntVar()
        self.lemon_rice = IntVar()
        self.besibelle_bhat = IntVar()

        #===============================total product price and tax variable============
        self.vegetable_price = StringVar()
        self.dal_rice_price = StringVar()
        self.south_indian_price = StringVar()

        self.vegetable_tax = StringVar()
        self.dal_rice_tax = StringVar()
        self.south_indian_tax = StringVar()

        #=========================== customar details============================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.c_gst=StringVar()
        self.search_bill=StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        #==========================costomar detailes
        F1=LabelFrame(self.root,text="Customer details", bd=10, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)  # fd is foreground to set the fount or text color
        F1.place(x=0,y=80,relwidth=1)  # here relwidth is in 0.0 to 1.0 means if 1.0 it will fill whole width

        cname_lbl=Label(F1,text="Customer name", bg=bg_color,fg="white", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=10,pady=5)
        cname_text=Entry(F1,width=12,font="arial 15", textvariable=self.c_name, bd=4, relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)  # relief is style of widget and textvariable is used to provide value to variable

        gname_lbl = Label(F1, text="Gst no.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=6, padx=10, pady=5)
        gname_text = Entry(F1, width=12, font="arial 15", textvariable=self.c_gst, bd=4, relief=SUNKEN).grid(row=0,column=7,padx=5,pady=5)

        cphn_lbl = Label(F1, text="Phone no.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=10, pady=5)
        cphn_text = Entry(F1, width=12, font="arial 15",textvariable=self.c_phon, bd=4, relief=SUNKEN).grid(row=0, column=3, padx=5, pady=5)

        c_bill_lbl = Label(F1, text="Bill number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=10, pady=5)
        c_bill_text = Entry(F1, width=12, font="arial 15",textvariable=self.search_bill, bd=4, relief=SUNKEN).grid(row=0, column=5, padx=5, pady=5)

        bill_btn=Button(F1,text="search", command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=9,padx=10,pady=10)


        #==========================cosmetics fram=====================
        F2=LabelFrame(self.root,text="vegetables fram", bd=10, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)  # bd is border
        F2.place(x=5,y=180,width=335,height=380)

        bath_lbl=Label(F2, text="Mix veg", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")  # sticky concatenation of zero or more of N, E, W, S, NE, NW, SE, SW
        bath_text=Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.mix_veg, bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=10)

        face_cream=Label(F2, text="chhole", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cream_text=Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.chhole, bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=10)

        face_wash=Label(F2, text="Pav Bhaji", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_text=Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.pav_bhaji, bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=10)

        hair_soap=Label(F2, text="Veg Kolhapuri", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_soap_text=Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.veg_kolhapuri, bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10, pady=10)

        hair_gel=Label(F2, text="Paneer", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_text=Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.paneer, bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10, pady=10)

        body_loshan=Label(F2, text="Rajma", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_loshan_text=Entry(F2, width=10, font=("times new roman", 16, "bold"),textvariable=self.rajma, bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10, pady=10)

        #==========================dal and rice fram=====================
        G1=LabelFrame(self.root,text="Dal & rice fram", bd=10, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        G1.place(x=340,y=180,width=325,height=380)

        rice=Label(G1, text="Black Dal", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_text=Entry(G1, width=10, font=("times new roman", 16, "bold"),textvariable=self.black_gal, bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=10)

        Food_oil=Label(G1, text="Dal Fry", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food_oil_text=Entry(G1, width=10, font=("times new roman", 16, "bold"),textvariable=self.dal_fry, bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=10)

        dall=Label(G1, text="Kadhi", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        dall_text=Entry(G1, width=10, font=("times new roman", 16, "bold"),textvariable=self.kadhi, bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=10)

        wheat=Label(G1, text="Biryani", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_text=Entry(G1, width=10, font=("times new roman", 16, "bold"),textvariable=self.biryani, bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10, pady=10)

        sugar=Label(G1, text="Pulav", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_text=Entry(G1, width=10, font=("times new roman", 16, "bold"),textvariable=self.pulav, bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10, pady=10)

        tea=Label(G1, text="Jeera ric", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_text=Entry(G1, width=10, font=("times new roman", 16, "bold"),textvariable=self.jeera_rice, bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10, pady=10)

        #==========================south indian fram=====================
        G2=LabelFrame(self.root,text="South indian", bd=10, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        G2.place(x=665,y=180,width=335,height=380)

        mazza=Label(G2, text="Sambhar", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        mazza_text=Entry(G2, width=10, font=("times new roman", 16, "bold"),textvariable=self.sambhar, bd=5, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=10)

        COCK=Label(G2, text="Idlli", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        COCK_text=Entry(G2, width=10, font=("times new roman", 16, "bold"),textvariable=self.idlli, bd=5, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=10)

        Frooti=Label(G2, text="Dusha", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Frooti_text=Entry(G2, width=10, font=("times new roman", 16, "bold"),textvariable=self.dusha, bd=5, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=10)

        Thumbsup=Label(G2, text="Coconut chutney", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Thumbsup_text=Entry(G2, width=10, font=("times new roman", 16, "bold"),textvariable=self.coconut_chatney, bd=5, relief=SUNKEN).grid(row=3,column=1, padx=10, pady=10)

        Limca=Label(G2, text="Lemon rice", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Limca_text=Entry(G2, width=10, font=("times new roman", 16, "bold"),textvariable=self.lemon_rice, bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10, pady=10)

        Sprite=Label(G2, text="Basibelle bhat", font=("times new roman", 16, "bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Sprite_text=Entry(G2, width=10, font=("times new roman", 16, "bold"),textvariable=self.besibelle_bhat, bd=5, relief=SUNKEN).grid(row=5,column=1, padx=10, pady=10)

        #==================================bill area=====================================================
        P1=Frame(self.root, bd=10, relief=SUNKEN,)  # frame is used to organize grope of widgets, it is like container
        P1.place(x=1000, y=180, width=355, height=380)
        bill_title=Label(P1,text="Bill area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(P1, orient=VERTICAL)
        self.textarea=Text(P1, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview())
        self.textarea.pack(fill=BOTH, expand=1)

        #========================button frame================================

        B1=LabelFrame(self.root,text="Bill menu", bd=10, font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        B1.place(x=0,y=560,relwidth=1,height=140)

        M1=Label(B1,text="Total vegetable price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="W")
        M1=Entry(B1, width=18,textvariable=self.vegetable_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)

        M2 = Label(B1, text="Total rice-dal price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="W")
        M2 = Entry(B1, width=18,textvariable=self.dal_rice_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, pady=1, padx=10)

        M3 = Label(B1, text="Total south-indian price", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="W")
        M3 = Entry(B1, width=18,textvariable=self.south_indian_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, pady=1, padx=10)

        C1 = Label(B1, text=" vegetable tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="W")
        C1 = Entry(B1, width=18,textvariable=self.vegetable_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=1, padx=10)

        C2 = Label(B1, text=" dal-rice tax", bg=bg_color, fg="white", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="W")
        C2 = Entry(B1, width=18,textvariable=self.dal_rice_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, pady=1, padx=10)

        C3 = Label(B1, text=" south-indian tax", bg=bg_color, fg="white",font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="W")
        C3 = Entry(B1, width=18,textvariable=self.south_indian_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, pady=1, padx=10)

        btn_f=Frame(B1,bd=7,relief=GROOVE)
        btn_f.place(x=740,width=585,height=105)

        total_btn=Button(btn_f,text="Total", command=self.total,bg="cadetblue",fg="white",pady=15, width=10, bd=2, font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        genrate_tax_btn=Button(btn_f,text="Gnerate tax", command=self.bill_area,bg="cadetblue",fg="white",pady=15, width=10, bd=2, font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",bg="cadetblue", command=self.clear_data,fg="white",pady=15, width=10, bd=2, font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",bg="cadetblue", command=self.Exit_app,fg="white",pady=15, width=10, bd=2, font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()   #this line of code directly print on textarea

    def total(self):
        # variable to store vegetable data
        self.s_v=self.mix_veg.get() *120
        self.f_v=self.chhole.get() * 115
        self.fw_v=self.pav_bhaji.get() * 115
        self.spray_v=self.veg_kolhapuri.get() * 120
        self.gell_v=self.paneer.get() * 150
        self.loshan_v=self.rajma.get() * 95
        self.total_vegetable_price=float(
            self.s_v+
            self.f_v+
            self.fw_v+
            self.spray_v+
            self.gell_v+
            self.loshan_v
            )
        self.vegetable_price.set("Rs. "+str(self.total_vegetable_price))
        self.co_tax=round((self.total_vegetable_price*0.05),2)
        self.vegetable_tax.set("Rs. "+str(self.co_tax))

        #variable to store dal&rice data
        self.rice_v=self.black_gal.get() * 95
        self.food_v=self.dal_fry.get() * 95
        self.daal_v=self.kadhi.get() * 90
        self.wheat_v=self.biryani.get() * 100
        self.sugar_v=self.pulav.get() * 90
        self.tea_v=self.jeera_rice.get() * 85
        self.total_dal_rice_price = float(
            self.rice_v +
            self.food_v +
            self.daal_v +
            self.wheat_v +
            self.sugar_v +
            self.tea_v)
        self.dal_rice_price.set("Rs. "+str(self.total_dal_rice_price))
        self.g_tax=round((self.total_dal_rice_price*0.05),2)
        self.dal_rice_tax.set("Rs. "+str(self.g_tax))

        #variable to store south indian
        self.m_v=self.sambhar.get() * 40
        self.c_v=self.idlli.get() * 20
        self.frooti_v=self.dusha.get() * 30
        self.thumbsup_v=self.coconut_chatney.get() * 20
        self.limca_v=self.lemon_rice.get() * 80
        self.sprite_v=self.besibelle_bhat.get() * 95
        self.total_south_indian_price = float(
            self.m_v +
            self.c_v+
            self.frooti_v+
            self.thumbsup_v+
            self.limca_v+
            self.sprite_v
        )

        self.south_indian_price.set("Rs. "+str(self.total_south_indian_price))
        self.c_tax=round((self.total_south_indian_price*0.05),2)
        self.south_indian_tax.set("Rs. "+str(self.c_tax))

        self.total_bill=float(  self.c_tax +
                                self.co_tax +
                                self.g_tax +
                                self.total_vegetable_price +
                                self.total_dal_rice_price +
                                self.total_south_indian_price)


    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\tWelcome webcode reatil\n")
        self.textarea.insert(END,f"\n Bill no: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone no: {self.c_phon.get()}")
        self.textarea.insert(END,f"\n Gst no: {self.c_gst.get()}")
        self.textarea.insert(END,f"\n=======================================")
        self.textarea.insert(END,f"\n products\t\t\tQTY \tPrice")
        self.textarea.insert(END,f"\n=======================================")

    def bill_area(self):

        if self.c_name.get()=="" or self.c_phon.get()=="" or self.c_gst.get()=="":
            messagebox.showerror("Error","customer detailes are must")
        elif self.vegetable_price.get()=="Rs. 0.0" and self.dal_rice_price.get()=="Rs. 0.0" and self.south_indian_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","no products are seleted")

        else:
            self.welcome_bill()
            #======vegetable=========
            if self.mix_veg.get()!=0:
                self.textarea.insert(END,f"\n Mix veg\t\t\t{self.mix_veg.get()}\t{self.s_v}")
            if self.chhole.get()!=0:
                self.textarea.insert(END,f"\n Chhole\t\t\t{self.chhole.get()}\t{self.f_v}")
            if self.pav_bhaji.get() != 0:
                self.textarea.insert(END, f"\n Pav Bhaji\t\t\t{self.pav_bhaji.get()}\t{self.fw_v}")
            if self.paneer.get()!=0:
                self.textarea.insert(END,f"\n Veg Kolhapuri\t\t\t{self.paneer.get()}\t{self.spray_v}")
            if self.rajma.get()!=0:
                self.textarea.insert(END,f"\n Paneer\t\t\t{self.rajma.get()}\t{self.gell_v}")
            if self.veg_kolhapuri.get()!=0:
                self.textarea.insert(END,f"\n Rajma\t\t\t{self.veg_kolhapuri.get()}\t{self.loshan_v}")

            #======dal_rice=========
            if self.black_gal.get()!=0:
                self.textarea.insert(END,f"\n Black Dal\t\t\t{self.black_gal.get()}\t{self.rice_v}")
            if self.dal_fry.get()!=0:
                self.textarea.insert(END,f"\n dal Fry\t\t\t{self.dal_fry.get()}\t{self.food_v}")
            if self.kadhi.get() != 0:
                self.textarea.insert(END,f"\n Kadhi\t\t\t{self.kadhi.get()}\t{self.daal_v}")
            if self.biryani.get()!=0:
                self.textarea.insert(END,f"\n Biryani\t\t\t{self.biryani.get()}\t{self.wheat_v}")
            if self.pulav.get()!=0:
                self.textarea.insert(END,f"\n Pulav\t\t\t{self.pulav.get()}\t{self.sugar_v}")
            if self.jeera_rice.get()!=0:
                self.textarea.insert(END,f"\n Jeera Rice\t\t\t{self.jeera_rice.get()}\t{self.tea_v}")

            #======south indian=========
            if self.sambhar.get()!=0:
                self.textarea.insert(END,f"\n Sambhar\t\t\t{self.sambhar.get()}\t{self.m_v}")
            if self.idlli.get()!=0:
                self.textarea.insert(END,f"\n Idlli\t\t\t{self.idlli.get()}\t{self.c_v}")
            if self.dusha.get() != 0:
                self.textarea.insert(END, f"\n Dusha\t\t\t{self.dusha.get()}\t{self.frooti_v}")
            if self.coconut_chatney.get()!=0:
                self.textarea.insert(END,f"\n Coconut Chutney\t\t\t{self.coconut_chatney.get()}\t{self.thumbsup_v}")
            if self.lemon_rice.get()!=0:
                self.textarea.insert(END,f"\n Lemon Rice\t\t\t{self.lemon_rice.get()}\t{self.limca_v}")
            if self.besibelle_bhat.get()!=0:
                self.textarea.insert(END,f"\n Basibelle Bhat\t\t\t{self.besibelle_bhat.get()}\t{self.sprite_v}")

            self.textarea.insert(END, f"\n---------------------------------------")
            if self.vegetable_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\n Vegetable tax\t\t\t{self.vegetable_tax.get()}")
            if self.dal_rice_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\n Dal & rice tax\t\t\t{self.dal_rice_tax.get()}")
            if self.south_indian_tax.get()!="Rs. 0.0":
                self.textarea.insert(END, f"\n south indian tax\t\t\t{self.south_indian_tax.get()}")
            self.textarea.insert(END, f"\n Total bill: \t\t\tRs. {self.total_bill}")
            self.textarea.insert(END, f"\n---------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save bill","do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bill_folder/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no. :{self.bill_no.get()} saved successfully")
        else:
            return
    def find_bill(self):
        present ="no"
        for i in os.listdir("bill_folder/"):            # 0  . 1
            if i.split('.')[0]==self.search_bill.get(): #3245.txt
                f1=open(f"bill_folder/{i}","r")
                self.textarea.delete("0.1",END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid bill no.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear data")
        if op>0:
            # ==================================cosmetics variable===========================
            self.mix_veg.set(0)
            self.chhole.set(0)
            self.pav_bhaji.set(0)
            self.veg_kolhapuri.set(0)
            self.paneer.set(0)
            self.rajma.set(0)

            # ==================================grocery variable===========================
            self.black_gal.set(0)
            self.dal_fry.set(0)
            self.kadhi.set(0)
            self.biryani.set(0)
            self.pulav.set(0)
            self.jeera_rice.set(0)

            # ==================================cold drinks variable===========================
            self.sambhar.set(0)
            self.idlli.set(0)
            self.dusha.set(0)
            self.coconut_chatney.set(0)
            self.lemon_rice.set(0)
            self.besibelle_bhat.set(0)

            # ===============================total product price and tax variable============
            self.vegetable_price.set("")
            self.dal_rice_price.set("")
            self.south_indian_price.set("")

            self.vegetable_tax.set("")
            self.dal_rice_tax.set("")
            self.south_indian_tax.set("")

            # =========================== customar details============================
            self.c_name.set("")
            self.c_phon.set("")
            self.c_gst.set("")
            self.search_bill.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()

root = Tk()
root.iconbitmap('File_Management.ico')
obj = bill_app(root)
root.mainloop()