#!/usr/bin/python3

import sys
#^^^^^^^^^^^^^^^this was the module included in the program^^^^^^^^^^^^^^^^^^^^^


#*****************class for the flights*****************************************
class plane():
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
         self.price=pr
         self.bags_allowed=ba
         self.bag_price=bp
         self.flight_number=fl

     def print_plane(self):
        print(self.flight_number)

     def __eq__(self,plane_o):
         if isinstance(plane_o, plane):
             return self.flight_number==plane_o.flight_number;
         return NotImplemented
     def __hash__(self):
         return hash(self.flight_number)

#********************methods for the program************************************
def createEach(plane_set,line):
    arr=line.split(",")
    plane_n=plane();
    plane_n.create(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])
    plane_set.add(plane_n)
    #plane_n.print_plane()

#***************this is the first line of the main******************************
plane_set=set()
for line in sys.stdin:
    line = line.strip()
    createEach(plane_set,line)
    #print(line)
for item in plane_set:
    item.print_plane()
