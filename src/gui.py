import tkinter as tk

# Function to handle button click event
def on_submit():
    user_input = text.get("1.0", "end-1c")  # Retrieve all text from the widget
    # Do something with the user input, for example, print it
    print("User input:", user_input)

# Create the main application window
app = tk.Tk()
app.title("Input GUI")

# Create a label widget
label = tk.Label(app, text="Enter your input:")
label.pack()

# Create a text widget for multi-line input
text = tk.Text(app, width=50, height=10)  # Adjust width and height as needed
text.pack()

# Create a button widget
button = tk.Button(app, text="Submit", command=on_submit)
button.pack()

# Run the application
app.mainloop()
