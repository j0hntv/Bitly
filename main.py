import requests
import os
from dotenv import load_dotenv
import argparse

def bitlink(token, url):
    headers = {'Authorization': token}

    url_api_info = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    url_api_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
    url_api_shorten = 'https://api-ssl.bitly.com/v4/shorten'

    response = requests.get(url_api_info, headers=headers)

    if response.ok:
        response = requests.get(url_api_clicks, headers=headers)
        return f'Total clicks: {response.json()["total_clicks"]}'
    
    else:
        payload = {'long_url': url}
        response = requests.post(url_api_shorten, headers=headers, json=payload)

        if response.ok:
            return response.json()['link']
        else:
            return f'Error {response.status_code}.'

def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    parser = argparse.ArgumentParser(description='URL converter')
    parser.add_argument('url', help='URL link to convert')
    args = parser.parse_args()
    url = args.url
    link = bitlink(token, url)
    print(link)
    
if __name__ == '__main__':
    main()
