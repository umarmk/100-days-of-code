# This is a comment

'''this is
a multi line
comment'''

'''To use interactive python,
select the code block or line
press shift + enter to run in an interactive (jupyter) window'''

name = "Umar"
age = 22

my_string = "random text fr"

my_long_string = '''this is a 
very long string
idk what this means'''

print(my_string, "\n", my_long_string)

full_string = my_string + " " + my_long_string
print(full_string)

is_logged_in = True # Boolean

voting_age = 18
person_age = 21
can_vote = person_age >= voting_age
print(can_vote)

age = 18
has_license = True
drunk = True
can_drive = age >= 18 and has_license and not drunk 
print(can_drive)

score = 10
score = score + 5
score += 5
print(score)

# f strings
name = "Umar"
my_name = f"my name is {name}"
print(my_name)

# string stuff
sentence = "random shi fr"
sentence.upper()
sentence.lower()
sentence.title()
sentence.startswith("r") # Boolean
sentence.endswith("k")
"random" in sentence # Boolean
# find
sentence.find("shi")
sentence.count("r")
# replace
new_sentence = sentence.replace("fr", "bro")
print(new_sentence)

# conditionals
temp = "no"
if type(temp) == int:
    print("HOT")
if type(temp) != int: # bad logic just for vibes
    print("COLD")
else:
    print("write a valid temp")

# loops
for i in range(7):
    print(i)
print(i, i+1)

for k in range(2, 11, 2):
    print(k)

# data structures
list1 = ["you", "me", "us", "we", 1, 2, 3]
print(list1, "------>" ,type(list1))
