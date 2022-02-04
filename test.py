"""
a="HEMANTH";
for i in range(11) :
	print(a);

i="HEMANTH";
j=0
while (j<=10):
	print(i);
	j=j+1;

a=int(input("Enter a numer1:"))
b=int(input("Enter a numer2:"))
for i in range (10):
 if (a>b):
  print("true,,The First Number is Greater")
 else:
  print("false,,The First number is less")


a=["Hemanth",170135,"Rajesh",170134]
for i in a:
	print(i);

a=("Hemanth",170135,"Rajesh",170134)
print(type(a));
print(a);
a=list(a)
a.append("akash")
print(a);
a=tuple(a)
print(a);

a="HEMANTH"
b=7
c="o170135"
print("This Is a value A={0},B={2},C={1}".format(a,b,c));
a=list(input("Enter A number:"))
print(a[::-1]);

n =int(input("ENTER NO.OF SUBJECTS:"))
cgpa = []
credits = []
result=0
credit=0
for i in range(n):
	cgpa.append(int(input("subject {} cgpa = ".format(i+1))))
	credits.append(int(input("subject {} credits = ".format(i+1))))

	result=result+(cgpa[i]*credits[i])
	credit=credits[i]+credit
final=result/credit
print(final);
"""
# ADD TWO NUMBERS
"""
first_num = int(input("GIVE THE FIRST  NUM == "))
second_num = int(input("GIVE THE SECOND NUM == "))
sum = first_num + second_num
print("THE SUM IS {}".format(sum))
"""
"""
# Check Prime Number
num = int(input("GIVE THE NUMBER TO CHECK THE NUMBER PRIME OR NOT: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print("{} Is not Prime Number".format(num))
else:
    print("{} Is A Prime Number".format(num))


# Check prime number without flag
num = int(input("Number:  "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("{} Number is not prime".format(num))
            break
    else:
        print("{} Number is prime".format(num))
else:
    print("{} Number is not prime".format(num))
"""
n = int(input("NUMBER FOR Factorial== "))
factorial = 1
if n < 0:
    print("FACTORIAL DOESNT EXIST")
elif n == 0:
    print("FACTORIAL IS 1")
else:
    for i in range(1, n+1):
        factorial = (factorial*i)
    print("Factorial is {}".format(factorial))
