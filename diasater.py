import tkinter as tk
from tkinter import ttk, messagebox

class DisasterManagementSystem:
    def __init__(self):
        self.camps = {}
        self.victims = {}
        self.supplies = {"medicine": 0, "food": 0}
        self.camp_counter = 1
        self.victim_counter = 1

    def add_camp(self, capacity):
        camp_id = self.camp_counter
        self.camps[camp_id] = {
            "capacity": capacity,
            "current_occupancy": 0,
            "victims": []
        }
        self.camp_counter += 1
        return camp_id

    def register_victim(self, name, place, health_status):
        if health_status not in ["critical", "normal"]:
            return "Invalid health status"
        
        available_camp = None
        for camp_id, camp_data in self.camps.items():
            if camp_data["current_occupancy"] < camp_data["capacity"]:
                available_camp = camp_id
                break
        
        if available_camp is None:
            return "All camps are full. Cannot register victim."
        
        victim_id = self.victim_counter
        self.victims[victim_id] = {
            "name": name,
            "place": place,
            "camp_id": available_camp,
            "health_status": health_status
        }
        
        self.camps[available_camp]["victims"].append(victim_id)
        self.camps[available_camp]["current_occupancy"] += 1
        self.victim_counter += 1
        
        return f"Victim registered in Camp {available_camp}"

    def add_supplies(self, medicine=0, food=0):
        self.supplies["medicine"] += medicine
        self.supplies["food"] += food
        return f"Supplies added: Medicine: {medicine}, Food: {food}"

    def distribute_supplies(self, camp_id, medicine, food):
        if camp_id not in self.camps:
            return "Camp not found"
        if medicine > self.supplies["medicine"] or food > self.supplies["food"]:
            return "Insufficient supplies"
        
        self.supplies["medicine"] -= medicine
        self.supplies["food"] -= food
        return f"Distributed to Camp {camp_id}: Medicine: {medicine}, Food: {food}"

    def generate_report(self):
        total_camps = len(self.camps)
        total_victims = len(self.victims)
        
        max_occupancy_camp = max(self.camps.items(), 
                                 key=lambda x: x[1]["current_occupancy"])
        
        return f"""
        ========== DISASTER RELIEF REPORT ==========
        Total Camps: {total_camps}
        Total Victims Registered: {total_victims}
        Camp with Highest Occupancy: Camp {max_occupancy_camp[0]} ({max_occupancy_camp[1]['current_occupancy']}/{max_occupancy_camp[1]['capacity']})
        Total Medicine Distributed: {self.supplies['medicine']}
        Total Food Packets Distributed: {self.supplies['food']}
        ==========================================
        """

    def display_victims(self):
        for victim_id, victim_data in self.victims.items():
            print(f"ID: {victim_id}, Name: {victim_data['name']}, Place: {victim_data['place']}, Camp: {victim_data['camp_id']}, Health: {victim_data['health_status']}")


