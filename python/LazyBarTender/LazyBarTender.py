input = {
"customer1": ["n1", "n2", "n3"],
"customer2": ["n1"],
"customer3": ["n4", "n5"],
"customer4": ["n6"],
"customer5": ["n8"],
"customer6": ["n8", "n3"],
"customer6": ["n1", "n2"],

}

drinks = ["n1", "n2", "n3", "n4", "n5", "n6"]
output = []


def lazy_bar_tender(input, drinks):
	for key,val in input.iteritems():
		if not output:
			output.append(val[0])
		else:
			# check if outputDict elements are not present in ask
			for item in val:
				if item not in drinks:
					continue
				if item in output:
					continue
				else:
					output.append(item)
					break


lazy_bar_tender(input, drinks)
print output
