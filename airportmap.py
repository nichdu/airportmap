import csv

print('<?xml version="1.0"?>')
print('<svg height="1800" width="3600" version="1.1"')
print('    xmlns="http://www.w3.org/2000/svg">')
with open('airports.dat', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
	for row in reader:
		x = int((float(row[7]) + 180) * 10)
		y = 1800 - int((float(row[6]) + 90) * 10)
		print(f'<circle cx="{x}" cy="{y}" stroke="black" stroke-width="1" fill="black" r="1"/>')
print('</svg>')