import tkinter as tk
from card_kingdom_finder import cardkingdom_finder
from tcg_player_finder import tcg_player_finder
from llm_script import llm_compare 

# Function to handle button click event

def on_submit(output, input, output_label, cardkingdom_output_label, tcg_label, summary_label):
    # Do something with the user input, for example, print it    
    user_input = input.get("1.0", "end-1c")  # Retrieve all text from the widget


    with open(output, 'w') as file:
        file.write(user_input)
    
    output_label.config(text=f"Cards You Requested:\n\n{user_input}")  # Update user input label
    print(f"User Desired Cards in {output}")


    cardkingdom_finder(output)


    # Call cardkingdom_finder and update its output label
    with open("../data/card_data/cardkingdom.txt" , 'r') as file:
        cardkingdom_output = file.read()
    
    cardkingdom_output_label.config(text=f"Card Kingdom Results:\n\n {cardkingdom_output}")

    tcg_player_finder(output)

    # Call tcg_player_finder and update its output label
    with open("../data/card_data/tcgplayer.txt" , 'r') as file:
        tcg_output = file.read()
    
    tcg_label.config(text=f"TCG Player Results:\n\n {tcg_output}")


    # Summarize results and update summary label
    (llm_compare(cardkingdom_output, tcg_output))

    with open("../data/llm_output/llm-compare.txt", 'r') as file:
      summary_text = file.read()
      summary_label.config(text=f"Summary:\n\n{summary_text}")
    


def gui_maker(user_data):

    # Create the main application window
    app = tk.Tk()
    app.title("MTG Card Wizard")

    # Create frames for layout
    input_frame = tk.Frame(app)
    output_frame = tk.Frame(app)
    tcg_frame = tk.Frame(app)
    input_frame.pack()
    output_frame.pack(fill=tk.X)  # Stretch output frame horizontally
    tcg_frame.pack(fill=tk.X)




    # Create a label widget
    label = tk.Label(app, text="Enter your input:")
    label.pack()

    # Create a text widget for multi-line input
    text = tk.Text(app, width=50, height=10)  # Adjust width and height as needed
    text.pack()


    # Create a button widget
    button = tk.Button(
        input_frame, text="Submit", command=lambda: on_submit(user_data, text, output_label, cardkingdom_output_label, tcg_label, summary_label)
        )
    button.pack()


    # Labels for displaying user input, cardkingdom output, and future finder output
    output_label = tk.Label(output_frame, text="Cards You Requested")
    output_label.pack(side=tk.LEFT)

    cardkingdom_output_label = tk.Label(output_frame, text="Card Kingdom Results:")
    cardkingdom_output_label.pack(side=tk.LEFT)

    tcg_label = tk.Label(output_frame, text="TCG Player Results:")
    tcg_label.pack(side=tk.LEFT)

    summary_label = tk.Label(output_frame, text="Summary:")  # New label for summary
    summary_label.pack()  # Place the summary label above cardkingdom and future finder labels





    # Run the application
    app.mainloop()

