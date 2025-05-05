import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def api_call():
    print(f'making api call with {api_key}')



if __name__ == "__main__":
    api_call()






# pip install python-dotenv 


# MY_ENV_VAR="This is my env var content."