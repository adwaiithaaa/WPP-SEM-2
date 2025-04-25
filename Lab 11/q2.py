import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()
lower_case = s.str.lower()
length_of_strings = s.str.len()

print("Upper case:\n", upper_case)
print("Lower case:\n", lower_case)
print("Length of strings:\n", length_of_strings)