

import pandas as pd

def save_to_excel(earning_estimates_df, revenue_estimates_df, historical_earnings_df, historical_revenue_df):
    # Save the dataframes to an Excel file with multiple tabs
    with pd.ExcelWriter("estimates_historical.xlsx",
                        engine='xlsxwriter',
                        engine_kwargs={'options': {'strings_to_numbers': True}}) as writer:

        # Save each dataframe to a separate tab
        historical_earnings_df.to_excel(writer, sheet_name="Historical_Earnings", index=False)
        historical_revenue_df.to_excel(writer, sheet_name="Historical_Revenue", index=False)
        earning_estimates_df.to_excel(writer, sheet_name="Earning_Estimates", index=False)
        revenue_estimates_df.to_excel(writer, sheet_name="Revenue_Estimates", index=False)
