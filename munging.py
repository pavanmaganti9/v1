import pandas as pd

sv = pd.read_csv('work.csv',index_col=0)
sv.to_html('contact1.html')