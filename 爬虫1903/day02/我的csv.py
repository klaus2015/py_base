import csv

with open('fy.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['zxm','cx'])
    writer.writerows([('zxm','fwl'),('zxm','ll'),('zxm','feng')])
