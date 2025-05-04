import webbrowser
import time

# Spotify track link
URL = "https://open.spotify.com/track/5EbwDW4cgCWcbTt5HRN6sV"
duration = 200  # seconds (3 min 20 sec)

while True:
    webbrowser.open(URL)
    time.sleep(duration)
