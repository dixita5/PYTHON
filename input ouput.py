num=int(input("Enter the number: "))
num

name=str(input("Enter your Name: " ))
name

n1=type(num)
n1

n2=type(name)
n2

#Whatever you enter as input, input function convert it into a string. if you enter an integer value still input() function convert it into a string. You need to explicitly convert it into an integer in your code using typecasting.
num2=input("Enter the Number: ")
n2=type(num2)
n2

x,y=input("Enter a two value: ").split()
print("X: ",x)
print("Y: ",y)
print()

x,y,z=input("Enter a two value: ").split()
print("X: ",x)
print("Y: ",y)
print("Z: ",z)
print()

a,b=input("Enter two number: ").split()
print("First number is {} and second number is {}".format(a,b))
print()


#taking multiple inputs
x=list(map(str,input("Enter a multiple value: ").split()))
print("List of students: ",x)
type(x)


x,y=[int(x) for x in input("Enter two values: ").split()]
print("First number: ",x)
print("second number: ",y)


x,y,z=[int(x) for x in input("Enter three values: ").split()]
print("First number: ",x)
print("second number: ",y)
print("Third number: ",z)

#taking multiple inputs
x, y ,z= [int(x) for x in input("Enter three values: ").split()] 
print("First number is {} and second number is {} and the third number is {}".format(x, y, z)) 
print() 


x=[int(x) for x in input("Enter multiple value: ").split()]
print("List contains: ",x)


#separated by comma(,)
x=[int(x) for x in input("Enter multiple values: ").split(",")]
print("List contains: ",x)