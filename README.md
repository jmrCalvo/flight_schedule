# Flights Schedule
The program will output all the differents combinations that can be done according to some especificaiones described on
[Python weekend Kiwi.com](https://gist.github.com/martin-kokos/6ccdeeff45a33bce4849567b0395526c)

## Compile
  There is two ways of use it:
  
      specifying the number of bags:                     cat input.csv | ./flight_combination.py 2 > output.csv
    
      whithout specifying, predetimante value = 0:       cat input.csv | ./flight_combination > output.csv
    
## Results obtained
  
  Interpretation of data:
    * `list of cities` followed by comas   
    * `list of flights` followed by comas 
    * `departure`_`arrival` followed by comas
    * `price` the total price 

  Example of output:
```
list of cities;list of flights;departure_arrival;price
DPS,HKT;PV414;2017-02-11T09:15:00_2017-02-11T12:55:00;67.0
DPS,HKT,USM;PV414,PV243;2017-02-11T09:15:00_2017-02-11T12:55:00,2017-02-11T15:45:00_2017-02-11T16:40:00;89.0
DPS,HKT,DPS;PV414,PV388;2017-02-11T09:15:00_2017-02-11T12:55:00,2017-02-12T14:35:00_2017-02-12T16:55:00;116.0
DPS,HKT,DPS;PV414,PV213;2017-02-11T09:15:00_2017-02-11T12:55:00,2017-02-11T16:15:00_2017-02-11T18:35:00;122.0
BWN,DPS;PV042;2017-02-12T22:50:00_2017-02-13T01:10:00;56.0
DPS,HKT;PV519;2017-02-11T00:20:00_2017-02-11T04:00:00;79.0
```
