

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(symbol, table_id, estimate_type):
    # Define the URL for the Yahoo Finance page containing the data
    url = f"https://finance.yahoo.com/quote/{symbol}/analysis"

    # Define headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the section containing the specified table
        section = soup.find("section", {"data-testid": table_id})

        # Check if the section exists
        if section:
            # Find the table within the section
            table = section.find("table")

            # Check if the table exists
            if table:
                # Find all table rows
                rows = table.find_all("tr")
                # Loop through the rows to find the row containing the specified estimate type
                for row in rows:
                    # Check if the row contains the specified estimate type
                    if estimate_type in row.text:
                        # Extract the data associated with the estimate type
                        estimate_data = [data.text.strip() for data in row.find_all("td")[1:]]
                        # Create a DataFrame with the ticker and estimate data
                        return pd.DataFrame([[symbol] + estimate_data], columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])
                # If the estimate type is not found
                print(f"{estimate_type} data not found for {symbol}.")
                return None
            else:
                # If the table is not found within the section
                print(f"Table not found within the section for {symbol}.")
                return None
        else:
            # If the section is not found
            print(f"Section not found for {symbol}.")
            return None
    else:
        # If the request fails
        print(f"Failed to retrieve data for {symbol}. Status code:", response.status_code)
        return None

# Define symbols for which to retrieve data
symbols = ["AAPL", "MSFT", "NVDA", "META"]

# Define the IDs of the tables containing the data
table_ids = {"Earnings Estimate": "earningsEstimate", "Revenue Estimate": "revenueEstimate"}

# Initialize empty DataFrames for each table
earning_estimates_df = pd.DataFrame(columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])
revenue_estimates_df = pd.DataFrame(columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])
historical_earnings_df = pd.DataFrame(columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])
historical_revenue_df = pd.DataFrame(columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])

# Iterate through symbols and table IDs to retrieve data
for symbol in symbols:
    for table_name, table_id in table_ids.items():
        if table_name == "Earnings Estimate":
            data = get_data(symbol, table_id, "Year Ago EPS")
            historical_earnings_df = pd.concat([historical_earnings_df, data], ignore_index=True)
            data = get_data(symbol, table_id, "Avg. Estimate")
            earning_estimates_df = pd.concat([earning_estimates_df, data], ignore_index=True)


        elif table_name == "Revenue Estimate":
            data = get_data(symbol, table_id, "Year Ago Sales")
            historical_revenue_df = pd.concat([historical_revenue_df, data], ignore_index=True)
            data = get_data(symbol, table_id, "Avg. Estimate")
            revenue_estimates_df = pd.concat([revenue_estimates_df, data], ignore_index=True)

# Save the dataframes to an Excel file with multiple tabs
with pd.ExcelWriter("estimates_historical.xlsx",
                    engine='xlsxwriter',
                    engine_kwargs={'options': {'strings_to_numbers': True}}) as writer:

    # Save each dataframe to a separate tab
    historical_earnings_df.to_excel(writer, sheet_name="Historical_Earnings", index=False)
    historical_revenue_df.to_excel(writer, sheet_name="Historical_Revenue", index=False)
    earning_estimates_df.to_excel(writer, sheet_name="Earning_Estimates", index=False)
    revenue_estimates_df.to_excel(writer, sheet_name="Revenue_Estimates", index=False)
