import tkinter as tk
from tkinter import messagebox, ttk

class InventoryManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("700x500")
        
        self.inventory = {}
        
        # UI Elements
        self.create_widgets()
        
    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Product Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_quantity = tk.Label(self.root, text="Quantity:")
        self.label_quantity.grid(row=1, column=0, padx=10, pady=10)
        
        self.entry_quantity = tk.Entry(self.root)
        self.entry_quantity.grid(row=1, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.edit_button = tk.Button(self.root, text="Edit Product", command=self.edit_product)
        self.edit_button.grid(row=2, column=1, padx=10, pady=10)
        
        self.tree = ttk.Treeview(self.root, columns=("Product", "Quantity"), show="headings")
        self.tree.heading("Product", text="Product Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        self.delete_button = tk.Button(self.root, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=4, column=0, padx=10, pady=10)
        
        self.report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=4, column=1, padx=10, pady=10)
    
    def add_product(self):
        name = self.entry_name.get().strip()
        quantity = self.entry_quantity.get().strip()
        
        if not name or not quantity.isdigit():
            messagebox.showerror("Input Error", "Please enter valid product details.")
            return
        
        quantity = int(quantity)
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity
        
        self.update_treeview()
    
    def edit_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a product to edit.")
            return
        
        name = self.tree.item(selected_item[0], "values")[0]
        new_quantity = self.entry_quantity.get().strip()
        
        if not new_quantity.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid quantity.")
            return
        
        self.inventory[name] = int(new_quantity)
        self.update_treeview()
        
    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a product to delete.")
            return
        
        for item in selected_item:
            name = self.tree.item(item, "values")[0]
            del self.inventory[name]
            self.tree.delete(item)
        
    def generate_report(self):
        low_stock = [name for name, qty in self.inventory.items() if qty < 5]
        report_message = "Low Stock Products:\n" + "\n".join(low_stock) if low_stock else "All products are sufficiently stocked."
        messagebox.showinfo("Inventory Report", report_message)
        
    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for name, quantity in self.inventory.items():
            self.tree.insert("", "end", values=(name, quantity))

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManager(root)
    root.mainloop()
