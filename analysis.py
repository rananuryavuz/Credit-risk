import pandas as pd
from datetime import datetime

def calc_data(data):

    column_date_2 = pd.to_datetime(str(data['Date2']), format='%Y%m%d', errors='ignore')
    column_date_5 = pd.to_datetime(data['Date_5'], format='%Y%m%d', errors='ignore')

    res = list(filter(lambda x: not pd.isnull(x), column_date_5.tolist()))
    
    if len (res) == 0:
        return 0
    else:
        res = sorted(res, key=lambda x: datetime.strptime(x, '%Y-%m-%d'), reverse=True)
        if (res[0] > column_date_2):
            opened_after_delinquency = 1
        else:
            opened_after_delinquency = 1
        return (data['Date_5_Amount'].sum() * opened_after_delinquency)
    return 0


if __name__ == '__main__':
    df = pd.read_csv("Ir_test.csv") 
    res = df.groupby('ID').apply(calc_data)
    res.to_csv(r'result.csv')
