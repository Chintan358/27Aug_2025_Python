
l = ['a','b','c','d','e']
ap = {}
cont='y'
while cont != 'n':
    print("***************Appoinment Desk****************")
    print("""
        Enter Choice :
        1 : Book appointment
        2 : View appoinment
        3 : Cancel appinment
        4 : Doctor availability
    """)
    choice = int(input("Enter your choice : "))
    if choice ==1:
        print("*****Book Appoinment*****")
        name = input("enter your name : ")
        age = input("Enter your age : ")
        phone = input("enter Phone : ")
        dname = input("Enter doctor name : ")
        slot = input("enter preffred slot [10am,11am,12pm,2pm,3pm] ")
        if dname in l : 
            count=0
            for i,j in ap.items():
                if j.get('dname')==dname and j.get('slot')==slot:
                    count+=1

            if count>=3:
                print("this slot is book. try another slot or doctor")
            else:
                ap.update({phone:{'name':name,'age':age,'phone':phone,'dname':dname,'slot':slot}})
        else :
            print("Invalid doctor name")

    elif choice==2:
        print("*****View appoinment*****")
        for i,j in ap.items():
            print(i)
            for x,y in j.items():
                print(f"{x} : {y}")
    elif choice==3:
        print("*****Cancel Appoinment*****")

    elif choice==4:
        print("****Check Doctor avaialbility******")
        
    else :
        print("Invalid choice")

    cont = (input("Do you wnat to continue? y or no : ")).lower()