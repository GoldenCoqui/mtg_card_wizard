import tkinter as tk

# Function to handle button click event

def on_submit(output, input):
    # Do something with the user input, for example, print it
    # Do something with the user input, for example, print it
    
    user_input = input.get("1.0", "end-1c")  # Retrieve all text from the widget


    with open(output, 'w') as file:
        file.write(user_input)

    print(f"User input: {user_input}")
    



def main():
    user_data = "test2.txt"

    # Create the main application window
    app = tk.Tk()
    app.title("MTG Card Wizard")

    # Create a label widget
    label = tk.Label(app, text="Enter your input:")
    label.pack()

    # Create a text widget for multi-line input
    text = tk.Text(app, width=50, height=10)  # Adjust width and height as needed
    text.pack()


    # Create a button widget
    button = tk.Button(app, text="Submit", command=lambda: on_submit(user_data, text))
    button.pack()



    # Run the application
    app.mainloop()

if __name__ == "__main__":
    main()