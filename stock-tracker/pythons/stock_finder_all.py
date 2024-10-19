import pandas as pd
import os
from datetime import datetime

# Set the path to the directory containing the CSV files
base_path = '/Users/yingjianding/Documents/stocks_rank/'

# Get all files prefixed with "zacks_all_" and sort them
files = sorted([f for f in os.listdir(base_path) if f.startswith('zacks_all_')])

# Function to extract date from filename
def extract_date(filename):
    date_str = filename.split('_')[-1].split('.')[0]
    return datetime.strptime(date_str, '%Y-%m-%d')

# Read all CSV files
dataframes = []
for file in files:
    date = extract_date(file)
    df = pd.read_csv(os.path.join(base_path, file))
    df['Date'] = date
    dataframes.append(df)

# Concatenate all dataframes
all_data = pd.concat(dataframes).sort_values('Date')

# Group by Ticker and find changes
def find_changes(group):
    changes = group[group['Zacks Rank'].diff() != 0].copy()
    changes['Previous Rank'] = changes['Zacks Rank'].shift(1)
    changes['Rank Change'] = changes['Zacks Rank'] - changes['Previous Rank']
    return changes.dropna()

changed_stocks = all_data.groupby('Ticker', group_keys=False).apply(find_changes).reset_index(drop=True)

# Sort the changed stocks by the magnitude of rank change and date
changed_stocks = changed_stocks.sort_values(['Date', 'Rank Change'], ascending=[True, False])

# Print the results
print("\nStocks with changed ranks:")
for _, row in changed_stocks.iterrows():
    print(f"Date: {row['Date'].date()}, Ticker: {row['Ticker']}, Old Rank: {row['Previous Rank']}, New Rank: {row['Zacks Rank']}, Change: {row['Rank Change']}")

print(f"\nTotal number of rank changes: {len(changed_stocks)}")

# Save the results to a CSV file
output_file = os.path.join(base_path, 'rank_changes_all.csv')
changed_stocks.to_csv(output_file, index=False)
print(f"\nResults have been saved to '{output_file}'")
