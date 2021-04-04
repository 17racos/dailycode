#/bin/bash!
NOW=$(date +"%m-%d-%Y")
echo $NOW
git add . 
git push -u origin main 
git commit -m "adding project2 and updates on project1 and gitpush script,'$NOW'"
#commitcomment = input()
#git commit -m "'commitcoment','$NOW'"
