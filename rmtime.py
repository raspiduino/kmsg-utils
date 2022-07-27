#!/usr/bin/python3

import sys

# Check if enough parameters
if len(sys.argv) < 3:
	print("Usage: python3 rmtime.py kmsg.txt out.txt")
	exit(1)

# Open and parse the file
try:
	f = open(sys.argv[1])
	a = f.read().split("\n")
	f.close()

# File not exist
except FileNotFoundError:
	print("File not found: " + sys.argv[1])
	exit(1)

# Placeholder
out = []
counter = 0

# Process each line
try:
	for i in a:
		o = "" # String placeholder

		b = i.split("[")

		o += b[0]

		if len(b) > 2:
			# Other thing might have been parse too
			# Now get them back
			for i in b[2:]:
				o += "[" + i

		out.append(o) # Finally add it to array
		counter += 1

except IndexError:
	print("You might not have a vaild kernel log file. Error parsing line " + str(counter))

# Write result
try:
	f = open(sys.argv[2], "w")
	f.write('\n'.join(out))
	f.close()

except FileNotFoundError:
	print("File not found: " + sys.argv[2])
