std=[]
for i in range(5):
    grade=int(input("grade: "))
    std.append(grade)
for i in std:
    print(i)
print("AVG= ",(sum(std)/len(std)))
stdpass=[]
stdfail=[]
for i in std:
    if (i>=60):
        stdpass.append(i)
    else:
        stdfail.append(i)
if(len(stdpass)==0):
    print("no pass")
else:
    print("pass: ")
    for i in stdpass:
        print(i)
if(len(stdfail)==0):
    print("no Fail")
else:
    print("fail: ")
    for i in stdfail:
        print(i)
print("SUM= ",(sum(stdfail)))
