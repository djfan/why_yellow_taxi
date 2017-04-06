# Data

[TLC Trip Record Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)

![](http://www.nyc.gov/html/tlc/images/features/fi_about_photo_trip_records.png)

------

[2016\_(May)\_New_York_City_Subway_Station_Entrances](https://geo.nyu.edu/catalog/nyu_2451_34760)

**Author(s):** GIS Lab, Newman Library, Baruch CUNY

**Description:** This point layer was created using the data feeds from the Metropolitan Transportation Authority (MTA). It represents the subway station entrance locations for the MTA NYC Transit Subway, where an entrance represents a physical entryway or exit from a subway station to a street or building. The data originally came in a CSV format, and was plotted using the coordinates for the entrances and saved as a spatial layer in the local state plane coordinate system. The features include several attributes that describe the physical details of the entrances (nearest street or corner, whether they are entrance or exit only, whether they have stairs, escalators, or elevators, etc) and of the stations (lines served and trains that stop there). The station entrances for the Staten Island Railway are not included. The features do not have a unique identifier. 

------

[2016\_(May)\_New_York_City_Subway_Routes](https://geo.nyu.edu/catalog/nyu_2451_34758)

**Author(s):** GIS Lab, Newman Library, Baruch CUNY

**Description:** This line layer was created from the GTFS data feeds from the Metropolitan Transportation Authority (MTA) to represent the MTA NYC Transit Subway routes. A python script was written to take the data files as input and plot and save them as a spatial layer in the local state plane coordinate reference system. Lines in this layer represent individual subway routes that follow physical track locations; they were generalized from the GTFS format where lines depicted individual services. Each line represents the route that a specific train takes during normal weekday and rush hour service. The unique ID is route_id, a field created by the MTA that uses the familiar letter or number designation for trains, with distinct ids for each of the three shuttle (S) trains. 

------

[2015_New_York_City_Subway_Complexes_and_Ridership](https://geo.nyu.edu/catalog/nyu_2451_34502)

**Author(s):** GIS Lab, Newman Library, Baruch CUNY

**Description:** The subway complexes layer was created to represent ridership data for the NYC subway system (Metropolitan Transportation Authority, or MTA). This layer is a subset of the subway stations layer (nyu_2451_34503) that has been combined with MTA statistics on ridership; it was originally created in August 2012 and has been updated annually. Ridership data is not available for each individual subway station, as many stations are linked via common entrances and passageways where transfers are free, and because ridership data is not collected for the Staten Island Railway stations. This layer was created by choosing an individual station from nyu_2451_34503 to represent the entire complex, and modifying the station name and train fields appropriately. It should be used for mapping ridership data or for analysis that requires this data, and not for specifying actual station locations or measuring distances. There are 421 complexes, and the field station_ct indicates how many stations are part of a complex. Annual, average weekday, and average weekend ridership is provided for 2007 to 2014. The unique ID is complex_id, which was created by alphabetizing the complexes by borough and station name and assigning a sequential number to a borough prefix. This layer does not include the new 34th St - 11 Av station on the 7 line; it will be updated in summer 2016 once ridership data becomes available. This layer was created as part of the NYC Geodatabase (NYC GDB) project, a resource designed for basic geographic analysis and thematic mapping within the five boroughs of New York City.





***.zip contains .shp***



