#Dalton Abbott
#file name: Module_2_lab
#this code will ask for students names and gpas, then tell if they made the honor roll or deans list

honor = 3.25 #minimum gpa for honor roll
dean = 3.5 #minimum gpa for deans list
while True:
    stu_lname = input("plese enter students last name(Enter 'ZZZ' if you wish to exit): ")
    
    if stu_lname == 'ZZZ':
        break #ends program when ZZZ entered

    stu_name = input("Plese enter students first name: ")
    gpa = float(input("pleasse enter studetns GPA: ")) #takes gpa from string and makes it a float 
    if gpa < 3.25:
        print (stu_name + ' ' + stu_lname + ' did not qualify for honor roll or the deans list.') #makes program break proof 
    elif gpa >= honor and gpa < dean:
        print (stu_name + ' ' + stu_lname + ' qualified for honor roll only.') # makes sure gpa is enough to make honor roll, but no too high to mess with deans list calculations
    else:
        print (stu_name + ' ' + stu_lname + ' qualified for honor roll and the deans list') #only option left with previous rules implemented
        
