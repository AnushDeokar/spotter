touch subdomains.txt
read -p "Enter the domain Name " name
./subfinder -d $name
python3 execute2.py  $name
./massdns/bin/massdns -r massdns/lists/resolvers.txt -t CNAME -o S -w cname_list.txt subdomains.txt 