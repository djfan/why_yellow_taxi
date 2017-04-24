| No.  | Name            | Dumbo? Local? | Data                                     | Note                                     |
| ---- | --------------- | ------------- | ---------------------------------------- | ---------------------------------------- |
| 1    | Dumbo_Run.ipynb | Local         | df_shuffle.csv                           |                                          |
| 2    |                 | Local         | (To-Do) yellow_tripdata_2016-01.csv in **NEW** MacBook |                                          |
| 3    | dumbo_run.py    | Dumbo         | df_shuffle.csv                           | Change **dir** (data path & output)      |
| 4    |                 | Dumbo         | yellow_tripdata_2016-01.csv              | I've Done this. Try it in your dumbo **dir**. |



### Task 1: Compare results in 1 and 3

```python
# Result in 1
counts  

[(u'A', 7),
 (u'Q', 5),
 (u'C', 11),
 (u'E', 7),
 (u'M', 2),
 (u'1', 12),
 (u'3', 2),
 (u'5', 1),
 (u'7', 1),
 (u'B', 1),
 (u'D', 1),
 (u'F', 4),
 (u'L', 3),
 (u'N', 5),
 (u'R', 5),
 (u'4', 1),
 (u'6', 7),
 (u'2', 2)]
```

```shell
# Result in 2
.out/
- _SUCCESS
- part-00000
- part-00001

hdfs dfs -cat out/part-00000

(u'A', 7)
(u'Q', 5)
(u'C', 11)
(u'E', 7)
(u'M', 2)
(u'1', 12)
(u'3', 2)
(u'5', 1)
(u'7', 1)

hdfs dfs -cat out/part-00001
(u'B', 1)
(u'D', 1)
(u'F', 4)
(u'L', 3)
(u'N', 5)
(u'R', 5)
(u'4', 1)
(u'6', 7)
(u'2', 2)

```



### Task 2: Compare results in 2 and 4

Question: I tried **2016-01.csv** in Dumbo, there're some wired line 'names' in the result, like 1,2 not '1' , '2' ?

- [ ] To-Do 



(If **TRUE** in **Task 2**)

### Task 3: Agg part-0000* for One Month, then Loop for all Months

- [ ] To-Do 



### (Optioanl) 

### Task 4: Make our script more pyspark-able

I just `sqlContext.read.load` to load entrances' gro-loactions, then use `geopandas` to deal with these geo-data. It should be some other ways to deal with it in spark.