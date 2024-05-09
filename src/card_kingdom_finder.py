from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cardkingdom_finder(input_cards):
    output_file = "../data/card_data/cardkingdom.txt"

    driver = webdriver.Chrome()

    driver.get("https://www.cardkingdom.com/builder")

    search_box = driver.find_element(By.NAME, "cardData")

    with open(input_cards, 'r') as file:
        desired_cards = file.read()

    search_box.send_keys(desired_cards)

    submit_button = driver.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

    wait = WebDriverWait(driver, 10)  # Set explicit wait timeout
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.flex-fill")))

    prices = driver.find_elements(By.CSS_SELECTOR, "p.flex-fill")


    order_quantity = prices[0].text
    order_price = prices[1].text

    # print(order_quantity)
    # print(order_price)

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
        # print(f"{name} {price}")

        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(f"{name} {price}\n")
    print("Submitted to Card Kingdom")

    driver.quit()
