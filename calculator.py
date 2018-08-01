#!/usr/bin python3

import sys
base=3500
try:
	wages = int(sys.argv[1])
except:
	print("Parameter Error")
w_b = wages - base

if w_b <= 0:
	tax = 0
	print(format(tax,".2f"))
elif w_b <= 1500:
	tax = w_b * 0.03
	print(format(tax,".2f"))
elif w_b <= 4500:
	tax = w_b * 0.1 - 105
	print(format(tax,".2f"))
elif w_b <= 9000:
	tax = w_b * 0.2 - 555
	print(format(tax,".2f"))
elif w_b <= 35000:
	tax = w_b * 0.25 - 1055
	print(format(tax,".2f"))
elif w_b <= 55000:
	tax = w_b * 0.3 - 2755
	print(format(tax,".2f"))
elif w_b <=80000:
	tax = w_b * 0.35 - 5505
	print(format(tax,".2f"))
else:
	tax = w_b * 0.45 - 13505
	print(format(tax,".2f"))
	
