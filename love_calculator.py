name1 = input("enter your name: ")
name_fiance = input("enter your fiancee's name: ")
combine_names  = name1 + name_fiance
#print(combine_names)
lower_case = combine_names.lower()
#print(lower_case)
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t + r + u + e
#print(true)

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l + o + v + e
#print(love)
love_score = str(true) + str(love)
#print(love_score)
if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your love score is {love_score} and you go together like coke and mentos ")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your love score is {love_score} and you are good together ")
else:
    print(f"Your love score is {love_score}")
