import requests

repository_url = input("Enter GitHub repository URL: ")

# splits the URL to get owner and repository name
part = repository_url.strip().split("/")
owner = part[-2]
repository = part[-1]

# calls GitHub API to get languages
url = f"https://api.github.com/repos/{owner}/{repository}/languages"
res = requests.get(url)

#Checks if API request worked, it it did not, it stops the program
if res.status_code != 200:
    print("Invalid repo")
    exit()

# converts the API response into a Python dictionary
languages = res.json()

#if any languages are founded, it prints them
if languages:
    print("\nRepo:", repository)
    print("Languages found:")
    for lang, bytes_used in languages.items():
        print(f"- {lang}")
else:
    print("Not found! Was not able to fetch data")
