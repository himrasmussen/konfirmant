'''
Because this is easier for the user than doing everything by hand.
'''

'''
Needs:
To take input from user.
Write input to template
Command for correcting previous input
Print current country info
'''

'''
Commands:
Write name of country
---- Done: Exits the script

take_input
---- Break: Go to next category; If last category: Go to new country.
'''

#Warning - Typos can't be fixed. Goto the textfile and fix it there.

import sys
import os
import shutil

def take_input(category):
    global cur_category_list, break_val
    value = input("Enter new '{}' entry. Press 'ENTER' exit.\n".format(category))
    if value == '':
        break_val = True
    else:
        cur_category_list.append(value)


input_categories = [
                "Norwegian name for country",
                "English name for country",
                "Abbreviation",
                "Norwegian name for nationality",
                "English name for nationality",
                "Boy names",
                "Girl names",
                "Surnames",
                "Birthplaces"
]

break_val = False
cur_category_list = []
while True:
    country = input("Write name of country. Press 'ENTER' to quit.\n")
    if country == '':
        break

    path = os.path.join("country_data", "{}.txt".format(country))
    with open(path, "a") as f:
        for category in input_categories:
            f.write("{}:".format(category))
            cur_category_list = []
            if category in ["Boy names", "Girl names", "Surnames", "Birthplaces"]:
                while True:
                    take_input(category)
                    if break_val:
                        break_val = False
                        break
            else:
                take_input(category)
            f.write(','.join(cur_category_list) + "\n")
            cur_category_list = []
        print("Moving to next country.\n")
print("\nDone with creating country data. :)")
