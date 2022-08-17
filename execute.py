import subprocess
import os
import argparse
parser = argparse.ArgumentParser()


parser.add_argument("-d", "--domain", help="Database name",default = "")
parser.add_argument("-o", "--output", help="User name")
parser.add_argument("-h", "--help", help="Password")
args = parser.parse_args()
# parser.add_argument("-size", "--size", help="Size", type=int)



os.chdir("./subdomain_finder/v2/cmd/subfinder/")
cwd = os.getcwd()

print("Current working directory is:", cwd)


for filename in os.listdir(os.getcwd()):   
    print(filename)
    if args.domain!="":
        proc = subprocess.Popen("go run "+filename+" -d "+args.domain, stdout=subprocess.PIPE, shell=True)
    proc.wait()

