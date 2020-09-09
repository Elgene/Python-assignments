def Calculate(str):
   length = len(str)
   print ("The length of the string ‘{0}’ is: {1}".format(str,length))
   return length

TotalLength=0

NoOfItem = int(input('How many item di you want in list?'))
my_list = []

for k in range(0,NoOfItem):
   FruitType = input("Enter string {0}:".format(k+1))
   my_list.append(FruitType)
   
print(my_list)

for fruit in my_list:        # traversal of List sequence
   TotalLength = TotalLength+Calculate(fruit)
	
print ("The total length of all strings is: {0}".format(TotalLength))


