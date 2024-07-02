
# main

import pandas as pd
from data_processing import process_data

def main():
    # Define symbols for which to retrieve data
    symbols = ["AAPL", "TSLA", "IBM", "CSCO", "ORCL", "ADP", "FI", "ACN", "ANET"]

    # Define the IDs of the tables containing the data
    table_ids = {"Earnings Estimate": "earningsEstimate", "Revenue Estimate": "revenueEstimate"}

    # Process the data
    earning_estimates_df, revenue_estimates_df, historical_earnings_df, historical_revenue_df = process_data(symbols, table_ids)

    # Save the dataframes to an Excel file with multiple tabs
    with pd.ExcelWriter("estimates_historical.xlsx",
                        engine='xlsxwriter',
                        engine_kwargs={'options': {'strings_to_numbers': True}}) as writer:

        # Save each dataframe to a separate tab
        historical_earnings_df.to_excel(writer, sheet_name="Historical_Earnings", index=False)
        historical_revenue_df.to_excel(writer, sheet_name="Historical_Revenue", index=False)
        earning_estimates_df.to_excel(writer, sheet_name="Earning_Estimates", index=False)
        revenue_estimates_df.to_excel(writer, sheet_name="Revenue_Estimates", index=False)

if __name__ == "__main__":
    main()
