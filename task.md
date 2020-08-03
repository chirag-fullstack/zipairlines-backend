# ZipAirlines

### Aircraft passenger capacity issue

We are creating a new software for a airline company called `ZipAirlines`.
 The company is assessing 10 different airplanes.

 - Each airplane has a fuel tank of (`200 liters * id` of the airplane) capacity.  For example, if the airplane `id = 2`, the fuel tank capacity is `2*200 = 400 liters`.
 - The airplane fuel consumption per minute is the logarithm of the airplane `id multiplied by 0.80 liters`.
 - `Each passenger` will increase fuel consumption for additional `0.002 liters per minute`.

 Write a RESTful API using Django Rest Framework to:

 - Allow for input of 10 airplanes with user defined id and passenger assumptions
 - Print `total airplane fuel consumption per minute` and `maximum minutes able to fly`
 