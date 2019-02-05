import re
string = "she sells sea shells on the sea shore"
pattern1 = "sea"
replace = "ocean"
string_1 = re.sub(pattern1,replace,string,1)
print(string_1)
