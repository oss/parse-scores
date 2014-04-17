import re

read = open(raw_input("Enter your file: "))
e1 = re.compile(r"\[(.+)\]")
e2 = re.compile(r"(.+)=(.+),|(.+)=(.+)\Z")
for line in read:
	total = 0
	URIBLtotal = 0
	matched = re.search(e1, line)
	matchedList = matched.group(1).split()
	for a in matchedList:
		splitMatch = re.search(e2, a)
		if splitMatch.group(2) is None:
			if "URIBL_" in splitMatch.group(3):
				total += float(splitMatch.group(4))
				URIBLtotal += float(splitMatch.group(4))
			else:
				total += float(splitMatch.group(4))
		else:
			if "URIBL_" in splitMatch.group(1):
				total += float(splitMatch.group(2))
				URIBLtotal += float(splitMatch.group(2))
			else:
				total += float(splitMatch.group(2))
	
	net = total - URIBLtotal
	net = round(net, 4)
	total = round(total, 4)
	print(total, net)
	
		
