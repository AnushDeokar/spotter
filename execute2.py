import sys
import time

def read_domain(scope):
    print("""
    
    _____  ______  ______  _______  _______  _____   _____
   / ___/ /  _  / / __  / /__  __/ /__  __/ / ___/  / _  /
  (__  ) /  ___/ / /_/ /    / /      / /   / ___/  /  __/
 /____/ /__/    /_____/    /_/      /_/   /____/  /_/_|
    
    IIT Jodhpur
    
    """
    
    )
    #f = open("commonspeak2-wordlists/subdomains/subdomains.txt", "r")
    wordlist = open('commonspeak2-wordlists/subdomains/subdomains.txt').read().split('\n')

    file1 = open("subdomains.txt", "a")  # append mode
    
    for word in wordlist:
        if not word.strip(): 
            continue
        file1.write('{}.{}\n'.format(word.strip(), scope))
        #print('{}.{}\n'.format(word.strip(), scope))
    file1.close()


read_domain(sys.argv[1])



print("""


All Subdomains have been collected.


""")

time.sleep(2)