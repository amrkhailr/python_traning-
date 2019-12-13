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
        switch['Default Gateway'] = value[4]
        switch['Switch stack'] = value[5]
        switch['Role'] = value[6]
        content.append(switch)
    return content

def ping_device(hostname):
    response = pyping.ping(hostname,count=2)
    if response.ret_code == 0:
        return True
    else:
        return False

if __name__ == "__main__" :
    myfile=input("Give your file path: ")
    cont=upload_csv(myfile)
    print(cont[:2])
    for sw in cont[:2]:
        resp=ping_device(sw['Internal IPv4 Address'])
        


