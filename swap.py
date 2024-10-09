#Swapping two numbers without using third variable
print("A program to swap two numbers without using third variable")
a,b = 10,20
print("Initial value  a >> ",a)
print("Initial value  b >> ",b)
a,b = b,a
print("Swapped value of a>> ",a)
print("Swapped value of b>> ",b)

#Swapping two numbers by using third variable
print("A program to swap two numbers by using third variable")
a,b = 10,20
c=a
a=b
b=c
print("SWapped value of a>>",a)
print("Swapped value of b>> ",b)