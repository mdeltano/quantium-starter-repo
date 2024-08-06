import csv

with open('./data/daily_sales_data_0.csv') as csv_file:
    with open('./data/daily_sales_data_final.csv', mode='w', newline='') as csv_write:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(csv_write, delimiter=',')

        for row in csv_reader:
            if row[0] == "pink morsel":
                var1 = float (row[1].removeprefix('$'))
                var2 = float (row[2])
                csv_writer.writerow([var1*var2,row[3],row[4]])