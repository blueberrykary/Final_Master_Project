import csv

with open('/home/blueberrykary/exp1.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
#     next(reader)
    
    with open('/home/blueberrykary/newexp1.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')
        
        for line in csv_reader:
            csv_writer.writerow(line)
