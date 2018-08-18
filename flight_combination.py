#!/usr/bin/python3

#******************************************************************************#
#                   created by: Jose Manuel Rodriguez Calvo                    #
#******************************************************************************#

import sys
import datetime
import warnings
#^^^^^^^^^^^^^^^this was the module included in the program^^^^^^^^^^^^^^^^^^^^^


#*****************class for the flights*****************************************
class Flights():
     source="NA"
     destination="NA"
     departure="NA"
     arrival="NA"
     price=0
     bags_allowed=0
     bag_price=0
     flight_number="NA"

     def create(self,so,des,dep,ar,fl,pr,ba,bp):
         self.source=so
         self.destination=des
         self.departure=dep
         self.arrival=ar
         self.price=float(pr)
         self.bags_allowed=int(ba)
         self.bag_price=float(bp)
         self.flight_number=fl

    #This three functions are for not add to the set repeated elements     
     def print_plane(self):
        print(self.flight_number)

     def __eq__(self,other):
         if isinstance(other, Flights):
             return self.flight_number==other.flight_number;
         return NotImplemented
     def __hash__(self):
         return hash(self.flight_number)

#********************methods for the program************************************

#create and add flights to the set to be able to manage the information correctly
def createEach(flights_set,line):
    arr=line.split(",")
    flight_n=Flights();

    try:
        flight_n.create(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])
    except Exception as e:
        stderr.write("Wrong format of a line in the input file".format(e))

    flights_set.add(flight_n)
#*******************************************************************************

#the function calculate the days and if it is negative it will return false, other
#wise it will return the hours that has passed since the arrival until the next departure
def calculateHours(time_dep,time_arr):
    try:
        begining=datetime.datetime.strptime(time_dep,"%Y-%m-%dT%H:%M:%S")
    except Exception as e:
        stderr.write("Wrong format of the departure time: Ex. 1999-02-23T12:03:50")

    try:
        end=datetime.datetime.strptime(time_arr,"%Y-%m-%dT%H:%M:%S")
    except Exception as e:
        stderr.write("Wrong format of the arrival time: Ex. 1999-02-23T12:03:50")

    days=(begining-end).days
    if days < 0 :
        return False
    else:
        seconds=(begining-end).seconds
        hours=seconds/3600;
        return hours
#*******************************************************************************

#the function will return a new string whit the info updated, including the new
#flight that will be added correctly, like is set in the especifications of the
#output in github
def updateWay(way_done,flight):
    tracing=way_done.split(";")
    cities=tracing[0]+","+flight.destination
    planes="%s,%s" % (tracing[1],flight.flight_number)
    new_way_done="%s;%s" % (cities,planes)
    new_way_done=new_way_done.replace("\n","")
    return new_way_done
#*******************************************************************************

#the function will update the price, adding to the price that has cost, the new
#one, including the bags that are transported
def updatePrice(price,flight,n_bags):
    try:
        total=flight.price + n_bags * flight.bag_price
        total+=price
    except Exception as e:
        stderr.write('error trying to calculate the price')
    return total
#*******************************************************************************

#print all the information concatenate with ";"
def printfligh(itineracy,price,time):
    total=str(price)
    line="%s;%s;%s" % (itineracy,time,total)
    line=line.replace("\n","")

    try:
        print (line)
        sys.stdout.flush()
    except Exception as e:
        stderr.write('Error trying to write every solution found')
#*******************************************************************************

#the funtion is based in one of the requirements in which the itineracy can only
#back to the initial point of start, the performance is very similar to the function
#coreFunction with the difference that this is not recursive
def addInitial(availables_flights,city,last_flight_taken,way_done,price,n_bags,time):
    #the purpose of the set selected_flights is to show all the flights that start
    #with the destination of the last flight that has been boarded, according to
    #the especifications
    selected_flights=set()
    for flights in availables_flights:
        if flights.destination == city:
            hours=calculateHours(flights.departure,last_flight_taken.arrival)
            if  hours != False and hours > 1 and hours < 4:
                    selected_flights.add(flights)
    #in a same way of coreFunction this is almost the same with the difference that
    # it will only print the flight
    for next_flight in selected_flights:
        new_way_done=updateWay(way_done,next_flight)
        new_price=updatePrice(price,next_flight,n_bags)
        new_time=time+","+next_flight.departure+"_"+next_flight.arrival
        printfligh(new_way_done,new_price,new_time)
