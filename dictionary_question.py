

#Question - 1

dict = {"x":10,"y":20,"z":30}
for key,value in dict.items():
    print(f"{key}:{value}")

#Question - 2
n =int(input("Input a Number :"))
d= {}
for x in range(1,n+1):
    d[x]=x**2
print(d)


#Question - 3
dict={}
for x in range(1,15+1):
    dict[x]=x**2
print(dict)


#Question - 4
d={'data1':100,'data2':-54,'data3':247}
data=d.values()
sum=0
for i in data:
    sum=sum+i
print(sum)

#Question - 5
color_dict={'red':'#FF0000','green':'#000000','black':'#000000','white':'#FFFFFF'}
my_keys=list(color_dict.keys())
my_keys.sort()
sorted_dict={i: color_dict[i] for i in my_keys}
print(sorted_dict)

#Question - 6 


