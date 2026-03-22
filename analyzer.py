import requests

repository_url = input("Enter GitHub repository URL: ")

# extract owner/repo
part = repository_url.strip().split("/")
owner = part[-2]
repository = part[-1]

# GitHub API
url = f"https://api.github.com/repos/{owner}/{repository}/languages"
res = requests.get(url)

if res.status_code != 200:
    print("Invalid repo")
    exit()

languages = res.json()

if languages:
    print("\nRepo:", repository)
    print("Languages found:")
    for lang, bytes_used in languages.items():
        print(f"- {lang}")
else:
    print("Not found! Was not able to fetch data")
