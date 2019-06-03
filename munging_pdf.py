import pandas as pd
import pdfkit
path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
sv = pd.read_csv('work.csv',index_col=0)
sv.to_html('docs/test.html')
PdfFilename='docs/pdfPrintOut.pdf'
pdfkit.from_file('docs/test.html', PdfFilename, configuration=config)

#generating from URL
pdfkit.from_url('https://www.youtube.com/watch?v=Fo7J2dHpMjk','sample1.pdf', configuration=config)