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

testdict1 = {}

testdict1.setdefault(network1, [])
testdict1[network1].append(network4)
testdict1[network1].append(network5)
#may be interesting

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



