n=int(input("sen khod ra vared konid"))
mine = 0
hour = 0
day = 0
if n<0 :
    print("INVALID")
elif n <= 60:
    sec = n
    print( day," days ",hour," hours ",mine, " minutes ",sec," seconds")
elif 60 <= n < 3600:
    mine = n//60
    sec = n%60
    print( day," days ",hour," hours ",mine, " minutes ",sec," seconds")
elif 3600 <= n < 86400:
    hour = n//3600
    mine = (n%3600)//60
    sec = (n%3600)%60
    print( day," days ",hour," hours ",mine, " minutes ",sec," seconds")
else:
    day = n//86400
    hour = (n%86400)//3600
    mine = ((n%86400)%3600)//60
    sec = ((n%86400)%3600)%60
    print( day," days ",hour," hours ",mine, " minutes ",sec," seconds")
