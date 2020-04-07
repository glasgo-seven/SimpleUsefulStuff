# --------------------------------------------------
#	Function that converts number in base_10 to base_2.
# --------------------------------------------------

def binary(num: int):
	'''
		Convert num in base_10 to base_2.
	'''
	s = ""
	while num > 0:
		s = f'{num % 2}{s}'
		num //= 2
	return s

_bin = binary(int(input("num_10 = ")))
print(f"num_2  = {_bin}")
