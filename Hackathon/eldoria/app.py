import requests

import re

def extract_secrets(scroll):
    # Regular expression to match the pattern {*secret*}
    pattern = r"\{\*(.*?)\*\}"
    secrets = re.findall(pattern, scroll)
    return secrets

if scroll_content:
    secrets = extract_secrets(scroll_content)
    
    if secrets:
        print("The secrets are:")
        for idx, secret in enumerate(secrets, 1):
            print(f"{idx}. {secret}")
    else:
        print("No secrets found in the scroll.")


def fetch_scroll_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve scroll. Status code: {response.status_code}")
        return None

scroll_url = "https://raw.githubusercontent.com/sombaner/copilot-hackathon-challenges/main/Data/Scrolls.txt"
scroll_content = fetch_scroll_content(scroll_url)

if scroll_content:
    print("Scroll content fetched successfully.")
else:
    print("Failed to fetch scroll content.")
