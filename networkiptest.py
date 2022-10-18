import re

network1 = 'test'
network2 = '172.169.0.25'
network3 = '192.168.1.25'
netmask = '255.255.255.0'

network4 = ['192.168']
network5 = ['192.168.1']

testdict = {network1: [["abc"],["abcd"]],
network2: ["def"],
network3: ["ihg"]}

testing = [['179.32', 150, False, [1, 3], "UNK"],['190.34', 100, True, [3, 4], "EGP"], ['100.34', 150, True, [1,2], 'EGP' ], ['129.32', 151, True, [1,2], "IGP"]]

#get a list passed in through parameters

def testbestpath(list1):
    returnlist = []
    currenthighest = list1[0][1]
    for entry in list1:
        if(entry[1] > currenthighest):
            returnlist.clear()
            returnlist.append(entry)
            currenthighest = entry[1]
        elif(entry[1] == currenthighest):
            returnlist.append(entry)
              
    print(returnlist)         

def testbestorg(list1):
    returnlist = []
    for entry in list1:
        if(entry[2] == True):
            returnlist.append(entry)


    print(returnlist)

def testshortestASPath(list1):
    #figure out how as path works
    returnlist = []   

def bestorigin(list1):
    returnlist = []
    lowestpref = 'UNK'
    for entry in list1:
        if(lowestpref == 'UNK'):
            if(entry[4] == 'UNK'):
                returnlist.append(entry)
            else:
                returnlist.clear()
                returnlist.append(entry)
                lowestpref = entry[4]
        elif(lowestpref =='EGP'):
            if(entry[4] == 'EGP'):
                returnlist.append(entry)
            elif(entry[4] == 'IGP'):
                returnlist.clear()
                returnlist.append(entry)
                lowestpref = 'IGP'

        elif(lowestpref =='IGP'):
            if(entry[4] == 'IGP'):
                returnlist.append(entry)   

#this seems like a really stupid approach                        
def determinelowestip(list1):
    returnlist = []
    currentlowest = list1[0][0]
    currentlowest = ''.join(currentlowest.split('.'))
    for entry in list1:
        value = entry[0]
        amt = ''.join(value.split('.'))
        if(amt <= currentlowest):
            print(amt)
            returnlist.clear()
            returnlist.append(entry)
            currentlowest = amt
            
    print(returnlist)


determinelowestip(testing)

testdict1 = {}

testdict2 = [{"test1": 1234}, {'test2': 5678}]
testdict3 = [{"test3": 12345}]
value = testdict3[0].keys()
print(value)
potentialmatches = []

#will return just the singular value of list


for i in testdict2:
    for x in i:
        potentialmatches.append(x)
        print("does this work " + x)

#for elem in list:
#do something to figure out what is the best match

print(potentialmatches)
#find the best prefix on those, and then mutate the list

testdict1.setdefault(network1, [])
testdict1[network1].append(network4)
#print(testdict1.get("contains"))
#testdict1[network1].append(network5)

match = []
for x in testdict1:
    if(x.startswith('tes')):
        value = testdict1.get(x)
        entryandvalue = {x: value}
        match.append(entryandvalue)

match.append({network2: network4})
print(match)
print(len(match))

testdict[network1] = network4
testdict[network1] = network5

print(testdict)
print(testdict1)

for x in testdict:
    print(x)


#used for converting given networks into correct prefixes for correct parsing afterwards
def converter(network):
    test = []
    pattern = re.compile(r'255')
    matches = pattern.findall(netmask)
    network = network.split(".")

    for i in range(len(matches)):
        test.append(network[i])

    test = '.'.join(test)

    print(test)

converter(network3)

#iterate through and add item to list
#immediately check if there no items in the list -> if so then send out no route message
#else
#call the method that created to iterate through the list of dictionaries, and then print out the values
#then given those values if the list is larger than 1, find the best route, then return that value
#if the list is = to 1, return that

#that should get us the available path to the network

#*acutally fuck that don't even need to do this since i am returning a sinular path, 
# can just return that path an add it to a separte list*

#the actual hard part








