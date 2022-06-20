class Alarm:
    def __init__(self, h, m):
        self.hour = h
        self.minute = m
        self.name = "Alarm"
    
    def __init__(self, h, m, n):
        self.hour = h
        self.minute = m
        self.name = n

    def isDaily(self):
        return True


class Weekly(Alarm):
     # 0 to 6 in days will determine if the alarm is triggered on a specific day of week

    def __init__(self, h, m):
        Alarm.__init__(self, h, m)
        self.days = [False, False, False, False, False, False, False]
    
    def __init__(self, h, m, n):
        Alarm.__init__(self, h, m, n)
        self.days = [False, False, False, False, False, False, False]

    def __init__(self, h, m, sun, mon, tue, wed, thu, fri, sat):
        self.hour = h
        self.minute = m
        self.name = "Alarm"
        self.days = [sun, mon, tue, wed, thu, fri, sat]

    def __init__(self, h, m, n, sun, mon, tue, wed, thu, fri, sat):
        self.hour = h
        self.minute = m
        self.name = n
        self.days = [sun, mon, tue, wed, thu, fri, sat]

    def __init__(self, h, m, n, dow):
        self.hour = h
        self.minute = m
        self.name = n
        self.days = dow

    @classmethod
    def isDaily(cls):
        return False
    
    @classmethod
    def daysOfWeekIntToList(cls, dow):
        dowList = []
        if dow/1000000 == 1:
            dowList.append(True)
            dow - 1000000
        else:
            dowList.append(False)
        if dow/100000 == 1:
            dowList.append(True)
            dow - 100000
        else:
            dowList.append(False)
        if dow/10000 == 1:
            dowList.append(True)
            dow - 10000
        else:
            dowList.append(False)
        if dow/1000 == 1:
            dowList.append(True)
            dow - 1000
        else:
            dowList.append(False)
        if dow/100 == 1:
            dowList.append(True)
            dow - 100
        else:
            dowList.append(False)
        if dow/10 == 1:
            dowList.append(True)
            dow - 10
        else:
            dowList.append(False)
        if dow == 1:
            dowList.append(True)
        else:
            dowList.append(False)
        return dowList