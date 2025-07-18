import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}",
}


def get_open_prs(repo_owner, repo_name):
    """Fetches open pull requests from a GitHub repository."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()