#*******************************************************************************

#the function of the coreFunction is from a flight given, search for all possible
#flights according to the especifications
def coreFunction(availables_flights,first_city,cities_visited,last_flight_taken,way_done,price,n_bags,time):
    #first of all is print the connection reached
    printfligh(way_done,price,time)

    #the purpose of the set selected_flights is to show all the flights that start
    #with the destination of the last flight that has been boarded, according to
    #the especifications
    selected_flights=set()
    for flights in availables_flights:
        if last_flight_taken.destination == flights.source:
            if flights.destination not in cities_visited:
                #the function calculateHours calculate the hourse between the next
                #flight departure and the past flight that has been taken
                hours=calculateHours(flights.departure,last_flight_taken.arrival)
                if  hours != False and hours > 1 and hours < 4:
                        selected_flights.add(flights)

    #the loop will be go over all the possible flights that can be taken
    for next_flight in selected_flights:

        #update the cities visited with the arrival city of the last flight taken
        newcities_visited=set()
        for cities in cities_visited:
            newcities_visited.add(cities)
        newcities_visited.add(next_flight.source)

        #this three lines of code is about the update for the information that will
        #be output, the time adding the next flight times, the way and the price
        new_time=time+","+next_flight.departure+"_"+next_flight.arrival
        new_way_done=updateWay(way_done,next_flight)
        new_price=updatePrice(price,next_flight,n_bags)

        #recursively will call again to the function but now with the info updated
        #of the last flight taken
        coreFunction(availables_flights,first_city,newcities_visited,next_flight,new_way_done,new_price,n_bags,new_time)

    #this function is based on the especifications that a passenger cannot travel
    #to the same city but it can come back to the initial one
    addInitial(availables_flights,first_city,last_flight_taken,way_done,price,n_bags,time)
#*******************************************************************************

#this is function that start the program, the purpose of this function is to list
#all the flights where a passenger can departure, and in each flight it will look
#for all the possible next flights calling to the coreFunction
def starter(flights_set,n_bags=0):
    #this is where all flights will be saved accordinf to the number of bags availables
    availables_flights=set()
    for n_flight in flights_set:
        if n_flight.bags_allowed >= n_bags :
            availables_flights.add(n_flight)

    #this will create another set where all the cities that are availables and has
    #been visited, the loop is to start with all the flights that are availables
    for a_flight in availables_flights:

        cities_visited=set()
        cities_visited.add(a_flight.source)

        #this three lines of code will record in a string, the way which is the cities
        #visited, and the flights taken, the price is the acumulative price for
        #bags and flight and finally the time record the departure and arrival
        way=a_flight.source+","+a_flight.destination+";"+a_flight.flight_number+"\n"
        price= a_flight.price + n_bags * a_flight.bag_price
        time=a_flight.departure+"_"+a_flight.arrival

        #the coreFunction which will be the responsable of look for difference connections
        coreFunction(availables_flights,a_flight.source,cities_visited,a_flight,way,price,n_bags,time)
#*******************************************************************************

#***************this is the first line of the main******************************

flights_set=set()
n_bags=0

for line in sys.stdin:
    line = line.strip()
    if line != "":
        createEach(flights_set,line)
    else:
        warnings.warn('there is a blank line in the file')

if len(sys.argv) == 2 :
    n_bags=int(sys.argv[1])

if n_bags>=0 and n_bags<=2:
    starter(flights_set,n_bags)
else:
    stderr.writte('Error: Wrong number of bags')
