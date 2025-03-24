from bs4 import BeautifulSoup
import requests
from src.preprocessing import preprocessingTextData
from src.tokenization import uniTokenization, biGramTokenization

def scrape_and_process_text(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all("p", class_="fezwLZ")
        news = " ".join([p.get_text() for p in paragraphs])

        # Preprocessing step
        processed_news = preprocessingTextData(news)

        # Tokenization
        single_tokens = uniTokenization(processed_news)  # Unigram tokenization
        bigram_tokens = biGramTokenization(single_tokens)  # Bigram tokenization

        return single_tokens, bigram_tokens

    except requests.exceptions.RequestException as e:
        print("Error fetching the webpage:", e)
        return None, None

    except Exception as e:
        print("An unexpected error occurred:", e)
        return None, None


