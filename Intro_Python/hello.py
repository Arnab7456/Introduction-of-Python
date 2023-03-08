print("hello")  
# basic implementaion 
age = 20
Name ="Arnab"
print(age)
print(Name)

hero = "arnab"
print(hero)

#check data type 
t1=4.5
t2=45
t3="hello Arnab"
t4=['hello' , 'how are you','bro']
t5 = True
print(t1 , type(t1))
print(t2 , type(t2))
print(t3 , type(t3))
print(t4 , type(t4))
print(t5 , type(t5))

#gfg documents

#Instead of writing this massive Python code
#we can also code this in a different way

#Python code to demonstrate working of iskeyword()

# importing "keyword" for keyword operations
import keyword
import keyword
# initializing strings for testing while putting them in an array
keys = ["for", "while", "tanisha", "break", "sky",
"elif", "assert", "pulkit", "lambda", "else", "sakshar"]

for i in range(len(keys)):
	# checking which are keywords
	if keyword.iskeyword(keys[i]):
		print(keys[i] + " is python keyword")
	else:
		print(keys[i] + " is not a python keyword")
