# Flights Schedule
The program will output all the differents combinations that can be done according to some especificaiones described on
[Python weekend Kiwi.com](https://gist.github.com/martin-kokos/6ccdeeff45a33bce4849567b0395526c)

## Compile
  There is two ways of use it:
  
      specifying the number of bags:                     cat input.csv | ./flight_combination.py 2 > output.csv
    
      whithout specifying, predetimante value = 0:       cat input.csv | ./flight_combination.py > output.csv
    
## Results obtained
  
  **Interpretation of data:** <br/>  
    `list of cities` followed by comas <br/>  
    `list of flights` followed by comas <br/>  
    `departure`_`arrival` followed by comas <br/>  
    `price` the total price <br/>  

 **Example of output:**
```
list of cities; list of flights;          departure_arrival;                         price

DPS,HKT;      PV414;        2017-02-11T09:15:00_2017-02-11T12:55:00;                  67.0
BWN,DPS;      PV042;        2017-02-12T22:50:00_2017-02-13T01:10:00;                  56.0
DPS,HKT;      PV519;        2017-02-11T00:20:00_2017-02-11T04:00:00;                  79.0
```
