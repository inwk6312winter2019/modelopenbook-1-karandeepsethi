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


