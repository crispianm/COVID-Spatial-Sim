chooseCRANmirror(ind=76)
install.packages('rgdal', type = "source", configure.args=c('--with-proj-include=/usr/local/include','--with-proj-lib=/usr/local/lib'))
install.packages("raster")
install.packages("ggplot2")
install.packages("sp")
install.packages("rgeos")
install.packages("maptools")
install.packages("sf")
install.packages("snakecase")
install.packages("optparse")
