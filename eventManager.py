import time
import os
from alarms import Alarm, Weekly

class User:
    '''
        Users have a name, username and password along with a list containing all their alarms
        They should be able to add alarms, remove specific alarms and list their current alarms
    '''
    def __init__(self, n, u, p):
        self.name = n
        self.username = u
        self.password = p
        self.alarms = []

    def addAlarm(self, a):
        self.alarms.append(a)

    def deleteAlarm(self, i):
        del self.alarms[i-1]

    def listAlarms(self):
        for i in range (len(self.alarms)):
            if self.alarms[i].isDaily():
                print(i+1, ". ", self.alarms[i].name, " ", self.alarms[i].hour, ":", self.alarms[i].minute, " (Daily)")
            else:
                print(i+1, ". ", self.alarms[i].name, " ", self.alarms[i].hour, ":", self.alarms[i].minute, " (Weekly)") # need to show specific days


class eventManager:

    # Global Variables
    global users
    global user
    global logged
    users = []
    user = User("Diego Ceballos", "admin", "aspire")
    logged = False

    @classmethod
    def cout(cls, str, t):
        print(str)
        time.sleep(t)

    @classmethod
    def addUser(cls):
        os.system('CLS')
        nname = input("Enter the name of the new user: ")
        nuname = input("Enter the new username: ")
        npass = input("Enter the password: ")
        users.append(User(nname, nuname, npass))
        input("User added. Press Enter to continue")

    @classmethod
    def addAlarm(cls, u):
        print("Select the type of alarm you would like to add")
        print("1. Daily Alarm")
        alarmType = input("2. Weekly Alarm\n")
        name = input("Please type the name of the Alarm: ")
        hour = int(input("Please type the hour of the alarm (24 hrs): "))
        minute = int(input("Please type the minute of the alarm: "))
        if alarmType == "2":
            daysOfWeek = int(input("enter days of week in binary starting with monday. Ex: 1111100 for weekdays:\n"))
            u.addAlarm(Weekly(hour, minute, name, Weekly.daysOfWeekIntToList(daysOfWeek)))
        else:
            u.addAlarm(Alarm(hour, minute, name))
        input("Alarm added. Press enter to continue")

    @classmethod
    def load(cls):
        global user
        global users
        os.system('CLS')
        print("Loading data\n")
        eventManager.cout(".", 0.1)
        # adding admin user to user list and test alarm
        users.append(user)
        eventManager.cout(".", 0.1)
        users[0].addAlarm(Alarm(20, 35, "Test"))
        eventManager.cout(".\n", 0.1)
        eventManager.cout("Success!", 0.1)
        eventManager.cout("!", 0.1)
        eventManager.cout("!", 0.1)

    @classmethod
    def enter(cls, u):
        global logged
        global user
        user = u
        os.system('CLS')
        print("Hello ", user.name, ", please select an option\n")
        print("1. Add Alarm")
        print("2. Delete Alarm")
        print("3. List Alarms")
        if user.username == "admin":
            print("4. Add User")
            option = input("5. Log Out\n")
        else:
            option = input("4. Log Out\n")
        os.system('CLS')
        if option == "1":
            eventManager.addAlarm(user)
        elif option == "2":
            print("Enter the index of the alarm to delete")
            u.listAlarms()
            i = int(input(""))
            u.deleteAlarm(i)
        elif option == "3":
            print("listing alarms")
            u.listAlarms()
            input("press enter to continue")
        elif option == "4" and user.username == "admin":
            eventManager.addUser()
        elif option == "4" or option == "5":
            logged = False
        else:
            print("option not available")

    @classmethod
    def start(cls):
        global logged
        eventManager.load()
        while(True):
            os.system('CLS')
            print("Welcome to the Alarm Management System\n")
            uname = input("Enter your username or type \"exit\" to exit\n")
            if(uname == "exit"):
                os.system('CLS')
                break
            upass = input("Enter your password\n")
            logged = False
            for i in range (len(users)):
                if uname == users[i].username:
                    if(upass == users[i].password):
                        logged = True
                        usr = users[i]
            if logged == False:
                print("Wrong username or password, try again") 
                time.sleep(1)
            while logged:
                eventManager.enter(usr)
            os.system('CLS')