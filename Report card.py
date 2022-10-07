
N1 = input("Student name ")
R1 = input("input roll no")
M1 = input("Maths marks")
M2 = input("Science marks")
M3 = input("Computer Science marks")
Q1 = input("would you like to see the report?")
perc = ( (int(M1) + int(M2) + int(M3) )/3)
add = ( int(M1) + int(M2) + int(M3))
if Q1 == "y":
    print("***STUDENTS REPORT CARD***")
    print( N1)
    print("Roll Number:" + R1)
    print("Maths marks:" + M1 )
    print("Science marks:" + M2)
    print("Csc Marks:" + M3)
    print("Total marks")
    print( add)
    print("Total Percentage is" )
    print( perc)
    print("Thank you")
else:
    print("Thank you")
    exit()




    






