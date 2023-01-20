import pandas as pd
def buddyPairing(fileName):
    dictionaryForm = {}
    nameList = []
    finalGroups: list = [] 
    randomGroup = []
    excel_file_path = fileName
    excel_records = pd.read_excel(excel_file_path)
    df = pd.DataFrame(excel_records)

# assessing compatability of users based on elements in common
    def comparing1(List1, List2):
        score = 0
        if List1[2] == List2[2]:
            score += 1
        if List1[3] == List2[3]:
            score += 1
        if List1[4] == List2[4]:
            score += 1
        for timeIndx in range(0,10):
            if len(List1[1])-1 >= timeIndx:
                for dateIndx in range(0,10):
                    if len(List1[0])-1 >= dateIndx:
                        if List1[1][timeIndx] in List2[1] and List1[0][dateIndx] in List2[0]:
                            score += 1
        if score > 2: 
            return True
        else:
            return False
# double check to make sure all users have been included in the pairings
    def check():
        missing = []
        for indx in df.index:
            status = False
            for i in range(0, len(finalGroups)):
                if df['Email'][indx] in finalGroups[i]:
                    status = True
            if status == False:
                missing.append(df['Email'][indx])
        if missing:
            return missing
        return True
# creating a dictionary of all users and their respective elements as well as a list of the names/emails that correspond
    for indx in df.index:
        dictionaryForm[df['Email'][indx]] = [df['Date'][indx].split(',')],df['Time'][indx].split(','),df['Level'][indx],df['Interest'][indx], df['Experience'][indx]
        nameList.append(df['Email'][indx])
    groupNum = 0
# creating pairs by using ratings from comparing1() and saving them in a list, users without viable 'buddies' will be moved to a randomGroup 
    while len(nameList) > 0:
        indx = 0
        finalGroups.append([nameList[indx]])
        for secIndx in range(1, len(nameList)):
            if comparing1(dictionaryForm[nameList[indx]], dictionaryForm[nameList[secIndx]]) == True:
                finalGroups[groupNum].append(nameList[secIndx])
            if len(finalGroups[indx]) >= 2:
                break
        for remv in range(len(finalGroups[groupNum])):
            nameList.remove(finalGroups[groupNum][remv])
        if len(finalGroups[groupNum]) == 1:
            randomGroup.append(finalGroups[groupNum][0])
            del finalGroups[groupNum]
            groupNum -= 1
        groupNum += 1
# users in randomGroup will be separated into pairs until the list is empty, if the number of users in randomGroup is odd, one group will be assigned three users
    if len(randomGroup)%2 == 0:
        for name in range(0,len(randomGroup)-1,2):
            finalGroups.append([randomGroup[name],randomGroup[name+1]])
            groupNum += 1
    else:
        finalGroups.append([randomGroup[0],randomGroup[1], randomGroup[2]])
        groupNum += 1
        for name in range(3,len(randomGroup)-1,2):
            finalGroups.append([randomGroup[name],randomGroup[name+1]])
            groupNum += 1
# before returning the final list of buddies, check() is called to ensure that all users have been sorted into a buddy group
    if check() == True:
        return finalGroups
    else:
        print(check(), " is missing")