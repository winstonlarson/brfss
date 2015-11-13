#BRFSS cleaning example

The BRFSS is a fairly large and messy dataset. To put it into a useable format, you have to do a bit of cleaning and massaging. This Notebook demonstrates cleaning the data bit by bit for 2014. Scripts for every year are in the `cleaning_code` folder. I had to do a separate script for each year because the codebooks change slightly nearly every year, and it's just enough to make it a real headache.

Pandas is a terrific tool for data cleaning and manipulation, and that's what I use here.

##Getting started
Let's start by importing our libraries. We'll be using Pandas and Numpy.

```python
import numpy as np
import pandas as pd
```

Next, we'll set our year variable (2014), which made it easy to change when I had to copy scripts for each year.

```python
year = '2014'
```

##Reading in the data

Let's use Pandas to read in the `.csv` of the raw data for 2014. This isn't available on GitHub because the file is too big. Also, since the file is so big, you might get a warning.

Since we didn't specify UTF-8 encoding in the R script for creating the `.csv`'s, we need to specify the encoding, which somehow ends up being the interesting choice of "cp1252." That little tidbit right there was a couple hours worth of Googling.

```python
df = pd.read_csv('data/brfss' + year + '.csv', encoding='cp1252')
```
```
/Users/wlarson/anaconda/lib/python3.4/site-packages/pandas/io/parsers.py:1130: DtypeWarning: Columns (121) have mixed types. Specify dtype option on import or set low_memory=False.
    data = self._reader.read(nrows)
```

Let's take a quick look at what we have here. As you can see, this is a rather large data set.

```python
df
```

