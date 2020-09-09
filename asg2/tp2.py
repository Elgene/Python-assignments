InitialAmount = int(input("Initial amount ($):"))

val1=0

remainder1=InitialAmount%100 #
if remainder1!=InitialAmount:
	val1=int(InitialAmount/100) 
	for x in range(val1):
		print("$100")

remainder2=remainder1%50 
if remainder2!=remainder1:
	val2=int(remainder1/50) 
	for x in range(val2):
		print("$50")
		
remainder3=remainder2%20 
if remainder3!=remainder2:
	val2=int(remainder2/20) 
	for x in range(val2):
		print("$20")

remainder4=remainder3%5 
if remainder4!=remainder3:
	val2=int(remainder3/5) 
	for x in range(val2):
		print("$5")

remainder5=remainder4%2 
if remainder5!=remainder4:
	val2=int(remainder4/2) 
	for x in range(val2):
		print("$2")

remainder6=remainder5%1 
if remainder6!=remainder5:
	val2=int(remainder5/1) 
	for x in range(val2):
		print("$1")
		




