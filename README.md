# AI Article Summarizer

The **AI Article Summarizer** is a Python program designed to scrape news articles from provided URLs, extracting relevant content, and saving it to individual text files.  Next, it takes those text files and puts them into Google Gemini API to summarize them, for a more bite size read. This README.md file provides comprehensive instructions on how to set up the environment, run the program, and understand the output.

## Table of Contents

- [Setup](#setup)
  - [Clone the Repository](#1-clone-the-repository)
  - [Create Conda Environment](#2-create-conda-environment)
  - [Get Google Gemini API Key](#3-get-google-gemini-api-key)
  - [Test Gemini API](#4-test-gemini-api)
- [Usage](#usage)
  - [Run the Program](#1-run-the-program)
  - [Format for Searching Cards](#2-format-for-searching-cards)
- [Output](#output)
- [Additional Information](#additional-information)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/GoldenCoqui/mtg_card_wizard.git
```

### 2. Create Conda Environment

```bash
conda env create -f env.yml
conda activate ai-summary
```

### 3. Get Google Gemini API Key
Go to https://ai.google.dev/ to generate your own API key. You will need a google account. `REMEMBER TO KEEP YOUR KEY SECURE`. Put your api key in a .env and set up the .env with the format below. You can leave your .env outside of the src and Data file.

```bash
API_KEY="Your-Actual-API-Key-Goes-Here"
```
### 4. Test Gemini API
Once you have your API key, try this code to see if the Gemini API will give you a response back.  The response should show up in the terminal.

```bash
import google.generativeai as genai
from dotenv import load_dotenv
import os

# loads .env that should hold API key KEEP PRIVATE
load_dotenv()

# configures your session with API key
genai.configure(api_key=os.getenv("API_KEY"))

# selects the gemini-pro model to send prompts to
model = genai.GenerativeModel('gemini-pro')

# sending prompts and saving them in a variable
response = model.generate_content("What country is Tokyo in?")

# prints Gemini response in the terminal
print(response.text)
```

# Usage

### 1. Run the Program

```bash
python run.py
```

### 2. Format for Searching Cards
When you have the GUI running, the text box to insert the cards you want to search for will be on the bottom.  The format for inserting the cards you want is VERY important.  The format should start with the quantity of the card you want and the cards name.  Make sure the spelling for the card name is exactly correct.

For Example
``` bash
1 Sol Ring
1 Arcane Signet
1 Zaxara, the Exemplary
1 Black Lotus
1 Kibo, Uktabi Prince
1 Asmoranomardicadaistinaculdacar 
```

Once you have the cards you want in the text box hit submit and program will run.

### Output

The program will start taking the inputs and searching them on Card Kingdom and TCG player using their deck-list search feature.  The results will then be taken by the program and put into text files (you can see data used in the data folder).  When all the data is collected from the websites they will be then sent to Google Gemini LLM API and the LLM will see which cards are unavaliable and will give a recommendation on what is the best deal for the user.

# Additional Information

   - The program uses the Selenium library for web automation.
   - The program uses Google Gemini API for summarizing the data and giving advice.
   - The program uses Python-dotenv to find the .env file to keep API key secure from version control
   - Ensure you have an active internet connection for the program to fetch the articles.

If you encounter any issues or have questions, feel free to open an issue on this repository.
