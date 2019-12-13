import pyping # pyping is only working for python 2. Try to find another ping module for Python 3
from ping3 import ping 
def upload_csv(filename):
    content=[]

    fopen=open(filename,"r")
    file_content=fopen.read()
    file_content = file_content.splitlines()
    file_content = file_content[2:] # take from third line to all the way to the last

    for n in file_content:
        switch={}
        value = n.split (',')
        
        switch['Switchname']= value[0]
        switch['Model']=value[1]
        switch['SerialNumber']= value[2]
        switch['Internal IPV4 Address'] = value[3]
        switch['Subnet Mask'] = value[4]
        switch['Default Gateway'] = value[5]
        switch['Switch stack'] = value[6]
        switch['Role'] = value[7]
        if '.' in value[3]:
            content.append(switch)
    return content

def ping_device(hostname):
    response = ping(hostname)
    if response:
        return True
    else:
        return False

if __name__ == "__main__" :
    myfile=input("Give your file path: ")
    cont=upload_csv(myfile)
    print(cont[:2])
    for sw in cont[:2]:
        try:
            resp=ping_device(sw['Internal IPV4 Address'])
            if resp:
                print(sw['Switchname'] + "is reachable" + sw['internal IPV4 Address'])
            else:
                print(sw['Switchname'] + "is not reachable")
        except:
            print(sw['Switch Name'] + " is not reachble with IP address:" + sw['internal IPV4 Address'])
    
