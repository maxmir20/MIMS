import mysql.connector
import googlemaps
import datetime

gmaps = googlemaps.Client(key= 
'AIzaSyAB3oOP1cCf0jmxBddv88at9MWV0oa-g6U'
)
def testGeo():
    return gmaps.location() 



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ChristmasTime",
    database="History_Schema"
)

mycursor = mydb.cursor()


#mycursor.execute("CREATE TABLE test_table3 (runtime TIME)") 
#mycursor.execute("CREATE TABLE history (Marker TIME, Latitude FLOAT, Longitude FLOAT, Elapsed TIME)")

#def start_clock():

#testInsert = "INSERT INTO history (Marker, Latitude, Longitude, Elapsed) VALUES (%s, %s, %s, %s)"

#mycursor.execute(testInsert)

#mydb.commit()

# for db in mycursor:
#     print(db)
# def hello():
#     print('hello world')

# hello()




# class Counter:
#     def __init__ (self, limit, initial = 0, min_digits = 1):
#         self.limit = limit
#         self.min_digits = min_digits/
#         if initial < limit - 1 and initial > 0: #sets the value to the initial parameter, so long as it is between 0 and one less tahn the limit
#             self.value = initial
#         else: #otherwise it will print an error and will make it limit -1
#             print("error the initial value must be less than the limit and greater than 0") 
#             self.value = self.limit - 1
        
        
        
#     def get_value(self): 
#         return int(self.value) #int version of the current value
        
#     def __str__(self):
#         zeroes = "" #creates variable to hold 0s
#         while len(zeroes) < (self.min_digits - len(str(self.value))): #loops for however great the difference is between the minimum digits and the number of digits in the value
#             zeroes += "0" 
#         return zeroes + str(self.value) #prints zeroes before string. If there are any

    
#     def tick(self):
#         if self.value == 0:
#             self.value = self.limit - 1 #resets initial if it hits zero
#             return True
#         else:
#             self.value -= 1 #otherwise decrease by 1
#             return False


# #driver test for counter
# def driver_test():
#     newclocks = []
#     for i in range(6):#creates 6 counters of different limits and digits and puts them in list, then iterates through each function for every value
#         newclocks.append(Counter(int(60/(i+1)), min_digits = (i+1))) 
#         print(newclocks[i].get_value()) 
#         for j in range(newclocks[i].limit): #counts down so it will iterate over 0, indicating that tick works
#             newclocks[i].tick()
#             print(newclocks[i].__str__())

# #driver test call (uncomment to test)
# #driver_test()

# class Stopwatch:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = Counter(24, hours,min_digits = 2) 
#         self.minutes = Counter(60,minutes,min_digits = 2)
#         self.seconds = Counter(60,seconds,min_digits = 2)

#     def __str__(self): #concatenates string using Counter.__str__() function to return values
#         return self.hours.__str__() + ":" + self.minutes.__str__() + ":" + self.seconds.__str__() 

#     def tick(self):
#         if self.seconds.tick(): #even if this isn't true, the value will still go down. If it is true....    
#             if self.minutes.tick(): #then it will get to here (causing the value to go down). Once this one is true...
#                 self.hours.tick() #then this will fire

#     def is_zero(self): #kinda sloppy, but evaluates the concatenated string directly
#         if self.hours.__str__() + ":" + self.minutes.__str__() + ":" + self.seconds.__str__() == "00:00:00": 
#             print(self.__str__())
#             return True
#         else:
#             return False

# # #driver test for timer                    
# # def driver_timer():
# #     new_timer = Timer(1, 30, 5)
# #     while new_timer.is_zero() != True: #iterates through until is_zero() is true
# #         print(new_timer.__str__())
# #         new_timer.tick()
    
# #     #print(new_timer.__str__()) #prints one final time because it will stop printing once it gets to 00:00:00


# # driver_timer()
testGeo()