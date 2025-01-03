from playwright.sync_api import sync_playwright
from config import ConfigManager
import time
import process as process

# Load credentials from configuration manager
config_manager = ConfigManager()
url = config_manager.url
username = config_manager.username1
password = config_manager.password

print(f"URL: {url} || Username: {username} || Password: {password}")

def automate_login():
    with sync_playwright() as p:
        try:
            # Launch a headless browser
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # Open the login page
            page.goto(url)

            # Wait for the username and password fields to appear
            page.wait_for_selector("input[name='userName']")
            page.wait_for_selector("input[name='password']")

            # Fill in the login form
            page.fill("input[name='userName']", username)
            page.fill("input[name='password']", password)

            # Ensure the login button is visible and click it
            page.wait_for_selector("button[type='submit']", state="visible")
            page.click("button[type='submit']")

            # Wait for the page to process the login
            page.wait_for_load_state("networkidle")

            # Print the current page title to confirm login
            print("Logged in successfully. Page title:", page.title())

            # Wait for the container div and the "Continue" button
            container_div = page.wait_for_selector("div.root-0-2-1")
            print("Container div found:", container_div)

            # Click the "Continue" button inside the div
            page.wait_for_selector("button[aria-label='Launch City of Seattle Utility Services']", state="visible")
                
            # Wait for navigation after clicking the "Continue" button
            with page.expect_navigation():
                page.click("button[aria-label='Launch City of Seattle Utility Services']")

            print("Clicked the 'Continue' button successfully.")

            # Wait for the username and password fields to appear
            page.wait_for_selector("input[name='userName']")
            page.wait_for_selector("input[name='password']")

            # Fill in the login form
            page.fill("input[name='userName']", username)
            page.fill("input[name='password']", password)

            # Ensure the login button is visible and click it
            page.wait_for_selector("button[type='submit']", state="visible")
            page.click("button[type='submit']")

            # Wait for the page to process the login
            page.wait_for_load_state("networkidle")

            # After the Oracle IDCS login process is done, we are redirected to the utility portal
            page.wait_for_load_state("load")  # Wait for the page to fully load after the navigation
            page.goto("https://myutilities.seattle.gov/eportal/#/billingoverview")

            # Wait for the page to load fully before closing
            page.wait_for_load_state("load")

            # Get the current URL after redirection to the final page
            current_url = page.url
            print("Redirected to:", current_url)

            print("Final page title:", page.title())

            # You can use page.query_selector or page.query_selector_all to extract specific elements
            element = page.query_selector("title")
            if element:
                print("Heading:", element.inner_text())

            # Perform any further actions on the final page if needed
            print("Successfully logged in and redirected to the utility portal.")

            process.search_acc(page)
            time.sleep(3)


        except Exception as e:
            print(f"An error occurred: {e}")
            # finally:
                # Close the browser
                # browser.close()

if __name__ == "__main__":
    automate_login()
