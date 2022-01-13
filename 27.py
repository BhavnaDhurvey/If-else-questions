
age=int(input("enter age"))
sex=input("enter sex")
if  sex=="female":
    print("urban areas") 
elif sex=="male":
    if age >=20 and age<=40:
        print("anywhere")
    elif age>=40 and age<=60:
        print("urban areas")
    else:
        print("error")
else:
    print("no idea")