from bs4 import BeautifulSoup
import html2text
import requests
from os import path

##################################################################################################

year_number = 2022
day_number = 5

absolute_path = path.dirname(path.abspath(__file__))
session_id = ""
with open(absolute_path + '/SessionID.txt', 'r') as file:
    session_id = file.read().rstrip()

##################################################################################################
# Get and process the webpage

raw_page_data = requests.get(
    f"https://adventofcode.com/{year_number}/day/{day_number}",
    headers={
        "cookie": f"session={session_id}"
    }
).text
page_soup = BeautifulSoup(raw_page_data, "html.parser")
articles = page_soup.findAll("article")

# Get the input

raw_input = requests.get(
    f"https://adventofcode.com/{year_number}/day/{day_number}/input",
    headers={
        "cookie": f"session={session_id}"
    }
).text.removesuffix("\n", )  # Requests gives an extra new line, so I'll just manually remove it (for now)

# Save the input file

input_file = open(f"./{day_number}/input.txt", "w")
input_file.write(raw_input)

# Write the webpage to Markdown

h = html2text.HTML2Text()
h.body_width = 0

if (len(articles) == 0):
    print("No articles were found. This day has likely not been unlocked yet.")

elif (len(articles) == 1):
    article_one_file = open(f"./{day_number}/instructions-one.md", "w")
    article_one_file.write(
        h.handle(str(articles[0])).lstrip("\n").rstrip("\n")
    )

else:
    article_one_file = open(f"./{day_number}/instructions-one.md", "w")
    article_one_file.write(
        h.handle(str(articles[0])).lstrip("\n").rstrip("\n")
    )

    article_two_file = open(f"./{day_number}/instructions-two.md", "w")
    article_two_file.write(
        h.handle(str(articles[1])).lstrip("\n").rstrip("\n")
    )