<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>x.state</th>
      <th>fmonth</th>
      <th>idate</th>
      <th>imonth</th>
      <th>iday</th>
      <th>iyear</th>
      <th>dispcode</th>
      <th>seqno</th>
      <th>x.psu</th>
      <th>...</th>
      <th>x.fobtfs</th>
      <th>x.crcrec</th>
      <th>x.aidtst3</th>
      <th>x.impeduc</th>
      <th>x.impmrtl</th>
      <th>x.imphome</th>
      <th>rcsbrac1</th>
      <th>rcsrace1</th>
      <th>rchisla1</th>
      <th>rcsbirth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0     </th>
      <td>      1</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1172014</td>
      <td>  1</td>
      <td> 17</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000001</td>
      <td> 2014000001</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1     </th>
      <td>      2</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1072014</td>
      <td>  1</td>
      <td>  7</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000002</td>
      <td> 2014000002</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2     </th>
      <td>      3</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1092014</td>
      <td>  1</td>
      <td>  9</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000003</td>
      <td> 2014000003</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3     </th>
      <td>      4</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1072014</td>
      <td>  1</td>
      <td>  7</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000004</td>
      <td> 2014000004</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 6</td>
      <td> 3</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4     </th>
      <td>      5</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1162014</td>
      <td>  1</td>
      <td> 16</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000005</td>
      <td> 2014000005</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5     </th>
      <td>      6</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1022014</td>
      <td>  1</td>
      <td>  2</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000006</td>
      <td> 2014000006</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6     </th>
      <td>      7</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1062014</td>
      <td>  1</td>
      <td>  6</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000007</td>
      <td> 2014000007</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  1</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7     </th>
      <td>      8</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1112014</td>
      <td>  1</td>
      <td> 11</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000008</td>
      <td> 2014000008</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  1</td>
      <td> 4</td>
      <td> 2</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8     </th>
      <td>      9</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1022014</td>
      <td>  1</td>
      <td>  2</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000009</td>
      <td> 2014000009</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 3</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9     </th>
      <td>     10</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1082014</td>
      <td>  1</td>
      <td>  8</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000010</td>
      <td> 2014000010</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10    </th>
      <td>     11</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1072014</td>
      <td>  1</td>
      <td>  7</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000011</td>
      <td> 2014000011</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11    </th>
      <td>     12</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1022014</td>
      <td>  1</td>
      <td>  2</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000012</td>
      <td> 2014000012</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12    </th>
      <td>     13</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1132014</td>
      <td>  1</td>
      <td> 13</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000013</td>
      <td> 2014000013</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13    </th>
      <td>     14</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1042014</td>
      <td>  1</td>
      <td>  4</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000014</td>
      <td> 2014000014</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 6</td>
      <td> 2</td>
      <td> 3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14    </th>
      <td>     15</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1022014</td>
      <td>  1</td>
      <td>  2</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000015</td>
      <td> 2014000015</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 3</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15    </th>
      <td>     16</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1062014</td>
      <td>  1</td>
      <td>  6</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000016</td>
      <td> 2014000016</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 5</td>
      <td> 3</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16    </th>
      <td>     17</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1072014</td>
      <td>  1</td>
      <td>  7</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000017</td>
      <td> 2014000017</td>
      <td>...</td>
      <td>NaN</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17    </th>
      <td>     18</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1072014</td>
      <td>  1</td>
      <td>  7</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000018</td>
      <td> 2014000018</td>
      <td>...</td>
      <td>  2</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 5</td>
      <td> 3</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18    </th>
      <td>     19</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1042014</td>
      <td>  1</td>
      <td>  4</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000019</td>
      <td> 2014000019</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19    </th>
      <td>     20</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1082014</td>
      <td>  1</td>
      <td>  8</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000020</td>
      <td> 2014000020</td>
      <td>...</td>
      <td>NaN</td>
      <td>  1</td>
      <td>  2</td>
      <td> 3</td>
      <td> 4</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20    </th>
      <td>     21</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1092014</td>
      <td>  1</td>
      <td>  9</td>
      <td> 2014</td>
      <td> 1200</td>
      <td> 2014000021</td>
      <td> 2014000021</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td> 2</td>
      <td> 2</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21    </th>
      <td>     22</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1032014</td>
      <td>  1</td>
      <td>  3</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000022</td>
      <td> 2014000022</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 6</td>
      <td> 4</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22    </th>
      <td>     23</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1132014</td>
      <td>  1</td>
      <td> 13</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000023</td>
      <td> 2014000023</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 5</td>
      <td> 2</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23    </th>
      <td>     24</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1152014</td>
      <td>  1</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000024</td>
      <td> 2014000024</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  1</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24    </th>
      <td>     25</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1072014</td>
      <td>  1</td>
      <td>  7</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000025</td>
      <td> 2014000025</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 5</td>
      <td> 2</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25    </th>
      <td>     26</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1142014</td>
      <td>  1</td>
      <td> 14</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000026</td>
      <td> 2014000026</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 2</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26    </th>
      <td>     27</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1112014</td>
      <td>  1</td>
      <td> 11</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000027</td>
      <td> 2014000027</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27    </th>
      <td>     28</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1082014</td>
      <td>  1</td>
      <td>  8</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000028</td>
      <td> 2014000028</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28    </th>
      <td>     29</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1072014</td>
      <td>  1</td>
      <td>  7</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000029</td>
      <td> 2014000029</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 4</td>
      <td> 3</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29    </th>
      <td>     30</td>
      <td>  1</td>
      <td>  1</td>
      <td>  1142014</td>
      <td>  1</td>
      <td> 14</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014000030</td>
      <td> 2014000030</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  9</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>464634</th>
      <td> 464635</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005959</td>
      <td> 2014005959</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  1</td>
      <td> 6</td>
      <td> 2</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464635</th>
      <td> 464636</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12132014</td>
      <td> 12</td>
      <td> 13</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005960</td>
      <td> 2014005960</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 5</td>
      <td> 5</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464636</th>
      <td> 464637</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12112014</td>
      <td> 12</td>
      <td> 11</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005961</td>
      <td> 2014005961</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 2</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464637</th>
      <td> 464638</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12142014</td>
      <td> 12</td>
      <td> 14</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005962</td>
      <td> 2014005962</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 5</td>
      <td> 1</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464638</th>
      <td> 464639</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005963</td>
      <td> 2014005963</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 6</td>
      <td> 2</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464639</th>
      <td> 464640</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12122014</td>
      <td> 12</td>
      <td> 12</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005964</td>
      <td> 2014005964</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464640</th>
      <td> 464641</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12122014</td>
      <td> 12</td>
      <td> 12</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005965</td>
      <td> 2014005965</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 5</td>
      <td> 5</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464641</th>
      <td> 464642</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005966</td>
      <td> 2014005966</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  1</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464642</th>
      <td> 464643</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12142014</td>
      <td> 12</td>
      <td> 14</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005967</td>
      <td> 2014005967</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 2</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464643</th>
      <td> 464644</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12152014</td>
      <td> 12</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1200</td>
      <td> 2014005968</td>
      <td> 2014005968</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td> 4</td>
      <td> 1</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464644</th>
      <td> 464645</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12132014</td>
      <td> 12</td>
      <td> 13</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005969</td>
      <td> 2014005969</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  1</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464645</th>
      <td> 464646</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005970</td>
      <td> 2014005970</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 4</td>
      <td> 2</td>
      <td> 3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464646</th>
      <td> 464647</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12122014</td>
      <td> 12</td>
      <td> 12</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005971</td>
      <td> 2014005971</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 5</td>
      <td> 5</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464647</th>
      <td> 464648</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12152014</td>
      <td> 12</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005972</td>
      <td> 2014005972</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 2</td>
      <td> 3</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464648</th>
      <td> 464649</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12152014</td>
      <td> 12</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1200</td>
      <td> 2014005973</td>
      <td> 2014005973</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td> 5</td>
      <td> 5</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464649</th>
      <td> 464650</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12152014</td>
      <td> 12</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005974</td>
      <td> 2014005974</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464650</th>
      <td> 464651</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005975</td>
      <td> 2014005975</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464651</th>
      <td> 464652</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12152014</td>
      <td> 12</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005976</td>
      <td> 2014005976</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464652</th>
      <td> 464653</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12112014</td>
      <td> 12</td>
      <td> 11</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005977</td>
      <td> 2014005977</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 5</td>
      <td> 5</td>
      <td> 3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464653</th>
      <td> 464654</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12162014</td>
      <td> 12</td>
      <td> 16</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005978</td>
      <td> 2014005978</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  1</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464654</th>
      <td> 464655</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12152014</td>
      <td> 12</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005979</td>
      <td> 2014005979</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 5</td>
      <td> 3</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464655</th>
      <td> 464656</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12122014</td>
      <td> 12</td>
      <td> 12</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005980</td>
      <td> 2014005980</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  2</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464656</th>
      <td> 464657</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12162014</td>
      <td> 12</td>
      <td> 16</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005981</td>
      <td> 2014005981</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 6</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464657</th>
      <td> 464658</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005982</td>
      <td> 2014005982</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 4</td>
      <td> 2</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464658</th>
      <td> 464659</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005983</td>
      <td> 2014005983</td>
      <td>...</td>
      <td>  2</td>
      <td>  1</td>
      <td>  2</td>
      <td> 5</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464659</th>
      <td> 464660</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12112014</td>
      <td> 12</td>
      <td> 11</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005984</td>
      <td> 2014005984</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464660</th>
      <td> 464661</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005985</td>
      <td> 2014005985</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  2</td>
      <td> 6</td>
      <td> 2</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464661</th>
      <td> 464662</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12152014</td>
      <td> 12</td>
      <td> 15</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005986</td>
      <td> 2014005986</td>
      <td>...</td>
      <td>  2</td>
      <td>  2</td>
      <td>  1</td>
      <td> 5</td>
      <td> 1</td>
      <td> 2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464662</th>
      <td> 464663</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12132014</td>
      <td> 12</td>
      <td> 13</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005987</td>
      <td> 2014005987</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 4</td>
      <td> 1</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>464663</th>
      <td> 464664</td>
      <td> 72</td>
      <td> 11</td>
      <td> 12102014</td>
      <td> 12</td>
      <td> 10</td>
      <td> 2014</td>
      <td> 1100</td>
      <td> 2014005988</td>
      <td> 2014005988</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>  1</td>
      <td> 6</td>
      <td> 6</td>
      <td> 1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>464664 rows × 280 columns</p>
