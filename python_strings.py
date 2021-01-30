# function len()

a = "Hello World"
print("The word "+a+" contains: "+str(len(a))+" letters")

# multiple string lines
b = """This stuff is not really complex...."""
print(b)
# printing the first character of the long string
print(b[0])

# Looping through a string
for x in "banana":
    print(x)

# check if phrase is in string
txt = "The best anime is bleach!"
if "anime" in txt:
    print("Yes, 'anime' is present")

# check if phrase is NOT in string

text = "my fav. characater from bleach is naruto"
if "ichigo " not in text:
    print("THE ANIME IS CALLED BLEACH NOT NARUTO DUMDASS!")

# slicing strings
phrase = "anime is love <3"
print(phrase[2:5])

# slice string from start
phrase2 = "music is love <3"
print(phrase2[:5])

# slice string to end
phrase3 = "python is fun"
print(phrase3[2:])

# negative indexing
phrase4 = "Hello, World"
print(phrase4[-5:-2])

# upper case
phrase5 = "anime"
print(phrase5.upper())

# lower case
phrase6 = "LOVE"
print(phrase6.lower())

# remove whitespace
phrase7 = "Hello world, I am a program"
print(phrase7.strip())

# replace string
phrase8 = "I hate anime"
print(phrase8.replace("hate", "love"))

# split string
phrase9 = "I am 20 ,years old."
print(phrase9.split(","))

# concat strings
A = "Python"
B = " isn't just a snake..."
C = A + B
print(C)

# formatting strings
age = 20
txt = "My name is YourAverageProgrammer924, I am {}"
print(txt.format(age))
