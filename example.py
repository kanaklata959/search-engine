# Example: Using the Search Engine

"""
This example shows how to use the search engine provided in the 'kanaklata959/search-engine' repository.

## Steps:
1. Import the necessary modules from the search engine.
2. Initialize the search engine with the required parameters.
3. Perform a search query.
4. Display the results.
"""

from search_engine import SearchEngine

# Initialize the search engine
search_engine = SearchEngine(api_key='your_api_key', index='your_index')

# Perform a search query
query = 'example search'
results = search_engine.search(query)

# Display the results
for result in results:
    print(result)
