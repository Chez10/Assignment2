import re
import socket
class Assignment2:
    # Task 1
    def __init__(self, year):
        #year is an int
        self.year = year

    # Task 2
    def tellAge(self, currentYear):
        print("Your age is", currentYear-self.year)

    # Task 3
    def listAnniversaries(self):
        age =2022 - self.year
        anilist=[i for i in range(10, age +1 , 10)]

        return anilist

    # Task 4
    def modifyYear(self, n):
        # n is an int
        yearString = str(self.year)
        yearN= self.year * n
        yearNString = str(yearN)

        return yearString[:2]* n + yearNString[::2]

    # Task 5
    @staticmethod
    def checkGoodString(string):
        # string is a str
        #u = re.findall(r'\d+', string)
        u=0
        for i in string:
            if i.isdigit():
                u += 1
        if len(string) >= 9 and string[0].islower() and u == 1:
            return True
        return False

    # Task 6
    @staticmethod
    def connectTcp(host: str, port: int) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.close()

            return True

        except Exception as e:
            print(f"Error: {e}")
            return False

#Testing the methods
#Task 2
print('Task 2, example:')
a = Assignment2(1)
a.tellAge(2022)
print('')

#Task 3
print('Task 3, example 1:')
a = Assignment2(2000)
ret = a.listAnniversaries()
print(ret)
print('')
#and
print('Task 3, example 2:')
a = Assignment2(1991)
ret = a.listAnniversaries()
print(ret)
print('')

#Task 4
print('Task 4, example:')
ret = a.modifyYear(5)
print(ret)
print('')

#Task 5
print('Task 5, example:')
ret = Assignment2.checkGoodString("f1obar0more")
print(ret)
ret = Assignment2.checkGoodString("foobar0more")
print(ret)
print('')

#Task 6
print('Task 6, example:')
retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")