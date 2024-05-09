from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of cardkingdom.com
url = 'https://www.cardkingdom.com/builder'

# User input
user_input = "1 Arcane Signet"

# Define the form data (as per the website's structure)
form_data = {
    'decklist-form': user_input,
}

# Launch a Chrome browser
driver = webdriver.Chrome()

# Navigate to the website
driver.get(url)

# Find the textarea for decklist-form and input the user input
input_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'decklist-form')))
input_box.clear()
input_box.send_keys(user_input)

# Wait for the search results to load (if any)
# You may need to adjust the waiting time based on the website's loading speed
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'search-results-header')))

# Capture the HTML content after the form submission
html_content = driver.page_source

# Close the browser
driver.quit()

# Save the HTML content to a text document
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML content saved to output.html")
