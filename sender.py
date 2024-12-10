from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()

print(os.environ.get('SLACK_ID'))

import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'Hello, slack!',
}

response = requests.post(
    f'https://hooks.slack.com/services/T083FAUM283/B0844A39740/{os.environ.get("SLACK_ID")}',
    headers=headers,
    json=json_data
)


print(response)
