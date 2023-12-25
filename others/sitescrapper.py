import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the data you want from the website
        data_elements = soup.find_all("div", class_="main_text")

        # Save data to a file
        with open("./others/scrapped_data.txt", "w", encoding="utf-8") as file:
            for element in data_elements:
                file.write(str(element) + "\n")

        print("Scrapping successful. Data saved to 'scrapped_data.txt'.")
    else:
        print(f"Error: Unable to fetch the website. Status code: {response.status_code}")


if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the website you want to scrape
    target_url = "https://news.sbs.co.kr/news/endPage.do?news_id=N1007473557&plink=NEWLIST&cooper=SBSNEWSSPECIAL"
    scrape_website(target_url)