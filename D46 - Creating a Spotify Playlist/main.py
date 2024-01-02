import spotipy
from spotipy.oauth2 import SpotifyOAuth
from line_reader import read_specific_line

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "http://localhost:4304/auth/spotify/callback",
        client_id = read_specific_line("keys.txt", 1),
        client_secret = read_specific_line("keys.txt", 2),
        show_dialog = True,
        cache_path = "token.txt",
        username = "316axmj7ck5xtrrrucwk264l6v44"
    )
)

user_id = sp.current_user()["id"]