#ACSL 2015-2016 All Star #2
def binary_fractions(a, b):
  frac = a / b
  bin_frac_value = 0
  bin_frac_digits = '0.'

  i = -1
  while i > -7:
    if bin_frac_value + 2 ** i <= a / b:
      bin_frac_value += 2 ** i
      bin_frac_digits += '1'
    else:
      bin_frac_digits += '0'

    i -= 1

  bin_frac_value = str(bin_frac_value)
  
  for i in range(8 - len(bin_frac_value)):
    bin_frac_value += '0'

  print(bin_frac_digits)
  print(bin_frac_value)

binary_fractions(3, 10)
