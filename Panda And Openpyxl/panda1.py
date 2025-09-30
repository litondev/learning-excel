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

# for index,row in book.iterrows():
    # print(index,row["Nama"])

# book.loc[df["Nama"] == "Pepew"]
    # IN 
    # NOT IN 
    # AND 
    # OR 

# print(book.describe())

# book.sort_values("Nama",ascending=False)
# book.sort_values(["Nama","Nilai"],ascending=False)
# book.sort_values(["Nama","Nilai"],ascending=[1,0])

# book["Total"] = book["Nilai"] + book["Nilai Lain"]

# book = book.drop(columns=['Total'])

# book['Total'] = df.iloc[:,4:10].sum(axios=1)

# cols = list(book.columns)
# book = book[cols[0:4] + [cols[-1]] + cols[4:12]]

# book.to_csv("halo.csv",index=False)
# to_excel

# halo = df.iloc[df["Nama"] == "aku"]
# halo.to_csv("halo.csv")

# book.loc[df["Nama"].str.contains("Mega")]

# book.loc[dg["Nama"] === 'A',"Nama"] = "Agus"

# book.groupby(["Nama"])

# book.groupby(["Nama"]).mean().sort_values("Nilai",ascending=False)