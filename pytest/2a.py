NoOfItem = int(input('How many item di you want in list?'))
my_list = []

for k in range(0,NoOfItem):
   FruitType = input("Enter string {0}:".format(k+1))
   my_list.append(FruitType)
   
print(my_list)




