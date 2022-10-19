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

testdest = '192.169.0.25'
def testfunc(lofdict, dest):
    LoN  = {}
    largestmatch = float('-inf')
    for k, v in lofdict.items():
        netprefix = convertbinary(v['network'], findnetmask(v['netmask']))
        if(dest.startswith(netprefix)):
            val = len(netprefix)
            if val > largestmatch:
                largestmatch = val

    for k,v in lofdict.items():
        netprefix = convertbinary(v['network'], findnetmask(v['netmask']))
        if(len(netprefix) == largestmatch):
            LoN[k] = v

    return LoN        




def findnetmask(netmask):
    count = 0
    nsplit = netmask.split('.')
    binary = []
    for i in nsplit:
        binary.append((bin(int(i)).replace('0b',"")).zfill(8))  

    num = "".join(binary)
    for i in num:
        if i == '1':
            count += 1

    return count

findnetmask('255.255.0.0')
   


#probably the most convoluted way to generate the prefix of a string...
def convertbinary(network, netmask):
    #this is to split it up, and then calculate each deciman version of the binary string, 
    # then evetually fill it to be what we need
    nsplit = network.split('.')
    binary = []
    #creates the 8 bit representation of the network
    for i in nsplit:
        binary.append((bin(int(i)).replace('0b',"")).zfill(8))

    res = "".join(binary)
    resstring = ""
    #then we have a 32 bit number here, then we iterate through and take only the that can work
    #find some way to generate the number for the netmask
    for x in range(netmask):
        resstring += (res[x])
        #then this generates the specific prefix with the netmask
    str1 = resstring.zfill(32)
    #this then padds back the string into the 32 bit representation to be able to be grouped into the groups of 8
    #example
    N = 8
    sublist = [str1[n:n+ N] for n in range(0, len(str1), N)]
    list2 = []
    for i in sublist:
        val = int(i,2)
        if(val != 0):
            list2.append(str(val))

    prefix = ".".join(list2)        
    return prefix      


print(testfunc(testdict1, testdest))


#goal, take network apply the netmask, and then get a prefix, and then check which one is the most specific



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



