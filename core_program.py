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

def calculatehours(time_dep,time_arr):
    begining=datetime.datetime.strptime(time_dep,"%Y-%m-%dT%H:%M:%S")
    end=datetime.datetime.strptime(time_arr,"%Y-%m-%dT%H:%M:%S")
    days=(begining-end).days
    if days < 0 :
        return False
    else:
        seconds=(begining-end).seconds
        hours=seconds/3600;
        return hours

def core_function(availables_flights,first_city,cities_visited,cities_nonvisited,last_flight_taken,way_done,price,n_bags):
    #include here the first flight taken in each instance to the stdout*****!!!!!!!!!!!
    selected_flights=set()

    for flights in availables_flights:
        if last_flight_taken.destination==flights.source:
            if flights.source not in cities_visited:
                hours=calculatehours(flights.departure,last_flight_taken.arrival)
                if  hours != False:
                    if hours > 1 and hours < 4:
                        ##########aqui



    print("\n")

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
        for all_flights in availables_flights:
            if all_flights.source != a_flight.source:
                cities_nonvisited.add(all_flights.source)

        way=a_flight.source+","+a_flight.destination+";"+a_flight.flight_number+"\n"
        price= a_flight.price + n_bags * a_flight.bag_price


        core_function(availables_flights,a_flight.source,cities_visited,cities_nonvisited,a_flight,way,price,n_bags)


#***************this is the first line of the main******************************
flights_set=set()
for line in sys.stdin:
    line = line.strip()
    createEach(flights_set,line)
    #print(line)
for item in flights_set:
    item.print_plane()

print("\n hasta aqui es el primer set \n")
starter(flights_set,0)
