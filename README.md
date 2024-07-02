# Disclaimer: 

This code is for informational and educational purposes only and does not constitute investment advice. Users should conduct their own research and consult with a professional financial advisor before making any investment decisions. The author is not responsible for any investment actions taken based on the information provided in and from this repository.

# Use Case 
Are you a fundamental analyst without access to a Bloomberg terminal? 

Do you want to compare how richly a stock is trading compared to its peers? For example, all else being constant, do you want to know if it's cheaper to invest in NVDA or AAPL for the same return on investment based on Wall Street earnings consensus? 

If yes, then you must have struggled with manually inputting revenue and earnings estimates information.

This Python script pulls analysts’ estimates (both revenue and earnings) from Yahoo Finance and compiles the output into an Excel file.

# Sample Output: 
![image](https://github.com/Dispassionate-Analyst/earning_estimates_scrapper/assets/164734048/ec9fe697-6dd4-4265-aa94-a392fc4596c0)

Output size less than 10kb and took less than 1 sec to run 

Results: 
![image](https://github.com/Dispassionate-Analyst/earning_estimates_scrapper/assets/164734048/93948a2b-cd89-4f39-9853-bb3265924254)

# Constraints: 
Yahoo Finance has a limit of 60 GET requests per minute and 360 GET requests per hour. The upcoming update will ensure requests stay within the limit; instead of encountering an error, the script will pause for a minute before continuing to bypass said limits by Yahoo Finance.

