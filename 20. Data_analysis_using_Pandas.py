import pandas as pd
# import the library pandas
# if it is not installed, please install the library by running the command given below on terminal
# pip install pandas
# this will install the library for you which will be used for data analysis
df = pd.read_csv("crypto-markets.csv",
                 usecols = ["date", "symbol", "open", "close"],
                 index_col="date")
# index_col will get rid of the sequence 0, 1, 2 and consider the date field as the index
# usecols will only display the specific columns mentioned from the csv passed as input
print(df)

# using df.head(15): this will print the first 15 rows from the excel sheet
print(df.head(15))

# using df.tail(15): this will print the last 15 rows from the excel sheet
print(df.tail(15))

# we will now calculate the difference between open and close columns from the sheet and store it in the third column
df["difference"] = df.open - df.close
print(df.head(15))
# this will print the difference value between the first open and close values from the sheet in a new column difference

# count the number of rows present with a specific symbol
print(df["symbol"].value_counts())

# also to fetch only the symbols from the dataset you can use unique
# this returns the array of symbols from the dataset
print(df["symbol"].unique())

# to print only specific columns from the dataset you can use the following
print(df[["symbol", "open"]])
# the output of the above statement will contain symbol and open value from the dataset along with date as it is the indexed field

# we can also create a new dataFrame with the specific columns mentioned
df2 = df[["symbol", "open"]]
print(df2)
# this table will contain the exact same output which was obtained by the above print statement

# we will define a new dataFrame which will only contain the values with symbol BTC
btcDf = df[df.symbol == "BTC"]
print(btcDf)
# the above dataFrame will only have the values with BTC symbol

# we will now print the new dataFrame in descending order w.r.t the difference
print(btcDf.sort_values("difference", ascending=False))
# the first value is the entry with the biggest difference in the BTC value

# we can also print only those values whose difference is more than 1200
print(btcDf[btcDf.difference > 1200])
# we can also print open, close values greater than 10000 using a similar condition

# now we will write the sorted dataFrame in a new csv file using to_csv
btcDf.sort_values("difference", ascending=False).to_csv("BTC_Difference.csv")