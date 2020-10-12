import re


f1 = open("output.txt", "r")
f2 = open("HbB_FASTAs-out.txt", "r")

dict1 = {}
dict2 = {}
for i in range(78):

    h1 = re.match('(.*) \/ (.*),',f1.readline())
    s1f1 =  re.match('seq1:(.*)',f1.readline()).group(1).strip()
    s2f1 =  re.match('seq2:(.*)',f1.readline()).group(1).strip()
    
    dict1[(h1.group(1),h1.group(2))] = (s1f1,s2f1)
    
    h2 =  re.match('(.*)--(.*):',f2.readline())
    s1f2 =  f2.readline().strip()
    s2f2 =  f2.readline().strip()

    dict2[(h2.group(1),h2.group(2))] = (s1f2,s2f2)
    
    # if(s1f1.strip() != s1f2.strip()):
        # print(s1f1)
        # print(s1f2)
        # print(False)
    # if(s2f1.strip() != s2f2.strip()):
        # print(False)
        

for key in dict1.keys():
    if(dict1[key][0][:10] != dict2[key][0][:10]):
        print(key)
        print(dict1[key][0][:10])
        print(dict2[key][0][:10])
        print(False)
    else:
#        print(True)
#        print(dict1[key][0][:10])
#        print(dict2[key][0][:10])
        pass


# count = 1
# seq1 = 0
# seq2 = 0
# for i in f:
    # count = count + 1
    # if(re.match('seq1:(.*)',i)):
        # seq1 = re.match('seq1:(.*)',i).group(1)
    # if(re.match('seq2:(.*)',i)):
        # seq2 = re.match('seq2:(.*)',i).group(1)
    # if(count == 3):
        # if(seq1 == seq2):
            # print(True)
        # else:
            # print(False)  
            # print(seq1)
            # print(seq2)
        # count = 0