</div>

```python
print("Number of rows:", len(df))
print("Number of columns (variables in the survey):", len(df.columns))
print(df.columns)
```

```
Number of rows: 464664
Number of columns (variables in the survey): 280
Index(['Unnamed: 0', 'x.state', 'fmonth', 'idate', 'imonth', 'iday', 'iyear', 'dispcode', 'seqno', 'x.psu', 'ctelenum', 'pvtresd1', 'colghous', 'stateres', 'ladult', 'numadult', 'nummen', 'numwomen', 'genhlth', 'physhlth', 'menthlth', 'poorhlth', 'hlthpln1', 'persdoc2', 'medcost', 'checkup1', 'exerany2', 'sleptim1', 'cvdinfr4', 'cvdcrhd4', 'cvdstrk3', 'asthma3', 'asthnow', 'chcscncr', 'chcocncr', 'chccopd1', 'havarth3', 'addepev2', 'chckidny', 'diabete3', 'diabage2', 'lastden3', 'rmvteth3', 'veteran3', 'marital', 'children', 'educa', 'employ1', 'income2', 'weight2', 'height3', 'numhhol2', 'numphon2', 'cpdemo1', 'internet', 'renthom1', 'sex', 'pregnant', 'qlactlm2', 'useequip', 'blind', 'decide', 'diffwalk', 'diffdres', 'diffalon', 'smoke100', 'smokday2', 'stopsmk2', 'lastsmk2', 'usenow3', 'alcday5', 'avedrnk2', 'drnk3ge5', 'maxdrnks', 'flushot6', 'flshtmy2', 'pneuvac3', 'shingle2', 'fall12mn', 'fallinj2', 'seatbelt', 'drnkdri2', 'hadmam', 'howlong', 'profexam', 'lengexam', 'hadpap2', 'lastpap2', 'hadhyst2', 'pcpsaad2', 'pcpsadi1', 'pcpsare1', 'psatest1', 'psatime', 'pcpsars1', 'bldstool', 'lstblds3', 'hadsigm3', 'hadsgco1', 'lastsig3', ...], dtype='object')
```

