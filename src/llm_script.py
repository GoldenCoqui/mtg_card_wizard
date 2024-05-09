
import os
import google.generativeai as genai
from dotenv import load_dotenv
import textwrap

# loads .env that will hold API key KEEP PRIVATE
load_dotenv()

# API key configuration
genai.configure(api_key=os.getenv("API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

def llm_compare(cardkingdom_output, tcg_player_output):
  try:
    genai.configure(api_key=os.getenv("API_KEY"))

    # selects the gemini-pro model to send prompts to
    model = genai.GenerativeModel('gemini-pro')

    # enables chat feature to remeber past prompts
    chat = model.start_chat(history=[])


    chat.send_message(
      f" Remeber this list, this is a list of cards with their respective price, this list is called card kingdom\n\n {cardkingdom_output}"
      )

    chat.send_message(
      f"Remeber this list, this is a list of cards with their respective price, this list is called tcg player\n\n {tcg_player_output}"
    )

    response = chat.send_message(
      "find cards from card kingdom with a price of $0.00 (it must be EXACTLY zero, if it is $0.01 and above it is avaliable) and say that they are unavaliable and from what list"
    )



    with open("../data/llm_output/llm-compare.txt", 'w', encoding='utf-8') as file:
      file.write(f"{response.text}\n\n")
  
    response = chat.send_message(
      "find cards from tcg player with a price of $0.00 (it must be EXACTLY zero, if it is $0.01 and above it is avaliable) and say that they are unavaliable and from what list"
    )

    with open("../data/llm_output/llm-compare.txt", 'a', encoding='utf-8') as file:
      file.write(f"{response.text}\n\n")

    response = chat.send_message(
      "Using the given information what would you suggest as getting the best deal"
    )

    with open("../data/llm_output/llm-compare.txt", 'a', encoding='utf-8') as file:
      file.write(f"{response.text}\n\n")

    
  except Exception as e:
    print(f"Error Summarizing: {str(e)}")