#درس السيت
''''
x={1,5,8,7,9,3,9}
#x.add(99)          #لأضافة رقم >>
#print (sum(x))
#print (len (x))
#x.discard(10)  #للحذف سواء موجود اوغير موجود
#x.remove # للحذف الموجود والغير موجود يطلع خطاء
'''
'''

print (x)
if x == false :
    print ("no ")
'''
'''
x={'Name':'Ali' ,'Age':22 , 'Class':2, 'Hour':4 ,'Term':2,'Yaer':2023,'Weight':90}
for i in x:
    print (i,x [i])
'''

'''
x={}
for i in range(2):
    Key=(input ("Key"))
    Value=(input ("Value"))
    x[Key]=Value
print (x)
'''

'''
x={'Name':'Ali' ,'Age':22 , 'Class':2, 'Hour':4 ,'Term':2,'Yaer':2023,'Weight':90}
#print(x["Yaer"]) #اضهار الفاليو 
#print (x.get("Yaer"))#اضهار الفاليو وان لم تكن موجودة يضهر None
'''
'''
x={'Age':[20,6,10.55,60]}
for i in x:
    print (x[i])
    print (max(x[i]))
    print(min(x[i]))


'''
'''
x={'Name1':['Ali' ,22],'Name2':['Ahmaed' ,40],'Name3':['Asd' ,6],'Name4':['Imad' ,33]}

for i in x:
    print (x[i])

print (max(x))
'''

'''
x={'Name':'Ali' ,'Age':22 , 'Class':2, 'Hour':4 ,'Term':2,'Yaer':2023,'Weight':90}
#x['Age']=60 تضيف او تغير
#x['City']=("Riadah")تضيف او تغير 
x.update({'City':"Ryadah"})#تقدر تضيف اكثر من قيمة
print (x)
'''
'''
x={'Name':'Ali' ,'Age':22 }
print(x.keys())# لطباعة الكي فقط 
print(x.values())#لطباعة الفليو فقط
print(x.items())#لطباعة كامل 
'''
x={'Name':'Ali' ,'Age':22 }
#del x['Age']# لحذف
#x.pop('Age')#لحذف
#x.clear()# لحذف جميع الدكشنري

print (x)