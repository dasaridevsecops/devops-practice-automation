import os
import requests

# ============================================================
# Configuration
# ============================================================

#github_token = os.environ["GITHUB_TOKEN"]
github_token = "xxxxxxxxxx"
organization_name = "dasaridevsecops"
repo_name = "devops-practice-terraform"
branch_name = "main"

# ============================================================
# GitHub API
# ============================================================

url = (
    f"https://api.github.com/repos/"
    f"{organization_name}/{repo_name}/branches/"
    f"{branch_name}/protection"
)

headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# ============================================================
# Delete branch protection
# ============================================================

response = requests.delete(
    url,
    headers=headers
)

if response.status_code == 204:

    print(
        f"Branch protection deleted successfully for "
        f"{organization_name}/{repo_name}:{branch_name}"
    )

elif response.status_code == 404:

    print(
        f"No branch protection rule found for "
        f"{organization_name}/{repo_name}:{branch_name}"
    )

else:

    print(
        f"Failed to delete branch protection."
    )

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")