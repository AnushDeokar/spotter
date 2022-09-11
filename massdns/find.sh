cat list.txt | ./unfurl --unique domains >>  unfurloutput.txt  
./subfinder -dL unfurloutput.txt -o subdomains.txt
./bin/massdns -r lists/resolvers.txt -t CNAME -o S -w cname_list.txt subdomains.txt 
python3 remove.py 
./httpx -l finaldomains.txt -mc 404 -o httpxresults.txt
cat httpxresults.txt | ./unfurl --unique domains >>  httpxfinalresults.txt
./bin/massdns -r lists/resolvers.txt -t CNAME -o S -w finaloutput.txt httpxfinalresults.txt
./subzy -targets httpxfinalresults.txt 
# rm unfurloutput.txt
# rm httpxresults.txt
# rm finaldomains.txt
# rm subfinderoutput.txt
