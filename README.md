### Exploring US Bike Share Data
____________________________________________________________________________________________________________________________________________

In this project, I used Python programming language to explore data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States. I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.

### The Datasets
____________________________________________________________________________________________________________________________________________

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

The image below shows the data for the first 10 rides in the **new_york_city.csv file**

![Data for the first 10 rides in the **new_york_city.csv file**](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)


### The Files
____________________________________________________________________________________________________________________________________________

To answer the statistical questions regarding the bike share system, I created a Python script to help guide my work in this project. The code with helper comments are provided in a **bikeshare** file. Also, I needed the three city dataset files too:

* chicago.csv
* new_york_city.csv
* washington.csv

### Software
____________________________________________________________________________________________________________________________________________

The program was written using `Python 3` and some libraries installed using `Anaconda`:
```
* time
* NumPy 
* Pandas 
```
### Credits
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.

