# Flights Combinations
The program will output all the differents combinations that can be done according to some especificaiones described on
[Python weekend Kiwi.com](https://gist.github.com/martin-kokos/6ccdeeff45a33bce4849567b0395526c)

## Compile
  The program has been runned in linux. There is two ways of use it:

      specifying the number of bags:                     cat input.csv | ./flight_combination.py 2 > output.csv

      whithout specifying, predetermined value = 0:      cat input.csv | ./flight_combination.py > output.csv

## Results obtained

  **Interpretation of data:** <br/>  
    `list of cities` followed by comas <br/>  
    `list of flights` followed by comas <br/>  
    `departure`_`arrival` followed by comas <br/>  
    `price` the total price <br/>  

 **Example of output:**
```
list of cities;list of flights;departure_arrival;price

DPS,HKT;PV414;2017-02-11T09:15:00_2017-02-11T12:55:00;67.0
BWN,DPS;PV042;2017-02-12T22:50:00_2017-02-13T01:10:00;56.0
DPS,HKT,USM;PV260,PV634;2017-02-11T08:50:00_2017-02-11T12:30:00,2017-02-12T16:00:00_2017-02-12T16:55:00;  110.0
```
