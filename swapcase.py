statement = "PyThon"

mod_s=""
for words in statement:
    if words.isupper():
        mod_s+=words.lower()
    else:
        mod_s+=words.upper()
print(mod_s)