import os.path
from get_recommendation import get_recommendation
PREF_FILE = 'musicrec-store.txt'
userDictGlobal={}
def loadUsers (fileName) :
    '''Reads in a file of stored users' preferences
    stored in the file
    "fileName'
    Returns a dictionary containing a mapping
    of user names to a list preferred artists
    '''
    if os.path.exists(fileName):
        #print(os.path.exists(fileName))
        file = open(fileName,'r')
        userDict = {}
        for line in file:
            # Read and parse a single line
            [userName, bands] = line.strip().split(':')
            bandList = bands.split(',')
            bandList. sort()
            userDict[userName] = bandList
        file.close ()
    else:
        file=open(fileName,'x') # 'x' is to create the file
        userDict={}
        #print(os.path.exists(fileName))
    userDictGlobal=userDict
    return userDictGlobal
def first_interaction(userDict):
    name=input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):\n")
    if(name in userDict.keys()):
        print("user already exists")
        main_menu(userDict,name)
    else:
        print("new user")
        get_preferences(userDict,name)
def get_preferences(userDict,name):
    x = True
    preference_list = []
    while (x == True):
        preference = input("Enter an artist that you like (Enter to finish):")
        if (len(preference) == 0):
            x = False
            main_menu(userDictGlobal,name)
        else:
            if name in  userDict:
                preference_list = userDict[name]
                preference_list.append(preference.title())
                preference_list.sort()
                #userDict[name] = [userDict[name],preference]
                userDict[name]= preference_list
                userDictGlobal = userDict
                print(userDictGlobal)
            else:
                preference_list.append(preference.title())
                preference_list.sort()
                userDict[name] = preference_list
                #userDict[name] = [userDict[name],preference]
                userDictGlobal=userDict
                print(userDictGlobal)

'''def get_recommendation(userDict,name):
    

    #print(user_preference)'''



def main_menu(userDict,name):
    option=input("Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit\n")
    if option=='e':
        print("option preferences:",userDict)
        get_preferences(userDict,name)

    elif option=='r':
        get_recommendation(userDict,name)
        main_menu(userDict,name)


if __name__=="__main__":
    #get_recommendation()
    user=loadUsers("musicrecplus.txt")
    first_interaction(user)
