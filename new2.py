import os , random
with open('test.txt','a') as file:
        file.write("comit")
        os.system('git add test.txt')
        os.system('git commit --date=" 2023-12-12" -m 1')
    
        os.system('git push -u origin main')
