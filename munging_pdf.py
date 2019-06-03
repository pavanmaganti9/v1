import pandas as pd
import pdfkit
path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
sv = pd.read_csv('work.csv',index_col=0)
sv.to_html('test.html')
PdfFilename='pdfPrintOut.pdf'
pdfkit.from_file('test.html', PdfFilename, configuration=config)