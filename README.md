# **Why Yellow Taxi, Not Subway**

#### Question:

Sometimes people could take subway from A to B (directly, no transfer), but they take a yellow cab instead. We are wondering which subway line is the one that people are most unwilling to take, by detecting people’s choice pattern based on location, time and day of the week, we would like to answer the question why people would choose yellow cab instead of subway.

#### Repository

| #    | Folder      | Note                                     |
| ---- | ----------- | ---------------------------------------- |
| 1    | Data        | All Data                                 |
| 2    | Buffer      | Create Buffer Area of Subway Entrances (Run in Local) |
| 3    | Sjoin       | Spatial Join (Run in Local)              |
| 4    | Filter      | Filter Service Time (Run in Local)       |
| 5    | Run         | Testing Scripts (Run in Dumbo)           |
| 6    | Output      | **Final-Version** Scripts and Results (Run in Dumbo) |
| 7    | Viz         | Plots                                    |
| 8    | Deliverable | Slide, Docs                              |
| 9    | docs        | Website ( *to be continued ...* )        |

#### Structure:

```
.
├── Buffer
│   ├── Entrance_Buffer_100_Feet_EPSG4269_NAD83.ipynb
│   ├── README.md
│   ├── Use_Geojson2build_Buffer_Not_Shapefile.ipynb
│   └── entr_buffer_100_feet_epsg4269_nad83
│       ├── entr_buffer_100_feet_epsg4269_nad83.cpg
│       ├── entr_buffer_100_feet_epsg4269_nad83.dbf
│       ├── entr_buffer_100_feet_epsg4269_nad83.prj
│       ├── entr_buffer_100_feet_epsg4269_nad83.shp
│       └── entr_buffer_100_feet_epsg4269_nad83.shx
├── Data
│   ├── 2015_New_York_City_Subway_Complexes_and_Ridership.json
│   ├── 2015_New_York_City_Subway_Complexes_and_Ridership.zip
│   ├── 2016_(May)_New_York_City_Subway_Routes.json
│   ├── 2016_(May)_New_York_City_Subway_Routes.zip
│   ├── 2016_(May)_New_York_City_Subway_Station_Entrances.json
│   ├── 2016_(May)_New_York_City_Subway_Station_Entrances.zip
│   ├── README.md
│   ├── df_shuffle.csv
│   └── df_shuffle.pkl
├── Filter
│   ├── README.md
│   └── Sjoin_Pyspark_5_ServiceTime.ipynb
├── Interactive_Time_Series_Plot
│   ├── Interactive\ Time\ Series\ Plot\ -\ by\ hour,\ Jan\ 2016.ipynb
│   ├── README.md
│   └── jan_hour.csv
├── LICENSE
├── Output
│   ├── 1_dumbo_run_ys.py
│   ├── 2_taxirun.sh
│   ├── 3_raw
│   │   ├── apr
│   │   ├── aug
│   │   ├── dec
│   │   ├── feb
│   │   ├── jan
│   │   ├── jul
│   │   ├── jun
│   │   ├── mar
│   │   ├── may
│   │   ├── nov
│   │   ├── oct
│   │   └── sep
│   ├── 4_clean_raw_data.ipynb
│   ├── 5_csv
│   │   ├── apr.csv
│   │   ├── aug.csv
│   │   ├── dec.csv
│   │   ├── feb.csv
│   │   ├── jan.csv
│   │   ├── jul.csv
│   │   ├── jun.csv
│   │   ├── mar.csv
│   │   ├── may.csv
│   │   ├── nov.csv
│   │   ├── oct.csv
│   │   └── sep.csv
│   ├── 6_Analysis\ of\ yellow\ cab\ trips\ along\ subway\ line.ipynb
│   ├── 7_plots
│   │   ├── LINE\ 3\ &2.png
│   │   ├── LINE\ J\ &\ Z.png
│   │   ├── anomaly\ C.png
│   │   ├── anomaly\ July\ 2015.png
│   │   ├── anomaly\ June\ 2015.png
│   │   ├── anomaly\ c\ zoom\ in.png
│   │   ├── boxplot\ outliers.png
│   │   ├── histogram\ line\ C\ &\ 1\ .png
│   │   ├── histogram\ of\ all\ trips.png
│   │   ├── june\ 18\ 19,\ 2015.png
│   │   ├── outliers\ time\ series.png
│   │   ├── time\ series\ all\ year.png
│   │   └── time\ series\ jan\ 23\ detail.png
│   └── README.md
├── README.md
├── Run
│   ├── Dumbo_Run.ipynb
│   ├── README.md
│   └── dumbo_run.py
├── Sjoin
│   ├── README.md
│   ├── Sjoin_Pyspark_1.ipynb
│   ├── Sjoin_Pyspark_1.py
│   ├── Sjoin_Pyspark_2.ipynb
│   ├── Sjoin_Pyspark_2.py
│   ├── Sjoin_Pyspark_3_byWeekday.ipynb
│   ├── Sjoin_Pyspark_4_byHour.ipynb
│   ├── Sjoin_Pyspark_4_byWDandHour.ipynb
│   └── sjoin.py
├── Use\ IPython\ notebook\ interactively\ on\ a\ HPC\ system
├── Viz
│   ├── 1_buffer.png
│   ├── 2_pick_up.png
│   ├── 3_drop_off.png
│   ├── 4_taxi_route.png
│   └── services.png
└── docs
    
```