from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def tcg_player_finder(input_cards):
    output_file = "../data/card_data/tcgplayer.txt"

    driver = webdriver.Chrome()

    driver.get("https://www.tcgplayer.com/massentry?productline=Magic")

    wait = WebDriverWait(driver, 10)  # Set explicit wait timeout
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.mass-entry-input.no-border")))


    search_box = driver.find_element(By.CSS_SELECTOR, "section.mass-entry-input.no-border")

    with open(input_cards, 'r') as file:
        desired_cards = file.read()

    search_box.send_keys(desired_cards)

    submit_button = driver.find_element(By.CLASS_NAME, "mass-entry__body__actions--submit")
    submit_button.click()

    wait = WebDriverWait(driver, 10)  # Set explicit wait timeout
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.items-breakdown")))

    info_breakdown = driver.find_elements(By.CSS_SELECTOR, "p")


    pacakges = info_breakdown[0].text
    items = info_breakdown[1].text
    item_total = info_breakdown[2].text
    shipping = info_breakdown[3].text


    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(f"{pacakges}\n")
        file.write(f"{items}\n")
        file.write(f"{item_total}\n")
        file.write(f"{shipping}\n\n")


    cards_name = driver.find_elements(By.CSS_SELECTOR, "p.name")
    cards_price = driver.find_elements(By.CSS_SELECTOR, "p.price")

    # # Loop through elements from cards_name and cards_price together using zip
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
    # print("Submitted to Card Kingdom")

    driver.quit()
