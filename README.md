# Safest-City-Prediction
Taking into consideration the COVID-19 situation, this project aims to develop a model which would take an input of the user's current location city and predict which neighbouring city is the safer to go to (wrt COVID-19 stats in India).

Objective:
Many migrant workers in our country are stranded and are told to vacate houses due to the COVID-19 paranoia. 
The aim was to develop a model which would take an input of their current location city and then give them the output response of which city amongst their nearby cities were safest for them to go to.

IDE Used:  Spyder (Python 3.7)

Algorithm: As everyone in our team liked the idea, I started working on the algorithm and the model as everyone else in the team were into web development and designing. 

The algorithm was divided into two parts:
#ALGORITHM PART1 TO FIND NEARBY AREAS CLUSTERING BASED ON LATITUDE AND LONGITUDE
#ALGORITHM PART2 ML MODEL ON CLUSTERED DATA TO FIND BEST SUITED PLACE

•	[#Algo 1  begins] Cluster data of Indian cities into 20 clusters. 
•	The cluster of the city_name which we get as the input is recognized
•	Then merge the two datasets with the state column being the common column.
•	[#Algo 2 begins] On all the cities, in the same cluster as input city, a formula is applied :
factor_one=(['Value.deaths']/['Value.confirmed'])
factor_two=(['Value.deaths'])/['Population_of_given_state'])**2
factor = float(1/(factor_one*factor_two))
•	The value of these factors for the cities in the same cluster as the query are appended into a list.
•	The list is then sort and from there we retrieve the highest factor value.
•	The city corresponding to that factor value is returned as the output.

Implementation: 
Algorithm part 1 was run successfully and all clusters had cities located nearby, with visualiztion of cluster.
Algorithm part 2 was not giving satisfactory results, still working on it.

Dataset for Algo part 1:
It consists of 214 rows and 5 columns. It included 214 cities of our country and their corresponding latitude and longitude information.

Dataset for Algo part 2:
It was taken from the official website of our government. It consists of covid statistics in different states of India. 

