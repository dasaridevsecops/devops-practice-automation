import requests
import json

github_token = "xxxxxxxxxx"

#$env:GITHUB_TOKEN="xxxxxxxxxx"

# Multiple GitHub organizations
organizations = [
    "dasaridevsecops"
]

# Repository configuration
repo_name = "devops-practice-terraform"
description = "This repo is to discuss about python usecases"

# Branch to protect
branch_name = "main"

BASE_URL = "https://api.github.com"

headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def create_repository(organization_name):

    url = f"{BASE_URL}/orgs/{organization_name}/repos"

    payload = {
        "name": repo_name,
        "description": description,
        "private": False
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    if response.status_code == 201:

        print(
            f"Repository '{repo_name}' created successfully "
            f"in organization '{organization_name}'."
        )

        return True

    elif response.status_code == 422:

        print(
            f"Repository '{repo_name}' already exists "
            f"in organization '{organization_name}'."
        )

        return True

    else:

        print(
            f"Failed to create repository in "
            f"'{organization_name}'."
        )

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        return False

def check_branch(organization_name):

    url = (
        f"{BASE_URL}/repos/"
        f"{organization_name}/{repo_name}/branches/{branch_name}"
    )

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code == 200:

        print(
            f"Branch '{branch_name}' exists in "
            f"{organization_name}/{repo_name}"
        )

        return True

    else:

        print(
            f"Branch '{branch_name}' does not exist in "
            f"{organization_name}/{repo_name}"
        )

        print(f"Response: {response.text}")

        return False

def protect_branch(organization_name):

    url = (
        f"{BASE_URL}/repos/"
        f"{organization_name}/{repo_name}/branches/"
        f"{branch_name}/protection"
    )

    payload = {

        # ----------------------------------------------------
        # Require pull request before merging
        # ----------------------------------------------------

        "required_pull_request_reviews": {

            "dismissal_restrictions": {},

            "dismiss_stale_reviews": True,

            "require_code_owner_reviews": True,

            "required_approving_review_count": 2,

            "require_last_push_approval": True
        },

        # ----------------------------------------------------
        # Require status checks
        # ----------------------------------------------------

        "required_status_checks": {

            "strict": True,

            "contexts": [
                "build",
                "test",
                "security-scan"
            ]
        },

        # ----------------------------------------------------
        # Enforce branch protection for administrators
        # ----------------------------------------------------

        "enforce_admins": True,

        # ----------------------------------------------------
        # Restrict who can push
        # ----------------------------------------------------

        "restrictions": None,

        # ----------------------------------------------------
        # Prevent force pushes
        # ----------------------------------------------------

        "allow_force_pushes": False,

        # ----------------------------------------------------
        # Prevent branch deletion
        # ----------------------------------------------------

        "allow_deletions": False,

        # ----------------------------------------------------
        # Require conversation resolution
        # ----------------------------------------------------

        "required_conversation_resolution": True
    }

    response = requests.put(
        url,
        headers=headers,
        json=payload
    )

    if response.status_code == 200:

        print(
            f"Branch protection successfully configured for "
            f"{organization_name}/{repo_name}:{branch_name}"
        )

        return True

    else:

        print(
            f"Failed to configure branch protection for "
            f"{organization_name}/{repo_name}"
        )

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        return False

for organization_name in organizations:

    print("\n" + "=" * 70)

    print(
        f"Processing organization: {organization_name}"
    )

    print("=" * 70)

    # Step 1: Create repository
    repo_created = create_repository(
        organization_name
    )

    if not repo_created:
        continue

    # Step 2: Check branch
    branch_exists = check_branch(
        organization_name
    )

    if not branch_exists:

        print(
            f"Skipping branch protection because "
            f"'{branch_name}' does not exist."
        )

        continue

    # Step 3: Apply branch protection
    protect_branch(
        organization_name
    )


print("\nProcessing completed.")