## Collecting our variables of interest

Great, so we have a lot of rows and 280 columns. We're just trying to find some basic demographic information. If we look through the codebook, we can find those variable names. Note that an underscore in the codebook is the same as `x.` in the data, and that variables are all caps in the codebook but lowercase in the data.

- **Income:** income2
- **Race:** x.race
- **State:** x.state
- **Age:** x.ageg5yr
- **Sex:** sex
- **Height:** height3
- **Weight:** weight2

We'll use height and weight to calculate BMI. In later years (like 2014), the good people at the CDC calculate that and include it as a separate variable, but in earlier years, they weren't so advanced, so we'll always just grab height and weight and calculate it ourselves.

We can use Pandas to easily grab the columns we want. We're going to grab those columns as Pandas Series, clean them up, and then piece everything back together as a master DataFrame.

```python
income = df['income2']
race = df['x.race']
state = df['x.state']
age = df['x.ageg5yr']
sex = df['sex']
height = df['height3']
weight = df['weight2']
```

If we look at one of these variables, we can get a peek at the way the survey data is coded.

```python
income
```

```
0      7
1      4
2      7
3      5
4      4
5      6
6      8
7      1
8     77
9      7
10    77
11     6
12     8
13     5
14     5
...
464649     8
464650     3
464651     1
464652     6
464653     5
464654     1
464655     2
464656    99
464657     2
464658     5
464659     6
464660     7
464661    99
464662     2
464663     4
Name: income2, Length: 464664, dtype: float64
```

