#Examples of invalid binary numbers: abc 10102011 10101FF 0000 1111 (note: contains a space)
#Examples of valid, rejected binary numbers: 00000000 1111 01110000001
#Examples of valid, accepted binary numbers: 1000001 11000000 1111


binary = input(str("Enter a binary number: "))
print(binary)
binary_list = list(map(str, binary))
print(binary_list)
valid = True
accepted = True
convert = ""
var = binary_list.count('1')
print(var)

for character in binary:
    if character != '1' and character != '0':
        valid = False
        break
    if var != 2:
      accepted = False


if (valid == True and accepted == True):
  print("Input", binary ,"is valid and accepted")
  convert =  int(binary, 2)
  print ("The number is ", convert)
elif (valid == False):
  print ("Input was invalid")
elif (accepted == False):
  print ("Input was rejected") 
  


