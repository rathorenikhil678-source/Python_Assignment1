import requests
#give the data of random person

url = "https://randomuser.me/api/"

response = requests.get(url)

data = response.json()

user = data["results"][0]

print("Name:",
      user["name"]["first"],
      user["name"]["last"])

print("Email:",
      user["email"])

print("Country:",
      user["location"]["country"])

print("Phone:",
      user["phone"])
