
str1=input("Enter your string:")
even_array=[]
odd_array=[]

for i in range(0,len(str1)):
    if i%2 == 0:
        even_array.append(str1[i])
    else:
        odd_array.append(str1[i])

print("Even characters in array",even_array)
print("Odd characters in array",odd_array)





