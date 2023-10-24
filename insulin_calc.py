
mystring = input("Enter your insulin sequence :  ")
a = mystring
number1 = input("Which character number is your first character of insulin sequence ? : ")
number2 = input("Which character number is your last character of insulin sequence ? : ")
number3 = input("Which character number is your first character of binsulin sequence ? : ")
number4 = input("Which character number is your last character of binsulin sequence ? : ")
number5 = input("Which character number is your first character of cinsulin sequence ? : ")
number6 = input("Which character number is your last character of cinsulin sequence ? : ")
number7 = input("Which character number is your first character of ainsulin sequence ? : ")
number8 = input("Which character number is your last character of ainsulin sequence ? : ")
number1 = int(number1)-1
number3 = int(number3)-1
number5 = int(number5)-1
number7 = int(number7)-1
print("Your string is : ",a)
print("lsinsulin-seq-clean is : ",a[int(number1):int(number2)])
print("binsulin-seq-clean is : ",a[int(number3):int(number4)])
print("cinsulin-seq-clean is : ",a[int(number5):int(number6)])
print("ainsulin-seq-clean is : ",a[int(number7):int(number8)])