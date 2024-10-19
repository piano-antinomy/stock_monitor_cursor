import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Fetch data
coin = yf.download("COIN", start="2023-01-01", end="2023-12-31")
cony = yf.download("CONY", start="2023-01-01", end="2023-12-31")

# Combine closing prices
df = pd.DataFrame({
    'COIN': coin['Close'],
    'CONY': cony['Close']
})

# Create comparison graph
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['COIN'], label='COIN')
plt.plot(df.index, df['CONY'], label='CONY')
plt.title('COIN vs CONY Stock Price Comparison (2023)')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

# Correlation analysis
correlation = df['COIN'].corr(df['CONY'])
print(f"Correlation between COIN and CONY: {correlation}")

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['COIN'], df['CONY'])
plt.title('COIN vs CONY Scatter Plot')
plt.xlabel('COIN Price')
plt.ylabel('CONY Price')
plt.show()

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(df['COIN'], df['CONY'])
print(f"R-squared: {r_value**2}")
print(f"p-value: {p_value}")
