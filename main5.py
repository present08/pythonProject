from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import time

# Set up the WebDriver (update the path to your WebDriver executable)
driver = webdriver.Chrome()

# Open the target webpage
driver.get('http://www.cgv.co.kr/movies/?lt=1&ft=0')

# Pause to allow the page to fully load
time.sleep(5)  # Adjust sleep time if necessary for the page to load completely

# Create a directory to save downloaded images
output_folder = 'cgv_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Locate all image elements on the page
try:
    # Find all image elements
    image_elements = driver.find_elements(By.TAG_NAME, 'img')

    # Iterate over each image element and download the images
    for index, image_element in enumerate(image_elements):
        # Get the URL of the image
        image_url = image_element.get_attribute('src')

        # Check if the URL is valid
        if image_url and image_url.startswith('http'):
            try:
                # Download the image
                response = requests.get(image_url, stream=True)
                response.raise_for_status()  # Check if the request was successful

                # Define the path to save the image
                image_path = os.path.join(output_folder, f'image_{index}.jpg')

                # Save the image to the specified path
                with open(image_path, 'wb') as file:
                    file.write(response.content)

                print(f"Downloaded: {image_path}")

            except requests.exceptions.RequestException as e:
                print(f"Failed to download {image_url}: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

# Close the WebDriver
driver.quit()
