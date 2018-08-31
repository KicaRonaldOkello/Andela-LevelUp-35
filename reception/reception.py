
vip = []
ordinary = []


def registration_checker(name1):
    file1 = open('vip_list.txt', 'r')
    for line in file1:
        vip.append(line.strip())

    file2 = open('ordinary_list.txt', 'r')
    for line in file2:
        ordinary.append(line.strip())

    if name1 == "":
        print ("Please enter a valid name")
    else:
        name = [a for a in vip if name1.lower() in a.lower()]
        ord = [a for a in ordinary if name1.lower() in a.lower()]
    
        if name:
            print (name[0] + " is on VIP")
        elif ord:
            print (ord[0] + " is on ordinary")
        else:
            print (name1 +" is not on the list")

name2 = ""
while name2 != '0':
    name2 = input("Enter name and 0 to quit: ")
    registration_checker(name2.strip())



