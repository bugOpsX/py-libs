import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data.get("type") == "single":
            return data.get("joke")
        elif data.get("type") == "twopart":
            return f"{data.get('setup')} - {data.get('delivery')}"
        else:
            return "No joke found right now!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print(get_joke())
