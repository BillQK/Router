import re

network1 = '11.0.0.25'
network2 = '172.169.0.25'
network3 = '192.168.1.25'
netmask = '255.255.255.0'
network4 = 'test'
network5 = 'testing'

testdict = {network1: ["abc"],
network2: ["def"],
network3: ["ihg"]}

testdict1 = {'192.168.12.2': {'network': '192.168.12.0', 'netmask': '255.255.255.0'}, 
'192.168.0.1' : {'network' : '192.168.0.0' ,'netmask': '255.255.0.0' },
'192.0.0.2' : {'network' : '192.0.0.2', 'netmask': '255.0.0.0'}}

#actually don't have bitwise logic for these entries so it falsely says that there is no route when there should be...


testdict3 = [{'network': '192.168.0.0', 'netmask': '255.255.255.0'},
            {'network': '192.168.1.0', 'netmask': '255.255.255.0'}]

test = {'network': '192.168.0.0', 'netmask': '255.255.255.0'}
          

testlist = [{'network': '192.168.0.0', 'netmask': '255.255.255.0', 'src': '192.168.0.2'},
             {'network': '192.168.1.0', 'netmask': '255.255.255.0', 'src': '192.168.0.2'},
             {'network': '192.168.2.0', 'netmask': '255.255.255.0', 'src': '192.168.0.2'},
             {'network': '192.168.3.0', 'netmask': '255.255.255.0', 'src': '192.168.0.2'}, 
             {'network': '172.169.0.0', 'netmask': '255.255.0.0', 'src': '172.168.0.2'}]


#have a list of annoucements
#so after we recieve a withdraw messsage that does not match a current entry in the list
#clear out all of our entries
#then with each entry in our list of announcements
#if update:
#add back to the array like normal, then aggregate with each update
#then check after we aggregated if we have created a matching revoked entry/have it
#if so then remove it
#if withdraw:
#store within a list of revoked paths, and don't add it back to our path

def binaryrepresentation(decimal):
    nsplit = decimal.split(".")
    binary = []
    for i in nsplit:
        binary.append((bin(int(i)).replace('0b',"")).zfill(8)) 

    num = "".join(binary)
    return num    

def groupip(bstr):
    N = 8
    sublist = [bstr[n:n+ N] for n in range(0, len(bstr), N)]
    list2 = []
    for i in sublist:
        val = int(i,2)
        list2.append(str(val))

    value = ".".join(list2)
    return value

def findnetmask(netmask):
    count = 0
    num = binaryrepresentation(netmask)
    for i in num:
        if i == '1':
            count += 1

    return count

def bprefix(network, netmask):
    num = binaryrepresentation(network)  
    counter = findnetmask(netmask)   
    retstr = ""
    for elem in range(counter):
        retstr += (num[elem])
    
    return retstr    

def determineadj(elem1, elem2):
    binaryelem1 = bprefix(elem1['network'], elem1['netmask'])
    binaryelem2 = bprefix(elem2['network'], elem2['netmask'])
    if(binaryelem1 == ""):
         binaryelem1 = '0'

    test = bin(int(binaryelem1, 2) + 1).replace('0b',"")
    if(test == binaryelem2):
        return True

def checkattributes(elem1, elem2):
    #this should be pretty straighforward and statements
    return True        

def decreasebits(netmask):
    num = binaryrepresentation(netmask)   
    str2 = list(num)
    netmaskcount = findnetmask(netmask)   
    str2[netmaskcount - 1] = '0'
    str2 = "".join(str2) 
    netmask = groupip(str2)       

    return netmask   

#this aggregates one at a time, it wouldn't update when one aggregation leads to another.
def testaggregation(self, loE):
    aggentry = None
    nexthop = None
    for k in loE:
        for v in loE:
            if(determineadj(k,v)):
                if(k['src'] == v['src']):
                    if(checkattributes(k,v)):
                        #maybe do this, not sure if it ruins the structure, but it should go one at a time...
                        aggentry = k
                        nexthop = v
                        k['netmask'] = decreasebits(k['netmask'])                 

    loE.remove(nexthop)
    newentry = {"network" : aggentry["network"],
    "netmask": decreasebits(aggentry["netmask"]),
    "localpref" : aggentry["localpref"],
    "ASPath" : aggentry["ASPath"],
    "origin" : aggentry["origin"],
    "selfOrigin" : aggentry["selfOrigin"],
    }
    loE.remove(aggentry)
    loE.append(newentry)                    


#testaggregation(testlist)


#probably the most convoluted way to generate the prefix of a string...
def convertbinary(network, netmask):
    nsplit = network.split('.')
    binary = []
    for i in nsplit:
        binary.append((bin(int(i)).replace('0b',"")).zfill(8))

    res = "".join(binary)
    resstring = ""
    for x in range(netmask):
        resstring += (res[x])

    return resstring    

    #amt = 32 - netmask    
    #for n in range(amt):
    #    resstring+= "0"

    #resstring, is the toal 8 bit   
    #str1 = resstring.zfill(32)
    #print(str1)   
    #N = 8
    #sublist = [resstring[n:n+ N] for n in range(0, len(resstring), N)]
    #list2 = []
    #for i in sublist:
    #    val = int(i,2)
    #    if(val != 0):
    #        list2.append(str(val))

    #prefix = ".".join(list2)        
    #return prefix      

testdict2 = {'192.168.2.0': [{'network': '192.168.0.0', 'netmask': '255.255.254.0'},
                            {'network': '192.168.0.0', 'netmask': '255.255.254.0'}], 
'172.168.0.2' : [{'network' : '192.168.3.0', 'netmask': '255.255.255.0'}]}    

def testfunc(lofdict, dest):
    LoN  = {}
    largestmatch = float('-inf')
    for k, v in lofdict.items():
        for i in v:
            netprefix = convertbinary(i['network'], findnetmask(i['netmask']))
            check = binaryrepresentation(dest)
            print(netprefix)
            print(check)
            if(check.startswith(netprefix)):
                val = len(netprefix)
                if val > largestmatch:
                    largestmatch = val

    for k,v in lofdict.items():
        for j in v:
            netprefix = convertbinary(j['network'], findnetmask(j['netmask']))
            if(len(netprefix) == largestmatch):
                LoN[k] = j

    return LoN  

#do with 1, 0, 3
testdest = '192.168.0.25'
print(testfunc(testdict2 , testdest))


#goal, take network apply the netmask, and then get a prefix, and then check which one is the most specific

testdict4 = {}

for entry in testlist:
    testdict4.setdefault(entry['src'],[]).append(entry)

print(testdict4)

testdict1.setdefault(network1, [])
testdict1[network1].append(network4)
testdict1[network1].append(network5)
#may be interesting

testdict[network1] = network4
testdict[network1] = network5

#print(testdict)
#print(testdict1)

#for x in testdict:
#    print(x)


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

#converter(network3)



