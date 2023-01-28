inv_alphabet = {contains the mapping of each number to letter}
output = []

code_input = str(raw_input("Enter your cipher here: "))
split_code = code_input.split(",")

split_code = [int(i) for i in split_code]

for i in split_code:
    output.append(inv_alphabet[i])

print output
