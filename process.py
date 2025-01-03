from playwright.sync_api import sync_playwright
from config import ConfigManager

def search_acc(page):
# Search for the account
    try:
        # Locate the link with the specific text "Select Account"
        select_account_link = page.locator("a[href='javascript:void(0)']:has-text('Select Account')").nth(0)  # Apply nth(0) as a method
        
        # Click the first matching element
        select_account_link.click()
        print("Successfully clicked the first 'Select Account' link.")
    except Exception as e:
        print(f"An error occurred while clicking 'Select Account': {e}")

def select_acc(page, account_number):
# Select the account
    try:
        # Locate the account number input field
        account_number_input = page.locator("input[name='accountNumber']")
        
        # Fill in the account number
        account_number_input.fill(ConfigManager.get_account_number())
        
        # Locate the "Search" button
        search_button = page.locator("button:has-text('Search')").nth(0)
        
        # Click the first matching element
        search_button.click()
        print("Successfully filled in the account number and clicked the 'Search' button.")
    except Exception as e:
        print(f"An error occurred while filling in the account number and clicking 'Search': {e}")


