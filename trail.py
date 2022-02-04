#From Starting

print("Hlo world")

#Python indentation means spaces

if 5 > 2:
    print ("TRUE")
else:
    print ("False")

#python variables

x=10
print (x)

#python user variable

y=int(input ("Give a number i will print it for you :"));
print (y)

z= input("give me a word i'll print it for you:");
print (z)

#Getting Datatype 

x=input("know DT:");
print(type(x))

#looping in str

for x in "hemanth":
	print(x)

#seraching in sentence:

h= "hi friends this is python"
print("hi" in h)

#Functions

def sum(x,y):
	print(x+y)
sum(2,3)


def my_function(**kid):
  print("His last name is " + kid["lname"])
  print("His first  name is " + kid["fname"])

my_function(fname = input("first name:"), lname =input('last name'))


