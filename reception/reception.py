
VIP = []
ORDINARY = []


def registration_checker(name1):
    """Function to check for name from guest lists."""
    file1 = open('vip_list.txt', 'r')
    for line in file1:
        VIP.append(line.strip())

    file2 = open('ordinary_list.txt', 'r')
    for line in file2:
        ORDINARY.append(line.strip())

    if name1 == "":
        print ("Please enter a valid name")
    else:
        name = [a for a in VIP if name1.lower() in a.lower()]
        ordin = [a for a in ORDINARY if name1.lower() in a.lower()]

        if name:
            print (name[0] + " is on VIP")
        elif ord:
            print (ordin[0] + " is on ordinary")
        else:
            print (name1 +" is not on the list")

name2 = ""
while name2 != '0':
    name2 = input("Enter name and 0 to quit: ")
    registration_checker(name2.strip())



