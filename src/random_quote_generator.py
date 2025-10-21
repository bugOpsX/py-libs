import requests
import random
from typing import Optional, List
from dataclasses import dataclass 


@dataclass
class Quote:
    text: str
    author: str
    category: str = "general"
    
    def __str__(self) -> str:
        border = "─" * (len(self.text) + 4)
        return f"\n┌{border}┐\n│  {self.text}  │\n└{border}┘\n  — {self.author}\n  [{self.category}]"


class QuoteFetcher:
    FALLBACK_QUOTES = {
        "motivation": [
            Quote("The only way to do great work is to love what you do.", "Steve Jobs", "motivation"),
            Quote("Believe you can and you're halfway there.", "Theodore Roosevelt", "motivation"),
            Quote("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill", "motivation"),
        ],
        "humor": [
            Quote("I'm not superstitious, but I am a little stitious.", "Michael Scott", "humor"),
            Quote("The road to success is dotted with many tempting parking spaces.", "Will Rogers", "humor"),
            Quote("I find television very educational. Every time someone turns it on, I go in the other room and read a book.", "Groucho Marx", "humor"),
        ],
        "life": [
            Quote("Life is what happens when you're busy making other plans.", "John Lennon", "life"),
            Quote("The purpose of our lives is to be happy.", "Dalai Lama", "life"),
            Quote("In three words I can sum up everything I've learned about life: it goes on.", "Robert Frost", "life"),
        ]
    }
    
    def __init__(self):
        self.api_url = "https://zenquotes.io/api/random"
        
    def fetch_quote_from_api(self) -> Optional[Quote]:
        try:
            response = requests.get(self.api_url, timeout=5)
            response.raise_for_status()
            data = response.json()[0]
            return Quote(
                text=data['q'],
                author=data['a'],
                category="general"
            )
        except Exception as e:
            print(f"API fetch failed: {e}")
            return None
    
    def get_random_quote(self, category: Optional[str] = None) -> Quote:
        if category and category.lower() in self.FALLBACK_QUOTES:
            return random.choice(self.FALLBACK_QUOTES[category.lower()])
        quote = self.fetch_quote_from_api()
        if quote:
            return quote
        all_quotes = [q for quotes in self.FALLBACK_QUOTES.values() for q in quotes]
        return random.choice(all_quotes)
    
    def get_quotes_by_category(self, category: str) -> List[Quote]:
        return self.FALLBACK_QUOTES.get(category.lower(), [])
    
    def list_categories(self) -> List[str]:
        return list(self.FALLBACK_QUOTES.keys())


def display_quote(quote: Quote, style: str = "box") -> None:
    if style == "simple":
        print(f"\n\"{quote.text}\"\n- {quote.author} [{quote.category}]\n")
    elif style == "fancy":
        print("\n" + "✨" * 30)
        print(f"💭 {quote.text}")
        print(f"   ✍️  {quote.author}")
        print(f"   🏷️  {quote.category}")
        print("✨" * 30 + "\n")
    else:
        print(quote)


if __name__ == "__main__":
    fetcher = QuoteFetcher()
    
    print("=" * 60)
    print("RANDOM INSPIRATIONAL QUOTE FETCHER")
    print("=" * 60)
    
    print("\n1. Random Quote from API:")
    quote = fetcher.get_random_quote()
    display_quote(quote, style="box")
    
    print("\n2. Motivational Quote:")
    quote = fetcher.get_random_quote(category="motivation")
    display_quote(quote, style="fancy")
    
    print("\n3. Humorous Quote:")
    quote = fetcher.get_random_quote(category="humor")
    display_quote(quote, style="simple")
    
    print("\n4. Available Categories:")
    print(", ".join(fetcher.list_categories()))
    
    print("\n" + "=" * 60)
