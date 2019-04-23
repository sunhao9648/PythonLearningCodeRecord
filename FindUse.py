s = "1w335ty65452dlqfs"
s1 = "5"
print(s.find(s1))
sum = s.find(s1)
print(s.find(s1,sum+1))

a1 = "abcde"
a2 = ""
a3 = "祝你生日快乐"
print(a1.isalpha())
print(a2.isalpha())
print(a3.isalpha())

b1 = "QAW"
b2 = "qwd"
print(b1.islower())
print(b2.islower())
print(b1.isupper())
print(b2.isupper())
print(b1.format(b2))
print("this is {}'s personal code execise".format("sunhao"))

hash = {"name":"sunhao","hobby":"coding"}
print ("{name} like {hobby}".format(**hash))

print ("右对齐:","{0:->8}".format(2))
print ("左对齐:","{0:-<8}".format(2))
print ("中对齐:","{0:-^8}".format(2))
