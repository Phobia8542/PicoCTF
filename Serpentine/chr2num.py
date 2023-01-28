# cipher = input("Input ASCII values : ")

hex = input("Enter chr value: ")

# conversion
dec = int(hex, 16)
 
print('Value in hexadecimal:', hex)
print('Value in decimal:', dec)
print('Value as letter:', chr(int(dec)))

#### Mistake below ### 

# o = (0x15, 0x07, 0x08, 0x06, 0x27, 0x21, 0x23, 0x15, 0x5c, 0x01, 0x57, 0x2a, 0x17, 0x5e, 0x5f, 0x0d, 0x3b, 0x19, 0x56, 0x5b, 0x5e, 0x36, 0x53, 0x07, 0x51, 0x18, 0x58, 0x05, 0x57, 0x11, 0x3a, 0x56, 0x0e, 0x5d, 0x53, 0x11, 0x54, 0x5c, 0x53, 0x14)

# o = input("Enter chr value: ")

# for c in o:

#    v = chr(c)
#    print(c, "is", v)

# print(o)

# Python program to convert ASCII to character

# take input
# num = int(input("Enter ASCII value: "))

# printing character
# print("Character =", chr(num))

# n = int(o)

# print("This easier to read?", chr(n))

# print("This easier to read?", (o))