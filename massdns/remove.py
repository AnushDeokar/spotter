file1 = open("cname_list.txt","r")

Lines = file1.readlines()
count = 0
file1 = open('finaldomains.txt', 'w')
for line in Lines:
    s = ""
    for i in range(len(line)):
        if line[i] == '.':
            if line[i+1] ==' ':
                break
        s+=line[i]
    s+="\n"
    file1.write(s)
file1.close()