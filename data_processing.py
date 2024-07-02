

import pandas as pd
from data_fetching import get_data

def process_data(symbols, table_ids):
    """Fetch and process data for given symbols and table IDs."""

    earning_estimates_df = pd.DataFrame(
        columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])
    revenue_estimates_df = pd.DataFrame(
        columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])
    historical_earnings_df = pd.DataFrame(
        columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])
    historical_revenue_df = pd.DataFrame(
        columns=["Ticker", "Current Quarter", "Next Quarter", "Current Year", "Next Year"])

    for symbol in symbols:
        for table_name, table_id in table_ids.items():
            if table_name == "Earnings Estimate":
                data = get_data(symbol, table_id, "Year Ago EPS")
                if data:
                    historical_earnings_df = pd.concat([historical_earnings_df, pd.DataFrame([{"Ticker": symbol,
                                                                                               "Current Quarter": data[
                                                                                                   0],
                                                                                               "Next Quarter": data[1],
                                                                                               "Current Year": data[2],
                                                                                               "Next Year": data[3]}])],
                                                       ignore_index=True)
                data = get_data(symbol, table_id, "Avg. Estimate")
                if data:
                    earning_estimates_df = pd.concat([earning_estimates_df, pd.DataFrame([{"Ticker": symbol,
                                                                                           "Current Quarter": data[0],
                                                                                           "Next Quarter": data[1],
                                                                                           "Current Year": data[2],
                                                                                           "Next Year": data[3]}])],
                                                     ignore_index=True)
            elif table_name == "Revenue Estimate":
                data = get_data(symbol, table_id, "Year Ago Sales")
                if data:
                    historical_revenue_df = pd.concat([historical_revenue_df, pd.DataFrame([{"Ticker": symbol,
                                                                                             "Current Quarter": data[0],
                                                                                             "Next Quarter": data[1],
                                                                                             "Current Year": data[2],
                                                                                             "Next Year": data[3]}])],
                                                      ignore_index=True)
                data = get_data(symbol, table_id, "Avg. Estimate")
                if data:
                    revenue_estimates_df = pd.concat([revenue_estimates_df, pd.DataFrame([{"Ticker": symbol,
                                                                                           "Current Quarter": data[0],
                                                                                           "Next Quarter": data[1],
                                                                                           "Current Year": data[2],
                                                                                           "Next Year": data[3]}])],
                                                     ignore_index=True)

    return earning_estimates_df, revenue_estimates_df, historical_earnings_df, historical_revenue_df
