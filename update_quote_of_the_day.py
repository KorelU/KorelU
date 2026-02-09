import requests

API_URL = "https://zenquotes.io/api/today/"
README_FILE = "README.md"
QUOTE_START = "<!--QOUTE_START-->"
QUOTE_END = "<!--QUOTE_END-->"

# Fetch the Quote and the Author
def fetch_quote():
    # Make the GET request ot the quotable API
    response = requests.get(API_URL)    
    # Convert the response into a list with one Python dictionary inside
    data = response.json()    
    # Get the content of the list, dicitonary          
    quote_text = data[0]['q']
    quote_author = data[0]['a']
    # Return the Quote and author formatted string
    return f"{quote_text} - {quote_author}"

def update_readme():
    # Open the README file in read mode
    with open(README_FILE, "r", encoding="utf-8") as f:
        # Read the entire file into content
        content = f.read() 

    # Try to get the quote and author
    try:
        # Get the quote and author
        quote_and_author = fetch_quote()
    # If an exception occurs 
    except requests.RequestException:
        quote_and_author = "In a world where you can be anything, be kind. - Oliver Gray."

    # Formate the quote and author
    formated_quote_and_author = f"\n> {quote_and_author}\n"

    # Split the string content into everything before the QUOTE_START line and everythign after it
    # Get everything before it
    before = content.split(QUOTE_START)[0] 
    # Re-append the QUOTE_START 
    before = before + QUOTE_START 

    # Split the string content into everything before the QUOTE_END line and everythign after it
    # Get everything after it
    after = content.split(QUOTE_END)[1]
    # Re-append the QUOTE_END before
    after = QUOTE_END + after

    # Now that we succesfully excluded the old quote include the new quote
    updated_content = before + formated_quote_and_author + after

    # Open the README file in write mode
    with open(README_FILE, "w", encoding="utf-8") as f:
        # Rewrite to the file everything but now with the new quote
        f.write(updated_content)


    print("README updated with today's quote!")


update_readme()
