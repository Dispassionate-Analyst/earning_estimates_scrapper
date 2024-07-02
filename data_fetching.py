

import requests
from bs4 import BeautifulSoup

def get_data(symbol, table_id, estimate_type):
    # Define the URL for the Yahoo Finance page containing the data
    url = f"https://finance.yahoo.com/quote/{symbol}/analysis"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        soup = BeautifulSoup(response.content, "html.parser")

        section = soup.find("section", {"data-testid": table_id})

        if section:
            table = section.find("table")

            if table:
                rows = table.find_all("tr")

                for row in rows:
                    if estimate_type in row.text:
                        estimate_data = [data.text.strip() for data in row.find_all("td")[1:]]
                        return estimate_data

                raise ValueError(f"{estimate_type} data not found for {symbol}.")

            else:
                raise ValueError(f"Table not found within the section for {symbol}.")

        else:
            raise ValueError(f"Section not found for {symbol}.")

    except requests.RequestException as e:
        print(f"Failed to retrieve data for {symbol}. Error: {e}")
        return None

    except Exception as e:
        print(f"Error processing data for {symbol}. Error: {e}")
        return None
