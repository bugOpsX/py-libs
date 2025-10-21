import sys
import requests
import random
import webbrowser
import os
# Force UTF-8 output so emojis print correctly
sys.stdout.reconfigure(encoding='utf-8')


TENOR_API_KEY = os.getenv("TENOR_API_KEY")
CLIENT_KEY = os.getenv("TENOR_CLIENT_KEY", "my_test_app") 

# Fallback text memes 
TEXT_MEMES = [
    "When nothing goes right… go left",
    "404: Motivation not found",
    "I have trust issues… with my code running on first try",
    "Programmer: turns coffee into bugs"
]

def fetch_trending_tenor_gif():
    """Fetch a random trending GIF from Tenor."""
    try:
        url = "https://tenor.googleapis.com/v2/featured"
        params = {
            "key": TENOR_API_KEY,
            "client_key": CLIENT_KEY,
            "limit": 10,
            "locale": "en_US",
            "media_filter": "minimal",
            "contentfilter": "medium"
        }
        r = requests.get(url, params=params, timeout=5)
        r.raise_for_status()
        
        results = r.json().get("results", [])
        if not results:
            return None

        choice = random.choice(results)
        return choice["media_formats"]["gif"]["url"]

    except Exception as e:
        
        return None

def get_meme():
    """Return a GIF meme if possible, otherwise a text meme."""
    gif_url = fetch_trending_tenor_gif()
    if gif_url:
        return {"type": "gif", "url": gif_url}
    else:
        return {"type": "text", "text": random.choice(TEXT_MEMES)}

if __name__ == "__main__":
    meme = get_meme()

    if meme["type"] == "gif":
        print("Opening GIF in browser:", meme["url"])
        webbrowser.open(meme["url"])
    else:
        print("Text Meme:", meme["text"])
