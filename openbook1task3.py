def get_access_list(fout):
    fout.seek(0)
    transit_access_in=[]
    global_access=[]
    fw_management_access_in=[]
    
    for line in fout:
        line=line.strip()
        if 'access-list' in line:
            if 'transit_access_in' in line:
                transit_access_in.append(line)
            elif 'global_access' in line:
                global_access.append(line)
            elif 'fw-management_access_in' in line:
                fw_management_access_in.append(line)
    print('access list for transit_access_in::\n',transit_access_in)
    print('access list for global_access::\n',global_access)
    print('access list for fw_management_access_in::\n',fw_management_access_in)
    



try:
    fout=open('running-config.cfg','r')
    fin=open('new-running-config.cfg','a+')
    print("The dictionary of ip addresses::",list_ifname_ip(fout))
    if new_config_file(fout,fin):
        print('New File Created Successfully')
    else:
        print('Not Able to Create New File File')
    get_access_list(fout)
except:
    print('Something Went wrong While working with Files.Please check files have proper permissions')

