"""
List data this way in txt file to be converted into a marriage license list:
• groom; groom_address; groom_dad; groom_mom; bride; bride_address; bride_dad; bride mom
• Kevin Allen Kerlish; 1201 E. Second St., Berwick; Michael Kerlish; Cynthia Kerlish; Jenna Elaine Szymaszek; Nanticoke; Michael Smith; Heather Szymaszek
• William Charles Little; 359 Fisher Ave., Catawissa; Charles Little; Jane Little; Danielle Nikole Presto; same; Karen Lou Presto; the late Anthony Howard Presto

Output looks like this:
• Kevin Allen Kerlish, 1201 E. Second St., Berwick, son of Michael Kerlish and Cynthia Kerlish, 
and Jenna Elaine Szymaszek, Nanticoke, daughter of Michael Smith and Heather Szymaszek
• William Charles Little, 359 Fisher Ave., Catawissa, son of Charles and Jane Little, 
and Danielle Nikole Presto, same, daughter of Karen Lou Presto and the late Anthony Howard 
Presto

• list structure
groom, groom_address, groom_dad, groom_mom,
bride, bride_address, bride_dad, bride mom
"""

import re

f = ""
new_list = ""

# Opens source txt file and creates a new txt file.
def file_opener(file_name):
    global f, new_list
    f = open(file_name + ".txt", "r")
    new_list = open(file_name + "_list.txt", "w")

#  Makes list of marriage licenses inside new txt file.	
def list_maker(county_choice):
    global f, new_list
    data = f.readlines()
    cc = county_choice.upper()
    if cc == "C":
        new_list.write("COLUMBIA COUNTY MARRIAGE LICENSES" + "\n")
    elif cc == "M":
        new_list.write("MONTOUR COUNTY MARRIAGE LICENSES"  + "\n")
    for line in data:
        parts = line.split(";")
        new_list.write("• " + parts[0] + "," + parts[1] + ", son of" + parts[2] + " and" + parts[3] + ", and" + parts[4] + "," + parts[5] + ", daughter of" + parts[6] + " and" + parts[7])
    new_list.write("\n")

# Closes source txt file and new txt file.
def file_close():
    f.close()
    new_list.close()

# Asks user for name of source txt file and for the county issuing the marriage licenses.
# Passes user's input into def list_maker.
def ask_user():
    original_list = input("Enter name of txt file to compile. Omit '.txt' extension.")
    county_choice = input("Which county issued these marriage licenses? Columbia or Montour? Please enter C or M.")
    file_opener(original_list)
    list_maker(county_choice)
    file_close()

ask_user()
