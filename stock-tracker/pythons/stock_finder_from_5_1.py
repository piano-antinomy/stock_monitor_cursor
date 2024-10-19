import pandas as pd

# Read the files
rank_5_file = '/Users/yingjianding/Documents/stocks_rank/rank_5_20240912.xls'
rank_1_file = '/Users/yingjianding/Documents/stocks_rank/rank_1_20240912.xls'

# Read the files into pandas DataFrames, treating them as TSV files
df_rank_5 = pd.read_csv(rank_5_file, sep='\t')
df_rank_1 = pd.read_csv(rank_1_file, sep='\t')

# Assuming the stock symbols are in a column named 'Symbol'
# If the column name is different, replace 'Symbol' with the correct column name
rank_5_stocks = set(df_rank_5['Symbol'])
rank_1_stocks = set(df_rank_1['Symbol'])

# Find stocks that moved from rank 5 to rank 1
moved_5_to_1 = rank_5_stocks.intersection(rank_1_stocks)

# Find stocks that moved from rank 1 to rank 5
moved_1_to_5 = rank_1_stocks.intersection(rank_5_stocks)

# Print the results
print("Stocks that moved from rank 5 to rank 1:")
for stock in moved_5_to_1:
    print(stock)

print(f"\nTotal number of stocks that moved from 5 to 1: {len(moved_5_to_1)}")

print("\nStocks that moved from rank 1 to rank 5:")
for stock in moved_1_to_5:
    print(stock)

print(f"\nTotal number of stocks that moved from 1 to 5: {len(moved_1_to_5)}")

# Save the results to a file
with open('moved_stocks.txt', 'w') as f:
    f.write("Stocks that moved from rank 5 to rank 1:\n")
    for stock in moved_5_to_1:
        f.write(f"{stock}\n")
    f.write(f"\nTotal number of stocks that moved from 5 to 1: {len(moved_5_to_1)}\n\n")
    
    f.write("Stocks that moved from rank 1 to rank 5:\n")
    for stock in moved_1_to_5:
        f.write(f"{stock}\n")
    f.write(f"\nTotal number of stocks that moved from 1 to 5: {len(moved_1_to_5)}")

print("\nResults have been saved to 'moved_stocks.txt'")
