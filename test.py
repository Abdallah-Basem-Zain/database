full_name = "abdallah basem zain"
splited = full_name.split(" ")
s2 = full_name.removesuffix(" "+full_name.split(" ")[len(splited) - 1])
s2 = s2.split(" ")
print(s2)
