from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

output_file = "../data/card_data/cardkingdom.txt"


driver = webdriver.Chrome()

# driver.implicitly_wait(10)

driver.get("https://www.cardkingdom.com/builder")

search_box = driver.find_element(By.NAME, "cardData")

# driver.implicitly_wait(20)  # Wait for up to 10 seconds for elements

search_box.send_keys("1 Arcane Signet \n1 Sol Ring \n1 Black Lotus")

submit_button = driver.find_element(By.CLASS_NAME, "btn")
submit_button.click()

# search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)  # Set explicit wait timeout
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.flex-fill")))

# price_element = driver.find_elements(By.CSS_SELECTOR, "p.flex-fill")
# price_value = price_element.text


# print(f"The Total is {price_value}")

prices = driver.find_elements(By.CSS_SELECTOR, "p.flex-fill")


order_quantity = prices[0].text
order_price = prices[1].text

print(order_quantity)
print(order_price)

with open(output_file, 'w', encoding="utf-8") as file:
    file.write(f"{order_quantity}\n")
    file.write(f"{order_price}\n")

cards_name = driver.find_elements(By.CSS_SELECTOR, "h3.title")
cards_price = driver.find_elements(By.CSS_SELECTOR, "span.card-total-price")

# Loop through elements from cards_name and cards_price together using zip
for card_name, card_price in zip(cards_name, cards_price):

    # Extract the text content from the current card name element
    name = card_name.text

    # Extract the text content from the current card price element
    price = card_price.text

    # Remove any leading or trailing whitespace from the extracted name
    # This ensures cleaner output (optional but recommended for aesthetics)
    name = name.strip()

    # Print the formatted output with card name, a space, and then the price
    print(f"{name} {price}")
    


# for price_element in prices:
#     # Extract the text content of EACH element in the list (assuming price is within the text)
#     price_value = price_element.text  # Access the .text attribute of the current element in the loop

#     print(f"Price: {price_value}")

# Wait for results to load (consider explicit waits for specific elements)
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-result")))  # Replace with selector for a result element

# # Find all results (you might need to adjust the selector)
# results = driver.find_elements(By.CSS_SELECTOR, ".card-result")

# # Loop through each result and extract data
# for result in results:
#     card_name = result.find_element(By.CSS_selector, ".card-title").text  # Extract card name (replace with selector)
#     card_price = result.find_element(By.CSS_selector, ".card-price").text  # Extract card price (replace with selector)
#     # Extract other relevant data using appropriate selectors

#     print(f"Card Name: {card_name}, Price: {card_price}")  # Print extracted data

driver.quit()
