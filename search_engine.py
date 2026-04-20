import requests
from bs4 import BeautifulSoup
import re
import math
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

class SearchEngine:
    def __init__(self):
        self.inverted_index = {}
        self.document_count = 0

    def crawl(self, url):
        logging.info(f'Crawling URL: {url}')
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.parse(response.text, url)
        except Exception as e:
            logging.error(f'Error crawling {url}: {e}') 

    def parse(self, html, url):
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        tokens = self.tokenize(text)
        self.index(tokens, url)

    def tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def index(self, tokens, url):
        for token in tokens:
            if token not in self.inverted_index:
                self.inverted_index[token] = set()
            self.inverted_index[token].add(url)
        self.document_count += 1

    def search(self, query):
        results = set(self.inverted_index.get(query.lower(), []))
        ranked_results = self.rank_results(results)
        return ranked_results

    def rank_results(self, results):
        # Placeholder for TF-IDF ranking logic
        return results

# Sample usage
if __name__ == '__main__':
    engine = SearchEngine()
    engine.crawl('https://example.com')
    results = engine.search('example')
    print(results)
