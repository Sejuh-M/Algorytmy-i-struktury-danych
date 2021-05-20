import csv
with open('mycsv.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['col1','col2','col2'])
    for i in range(100):
        thewriter.writerow(['one', 'two', 'tree'])
