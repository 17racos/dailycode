#/bin/bash!
NOW=$(date +"%m-%d-%Y")
echo $NOW
git add . 
git push -u origin main 
git commit -m "'daily commit ','$NOW'"
