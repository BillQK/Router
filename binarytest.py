def convertToBinary(msg):
    msg1 = msg["msg"]
    prefix = msg1["network"]
    netmask = msg1["netmask"]
    
    #converting to eventually check withe netmask(count the ones)
    #with the number that has the correct amount depending on the netmask
    #then thats the address that we send things to?

    separatedecimal = prefix.split(".")
    print(separatedecimal)
    nlist = []
    testlist = []

    for i in separatedecimal:
        nlist.append(bin(int(i)).replace("0b", ""))

    for i in nlist:
        testlist.append(i.zfill(8))

    str = '.'.join(testlist)  

    print(str)    
    #index = countOnes(bnetmask)
    #for index through length, replace that value with 0

#returns the count of a given netmask in ones to know how much to index by    
def countOnes(bnetmask):
    count = 0
    for i in bnetmask:
        if(i == 1):
            count +=1
    print(count)         
    return count   


message = {'type': 'update', 'src': '192.168.0.2', 'dst': '192.168.0.1', 'msg': {'network': '192.168.0.0', 'netmask': '255.255.255.0', 'localpref': 100, 'ASPath': [1], 'origin': 'EGP', 'selfOrigin': True}}
test = convertToBinary(message)    
