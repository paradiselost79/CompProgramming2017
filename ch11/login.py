import time, getpass

# 2018-02-06 16:34:26

def login(attempts): #user attempts to login, only has 3 attempts to start
    #print(attempts) debug to check attempts was getting changed
    users_pws=open('logins.txt','r') #user/pw file
    print("Welcome, please login")
    usern_entry=input('User: ')
    userp_entry=getpass.getpass("Password: ")
    for i in users_pws:
        check=i.split() #turns line into string to check, using 'x in y' check would come True even if username was password
        #print(check) debug test
        if usern_entry==check[0]:
            if userp_entry==check[1]:
                print("Successful login")
                logger(usern_entry,userp_entry,"Successful")
                time.sleep(2)
                quit()#in the future this will run whatever is supposed to happen after login
    print("INCORRECT USERNAME OR PASSWORD")
    logger(usern_entry,userp_entry,"Unsuccessful")
    attempts-=1 #only allow 3 attempts, so subtract one try each time, then check number remaing, at 0 quit
    if attempts==0:
        print("LOCKED OUT")
        time.sleep(2)
        quit()
    login(attempts)

def logger(x,y,z): #username, userpassword,success or not
    ts = time.gmtime()
    time_formatted=time.strftime("%Y-%m-%d %H:%M:%S", ts)
    loggerfile=open('logs.txt','a')
    loggerfile.write("%s %s %s %s \n" %(x,y,z,time_formatted))
    loggerfile.close()





login(3)