class DisasterManagementGUI:
    def __init__(self, root, system):
        self.root = root
        self.system = system
        self.root.title("Disaster Management System")
        self.root.geometry("1000x700")
        
        # Colors
        self.bg_color = "#1a1a2e"
        self.fg_color = "#ffffff"
        self.accent_color = "#e74c3c"
        self.tab_color = "#16213e"
        self.button_color = "#e74c3c"
        self.button_hover = "#c0392b"
        self.text_bg = "#0f3460"
        
        self.root.configure(bg=self.bg_color)
        self.setup_styles()
        self.create_widgets()
    
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("TNotebook", background=self.bg_color, borderwidth=0)
        style.configure("TNotebook.Tab", padding=[20, 10], font=("Arial", 11, "bold"))
        style.configure("TFrame", background=self.tab_color)
        style.configure("TLabel", background=self.tab_color, foreground=self.fg_color, font=("Arial", 10))
        style.configure("TEntry", fieldbackground=self.text_bg, foreground=self.fg_color, font=("Arial", 10))
        style.configure("TCombobox", fieldbackground=self.text_bg, foreground=self.fg_color, font=("Arial", 10))
        style.map("TButton", background=[("active", self.button_hover)])
        style.configure("TButton", background=self.button_color, foreground=self.fg_color, font=("Arial", 10, "bold"), padding=10)
    
    def create_widgets(self):
        header = tk.Frame(self.root, bg=self.accent_color, height=80)
        header.pack(fill=tk.X, padx=0, pady=0)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="🚨 Disaster Management System 🚨", 
                        bg=self.accent_color, fg=self.fg_color, font=("Arial", 24, "bold"))
        title.pack(pady=15)
        
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        camp_frame = ttk.Frame(notebook)
        notebook.add(camp_frame, text="🏕️ Manage Camps")
        self.setup_camp_tab(camp_frame)
        
        victim_frame = ttk.Frame(notebook)
        notebook.add(victim_frame, text="👥 Register Victims")
        self.setup_victim_tab(victim_frame)
        
        supplies_frame = ttk.Frame(notebook)
        notebook.add(supplies_frame, text="📦 Manage Supplies")
        self.setup_supplies_tab(supplies_frame)
        
        report_frame = ttk.Frame(notebook)
        notebook.add(report_frame, text="📊 Report")
        self.setup_report_tab(report_frame)
    
    def setup_camp_tab(self, frame):
        ttk.Label(frame, text="Camp Capacity:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.camp_capacity = ttk.Entry(frame, width=20)
        self.camp_capacity.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(frame, text="➕ Add Camp", command=self.add_camp).grid(row=0, column=2, padx=5, pady=5)
        
        self.camp_display = tk.Text(frame, height=18, width=80, bg=self.text_bg, fg=self.fg_color, font=("Arial", 10))
        self.camp_display.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(1, weight=1)
    
    def setup_victim_tab(self, frame):
        ttk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.victim_name = ttk.Entry(frame, width=20)
        self.victim_name.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame, text="Place:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.victim_place = ttk.Entry(frame, width=20)
        self.victim_place.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame, text="Health Status:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.victim_health = ttk.Combobox(frame, values=["critical", "normal"], width=17)
        self.victim_health.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(frame, text="✅ Register Victim", command=self.register_victim).grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        
        self.victim_display = tk.Text(frame, height=14, width=80, bg=self.text_bg, fg=self.fg_color, font=("Arial", 10))
        self.victim_display.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_columnconfigure(1, weight=1)
    
    def setup_supplies_tab(self, frame):
        ttk.Label(frame, text="Medicine:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.add_medicine = ttk.Entry(frame, width=20)
        self.add_medicine.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame, text="Food:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.add_food = ttk.Entry(frame, width=20)
        self.add_food.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(frame, text="➕ Add Supplies", command=self.add_supplies).grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame, text="Distribute to Camp:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.dist_camp_id = ttk.Entry(frame, width=20)
        self.dist_camp_id.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame, text="Medicine to Distribute:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.dist_medicine = ttk.Entry(frame, width=20)
        self.dist_medicine.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Label(frame, text="Food to Distribute:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.dist_food = ttk.Entry(frame, width=20)
        self.dist_food.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        ttk.Button(frame, text="🚚 Distribute Supplies", command=self.distribute_supplies).grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")
        
        self.supplies_display = tk.Text(frame, height=10, width=80, bg=self.text_bg, fg=self.fg_color, font=("Arial", 10))
        self.supplies_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        frame.grid_rowconfigure(7, weight=1)
        frame.grid_columnconfigure(1, weight=1)
    
    def setup_report_tab(self, frame):
        ttk.Button(frame, text="📄 Generate Report", command=self.generate_report).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.report_display = tk.Text(frame, height=20, width=80, bg=self.text_bg, fg=self.fg_color, font=("Arial", 10))
        self.report_display.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
    
    def add_camp(self):
        try:
            capacity = int(self.camp_capacity.get())
            camp_id = self.system.add_camp(capacity)
            messagebox.showinfo("Success", f"Camp {camp_id} added with capacity {capacity}")
            self.camp_capacity.delete(0, tk.END)
            self.refresh_camp_display()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid capacity")
    
    def register_victim(self):
        name = self.victim_name.get()
        place = self.victim_place.get()
        health = self.victim_health.get()
        
        if not name or not place or not health:
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        result = self.system.register_victim(name, place, health)
        messagebox.showinfo("Result", result)
        self.victim_name.delete(0, tk.END)
        self.victim_place.delete(0, tk.END)
        self.refresh_victim_display()
    
    def add_supplies(self):
        try:
            medicine = int(self.add_medicine.get()) if self.add_medicine.get() else 0
            food = int(self.add_food.get()) if self.add_food.get() else 0
            result = self.system.add_supplies(medicine, food)
            messagebox.showinfo("Success", result)
            self.add_medicine.delete(0, tk.END)
            self.add_food.delete(0, tk.END)
            self.refresh_supplies_display()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def distribute_supplies(self):
        try:
            camp_id = int(self.dist_camp_id.get())
            medicine = int(self.dist_medicine.get())
            food = int(self.dist_food.get())
            result = self.system.distribute_supplies(camp_id, medicine, food)
            messagebox.showinfo("Result", result)
            self.dist_camp_id.delete(0, tk.END)
            self.dist_medicine.delete(0, tk.END)
            self.dist_food.delete(0, tk.END)
            self.refresh_supplies_display()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values")
    
    def refresh_camp_display(self):
        self.camp_display.delete(1.0, tk.END)
        for camp_id, camp_data in self.system.camps.items():
            self.camp_display.insert(tk.END, f"Camp {camp_id}: {camp_data['current_occupancy']}/{camp_data['capacity']}\n")
    
    def refresh_victim_display(self):
        self.victim_display.delete(1.0, tk.END)
        for victim_id, victim_data in self.system.victims.items():
            self.victim_display.insert(tk.END, f"ID: {victim_id}, Name: {victim_data['name']}, Place: {victim_data['place']}, Camp: {victim_data['camp_id']}, Health: {victim_data['health_status']}\n")
    
    def refresh_supplies_display(self):
        self.supplies_display.delete(1.0, tk.END)
        self.supplies_display.insert(tk.END, f"Medicine Available: {self.system.supplies['medicine']}\nFood Available: {self.system.supplies['food']}\n")
    
    def generate_report(self):
        if not self.system.camps:
            messagebox.showwarning("Warning", "No camps added yet")
            return
        self.report_display.delete(1.0, tk.END)
        self.report_display.insert(tk.END, self.system.generate_report())


if __name__ == "__main__":
    root = tk.Tk()
    system = DisasterManagementSystem()
    gui = DisasterManagementGUI(root, system)
    root.mainloop()