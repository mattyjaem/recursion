#I'll be honest i have no idea what this is for
barcodes = []
numOfBarcodes = 0
while numOfBarcodes <= 100:
	barcode = input("Enter barcode: ")
	barcodes.append(barcode)

for i  in barcodes:
    barcode = barcodes[i]
    weights = 13131
    multWeights = 0
    for x in barcode:
        multWeights = multweights + barcode[x] * index.weights[x]

 #main program
 print (multWeights)