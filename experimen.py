from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import mysql.connector as sqlct

class MedicalStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Urvi Medical Store")
        self.root.geometry("800x600")

        # Initialize variables for username and password
        self.username_var = StringVar()
        self.password_var = StringVar()

        # Establish database connection and create necessary tables
        self.create_db()

        # Login page
        self.login_page()

    # Add a method to establish database connection and create necessary tables
    def create_db(self):
        try:
            self.mycn = sqlct.connect(host="localhost", user="root", password="", database="chetanvarade123")
            if self.mycn.is_connected():
                print("\tThank you for choosing to shop with Apollo Medical Store.")
                self.mycur = self.mycn.cursor()
                cmd1 = "CREATE TABLE IF NOT EXISTS _medicalproject(ProductCode INTEGER PRIMARY KEY, " \
                       "name CHAR(50) NOT NULL, Packing CHAR(50), Expirydate DATE, Company CHAR(50), " \
                       "Batch CHAR(10), Quantity INTEGER, Rate INTEGER)"
                self.mycur.execute(cmd1)
                cust1 = "CREATE TABLE IF NOT EXISTS customertable(BillNumber INTEGER, Customername VARCHAR(50), " \
                        "Doctorname VARCHAR(50), Productcode INTEGER, Quantity INTEGER, " \
                        "FOREIGN KEY(ProductCode) REFERENCES _medicalproject(ProductCode))"
                self.mycur.execute(cust1)
                self.mycn.commit()
        except sqlct.Error as e:
            print("Error:", e)

    # Modify other methods to access the cursor and connection
    def save_medicine(self):
        ProductCode = self.ProductCodeEntry.get()
        name = self.NameEntry.get()
        Packing = self.PackingEntry.get()
        ExpiryDate = self.ExpiryEntry.get()
        Company = self.CompanyEntry.get()
        Batch = self.BatchEntry.get()
        Quantity = self.QuantityEntry.get()
        Rate = self.RateEntry.get()
        try:
            # Access cursor and connection
            cmd = "INSERT INTO _medicalproject (ProductCode, name, Packing, Expirydate, Company, Batch, Quantity, Rate) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (ProductCode, name, Packing, ExpiryDate, Company, Batch, Quantity, Rate)
            self.mycur.execute(cmd, values)
            self.mycn.commit()
            messagebox.showinfo("Success", "Medicine added successfully!")
        except sqlct.Error as e:
            print("Error:", e)


    # In the __name__ == "__main__" block, just create the app instance and run the main loop

    def login_page(self):
        LoginFrame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        LoginFrame.pack(fill=BOTH, expand=1)

        l_title = Label(LoginFrame, text="Urvi Medical Store", bg="crimson", fg="white",
                        font=("times new roman", 40, "bold"))
        l_title.grid(row=0, columnspan=2, pady=20)

        # Username Entry
        username_label = Label(LoginFrame, text="Username:")
        username_label.grid(row=1, column=0, padx=20, pady=10)
        username_entry = Entry(LoginFrame, textvariable=self.username_var)
        username_entry.grid(row=1, column=1, padx=20, pady=10)

        # Password Entry
        password_label = Label(LoginFrame, text="Password:")
        password_label.grid(row=2, column=0, padx=20, pady=10)
        password_entry = Entry(LoginFrame, show="*", textvariable=self.password_var)
        password_entry.grid(row=2, column=1, padx=20, pady=10)

        # Login Button
        login_btn = Button(LoginFrame, text="Login", width=20, command=self.verify_login)
        login_btn.grid(row=3, columnspan=2, pady=20)

    def verify_login(self):
        # Get the entered username and password
        username = self.username_var.get()
        password = self.password_var.get()

        # Verify the username and password
        if username == "chetanvarade123" and password == "12345":
            # If login is successful, switch to the manage_medicine_frame
            self.switch_page(self.manage_medicine_frame)

        else:
            # Display an error message for unsuccessful login
            messagebox.showerror("Login Failed", "Invalid username or password")
    def create_db(self):
        self.mycn = sqlct.connect(host="localhost", user="root", password="", database="chetanvarade123")
        if self.mycn.is_connected():
            print("\tThank you for choosing to shop with Apollo Medical Store.")
        self.mycur = self.mycn.cursor()
        cmd1 = "CREATE TABLE IF NOT EXISTS _medicalproject(ProductCode INTEGER PRIMARY KEY, " \
               "name CHAR(50) NOT NULL, Packing CHAR(50), Expirydate DATE, Company CHAR(50), " \
               "Batch CHAR(10), Quantity INTEGER, Rate INTEGER)"
        self.mycur.execute(cmd1)
        cust1 = "CREATE TABLE IF NOT EXISTS customertable(BillNumber INTEGER, Customername VARCHAR(50), " \
                "Doctorname VARCHAR(50), Productcode INTEGER, Quantity INTEGER, " \
                "FOREIGN KEY(ProductCode) REFERENCES _medicalproject(ProductCode))"
        self.mycur.execute(cust1)

    def switch_page(self, new_frame_func):
        for widget in self.root.winfo_children():
            widget.destroy()
        new_frame_func()

    def manage_medicine_frame(self):
        ManageFrame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        ManageFrame.pack(fill=BOTH, expand=1)

        m_title = Label(ManageFrame, text="Manage Medicines", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # Add Medicine Button
        add_medicine_btn = Button(ManageFrame, text="Add Medicine", width=20, command=self.add_medicine)
        add_medicine_btn.grid(row=1, column=0, padx=20, pady=10)

        # Display Medicine Button
        display_medicine_btn = Button(ManageFrame, text="Display Medicines", width=20, command=self.display_medicine)
        display_medicine_btn.grid(row=1, column=1, padx=20, pady=10)

        # Search Medicine Button
        search_medicine_btn = Button(ManageFrame, text="Search Medicine", width=20, command=self.search_medicine)
        search_medicine_btn.grid(row=2, columnspan=2, pady=10)

        # Delete Medicine Button
        delete_medicine_btn = Button(ManageFrame, text="Delete Medicine", width=20, command=self.delete_medicine)
        delete_medicine_btn.grid(row=3, columnspan=2, pady=10)

        # Next Button
        next_btn = Button(ManageFrame, text="Next", width=20, command=lambda: self.switch_page(self.manage_billing_frame))
        next_btn.grid(row=4, columnspan=2, pady=20)

    def add_medicine(self):
        AddMedicineFrame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        AddMedicineFrame.pack(fill=BOTH, expand=1)

        a_title = Label(AddMedicineFrame, text="Add Medicine", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        a_title.grid(row=0, columnspan=2, pady=20)

        # Product Code
        ProductCodeLabel = Label(AddMedicineFrame, text="Product Code:")
        ProductCodeLabel.grid(row=1, column=0, padx=20, pady=10)
        self.ProductCodeEntry = Entry(AddMedicineFrame)
        self.ProductCodeEntry.grid(row=1, column=1, padx=20, pady=10)

        # Medicine Name
        NameLabel = Label(AddMedicineFrame, text="Medicine Name:")
        NameLabel.grid(row=2, column=0, padx=20, pady=10)
        self.NameEntry = Entry(AddMedicineFrame)
        self.NameEntry.grid(row=2, column=1, padx=20, pady=10)

        # Packing Details
        PackingLabel = Label(AddMedicineFrame, text="Packing Details:")
        PackingLabel.grid(row=3, column=0, padx=20, pady=10)
        self.PackingEntry = Entry(AddMedicineFrame)
        self.PackingEntry.grid(row=3, column=1, padx=20, pady=10)

        # Expiry Date
        ExpiryLabel = Label(AddMedicineFrame, text="Expiry Date (yyyy-mm-dd):")
        ExpiryLabel.grid(row=4, column=0, padx=20, pady=10)
        self.ExpiryEntry = Entry(AddMedicineFrame)
        self.ExpiryEntry.grid(row=4, column=1, padx=20, pady=10)

        # Company Name
        CompanyLabel = Label(AddMedicineFrame, text="Company Name:")
        CompanyLabel.grid(row=5, column=0, padx=20, pady=10)
        self.CompanyEntry = Entry(AddMedicineFrame)
        self.CompanyEntry.grid(row=5, column=1, padx=20, pady=10)

        # Batch Number
        BatchLabel = Label(AddMedicineFrame, text="Batch Number:")
        BatchLabel.grid(row=6, column=0, padx=20, pady=10)
        self.BatchEntry = Entry(AddMedicineFrame)
        self.BatchEntry.grid(row=6, column=1, padx=20, pady=10)

        # Quantity
        QuantityLabel = Label(AddMedicineFrame, text="Quantity:")
        QuantityLabel.grid(row=7, column=0, padx=20, pady=10)
        self.QuantityEntry = Entry(AddMedicineFrame)
        self.QuantityEntry.grid(row=7, column=1, padx=20, pady=10)

        # Rate
        RateLabel = Label(AddMedicineFrame, text="Rate:")
        RateLabel.grid(row=8, column=0, padx=20, pady=10)
        self.RateEntry = Entry(AddMedicineFrame)
        self.RateEntry.grid(row=8, column=1, padx=20, pady=10)

        # Save Button
        save_btn = Button(AddMedicineFrame, text="Save", width=20, command=self.save_medicine)
        save_btn.grid(row=9, columnspan=2, pady=20)

        # Back Button
        back_btn = Button(AddMedicineFrame, text="Back", width=20, command=lambda: self.switch_page(self.manage_medicine_frame))
        back_btn.grid(row=10, columnspan=2, pady=20)


    def display_medicine(self):
        DisplayMedicineFrame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        DisplayMedicineFrame.pack(fill=BOTH, expand=1)

        d_title = Label(DisplayMedicineFrame, text="Display Medicines", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        d_title.pack(side=TOP, fill=X)

        # Treeview for displaying medicines
        tree_scroll = Scrollbar(DisplayMedicineFrame, orient=VERTICAL)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.medicine_tree = ttk.Treeview(DisplayMedicineFrame, column=("Product Code", "Name", "Packing", "Expiry Date", "Company", "Batch", "Quantity", "Rate"),
                                          yscrollcommand=tree_scroll.set)
        self.medicine_tree.heading("Product Code", text="Product Code")
        self.medicine_tree.heading("Name", text="Name")
        self.medicine_tree.heading("Packing", text="Packing")
        self.medicine_tree.heading("Expiry Date", text="Expiry Date")
        self.medicine_tree.heading("Company", text="Company")
        self.medicine_tree.heading("Batch", text="Batch")
        self.medicine_tree.heading("Quantity", text="Quantity")
        self.medicine_tree.heading("Rate", text="Rate")

        self.medicine_tree['show'] = 'headings'
        self.medicine_tree.pack(fill=BOTH, expand=1)

        # Configure scrollbar
        tree_scroll.config(command=self.medicine_tree.yview)

        # Fetch and display medicine data from the database
        cmd2 = "SELECT * FROM _medicalproject"
        self.mycur.execute(cmd2)
        medicine_records = self.mycur.fetchall()
        if medicine_records:
            for record in medicine_records:
                self.medicine_tree.insert('', 'end', values=record)
        else:
            messagebox.showinfo("No Records", "No medicine records found in the database.")

        # Back Button
        back_btn = Button(DisplayMedicineFrame, text="Back", width=20, command=lambda: self.switch_page(self.manage_medicine_frame))
        back_btn.pack(side=BOTTOM, pady=20)

    def search_medicine(self):
        SearchMedicineFrame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        SearchMedicineFrame.pack(fill=BOTH, expand=1)

        s_title = Label(SearchMedicineFrame, text="Search Medicine", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        s_title.grid(row=0, columnspan=2, pady=20)

        # Medicine Name Entry
        med_name_label = Label(SearchMedicineFrame, text="Medicine Name:")
        med_name_label.grid(row=1, column=0, padx=20, pady=10)
        self.med_name_entry = Entry(SearchMedicineFrame)
        self.med_name_entry.grid(row=1, column=1, padx=20, pady=10)

        # Search Button
        search_btn = Button(SearchMedicineFrame, text="Search", width=20, command=self.perform_search)
        search_btn.grid(row=2, columnspan=2, pady=20)

        # Back Button
        back_btn = Button(SearchMedicineFrame, text="Back", width=20,
                          command=lambda: self.switch_page(self.manage_medicine_frame))
        back_btn.grid(row=3, columnspan=2, pady=20)

    def perform_search(self):
        med_name = self.med_name_entry.get()
        cmd4 = "SELECT * FROM _medicalproject WHERE name LIKE '%" + med_name + "%'"
        self.mycur.execute(cmd4)
        search_results = self.mycur.fetchall()

        if search_results:
            # Display search results in a messagebox
            result_text = "Search Results:\n"
            for result in search_results:
                result_text += f"Product Code: {result[0]}, Name: {result[1]}, Packing: {result[2]}, " \
                               f"Expiry Date: {result[3]}, Company: {result[4]}, Batch: {result[5]}, " \
                               f"Quantity: {result[6]}, Rate: {result[7]}\n"
            messagebox.showinfo("Search Results", result_text)
        else:
            messagebox.showinfo("No Records", "No medicine records found matching the search criteria.")

    def delete_medicine(self):
        delete_medicine = simpledialog.askinteger("Delete Medicine", "Enter the medicine product code that you want to delete:")
        cmd3 = "SELECT COUNT(*) FROM customertable WHERE Productcode=" + str(delete_medicine)
        self.mycur.execute(cmd3)
        total_record = self.mycur.fetchone()[0]
        if total_record == 0:
            cmd7 = "DELETE FROM _medicalproject WHERE ProductCode=" + str(delete_medicine)
            self.mycur.execute(cmd7)
            messagebox.showinfo("Success", "Record has been deleted")
        else:
            cmd7 = "UPDATE _medicalproject SET quantity=0 WHERE ProductCode=" + str(delete_medicine)
            self.mycur.execute(cmd7)
            messagebox.showinfo("Information", "This medicine has already been sold, so it can't be deleted. Hence, the quantity of this medicine is set to zero.")

    def manage_billing_frame(self):
        ManageBillingFrame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        ManageBillingFrame.pack(fill=BOTH, expand=1)

        b_title = Label(ManageBillingFrame, text="Manage Billing", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        b_title.grid(row=0, columnspan=2, pady=20)

        # Add New Bill Button
        add_new_bill_btn = Button(ManageBillingFrame, text="Add New Bill", width=20, command=self.add_newbill)
        add_new_bill_btn.grid(row=1, column=0, padx=20, pady=10)

        # Display Bill Button
        display_bill_btn = Button(ManageBillingFrame, text="Display Bill", width=20, command=self.display_bill)
        display_bill_btn.grid(row=1, column=1, padx=20, pady=10)

        # Search Bill Button
        search_bill_btn = Button(ManageBillingFrame, text="Search Bill", width=20, command=self.search_bill)
        search_bill_btn.grid(row=2, column=0, padx=20, pady=10)

        # Edit Bill Button
        edit_bill_btn = Button(ManageBillingFrame, text="Edit Bill", width=20, command=self.edit_bill)
        edit_bill_btn.grid(row=2, column=1, padx=20, pady=10)

        # Delete Bill Button
        delete_bill_btn = Button(ManageBillingFrame, text="Delete Bill", width=20, command=self.delete_bill)
        delete_bill_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Exit Button
        exit_btn = Button(ManageBillingFrame, text="Exit", width=20, command=self.root.quit)
        exit_btn.grid(row=4, columnspan=2, pady=10)

    def add_newbill(self):
        cmd3 = "select max(BillNumber) from customertable"
        self.mycur.execute(cmd3)
        r3 = self.mycur.fetchone()
        if r3[0] is not None:
            BillNumber = r3[0] + 1
        else:
            BillNumber = 1
        print("Your bill number is:", BillNumber)  # BILL NUMBER
        name = simpledialog.askstring("Input", "Enter your name:")  # NAME
        DoctorName = simpledialog.askstring("Input", "Enter your doctor's name:")  # DOCTOR'S NAME
        while True:
            Productcode = simpledialog.askinteger("Input",
                                                  "Enter product code of your medicine:")  # PRODUCT CODE OF MEDICINE
            Quantity = simpledialog.askinteger("Input", "Enter quantity for your medicine:")  # QUANTITY
            cmd = "insert into customertable values (%s, %s, %s, %s, %s)"
            values = (BillNumber, name, DoctorName, Productcode, Quantity)
            self.mycur.execute(cmd, values)
            addmed = simpledialog.askstring("Input", "Do you want to add medicine(y/n)?")
            if addmed.lower() == 'n':
                break
        self.mycn.commit()
        messagebox.showinfo("Success", "Record has been added")

    def display_bill(self):
        DisplayBillFrame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        DisplayBillFrame.pack(fill=BOTH, expand=1)

        b_title = Label(DisplayBillFrame, text="Display Bill", bg="crimson", fg="white",
                        font=("times new roman", 30, "bold"))
        b_title.pack(side=TOP, fill=X)

        # Treeview for displaying bills
        tree_scroll = Scrollbar(DisplayBillFrame, orient=VERTICAL)
        tree_scroll.pack(side=RIGHT, fill=Y)

        bill_tree = ttk.Treeview(DisplayBillFrame, column=(
            "Bill Number", "Customer Name", "Doctor Name",
            "Product Code", "Medicine Name", "Quantity", "Rate", "Amount"),
                                 yscrollcommand=tree_scroll.set)
        bill_tree.heading("Bill Number", text="Bill Number")
        bill_tree.heading("Customer Name", text="Customer Name")
        bill_tree.heading("Doctor Name", text="Doctor Name")
        bill_tree.heading("Product Code", text="Product Code")
        bill_tree.heading("Medicine Name", text="Medicine Name")
        bill_tree.heading("Quantity", text="Quantity")
        bill_tree.heading("Rate", text="Rate")
        bill_tree.heading("Amount", text="Amount")

        bill_tree['show'] = 'headings'
        bill_tree.pack(fill=BOTH, expand=1)

        # Configure scrollbar
        tree_scroll.config(command=bill_tree.yview)

        # Fetch and display bill data from the database
        cmd = "SELECT CT.BillNumber, CT.Customername, CT.DoctorName, CT.Productcode, MDT.name, CT.Quantity, MDT.Rate, CT.Quantity * MDT.Rate Amount " \
              "FROM customertable CT, _medicalproject MDT WHERE CT.Productcode=MDT.ProductCode"
        self.mycur.execute(cmd)
        bill_records = self.mycur.fetchall()
        if bill_records:
            for record in bill_records:
                bill_tree.insert('', 'end', values=record)
        else:
            messagebox.showinfo("No Records", "No bill records found in the database.")

        # Back Button
        back_btn = Button(DisplayBillFrame, text="Back", width=20,
                          command=lambda: self.switch_page(self.manage_billing_frame))
        back_btn.pack(side=BOTTOM, pady=20)

    def search_bill(self):
        Bill_Number = simpledialog.askinteger("Input", "Enter the bill number which you want to search :")
        cmd = "SELECT CT.BillNumber, CT.Customername, CT.DoctorName, CT.Productcode, MDT.name, CT.Quantity, MDT.Rate, CT.Quantity * MDT.Rate Amount " \
              "FROM customertable CT, _medicalproject MDT WHERE CT.Productcode=MDT.ProductCode AND CT.BillNumber=%s"
        self.mycur.execute(cmd, (Bill_Number,))
        bill_record = self.mycur.fetchone()
        if bill_record:
            messagebox.showinfo("Bill Information",
                                f"Bill Number: {bill_record[0]}\nCustomer Name: {bill_record[1]}\nDoctor Name: {bill_record[2]}\n"
                                f"Product Code: {bill_record[3]}\nMedicine Name: {bill_record[4]}\n"
                                f"Quantity: {bill_record[5]}\nRate: {bill_record[6]}\nAmount: {bill_record[7]}")
        else:
            messagebox.showinfo("No Records", "No bill record found for the given bill number.")

    def edit_bill(self):
        Bill_Number = simpledialog.askinteger("Input", "Enter the bill number that you want to edit :")
        Product_Code = simpledialog.askinteger("Input", "Enter the product code that you want to edit :")
        Quantity_New = simpledialog.askinteger("Input", "Enter the new quantity for the medicine :")
        cmd = "UPDATE customertable SET Quantity=%s WHERE BillNumber=%s AND Productcode=%s"
        self.mycur.execute(cmd, (Quantity_New, Bill_Number, Product_Code))
        self.mycn.commit()
        messagebox.showinfo("Success", "Record has been updated")

    def delete_bill(self):
        Bill_Delete = simpledialog.askinteger("Input", "Enter the bill number you want to delete:")
        cmd = "DELETE FROM customertable WHERE BillNumber=%s"
        self.mycur.execute(cmd, (Bill_Delete,))
        self.mycn.commit()
        messagebox.showinfo("Success", "The record has been deleted!")


if __name__ == "__main__":
    root = Tk()
    app = MedicalStoreApp(root)
    root.mainloop()
