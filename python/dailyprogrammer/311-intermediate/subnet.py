import sys

def calcSubnet(inputfile):
    '''
    Calculate covered range for each input IP in inputfile.
    Time complexity: O(n)
    '''
    fd = open(inputfile, 'r')
    ipcount = int(fd.readline())
    ipranges = []
    for x in range(ipcount):
        ip = fd.readline().rstrip('\n')
        [ip, mask] = ip.split('/')
        mask = int(mask)
        subips = map(int,ip.split('.'))
        staticips = mask/8
        bitshift = mask%8
        i = 0
        for i in range(len(subips)):
            if staticips > 0:
                staticips -= 1
                continue
            if bitshift != 0:
                subips[i] |= pow(2, 8-bitshift)
                bitshift = 0
                continue
            subips[i] = 255
        ipranges += [(ip, '.'.join(map(str,subips)), mask)]
    return ipcount, ipranges

def reduce(ipcount, ipranges):
    '''
    Remove redundant IP ranges from the set.
    Finds minimal solution without attempting to combine neighboring ranges.
    Time complexity: O(n^2)
    '''
    ret = ipranges[:]   # Actual copy of ipranges
    delset = []
    for x in range(ipcount):
        x0 = map(int,ipranges[x][0].split('.'))
        x1 = map(int,ipranges[x][1].split('.'))
        for y in range(ipcount):
            if x == y:
                continue
            y0 = map(int,ipranges[y][0].split('.'))
            y1 = map(int,ipranges[y][1].split('.'))
            lowbound = True
            uppbound = True
            # Check if y is within x's bounds, if so, add index to remove list.
            for (a,b,c,d) in zip(x0,y0,x1,y1):
                if a > b:
                    lowbound = False
                if c < d:
                    uppbound = False
            if lowbound and uppbound:
                delset += [y]
    delset = list(set(delset))  # Remove duplicates
    delset = sorted(delset)
    delset.reverse()
    for x in delset:
        del ret[x]
    return sorted(ret,key=lambda z : z[2])

def main():
    ipcount,ipranges = calcSubnet(sys.argv[1])
    subnet = reduce(ipcount,ipranges)
    for x in subnet:
        print "%s/%d" % (x[0],x[2])

if __name__ == '__main__':
    main()
