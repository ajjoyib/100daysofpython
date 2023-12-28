import requests
from bs4 import BeautifulSoup

def get_movie_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        website_html = response.text

        soup = BeautifulSoup(website_html, "html.parser")

        all_movies = soup.find_all(name="h3", class_="title")
        movie_titles = [movie.getText() if movie else None for movie in all_movies]
        movies = movie_titles[::-1]

        with open("D45 - Web Scraping with Beautiful Soup/movies.txt", mode="w", encoding="utf-8") as file:
            for movie in movies:
                file.write(f"{movie}\n")

        print("Scraping successful. Data saved to 'movies.txt'.")
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
    get_movie_titles(URL)