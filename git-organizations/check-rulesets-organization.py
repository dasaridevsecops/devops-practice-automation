import os
import requests

github_token = "xxxxxxxxxx"

organization = "dasaridevsecops"

url = f"https://api.github.com/orgs/{organization}/rulesets"

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
        print("No organization rulesets found.")

    for ruleset in rulesets:
        print("\n-----------------------------")
        print("ID:", ruleset.get("id"))
        print("Name:", ruleset.get("name"))
        print("Enforcement:", ruleset.get("enforcement"))
        print("Target:", ruleset.get("target"))

else:
    print(response.text)