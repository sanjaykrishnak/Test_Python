class NamespaceTest:
   cl_variable=1
	
   def __init__(self,val):
   	self.in_variable=val
   	
   def printme(self):
   	return 1;

nt1 = NamespaceTest(9)
nt2 = NamespaceTest(9)

pt = nt1.printme()

print('Print me function retur type->' + str(pt))
print('instance varialbe nt1->' + str(nt1.in_variable))
print('instance varialbe nt2->' + str(nt2.in_variable))

print(nt1.cl_variable)

nt1.cl_variable=3

print('class varialbe nt1->' + str(nt1.cl_variable))
print('class varialbe nt2->' + str(nt2.cl_variable))


