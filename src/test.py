import tkinter as tk
from card_kingdom_finder import cardkingdom_finder  # Assuming this function exists

# Function to handle button click event
def on_submit(output, input, output_label, cardkingdom_output_label):
    user_input = input.get("1.0", "end-1c")  # Retrieve all text from the widget

    # Write user input to file (optional)
    # with open(output, 'w') as file:
    #     file.write(user_input)

    print(f"User Desired Cards in {output}")
    output_label.config(text=user_input)  # Update user input label

    # Call cardkingdom_finder and update its output label
    cardkingdom_output = cardkingdom_finder(output)
    cardkingdom_output_label.config(text=cardkingdom_output)


def gui_maker(user_data):
    # Create the main application window
    app = tk.Tk()
    app.title("MTG Card Wizard")

    # Create frames for layout
    input_frame = tk.Frame(app)
    output_frame = tk.Frame(app)
    finder_frame = tk.Frame(app)
    input_frame.pack()
    output_frame.pack(fill=tk.X)  # Stretch output frame horizontally
    finder_frame.pack()

    # Create a label for user input
    label = tk.Label(input_frame, text="Enter your input:")
    label.pack()

    # Create a text widget for multi-line input
    text = tk.Text(input_frame, width=50, height=10)  # Adjust width and height as needed
    text.pack()

    # Create a button widget
    button = tk.Button(
        input_frame, text="Submit", command=lambda: on_submit(user_data, text, output_label, cardkingdom_output_label)
    )
    button.pack()

    # Labels for displaying user input, cardkingdom output, and future finder output
    output_label = tk.Label(output_frame, text="")
    output_label.pack(side=tk.LEFT)

    cardkingdom_output_label = tk.Label(output_frame, text="")
    cardkingdom_output_label.pack(side=tk.LEFT)

    future_finder_label = tk.Label(finder_frame, text="Future Finder Output")
    future_finder_label.pack()

    # Run the application
    app.mainloop()


if __name__ == "__main__":
    user_data = "test2.txt"  # Placeholder for potential file usage
    gui_maker(user_data)
