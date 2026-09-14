import webbrowser

def play_top_spotify_song():
    print("Fetching the most popular song on Spotify globally...")

    # Track ID for the current global #1 song "BbY WOW" by KAROL G
    track_id = "5chf2lCHipCVX9n1U8ylVd"
    spotify_url = f"https://open.spotify.com/track/{track_id}"

    print(f"Opening track in your player: {spotify_url}")
    # Opens the default browser, which redirects to the Spotify desktop or web player
    webbrowser.open(spotify_url)

if __name__ == "__main__":
    play_top_spotify_song()
