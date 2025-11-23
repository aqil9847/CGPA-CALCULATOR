def Calculate(grade, credit):
    
    tgrade = 0
    tcredit = 0
    l=len(grade)

    for i in range(0,l):
        tgrade += grade[i] * credit[i]
        tcredit += credit[i]

    if tcredit == 0:
        return 0.0
    else:
        return tgrade / tcredit

c='y'
while c=='y':
    print("---------------------------------------------------------")
    print("GGPA CALCULATOR")
    print("---------------------------------------------------------")
    n=int(input("Enter the number of grades and credits: "))
    print("---------------------------------------------------------")
    g=[]
    c=[]
    for i in range(0,n):
        a=float(input("Enter the grade mark: "))
        b=int(input("Enter the credit for the above grade: "))
        g.append(a)
        c.append(b)

    print("----------------------------------------------------------")
    print("Grade: ",g)
    print("Credits: ",c)
    print("Total Credits: ",sum(c))
    cgpa = Calculate(g,c)
    print(f"The CGPA is: ",cgpa)
    print("-----------------------------------------------------------")
    c=input("Do you wish to calculate any more CGPA(y/n): ")
    if c=='n':
        print("-----------------------------------------------------------")
        print("THANK YOU")
        print("-----------------------------------------------------------")
