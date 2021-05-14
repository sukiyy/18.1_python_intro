age = 19
isbirthday = False

if age >= 21:
    print("you can drink")
    if isbirthday:
        print("happy birthday, here is a free martini")
elif age >= 18:
    print("you can come in but no drinking!")
    if isbirthday:
        print("happy birthday, here is a free apple juice")
else:
    print("sporry go home kids")