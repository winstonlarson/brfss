# brfss
Insights into health and behavior using data from the CDC

###BRFSS Introduction

Every year since 1984, government employees have called around the country and asked the people who pick up a series of probing questions about their health and what they're doing about it. While it may sound annoying, the CDC's Behavioral Risk Factor Surveillance System (BRFSS) provides a wealth of information about health and health-related behaviors in the United States. It is the largest and longest running health survey system in the world, and in its current incarnation, it covers over 400,000 adult interviews from all 50 states, the District of Columbia, and three territories. For more information about the survey itself, you should check out the [CDC BRFSS site](http://www.cdc.gov/brfss/).

The BRFSS is a rich source of information on how demographics, behaviors, and other risk factors can correlate with health. Many important population health studies and measures use the BRFSS as a key data source. For example, it is the source of the CDC's "Healthy Days" measurement, a key performance metric for the healthcare industry. 

Unfortunately, BRFSS data isn't exactly easy to deal with. Its breadth and structure have changed considerably over the years, and there are important sampling considerations that must be taken into account when using the data to draw conclusions. My goal is to build this repository over time to demonstrate how to use BRFSS data and some of the interesting correlations and associations that can be drawn from this data set using machine learning and statistical techniques.

###Getting BRFSS data

To get started, you'll want to download the data from the [BRFSS Annual Survey Data](http://www.cdc.gov/brfss/annual_data/annual_data.htm) page. There you can find links to each year the survey has been conducted. The data is available in `.XPT` (SAS Transport Format) or in `.ASCII` files. You should be warned that these are pretty big files, especially in more recent years. All together, the raw data is somewhere around 10GB.

The codebooks are available from the CDC for 1990-2014. I was able to find the codebooks for 1987-1989 from the [Washington State Department of Health](http://www.doh.wa.gov/DataandStatisticalReports/DataSystems/BehavioralRiskFactorSurveillanceSystemBRFSS/BRFSSQuestionnairesandCodebooks). You can also find all the codebooks in this repo (in the `codebooks` folder, of course).

It's easiest to use the files in Python if you convert them into `.csv` format. I haven't been able to find a robust solution for translating `.XPT` format data in Python, so I use an R script called `sas2csv.R` (I promise, it's the only R script in the repo). [By the way, if you know of a nice way to deal directly with this data in Python, I'd love to hear from you.] Downloading all the files and translating them into `.csv` is a pain, so I've done it for you. Since the `.csv` files are too large to host on GitHub, I'm making them all (1984-2014) available through my AWS account, and you can find them  [here](https://www.amazon.com/clouddrive/share/HAfuNnNSbFqKmdyuodrVAQMpgcyqoFACuBoKWIqoWeG?ref_=cd_ph_share_link_copy).

###Cleaning BRFSS data
A quick flip through the codebooks quicky makes it clear that BRFSS data is not useful right out of the box. You'll have to do some heavy-duty cleaning to get what you want. And watchout: the codes and variable names can change subtly from year to year, so be certain to check the codebook for every year of interest.

I started by grabbing and cleaning the basic demographic data available for each respondant. Not only does this show how to clean and use BRFSS data, but you could for example see if the demographics of the survey change over time. I ended up grabbing the income group, race, state, age group, sex, and bmi of each respondant. 

Due to the differences in codes over time, the easiest way for me to clean the data was to make a separate script for each year's data set. The scripts read in the entire data set for the year, grab the variables of interest, replace the codes with meaningful data, and save it back out in a standardized format as a `.csv`. You can find the scripts for each year in the `cleaning_code` folder. Since this is a complicated and arduous process, I have detailed my methods for cleaning up an example year (2014) in an iPython notebook.

Since all of the years now have clean tables that behave the same way, when I want to do analysis across multiple years, it's a much simpler exercise of reading back in the cleaned tables and easily examining my variables of interest.
