#!/usr/bin/env python3

# Priorities
# a - z = 1 - 26
# A - Z = 27 - 52

# Find matching characters in two strings
def find_similarity(string_a, string_b):
    for index_a, character_a in enumerate(string_a):
        for index_b, character_b in enumerate(string_b):
            if character_a == character_b:
                return index_a, index_b, character_a

# Find matching characters in three strings
def find_similarity_three(string_a, string_b, string_c):
    for index_a, character_a in enumerate(string_a):
        for index_b, character_b in enumerate(string_b):
            if character_a == character_b:
                for index_c, character_c in enumerate(string_c):
                    if character_a == character_b == character_c:
                        return index_a, index_b, index_c, character_a

# Get the numerical position for a character
def alphabet_position(text):
    dict = {
        'a':'1','b':'2','c':'3','d':'4','e':'5',
        'f':'6','g':'7','h':'8','i':'9','j':'10',
        'k':'11','l':'12','m':'13','n':'14','o':'15',
        'p':'16','q':'17','r':'18','s':'19','t':'20',
        'u':'21','v':'22','w':'23','x':'24','y':'25',
        'z':'26','A':'27','B':'28','C':'29','D':'30',
        'E':'31','F':'32','G':'33','H':'34','I':'35',
        'J':'36','K':'37','L':'38','M':'39','N':'40',
        'O':'41','P':'42','Q':'43','R':'44','S':'45',
        'T':'46','U':'47','V':'48','W':'49','X':'50',
        'Y':'51','Z':'52',
    }
    for i in text:
        if i in dict:
            value = int(text.replace(i, dict[i]))
    return value

running_total = 0

# Open File
with open('03-rucksack-reorganization - input', 'r') as input:
    for line in input:
        
        line = line.replace('\n','')

        # Split at middle of string
        split_point = int(len(line)/2)
        compartment_one, compartment_two = line[:split_point], line[split_point:]

        matches = find_similarity(compartment_one, compartment_two)

        priority = alphabet_position(matches[2])

        running_total = running_total + priority

print(f"Part 1: {running_total}")

running_total = 0
contains_text = True # Used to know when to stop looping through text file

# Open File
with open('03-rucksack-reorganization - input', 'r') as input:
    while contains_text == True:
        elf_one = input.readline().replace('\n','')
        elf_two = input.readline().replace('\n','')
        elf_three = input.readline().replace('\n','')

        # If empty, stop looping through file
        if elf_one == "" or elf_two == "" or elf_three == "":
            contains_text = False

        matches = find_similarity_three(elf_one, elf_two, elf_three)

        if matches != None:
            priority = alphabet_position(matches[3])
        else:
            priority = 0
        running_total = running_total + priority


print(f"Part 2: {running_total}")


