# with open("abc.txt" , "r") as f :
#     data = f.readlines(2)
#     data2 = f.tell()
#     print(data)
    
    
# data = "all students are stupid"
# f = open("abc2.txt", "w")
# f.write(data)
# with open("abc2.txt" , "r+") as f:
#    text = f.read()
#    print(text)
#    print("the current  cursor POsition: ", f.tell())
#    f.seek(17)
#    print("The Current Curson Position : ", f.tell())
#    f.write("GEMS")
#    f.seek(0)
#    text = f.read()
#    print("Data after Modification: ")
#    print(text)
    
    
# import csv
# with open("emp.csv", "w", newline='') as f :
#     w = csv.writer(f)
#     w.writerow(["empId", "EMPName", "EMP_STATUS"])
#     n = int(input("Enter Number of Employees : "))
#     for i in range(n):
#         eno = input("EMP ID : ")
#         empstatus = input("Enter employee status : ")
#         emp_name = input("Employee Name :")
#         w.writerow([eno, emp_name, empstatus]) 
# print("Total Employee data writen in csv file successfully : ")


