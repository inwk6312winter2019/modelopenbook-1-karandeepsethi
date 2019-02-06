fout=open("running-config.cfg")
def list_ifname_ip(fout):
	add_dict={}
	for line in fout:
#		if "no"not in line:
			if "nameif" in line:
				line=line.strip()
				tc=line.split(" ")
			if "ipaddress" in line:
				line=line.strip()
				tcadd=line.split(" ")
				tup=(tcadd[2],)
				add_dict.setdefault(tc[1],(tcadd[2],tcadd[3]))

	return add_dict

print(list_ifname_ip(fout))


def new_configuration(fout):
	fin=open("new_running_config.cfg")
	for line in fout:
		if "ipaddress" in line:
			line=line.strip()
			line=line.split()
			ipadd=line[2]
			maskadd=line[3]
			ipadd=line.split()
			maskadd=line.split()
			if ipadd[0]=='172' or ipadd[0]=='192':
				ipadd[0]='10'

			if (maskadd[0]=='255' and maskadd[1]=='255')or maskadd[2]=='255':
				maskadd[1]=maskadd[2]='0'

			ipadd='ipaddress'+'.'.join(ipadd)+'.'.join(maskadd)

			return fin.write(ipadd)


print(new_configuration(fout))

