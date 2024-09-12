from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# Initialize WebDriver (Specify the correct path to your WebDriver)
driver = webdriver.Chrome()

# Open the target webpage
driver.get('https://novel.naver.com/webnovel/weekday')

# Pause briefly to allow the page to load completely
time.sleep(3)  # Adjust the time if needed

# Create a directory to save downloaded images
output_folder = 'downloaded_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Find all image elements on the page
try:
    image_elements = driver.find_elements(By.TAG_NAME, 'img')

    # Iterate over each image element and download the images
    for index, image_element in enumerate(image_elements):
        # Get the URL of the image
        image_url = image_element.get_attribute('src')

        # Only proceed if a valid URL is found
        if image_url:
            try:
                # Download the image
                response = requests.get(image_url, stream=True)
                response.raise_for_status()  # Check for request errors

                # Define the path to save the image
                image_path = os.path.join(output_folder, f'image_{index}.jpg')

                # Save the image
                with open(image_path, 'wb') as file:
                    file.write(response.content)

                print(f"Downloaded: {image_path}")

            except requests.exceptions.RequestException as e:
                print(f"Failed to download {image_url}: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

# Close the WebDriver
driver.quit()