##Cleaning up a column: Income

We'll start with cleaning up the income data. Looking at the codebook, the codes are:

* 1: <$10k
* 2: $10k - $15k
* 3: $15k - $20k
* 4: $20k - $25k
* 5: $25k - $35k
* 6: $35k - $50k
* 7: $50k - $75k
* 8: >$75k
* 77: Unknown
* 99: Refused

We're going to group 77 and 99 together as `np.nan`, and we're going to group 7 and 8 together as simply >$50k (in earlier BRFSS years, it stops at >$50K, rather than including the $50k-$75k and >$75k groups)

Pandas makes it easy to use a dictionary for replacement, so we'll put these codes into a dictionary.

```python
income_replace = {1:'<10k', 2:'10k-15k', 3:'15k-20k', 4:'20k-25k', 5:'25k-35k', 6:'35k-50k', 7:'>50k', 8:'>50k', 77:np.nan, 99:np.nan}
```

##Cleaning the other columns

Next, we'll clean the race column. If you are working with historical data, this is the trickiest column. The name of the variable, the meanings of the codes, and the groups represented change frequently over the years, and sometimes in subtle ways. Being able to use historical data is why my dictionary ends up grouping some things together that the 2014 dataset breaks out. See the codebook for more details.

```python
race_replace = {1:'white', 2:'black', 3:'native american', 4:'asian/pacific islander', 5:'asian/pacific islander', 6:'other/multiracial', 7:'other/multiracial', 8:'hispanic', 9:'refused/unknown'}
```

We'll skip the state column for now. It's represented as a FIPS statecode, and you can find more info on Wikipedia: [FIPS codes](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code).

Let's get the age and sex columns mapped.

```python
age_replace = {1:'18-24', 2:'25-29', 3:'30-34', 4:'35-39', 5:'40-44', 6:'45-49', 7:'50-54', 8:'55-59', 9:'60-64', 10:'65-69', 11:'70-74', 12:'75-79', 13:'80+', 14:np.nan}
sex_replace = {1:'male', 2:'female'}
```

The height and weight columns are a little trickier to deal with, so we'll handle those in a minute.

##Using Pandas to do the replacement
Since we've got our dictionaries of codes mapped to values, we can let Pandas do the heavy lifting of cleaning up our columns.

```python
income = income.replace(income_replace)
race = race.replace(race_replace)
age = age.replace(age_replace)
sex = sex.replace(sex_replace)
```

Let's check out one of our cleaned up columns. Now it is beautiful and easy-to-use:

```python
income
```

