from bs4 import BeautifulSoup
import requests

def top_music():
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        website_html = response.text

        soup = BeautifulSoup(website_html, "html.parser")

        song_names_span = soup.select(selector="li ul li h3")
        song_names = [song.getText().strip() if song else None for song in song_names_span]

        output_file_path = f"D46 - Creating a Spotify Playlist/songs{date.strip()}.txt"
        with open(output_file_path, "w") as file:
            a = 1
            for song in song_names:
                file.write(f"{a}.{song}\n")
                a += 1

    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    top_music()