import pandas as pd 

book = pd.read_excel("Book1.xlsx")
# read_csv

# print(book)

# print(book.head(1))

# print(book.columns[0])

# print(book["Nama"])

# print(book[["Nama","Nilai"]])

# print(book.iloc[1])

# print(book.iloc[1:2])

for index,row in book.iterrows():
    print(index,row)