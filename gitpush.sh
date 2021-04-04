#/bin/bash!
NOW=$(date +"%m-%d-%Y")
echo $NOW
git add . 
git push -u origin main 
#commitcomment = input()
git commit -m "'adding project2 and updates on project1 and gitpush script','$NOW'"
#git commit -m "'commitcoment','$NOW'"
