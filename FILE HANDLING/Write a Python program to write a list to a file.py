list=['my','name','is','mohd','ahsan']
a=open("apple.txt","w+")
for i in list:
    a.write("%s\n" %i)
f=a.close()
print(f)
b=open("apple.txt")
print(b.read())