```
0        >50k
1     20k-25k
2        >50k
3     25k-35k
4     20k-25k
5     35k-50k
6        >50k
7        <10k
8         NaN
9        >50k
10        NaN
11    35k-50k
12       >50k
13    25k-35k
14    25k-35k
...
464649       >50k
464650    15k-20k
464651       <10k
464652    35k-50k
464653    25k-35k
464654       <10k
464655    10k-15k
464656        NaN
464657    10k-15k
464658    25k-35k
464659    35k-50k
464660       >50k
464661        NaN
464662    10k-15k
464663    20k-25k
Name: income2, Length: 464664, dtype: object

##Cleaning the height and weight columns

Okay, now let's work with the height and weight data. We'll start by noting that 7777 and 9999 are 'unknown' or 'replaced' codes, so we'll NaN those right away. Also, in later years, the survey gave the option of taking height and weight in metric and imperial units. Earlier on, it's all imperial, so we'll make and option for using the metric system (which is denoted differently in the codes). Finally, our max weight changes over the years also, so we'll set that now to 999 lbs.

```python
hw_replace = {7777:np.nan, 9999:np.nan}
metric = True
max_weight = 999
height = height.replace(hw_replace)
weight = weight.replace(hw_replace)
```

###Dealing with the height codes

Alright, now we can tackle processing the height column. In the codebook, we see that things are a little funny.

* 200-711: Height in ft/in (\_|\_ \_) - i.e. the first digit is feet, the second and third digits are inches. So 509 is 5' 9''
* 9000-9998: Height in m/cm (9\_|\_ \_)

To handle this, we are going to run through the height column, grab the value, and turn it into a string. We'll pop the first token and save it as the feet, save the other two tokens as the inches, and then we will cast everything as floats and convert the result to inches and then to meters.

If the number is greather than 9000 and our metric toggle is `True`, then we know that it is a metric value, and we'll do a similar process.

_**Note:** I noticed that if I do all of this in Pandas, it is very slow. It's much faster to put the Series into a python list, do the operations and append the result to a new list, and then save the result back to a Series._

```python
height = height.tolist()
new_height = []
for row in height:
    h = str(row)

    if row < 1: # If the height is 0, it isn't real
        meters = np.nan

    elif row < 712:
        feet = float(h[0])
        inches = float(h[1:])
        if inches > 12: # Catches an error by the surveyor: no one is 5' 13" tall
            meters = np.nan
        else:
            inches = inches + feet*12
            meters = inches * 0.0254

    elif row < 9999 and row >= 9000 and metric:
        meters = float(h[1])+float(h[2:])*0.01
        if meters == 0: # If the height is 0, it isn't real
            meters = np.nan

    else: # If you've gotten this far, give up. You're NaN
        meters = np.nan

    new_height.append(meters)
```

Now let's do something similar for the weight. Except this time, we don't have to play fun games with strings for the imperial units (we still do with the metric units).

```python
weight = weight.tolist()
new_weight = []
for row in weight:

    if row < 10: # No person ages 18-99 should weigh 10 lbs.
        kg = np.nan

    elif row < max_weight:
        kg = row * 0.453592

    elif row < 9999 and metric:
        w = str(row)
        kg = float(w[1:])
        if kg < 10: # Again, no person 18-99 should weigh 10 kgs. And yes, I know that 10 lbs != 10 kgs, but whatever
            kg = np.nan

    else:
        kg = np.nan

    new_weight.append(kg)
```

###Calculating BMI

We've got height and weight in metric units. Let's compute the BMI, which is `bmi = w / h^2`.

BMIs that are less than 10 or greater than 200 are possible, but highly unlikely. At the moment, I'm not terribly interested in these outliers (which are honestly more likely the result of error than true BMIs anyway). We will exclude them.

```python
bmi = []
for h, w in zip(new_height, new_weight):
    b = w/(h*h)
    if b < 10 or b > 200:
        b = np.nan
    bmi.append(b)
```

We'll quickly save the height, weight, and BMI back to Pandas Series.

```python
height = pd.Series(new_height)
weight = pd.Series(new_weight)
bmi = pd.Series(bmi)
```

##Saving our clean data

We're almost there! Now, let's take all of our cleaned up columns and put them back together as a single DataFrame and name the columns something easy to understand. We'll save that out to a `.csv`.

```python
brfss_out = pd.concat([income, race, state, age, sex, height, weight, bmi], axis=1)
brfss_out.columns = ['income', 'race', 'state', 'age', 'sex', 'height', 'weight', 'bmi']
brfss_out.to_csv('brfss' + year + 'clean.csv')
```

And now, at long last, we are finished. We have a cleaned up set of demographic data in `brfss2014clean.csv`. It is in the same format as what we can spit out for all of the other years of the BRFSS 1987-2014, so it will be easy to run analyses across all the years.
