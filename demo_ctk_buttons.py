"""
Demo script showcasing CustomTkinter CTkButton styling with magenta colors
"""

import customtkinter as ctk
from tkinter import messagebox
import webbrowser

# Set appearance mode and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MagentaButtonDemo(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("Magenta CTkButton Demo")
        self.geometry("600x500")
        self.minsize(500, 400)
        
        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1)
        
        # Header
        self.header_label = ctk.CTkLabel(
            self.main_frame,
            text="🎨 Magenta CTkButton Demo",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.header_label.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="ew")
        
        # Subheader
        self.subheader_label = ctk.CTkLabel(
            self.main_frame,
            text="Showcasing CustomTkinter buttons with magenta color scheme",
            font=ctk.CTkFont(size=12)
        )
        self.subheader_label.grid(row=1, column=0, columnspan=3, padx=20, pady=(0, 20), sticky="ew")
        
        # Create buttons with different magenta styles in a 3-column grid
        self.create_buttons()
        
        # Footer
        self.footer_label = ctk.CTkLabel(
            self.main_frame,
            text="CustomTkinter with Magenta Styling",
            font=ctk.CTkFont(size=10)
        )
        self.footer_label.grid(row=4, column=0, columnspan=3, padx=20, pady=20, sticky="ew")
        
        # Exit button
        self.exit_button = ctk.CTkButton(
            self.main_frame,
            text="Exit Demo",
            command=self.destroy,
            fg_color="#FF00FF",
            hover_color="#CC00CC",
            border_width=2,
            border_color="#FF66FF"
        )
        self.exit_button.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
    
    def create_buttons(self):
        # Button 1: Standard magenta
        self.button1 = ctk.CTkButton(
            self.main_frame,
            text="Standard Magenta",
            command=lambda: self.show_message("Standard Magenta Button Clicked!"),
            fg_color="#FF00FF",  # Magenta
            hover_color="#CC00CC",  # Darker magenta
            width=150,
            height=40
        )
        self.button1.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        # Button 2: Magenta with border
        self.button2 = ctk.CTkButton(
            self.main_frame,
            text="Magenta with Border",
            command=lambda: self.show_message("Magenta with Border Button Clicked!"),
            fg_color="#FF00FF",
            hover_color="#CC00CC",
            border_width=3,
            border_color="#FF66FF",  # Lighter magenta border
            width=150,
            height=40
        )
        self.button2.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        # Button 3: Rounded magenta
        self.button3 = ctk.CTkButton(
            self.main_frame,
            text="Rounded Magenta",
            command=lambda: self.show_message("Rounded Magenta Button Clicked!"),
            fg_color="#FF00FF",
            hover_color="#CC00CC",
            corner_radius=25,  # More rounded corners
            width=150,
            height=40
        )
        self.button3.grid(row=2, column=2, padx=10, pady=10, sticky="ew")
        
        # Button 4: Light magenta
        self.button4 = ctk.CTkButton(
            self.main_frame,
            text="Light Magenta",
            command=lambda: self.show_message("Light Magenta Button Clicked!"),
            fg_color="#FF66FF",  # Lighter magenta
            hover_color="#CC33CC",  # Slightly darker on hover
            width=150,
            height=40
        )
        self.button4.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        
        # Button 5: Dark magenta
        self.button5 = ctk.CTkButton(
            self.main_frame,
            text="Dark Magenta",
            command=lambda: self.show_message("Dark Magenta Button Clicked!"),
            fg_color="#CC00CC",  # Darker magenta
            hover_color="#990099",  # Even darker on hover
            width=150,
            height=40
        )
        self.button5.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        # Button 6: Gradient effect (simulated)
        self.button6 = ctk.CTkButton(
            self.main_frame,
            text="Gradient Effect",
            command=lambda: self.show_message("Gradient Effect Button Clicked!"),
            fg_color="#FF33FF",  # Medium magenta
            hover_color="#CC00CC",  # Darker on hover
            border_width=2,
            border_color="#FF99FF",  # Light border for gradient effect
            width=150,
            height=40
        )
        self.button6.grid(row=3, column=2, padx=10, pady=10, sticky="ew")
    
    def show_message(self, message):
        """Show a message box with the given message"""
        messagebox.showinfo("Button Clicked", message)

def main():
    app = MagentaButtonDemo()
    app.mainloop()

if __name__ == "__main__":
    main()