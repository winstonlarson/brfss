options(stringsAsFactors=F, scipen = 999)

pkg = 'Hmisc'
if (!require(pkg, character.only = TRUE)) {
  install.packages(pkg)
  library(pkg, character.only = TRUE)
}

brfss <- sasxport.get("BRFSS_1985.XPT")
write.csv(brfss, file = "brfss1985.csv")

brfss <- sasxport.get("BRFSS_1986.XPT")
write.csv(brfss, file = "brfss1986.csv")

brfss <- sasxport.get("BRFSS_1987.XPT")
write.csv(brfss, file = "brfss1987.csv")

brfss <- sasxport.get("BRFSS_1989.XPT")
write.csv(brfss, file = "brfss1989.csv")

brfss <- sasxport.get("BRFSS_1990.XPT")
write.csv(brfss, file = "brfss1990.csv")

brfss <- sasxport.get("BRFSS_1991.XPT")
write.csv(brfss, file = "brfss1991.csv")

brfss <- sasxport.get("BRFSS_1992.XPT")
write.csv(brfss, file = "brfss1992.csv")

brfss <- sasxport.get("BRFSS_1993.XPT")
write.csv(brfss, file = "brfss1993.csv")

brfss <- sasxport.get("BRFSS_1994.XPT")
write.csv(brfss, file = "brfss1994.csv")

brfss <- sasxport.get("BRFSS_1996.XPT")
write.csv(brfss, file = "brfss1996.csv")

brfss <- sasxport.get("BRFSS_1997.XPT")
write.csv(brfss, file = "brfss1997.csv")

brfss <- sasxport.get("BRFSS_1998.XPT")
write.csv(brfss, file = "brfss1998.csv")

brfss <- sasxport.get("BRFSS_1999.XPT")
write.csv(brfss, file = "brfss1999.csv")

brfss <- sasxport.get("BRFSS_2000.XPT")
write.csv(brfss, file = "brfss2000.csv")

brfss <- sasxport.get("BRFSS_2001.XPT")
write.csv(brfss, file = "brfss2001.csv")

brfss <- sasxport.get("BRFSS_2002.XPT")
write.csv(brfss, file = "brfss2002.csv")

brfss <- sasxport.get("BRFSS_2003.XPT")
write.csv(brfss, file = "brfss2003.csv")

brfss <- sasxport.get("BRFSS_2004.XPT")
write.csv(brfss, file = "brfss2004.csv")

brfss <- sasxport.get("BRFSS_2005.XPT")
write.csv(brfss, file = "brfss2005.csv")

brfss <- sasxport.get("BRFSS_2006.XPT")
write.csv(brfss, file = "brfss2006.csv")

brfss <- sasxport.get("BRFSS_2007.XPT")
write.csv(brfss, file = "brfss2007.csv")

brfss <- sasxport.get("BRFSS_2008.XPT")
write.csv(brfss, file = "brfss2008.csv")

brfss <- sasxport.get("BRFSS_2009.XPT")
write.csv(brfss, file = "brfss2009.csv")

brfss <- sasxport.get("BRFSS_2010.XPT")
write.csv(brfss, file = "brfss2010.csv")

brfss <- sasxport.get("BRFSS_2011.XPT")
write.csv(brfss, file = "brfss2011.csv")

brfss <- sasxport.get("BRFSS_2012.XPT")
write.csv(brfss, file = "brfss2012.csv")

brfss <- sasxport.get("BRFSS_2013.XPT")
write.csv(brfss, file = "brfss2013.csv")

brfss <- sasxport.get("BRFSS_2014.XPT")
write.csv(brfss, file = "brfss2014.csv")
