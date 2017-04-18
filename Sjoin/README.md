## Doc

| Name                               | Notes / Data                |       |
| ---------------------------------- | --------------------------- | ----- |
| sjoin.py                           | Geopandas sjoin function    |       |
| Sjoin_Pyspark_1.ipynb / .py        | df_shuffle.csv              |       |
| Sjoin_Pyspark_2.ipynb / .py        | yellow_tripdata_2016-01.csv | 1.6 G |
| Sjoin_Pyspark_3\_byWeekday.ipynb   | df_shuffle.csv              |       |
| Sjoin_Pyspark\_4_byHour.ipynb      | df_shuffle.csv              |       |
| Sjoin_Pyspark\_4_byWDandHour.ipynb | df_shuffle.csv              |       |



## To-Do

- [ ] convert **.ipynb** into **.py**, then test them locally.
- [ ] take more factors like **weekend service changes** into consideration, if time permits. 



## Note

- If any …



## Result

*Run Sjoin_Pyspark_2.py locally in brand new MacBook Pro with TouchBar* ^ ^.

```python
sorted(counts, key=lambda x: x[1], reverse=True)
```

```python
[('1', 11795),
 (u'C', 8512),
 (u'E', 6547),
 ('6', 6464),
 (u'R', 6334),
 (u'F', 5823),
 (u'N', 5601),
 (u'M', 5282),
 (u'B', 4717),
 ('2', 4557),
 ('3', 4547),
 (u'A', 4421),
 (u'Q', 4300),
 (u'D', 3290),
 ('7', 2472),
 (u'L', 1507),
 ('5', 1270),
 ('4', 1256),
 (u'J', 422),
 (u'Z', 351),
 (u'GS', 191),
 (u'S', 182),
 (u'G', 105)]
```

![](http://web.mta.info/maps/images/subway_map_2400x2946opt.jpg)