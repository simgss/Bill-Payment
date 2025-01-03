import os
from dotenv import load_dotenv

load_dotenv()

class ConfigManager:
    def __init__(self):
        load_dotenv(dotenv_path='conf/.env')
        # URL Configuration
        self.url = os.getenv('URL')

        # Account Configuration
        self.username1 = os.getenv('USERNAME1')
        self.password = os.getenv('PASSWORD')
        accounts = os.getenv('ACCOUNTS', '')
        self.accounts = [account.strip() for account in accounts.split(',')] if accounts else []
        # print(f"Username: {self.username1}")
        
        

config_manager = ConfigManager()
# print(config_manager.url)
