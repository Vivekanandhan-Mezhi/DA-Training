letter = "abcfsdgedasdasde"
substring = "ccd"
count = 0
substring_length = len(substring)

if len(letter) > substring_length and len(letter) <= 10:
    for i in range(len(letter)):
        if letter[i:i+substring_length] == substring:
            count+=1

    print(count)
else:
    print("Error! Constraint mismatch...")

########Other solutions: ######################
# # Python code to demonstrate 
# # to count total number
# # of substring in string

# import re
# # Initialising string
# s = 'ababababa'


# # Count count of substrings using re.findall
# res= len(re.findall('(?=(aba))', s))

# print("Number of substrings", res)

#Pseudo code
# count = 0
# st = 0
# end = 3
# len(substring)

# slice string till len(sub string)
# check len(string) > len(substring) 
# if result == substring then 
# increment count else increment the loop till len(string)

# string[0:0+len(substring)] == substring
# count++
# string[1:3] 
# st++
# end++