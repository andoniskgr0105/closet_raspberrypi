import tkinter as tk
from tkinter import font
from datetime import datetime
from functions import send_sms

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.attributes('-fullscreen', True)  # Start maximized
        self.configure(bg='black')
        
        
        # Define custom font sizes
        self.logo_font = font.Font(size=20, weight='bold')
        self.date_time_font = font.Font(size=20)
        self.text_field_font = font.Font(size=30)
        self.button_font = font.Font(size=14, weight='bold')
        
        # Configure grid rows and columns
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Add logo text
        self.logo_label = tk.Label(self, text="My Logo", font=self.logo_font, bg='blue', fg='white')
        self.logo_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10,ipadx=50)
        
        # Add date and time display
        self.date_time_label = tk.Label(self, text="", font=self.date_time_font, bg='black', fg='white')
        self.date_time_label.grid(row=0, column=1, sticky=tk.E, padx=10, pady=10)
        
        # Update date and time every second
        self.update_time()
        
        # Add buttons
        self.buttons_frame = tk.Frame(self, bg='green')
        self.buttons_frame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
        self.buttons_frame.grid_rowconfigure(0, weight=1)
        self.buttons_frame.grid_rowconfigure(1, weight=1)
        self.buttons_frame.grid_rowconfigure(2, weight=1)
        self.buttons_frame.grid_rowconfigure(3, weight=1)
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)
        self.buttons_frame.grid_columnconfigure(2, weight=1)
        self.buttons_frame.grid_columnconfigure(3, weight=1)
        
        self.buttons = []
        for i in range(8):
            button = tk.Button(self.buttons_frame, text=str(i+1), width=8, height=4, bg='green', fg='black',
                               font=self.button_font, command=lambda i=i: self.button_pressed(i))
            button.bind("<ButtonRelease-1>", self.button_released)
            button.bind("<ButtonPress-1>", self.button_pressed_event)
            row, col = divmod(i, 4)  # Arrange buttons in a 4x2 grid
            button.grid(row=row, column=col, padx=10, pady=10)
            self.buttons.append(button)
        
        # Add text field
        self.text_field = tk.Label(self, text="", font=self.text_field_font, bg='green', fg='white',width=25,highlightbackground='red',highlightthickness=5)
        self.text_field.grid(row=2, column=0, columnspan=2, pady=20, sticky=tk.S)
        
        # Bind the Escape key to the close method
        self.bind("<Escape>", self.close_application)

    def button_pressed(self, index):
        message_text = f"Button {index+1} pressed"
        self.text_field.config(text=message_text)
        
        # Send SMS using the SMSSender class
        send_sms(message_text)

    
    def button_released(self, event):
        button = event.widget
        button.config(bg='green')

    def button_pressed_event(self, event):
        button = event.widget
        button.config(bg='yellow')

    def update_time(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_time_label.config(text=now)
        self.after(1000, self.update_time)  # Update every second

    def close_application(self, event=None):
        self.destroy()  # Close the application
