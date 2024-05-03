from bs4 import BeautifulSoup
import requests

def scrape_laptops(url):
    laptops = []
    
    page_number = 1
    
    try:
        while True:
            response = requests.get(f'{url}?page={page_number}')
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            laptop_blocks = soup.find_all('div', class_='card thumbnail')

            if not laptop_blocks:
                break

            for laptop_block in laptop_blocks:
                name = laptop_block.find('a', class_='title').text.strip()
                price = laptop_block.find('h4', class_='price').text.strip()
                description = laptop_block.find('p', class_='description').text.strip()
                reviews = laptop_block.find('p', class_='review-count').text.strip()
                laptops.append({'name': name, 'price': price, 'description': description, 'reviews': reviews})
            page_number += 1

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    return laptops

url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

laptops = scrape_laptops(url)
for i in laptops:
    print(i)
