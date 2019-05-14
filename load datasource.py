
'----------------------------------  load excel  --------  
import pandas as pd

df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
print (df)


'with sheet parameter
import pandas as pd

df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx', sheet_name='Type here the name of your Excel sheet')
print (df)