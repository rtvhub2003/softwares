
from bs4 import BeautifulSoup
import requests
import sys
from termcolor import colored
from time import sleep

def extract_and_display_webpage(option='default', searchTag='https://www.redbooks.ibm.com/'):
    # Send a GET request to the URL
    # response = requests.get(url)
    # response = requests.get(url, verify=False)

    # url = "https://www.myirtech.com/list.asp?id=561"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    not_connected = True
    attempt = 0

    # url = searchTag

    # for attempt in range(5):
    while not_connected:

        attempt += 1

        if "https://" in searchTag or "http://" in searchTag:
            url = searchTag
        else:
            url = f"https://search.brave.com/search?q={searchTag}&source=web"

        try:
            sleep(2)

            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            # print(response.content)
        

            # Parse the content of the response with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Replace images with "IMAGE" label
            for img in soup.find_all('img'):
                img.replace_with("[IMAGE]")

            # Extract and print text content with structure
            for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'b']):
                not_connected = False

                if option == '--link' and element.name == 'a':
                    print(colored(f"[LINK: {element.get('href')}]", 'red'),element.get_text())
                    # pass

                elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    # print(colored(f"╔{'═' * (len(element.get_text()) + 2)}╗", 'green'))
                    # print(colored(f"║ {element.get_text()} ║", 'green'))
                    # print(colored(f"╚{'═' * (len(element.get_text()) + 2)}╝", 'green'))

                    # print(colored(f"#{'#' * (len(element.get_text()) + 2)}#", 'green'))
                    # print(colored(f"# {element.get_text()} #", 'green'))
                    # print(colored(f"#{'#' * (len(element.get_text()) + 2)}#", 'green'))

                    print(colored(f"-{'-' * (len(element.get_text()) + 2)}-", color='black', on_color='on_white'))
                    print(colored(f"| {element.get_text()} |", color='black', on_color='on_white', attrs=['bold']))
                    print(colored(f"-{'-' * (len(element.get_text()) + 2)}-", color='black', on_color='on_white'))
                    print("\n")

                elif element.name == 'b':
                    boldText = element.get_text()
                    print(colored(f"{boldText}",color='yellow', attrs=['bold']))
                else:
                    print(colored(element.get_text()))
                    print()  # Add a new line after each paragraph
            break

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            # sleep(2)  # Wait for 1 second before retrying


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python script.py <URL>\n Usage: python script [option] <URL>")
    if len(sys.argv) == 3:
        option = sys.argv[1] # --link, to display url link
        url = sys.argv[2] # searchTag, searchURL
        # url = f'https://www.google.com/search?q={url}'
        extract_and_display_webpage(option, url)
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        # url = f'https://www.google.com/search?q={url}'
        extract_and_display_webpage(None, url)
    elif len(sys.argv) < 2:
        extract_and_display_webpage(None, "https://www.redbooks.ibm.com/")
    else:
        print("Usage: python script.py <URL>\n Usage: python script [--link] <URL>")