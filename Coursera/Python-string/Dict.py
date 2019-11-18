# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# fline = open(name)
# lst= list()
# fdict = dict()
# for line in fline :
#     if line.startswith("From") :
#         lst = line.split()
#         email=lst[1]
#         fdict[email]=fdict.get(email,0)+1
# #print(fdict)
# emailcount= None
# emailid= None
#
# for eid,ecount in fdict.items():
#     if emailcount is None or ecount > emailcount:
#         emailcount= ecount
#         emailid= eid
# print (emailid, int(emailcount/2))

name = "test.txt"
#if len(name) < 1 : name = "mbox-short.txt"
fname = open(name)
flist= list()
tlist= list()
fflist= list()
tdict= dict()
for line in fname:
    if line.startswith("From") :
        flist=line.split()
        if len(flist) > 5 :
        	time=flist[5]
        	tlist=time.split(":")
        	tdict[tlist[0]] = tdict.get(time[0], 0) + 1
sdict=(sorted(tdict.items()))
print (sdict)
for hh,mm in sdict :
   	 print(hh,mm)
