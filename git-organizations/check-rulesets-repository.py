import os
import requests

github_token = "xxxxxxxxxxxx"

organization = "dasaridevsecops"
repo = "devops-practice-terraform"

url = (
    f"https://api.github.com/repos/"
    f"{organization}/{repo}/rulesets"
)

headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = requests.get(
    url,
    headers=headers
)

print("Status:", response.status_code)

if response.status_code == 200:

    rulesets = response.json()

    if not rulesets:
        print("No repository rulesets found.")

    for ruleset in rulesets:

        print("\n-----------------------------")
        print("ID:", ruleset.get("id"))
        print("Name:", ruleset.get("name"))
        print("Status:", ruleset.get("enforcement"))
        print("Target:", ruleset.get("target"))

else:

    print(response.text)