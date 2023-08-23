from datetime import datetime

date1 = '13/12/2018'
date2 = '25/2/2019'

date1_obj = datetime.strptime(date1, '%d/%m/%Y')
date2_obj = datetime.strptime(date2, '%d/%m/%Y')

days_between = abs((date2_obj - date1_obj).days)

print('Number of days between', date1, 'and', date2, '=', days_between, 'days')


