#!/usr/bin/python3

import sys
import datetime
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

     def print_plane(self):
        print(self.flight_number)

     def __eq__(self,other):
         if isinstance(other, Flights):
             return self.flight_number==other.flight_number;
         return NotImplemented
     def __hash__(self):
         return hash(self.flight_number)

#********************methods for the program************************************
def createEach(flights_set,line):
    arr=line.split(",")
    flight_n=Flights();
    flight_n.create(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])
    flights_set.add(flight_n)

def calculateHours(time_dep,time_arr):
    begining=datetime.datetime.strptime(time_dep,"%Y-%m-%dT%H:%M:%S")
    end=datetime.datetime.strptime(time_arr,"%Y-%m-%dT%H:%M:%S")
    days=(begining-end).days
    if days < 0 :
        return False
    else:
        seconds=(begining-end).seconds
        hours=seconds/3600;
        return hours

def updateWay(way_done,flight):
    tracing=way_done.split(";")
    cities=tracing[0]+","+flight.destination
    planes="%s,%s" % (tracing[1],flight.flight_number)
    new_way_done="%s;%s" % (cities,planes)
    new_way_done=new_way_done.replace("\n","")
    return new_way_done

def updatePrice(price,flight,n_bags):
    total=flight.price + n_bags * flight.bag_price
    total+=price
    return total

def printfligh(itineracy,price,time):
    total=str(price)
    line="%s;%s;%s" % (itineracy,total,time)
    line=line.replace("\n","")

    print (line)
    sys.stdout.flush()


def addInitial(availables_flights,city,last_flight_taken,way_done,price,n_bags,time):
    selected_flights=set()
    for flights in availables_flights:
        if flights.destination == city:
            hours=calculateHours(flights.departure,last_flight_taken.arrival)
            if  hours != False and hours > 1 and hours < 4:
                    selected_flights.add(flights)

    for next_flight in selected_flights:
        new_way_done=updateWay(way_done,next_flight)
        new_price=updatePrice(price,next_flight,n_bags)
        new_time=time+"_"+next_flight.departure+","+next_flight.arrival
        printfligh(new_way_done,new_price,new_time)

def coreFunction(availables_flights,first_city,cities_visited,last_flight_taken,way_done,price,n_bags,time):
    #include here the first flight taken in each instance to the stdout*****!!!!!!!!!!!
    printfligh(way_done,price,time)
    selected_flights=set()

    for flights in availables_flights:
        if last_flight_taken.destination == flights.source:
            if flights.destination not in cities_visited:
                hours=calculateHours(flights.departure,last_flight_taken.arrival)
                if  hours != False and hours > 1 and hours < 4:
                        selected_flights.add(flights)


    # for itme in selected_flights:
    #     itme.print_plane()
    for next_flight in selected_flights:
        newcities_visited=set()
        for cities in cities_visited:
            newcities_visited.add(cities)
        newcities_visited.add(next_flight.source)
        new_time=time+","+next_flight.departure+","+next_flight.arrival
        new_way_done=updateWay(way_done,next_flight)
        new_price=updatePrice(price,next_flight,n_bags)

        coreFunction(availables_flights,first_city,newcities_visited,next_flight,new_way_done,new_price,n_bags,new_time)

    addInitial(availables_flights,first_city,last_flight_taken,way_done,price,n_bags,time)

def starter(flights_set,n_bags=0):
    availables_flights=set()
    for n_flight in flights_set:
        if n_flight.bags_allowed >= n_bags :
            availables_flights.add(n_flight)

    # for item in availables_flights:
    #     item.print_plane()
    for a_flight in availables_flights:
        cities_visited=set()
        cities_nonvisited=set()

        cities_visited.add(a_flight.source)

        way=a_flight.source+","+a_flight.destination+";"+a_flight.flight_number+"\n"
        price= a_flight.price + n_bags * a_flight.bag_price
        time=a_flight.departure+","+a_flight.arrival

        coreFunction(availables_flights,a_flight.source,cities_visited,a_flight,way,price,n_bags,time)


#***************this is the first line of the main******************************
flights_set=set()
for line in sys.stdin:
    line = line.strip()
    createEach(flights_set,line)
    #print(line)


starter(flights_set,0)
