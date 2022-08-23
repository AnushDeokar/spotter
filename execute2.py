import sys
def read_domain(fname, domain_name):
    print("""
    
    _____  ______  ______  _______  _______  _____   _____
   / ___/ /  _  / / __  / /__  __/ /__  __/ / ___/  / _  /
  (__  ) /  ___/ / /_/ /    / /      / /   / ___/  /  __/
 /____/ /__/    /_____/    /_/      /_/   /____/  /_/_|
    
    IIT Jodhpur
    
    """
    
    )
    f = open(fname, "r")
    Lines = f.readlines()
    file_path = 'subdomains.txt'
    sys.stdout = open(file_path, "w")
    domain_array = []
    for line in Lines:
        temp = line[:-1]
        domain_array.append(temp+"."+domain_name)
    for i in domain_array:
        print(i)




read_domain("/home/sonu/Desktop/Spotter/commonspeak2-wordlists/subdomains/subdomains.txt",  sys.argv[1])