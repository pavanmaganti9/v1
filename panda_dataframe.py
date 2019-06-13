import pandas as pd
import numpy as np
import pdfkit

xl = pd.read_excel('store.xls', index_col="Order ID")

# data frame from dictionary

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

print df

# data frame from numpy

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a1', 'b1', 'c1'])

print df2

# data frame from List

lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
lis = pd.DataFrame(lst)
print lis

first1 = xl.loc["CA-2014-115812"]

print first1


# selecting single column

name = xl['Customer Name']
print name

# selecting multiple column

name2 = xl[['Customer Name','Country','Sales']]
print name2

# merge two data frames

one = xl[['Customer ID', 'Product ID', 'Postal Code']]

df1 = one.head(10)

two = xl[['Customer Name','Country','Sales']]

df2 = two.head(10)

df_row = pd.concat([df1, df2], axis=1)

print df_row

# importing data to csv, html and pdf

df_row.to_csv('out.csv', index=False)

df_row.to_html('out.html', index=False)

df_row.to_json(r'out.json',orient='records')

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
PdfFilename = 'out.pdf'
pdfkit.from_file('out.html', PdfFilename, configuration=config)
