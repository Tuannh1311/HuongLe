#%%
import pandas as pd
import numpy as np
import os
from pandas import DataFrame, Series, read_excel, value_counts
from datetime import date, datetime,timedelta
#loop address
path = os.getcwd()
files = os.listdir(r'Autobooking/SOURCE/')
files
k = '24'
for i in range(0,len(files)):
    address = files[i]
    address_excelfile = fr"Autobooking/SOURCE/{address}"
    #dem so sheet:
    xl=pd.ExcelFile(address_excelfile)
    sheets_source_final =len(xl.sheet_names)
    for a in range (0,sheets_source_final):
        source = pd.read_excel(address_excelfile,sheet_name=a).fillna(0)
        sum_credit_debit = source['Debit'].astype(float) + source['Credit'].astype(float)
        source['sum_cre_deb'] = sum_credit_debit
        #Xu ly file source
        source_final = source[source['sum_cre_deb'] != 0]
        source_final
        sum_credit_debit_final = source_final['Debit'].astype(float) + source_final['Credit'].astype(float)
        no_row_df = (source_final['sum_cre_deb'] >0).sum()
        #tao bien Unique File indetification
        file_date = address.split('.')[0][-8:]
        unique_file_indentification=str('HH'+ file_date[2:])
        #tao new DF
        DF_columns =['key batch id','key message id',
                                'key item','company code','document type',
                                'document date','posting date','fiscal period',
                                'ledger group','header text','debit credit',
                                'gl account','currency','amount document','amount local currency','value date','segment',
                                'cost center','internal order','profit center','line text',
                                'assignment','XREF1','XREF2','XREF3','VENDOR no','Name','Tax no 1',
                                'street','city','MWSKZ','Gross/net','Tax amount','BP type','BSEG','Trading partner']
        DF_obj = DataFrame()
        DF_obj = DataFrame(np.arange(no_row_df*len(DF_columns)).reshape(no_row_df,len(DF_columns)),columns=DF_columns)
        # key batch id
        DF_obj['key batch id']=f'{unique_file_indentification}{k}'
        #key message id
        DF_obj['key message id'] = f'{unique_file_indentification}{k}'
        debit_count = source['Debit']>0
        credit_count = source ['Credit'] > 0
        debit_credit_count = debit_count.sum()+credit_count.sum()
        #key item
        DF_obj['key item']= range(1,len(DF_obj)+1)
        #company code
        DF_obj['company code'] = 'VN01'
        #document type
        DF_obj['document type'] = 'LR'
        #document date
        DF_obj['document date'] = str(file_date)
        #posting date
        week_day_infull = datetime.strptime(file_date,"%Y%m%d")
        week_day=datetime.strptime(file_date,"%Y%m%d").weekday()
        if week_day == 0:
            DF_obj['posting date'] = week_day_infull - timedelta(1)
        else:
            DF_obj['posting date'] = DF_obj['document date']
        #fiscal group:
        DF_obj['fiscal period'] = ''
        #ledger_group:
        DF_obj['ledger group']=''
        #header_text:
        DF_obj['header text'] = source.iloc[0][0]
        #debit_credit:
        DF_obj['debit credit']=np.where(source_final['Credit']>0,'C','')
        DF_obj['debit credit']=np.where(source_final['Debit']>0,'D',DF_obj['debit credit'])
        #gl account:
        DF_obj['gl account'] =list(source_final['IFRS'])
        #currency:
        DF_obj ['currency']='VND'
        #amount document:
        DF_obj['amount document'] = list(sum_credit_debit_final)
        #line text:
        DF_obj['line text'] = list(source_final['Text'])
        #assignment:
        DF_obj['assignment']= source_final.columns[0]
        #define blank value:
        DF_obj[['amount local currency','value date','segment','cost center','internal order','profit center','XREF1','XREF2','XREF3','VENDOR no','Name','Tax no 1','street','city','MWSKZ','Gross/net','Tax amount','BP type','BSEG','Trading partner']]=''
        #Check file rong truoc khi xuat
        if len(DF_obj) > 0:
            DF_obj.to_csv (fr'AUTO{unique_file_indentification}{k}.csv',index = False, header =False)
            k = str(int(k) + 1).rjust(2,"0")







# %%
