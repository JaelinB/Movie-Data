################################################################################
#    Computer Project #8
#
#    Program that takes in user input to print out the necessary n\
#    information based ont he input that is given
#
#    The first part of the program displays the menu options for the user
#
#    Next is the open_file fuction that opens the file based on the user input
#
#    The next function reads through the names.txt file and adds the \n
#    the names to a list
#
#    Moving on, the read_friends funciton goes through the friends.csv file \n
#    and adds the friends of the names to a list
#
#    After that, a dictionary is made that has all the friends of the names
# 
#    The next function finds the common friends from the names list
# 
#    Moving on, the find_max_friends function determines who has the most \n
#    friends and the amount of friends they have
# 
#    Similarly, the next function finds the max amount of common friends
# 
#    Next, the second friends function is made to determine all the second \n
#    friends
# 
#    Finally, the last function finds the max amount of second friends
# 
#    After all the functions are written, the main displays infromation \n
#    based on the file and option that the user input
# 
#    Error messages are printed for invalid options, files, and names. \n
#    a reprompt is followed          
#################################################################################

import csv
from re import I
MENU = '''
 Menu : 
    1: Popular people (with the most friends). 
    2: Non-friends with the most friends in common.
    3: People with the most second-order friends. 
    4: Input member name, to print the friends  
    5: Quit                       '''
# Menu Options

# Opens the file based on the input. Prints and error of file is \n
# invalid + reprompt 
def open_file(s):
    file_input= input(f"\nInput a {s} file: ")

    x = 0
    while x == 0: 
        try:
            file_pointer = open(file_input)
            break
        except: 
            print("\nError in opening file.")
            file_input = input("Enter file name: ")

    return file_pointer

# Returns the file opened by the user input


# Reads through the names.txt file and appends the names to an empty list
def read_names(fp):
    list_of_names =[]

    for each_line in fp:
        name = each_line.strip()
        list_of_names.append(name)
    return list_of_names
# Returns the list of all the names in names.txt
    

# Reads through the Friends.csv file to find the friends  of the Names.txt \n
# file  
def read_friends(fp,names_lst):
    reader = csv.reader(fp)
    list_of_friends = []

    for each_line in reader:
        list_of_friends.append(each_line)


    for line in list_of_friends:
        current_length = len(line)
        i = 0
        while i < current_length:
            try:
                namePos = int(line[i])
                name = names_lst[namePos]
                line[i] = name
                i+= 1
            except:
                line.pop(i)
                i+=1
    return list_of_friends

# Returns the list of friends for each name as strings

# Creates a dictionary with what is returned by read_names and read_friends
def create_friends_dict(names_lst,friends_lst):

    friends_dict = {}
    for i in range(len(names_lst)):
        friends_dict[names_lst[i]] = friends_lst[i]

    return friends_dict

# Returns a dictionary of the names and friends


# Finds the friends that the names have in common            
def find_common_friends(name1, name2, friends_dict):
    
    first_n = set(friends_dict[name1]) - set(name2)
    sec_n = set(friends_dict[name2]) - set(name1)

    com_f = first_n & sec_n

    return com_f
# Returns the common friends that each name has

# Determines who has the max amount of friends from the names list and \n
#  friends list
def find_max_friends(names_lst, friends_lst):
   
    num_friends = []
   
    for friend in friends_lst:
        num_friends.append(len(friend))
    
    max_find = max(num_friends)

    max_names = []
    for i in range(len(num_friends)):
        if num_friends[i] == max_find:
            max_names.append(names_lst[i])

    return sorted(max_names),max_find

# Returns the name of the person with the most friends and the numebr of \n
# friends they have 

# Finds which pair of people have the most frineds in commonfrom the \n
# friends dictionary
def find_max_common_friends(friends_dict):

    pair_dict = {}
    for name, val in friends_dict.items(): 
        for name2, val2 in friends_dict.items():
            if name == name2:
                continue

            if name in val2 or name2 in val:
                continue
            reversed_pair = (name2,name)
            if reversed_pair in pair_dict:
                continue

            common = find_common_friends(name,name2,friends_dict)

            pair_dict[name,name2] = common

    max_val = 0
    max_pair_list = []

    for pair,lst in pair_dict.items():
        # check if need to update max_val 
        if len(lst) > max_val:
            max_pair_list.clear()
            max_val = len(lst)
            max_pair_list.append(pair)

        elif len(lst) == max_val:
            max_pair_list.append(pair)
        
    max_pair_list.sort()

    return max_pair_list, max_val

# Returns the list of the max common friends and the max number of common \n
# friends 



# Finds the friends of friends from the friends dicitonary         
def find_second_friends(friends_dict):
    
    friends_of_friends = {}
    for name, val in friends_dict.items():
        second_friend = set()
        for friends in val:
            pos_sec_f = set(friends_dict[friends]) - set(friends_dict[name])

            second_friend = pos_sec_f | second_friend

        second_friend.discard(name)

        friends_of_friends[name] = second_friend
    
    return friends_of_friends

# Returns the second friends as a dictionary 

# Finds the max amount of second friends 
def find_max_second_friends(seconds_dict):
    num_friend = []
   
    for friend,val in seconds_dict.items():
        num_friend.append(len(val))
    
    max_find = max(num_friend)

    max_name = []
    for len_f,val in seconds_dict.items():
        if len(val) == max_find:
            max_name.append(len_f)

    return max_name,max_find

# Returns the names of the max second friends as a list and the number \n
# of max second friends as an int
def main():
    print("\nFriend Network\n")
    fp = open_file("names")
    names_lst = read_names(fp)
    fp = open_file("friends")
    friends_lst = read_friends(fp,names_lst)
    friends_dict = create_friends_dict(names_lst,friends_lst)
    
# Files opened and read through
    print(MENU)
    choice = input("\nChoose an option: ")
    while choice not in "12345":
        print("Error in choice. Try again.")
        choice = input("Choose an option: ")
        
    while choice != '5':

        if choice == "1":
            max_friends, max_val = find_max_friends(names_lst, friends_lst)
            print("\nThe maximum number of friends:", max_val)
            print("People with most friends:")
            for name in max_friends:
                print(name)
                
        elif choice == "2":
            max_names, max_val = find_max_common_friends(friends_dict)
            print("\nThe maximum number of commmon friends:", max_val)
            print("Pairs of non-friends with the most friends in common:")
            for name in max_names:
                print(name)
                
        elif choice == "3":
            seconds_dict = find_second_friends(friends_dict)
            max_seconds, max_val = find_max_second_friends(seconds_dict)
            print("\nThe maximum number of second-order friends:", max_val)
            print("People with the most second_order friends:")
            for name in max_seconds:
                print(name)

# Prints the names friends. If the name is not valid, the program will \n
# reprompt until valid    
        elif choice == "4":
            x = 0
            while x == 0:
                name_in = input("\nEnter a name: ")
                if name_in in names_lst:
                    print(f"\nFriends of {name_in}:")
                    f = friends_dict[name_in] 
                    for friends in f:
                        print(friends)
                    break
            
                else:
                    print(f"\nThe name {name_in} is not in the list.")
        else: 
            print("Shouldn't get here.")
            
        choice = input("\nChoose an option: ")
        while choice not in "12345":
            print("Error in choice. Try again.")
            choice = input("Choose an option: ")

if __name__ == "__main__":
    main()
