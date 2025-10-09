import customtkinter as ctk
from tkinter import messagebox
import webbrowser
import sys
import os

# Set the appearance mode and color theme
ctk.set_appearance_mode("Dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

class PWDToolsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("PWD Tools Hub - CustomTkinter Edition")
        self.geometry("900x700")
        self.minsize(800, 600)

        # Configure grid layout (3x4)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Create header
        self.create_header()

        # Create tool buttons
        self.create_tool_buttons()

        # Create footer
        self.create_footer()

    def create_header(self):
        # Header frame
        self.header_frame = ctk.CTkFrame(self, corner_radius=10)
        self.header_frame.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")
        self.header_frame.grid_columnconfigure(0, weight=1)

        # Header title
        self.header_label = ctk.CTkLabel(
            self.header_frame,
            text="🏗️ PWD Tools Hub",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.header_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Header subtitle
        self.subtitle_label = ctk.CTkLabel(
            self.header_frame,
            text="Infrastructure Management Suite - CustomTkinter Edition",
            font=ctk.CTkFont(size=14)
        )
        self.subtitle_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

    def open_tool(self, tool_name, tool_type="internal", url=None, page=None):
        """Handle tool button clicks"""
        if tool_type == "internal":
            messagebox.showinfo("Tool Opening", f"Opening {tool_name}...\n\nThis would open the {tool_name} tool in the Streamlit app.")
        else:
            if url:
                webbrowser.open(url)
                messagebox.showinfo("External Tool", f"Opening {tool_name} in your browser...")
            else:
                messagebox.showwarning("Error", f"URL not available for {tool_name}")

    def create_tool_buttons(self):
        # Tool definitions
        tools = [
            {
                "name": "Excel se EMD",
                "description": "Excel to EMD Refund Generator",
                "icon": "📊",
                "category": "financial",
                "status": "internal",
                "page": "pages/01_Excel_se_EMD.py"
            },
            {
                "name": "Bill & Deviation",
                "description": "Infrastructure Billing System with deviation tracking",
                "icon": "💰",
                "category": "financial", 
                "status": "external",
                "url": "https://raj-bill-generator-v01.streamlit.app/"
            },
            {
                "name": "Tender Processing",
                "description": "Comprehensive tender management system",
                "icon": "📋",
                "category": "processing",
                "status": "external", 
                "url": "https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/"
            },
            {
                "name": "Bill Note Sheet",
                "description": "Generate Bill Note Sheets",
                "icon": "📝",
                "category": "financial",
                "status": "internal",
                "page": "pages/04_Bill_Note_Sheet.py"
            },
            {
                "name": "Deductions Table",
                "description": "Manage Deductions in Contracts",
                "icon": "➖",
                "category": "financial",
                "status": "internal",
                "page": "pages/05_Deductions_Table.py"
            },
            {
                "name": "EMD Refund",
                "description": "EMD Refund Calculator and Tracker",
                "icon": "💸",
                "category": "financial",
                "status": "internal",
                "page": "pages/07_EMD_Refund.py"
            },
            {
                "name": "Financial Progress",
                "description": "Track Financial Progress of Projects",
                "icon": "📈",
                "category": "monitoring",
                "status": "internal",
                "page": "pages/08_Financial_Progress.py"
            },
            {
                "name": "Security Refund",
                "description": "Security Deposit Refund Calculator",
                "icon": "🔒",
                "category": "financial",
                "status": "internal",
                "page": "pages/09_Security_Refund.py"
            },
            {
                "name": "Stamp Duty",
                "description": "Calculate Stamp Duty for Documents",
                "icon": "⚖️",
                "category": "calculations",
                "status": "internal",
                "page": "pages/10_Stamp_Duty.py"
            }
        ]

        # Create buttons in a 3-column grid
        self.tool_buttons = []
        for i, tool in enumerate(tools):
            row = (i // 3) + 1  # Start from row 1 (after header)
            col = i % 3

            # Create button with magenta color scheme
            button = ctk.CTkButton(
                self,
                text=f"{tool['icon']}\n{tool['name']}\n{tool['description']}",
                font=ctk.CTkFont(size=12),
                width=200,
                height=120,
                corner_radius=15,
                fg_color="#FF00FF",  # Magenta
                hover_color="#CC00CC",  # Darker magenta on hover
                border_width=2,
                border_color="#FF66FF",  # Lighter magenta border
                command=lambda t=tool: self.open_tool(
                    t["name"], 
                    t["status"], 
                    t.get("url"), 
                    t.get("page")
                )
            )
            
            button.grid(row=row, column=col, padx=15, pady=10, sticky="nsew")
            self.tool_buttons.append(button)

    def create_footer(self):
        # Footer frame
        self.footer_frame = ctk.CTkFrame(self, corner_radius=10)
        self.footer_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=20, sticky="ew")
        self.footer_frame.grid_columnconfigure(0, weight=1)

        # Footer text
        self.footer_label = ctk.CTkLabel(
            self.footer_frame,
            text="© 2023 PWD Tools Hub | Infrastructure Management Suite\nBuilt with CustomTkinter | Designed for Lower Divisional Clerks",
            font=ctk.CTkFont(size=10),
            anchor="center"
        )
        self.footer_label.grid(row=0, column=0, padx=20, pady=15, sticky="ew")

        # Exit button with magenta styling
        self.exit_button = ctk.CTkButton(
            self.footer_frame,
            text="Exit Application",
            font=ctk.CTkFont(size=12, weight="bold"),
            width=150,
            height=35,
            corner_radius=10,
            fg_color="#FF00FF",  # Magenta
            hover_color="#CC00CC",  # Darker magenta on hover
            border_width=2,
            border_color="#FF66FF",  # Lighter magenta border
            command=self.quit
        )
        self.exit_button.grid(row=0, column=1, padx=20, pady=15, sticky="e")

    def quit(self):
        """Exit the application"""
        if messagebox.askyesno("Exit", "Are you sure you want to exit the PWD Tools Hub?"):
            self.destroy()
            sys.exit()

def main():
    app = PWDToolsApp()
    app.mainloop()

if __name__ == "__main__":
    main()