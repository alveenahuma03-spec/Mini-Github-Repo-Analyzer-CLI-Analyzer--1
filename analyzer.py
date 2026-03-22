import requests

repo_url = input("Enter GitHub repo URL: ")

# extract owner/repo
parts = repo_url.strip().split("/")
owner = parts[-2]
repo = parts[-1]

# GitHub API
url = f"https://api.github.com/repos/{owner}/{repo}/languages"
res = requests.get(url)

if res.status_code != 200:
    print("Invalid repo")
    exit()

languages = res.json()

print("\nRepo:", repo)
print("Languages used:")
for lang, bytes_used in languages.items():
    print(f"- {lang}")