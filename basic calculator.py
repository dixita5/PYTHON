def add(num1, num2): 
    print("RESULT: ", num1 + num2) 
  
# Function to subtract two numbers  
def subtract(num1, num2): 
    print("RESULT: ", num1 - num2) 
  
# Function to multiply two numbers 
def multiply(num1, num2): 
    print("RESULT: ", num1 * num2) 
  
# Function to divide two numbers 
def divide(num1, num2): 
    print("RESULT: ",num1 / num2) 
  
print("         BASIC CALCULATOR     ")
print("  1. Addition \n" \
      "  2. Subtraction \n" \
      "  3. Multiply \n" \
      "  4. Divide \n")
  
# Take input from the user  
ch = input("Select the choice: ") 
  
number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 
  
if ch == '1':  
    add(number_1, number_2) 
  
elif ch == '2': 
    subtract(number_1, number_2) 
  
elif ch == '3': 
    multiply(number_1, number_2) 
  
elif ch == '4': 
    divide(number_1, number_2)
else: 
    print("ENTER THE CORRECT OPTION") 
