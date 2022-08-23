touch subdomains.txt
read -p "Enter the domain Name? " name
python3 execute2.py  $name
./subfinder -d $name