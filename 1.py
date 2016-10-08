from itertools import groupby
# input must be separated values with comma and whitespaces
string = input("Play-->")
lst = list(string.split(', '))
print(lst)
# my_list = ['H', 'H', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'T', 'T', 'T']
strH = max(len(list(v)) for k, v in groupby(lst) if k == 'h' or k == 'H')
strT = max(len(list(v)) for k, v in groupby(lst) if k == 't' or k == 'T')

if (strH > strT):
	print("H wins", strH, "streaks")
elif (strH == strT):
	print("Draw")
else:
	print("T wins", strT, "streaks")
