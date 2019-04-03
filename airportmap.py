import csv
import sys

print('<?xml version="1.0"?>')
print('<svg height="1800" width="3600" version="1.1"')
print('    xmlns="http://www.w3.org/2000/svg">')
with open(sys.argv[1], 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
	for row in reader:
		if row[0] == 'item':
			continue;
		x = int((float(row[4]) + 180) * 10)
		y = 1800 - int((float(row[3]) + 90) * 10)
		print(f'<circle cx="{x}" cy="{y}" stroke="black" stroke-width="1" fill="black" r="1"/>')
print('</svg>')