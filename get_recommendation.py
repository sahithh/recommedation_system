def get_recommendation(userDict,name):
    user_preference = userDict[name]
    #print(user_preference)
    scoring(userDict,user_preference,name)

def scoring(userDict,user_preference,name):
    i=0
    j=0
    length= len(user_preference)-1
    score={}
    for user in userDict.keys():
        if not ('$' in user) and not (name in user) :
            score[user]=0
    #print(score)
    for user in userDict.keys():
        while length>=0:
            if(user_preference[length] in userDict[user]):
                #print(userDict[user])
                if not (name in user) and not ('$' in user):
                    score[user]= score[user]+1
                    length=length-1
                else:
                    length=length-1
            else:
                length=length-1
        length=len(user_preference)-1
    #print(score)
    best_user(score,userDict,user_preference,name)

def best_user(score,userDict,user_preference,name):
    userlist=list(score.keys())
    length_userlist=len(userlist)-1
    suggested_user=""
    high_score =0
    userName=userlist[length_userlist]
    #print(userName)
    #high_score = score[userName]
    '''if len(list(userDict[userName])) > score[userName]:
        high_score = score[userName]
        suggested_user = userName'''
    while length_userlist>=0:
        userName=userlist[length_userlist]
        if high_score < score[userName]:
            y=high_score
            high_score=score[userName]
            if len(list(userDict[userName])) > high_score:
                suggested_user = userName
            else:
                high_score=y
            length_userlist=length_userlist-1
        elif high_score==score[userName]:
            #print("decision made here ")
            if len(suggested_user)!=0:
                if len(list(userDict[userName])) > len(list(userDict[suggested_user])):
                    suggested_user= userName
                length_userlist=length_userlist-1
            else:
                length_userlist = length_userlist - 1
        else:
            length_userlist=length_userlist-1
    if len(suggested_user)==0:
        print("No recommendations available at this time.")
    else:
        drop_common_artist(list(userDict[suggested_user]),user_preference,name)
        #print("suggested:", userDict[suggested_user])

def drop_common_artist(suggested_user_preferences,user_preference,name):
    for i in user_preference:
        if i in suggested_user_preferences:
            suggested_user_preferences.remove(i)
    print("recommended artist are:")
    for i in suggested_user_preferences:
        print(i)








