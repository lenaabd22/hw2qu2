
x = int(input("Enter number: "))
reverse_num = 0 #قيمة اولية

while(x > 0):
    num = x % 10  #لفصل الرقم الاخير من الرقم الكلي نقوم بعمل باقي القسمة للرقم الكلي
    reverse_num = reverse_num * 10 + num  #نضرب الرقم الاخير ب 10 عشان لما نجمعله الرقم الي بعده ينضاف مع الصفر وما تتغير قيمته
    x = x // 10  #لايجاد باقي الرقم الكلي بعد ما طلعنا الرقم الاخير
print("Reverse of the number:",reverse_num)






