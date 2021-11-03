

#d To run, $ Rscript generate_ascii.r
#d use flag -h to see options

#d R code to create an ASCII map(?) of popuolation density for a shapefile.
#d Pop data comes from Columbia's pop thing
#d (https://sedac.ciesin.columbia.edu/data/collection/gpw-v4)
#d or facebook data for social good's population estimates as these are higher res
#d Shapefiles are UK local authorities.
#d (https://geoportal.statistics.gov.uk/datasets/local-authority-districts-december-2019-boundaries-uk-bfc)

#d Warning: Current implementation has a heavy relaiance on UK ONS data. e.g. use MSOAs to decide on shapefiles to use
#d            Either facebook data or Columbia are able to be altered relatively easily for different geographies.

library(rgdal)
library(raster)
library(ggplot2)
library(sp)
library(rgeos)
library(maptools)
library(sf)
library(snakecase)
library(optparse)

#d##########
#d Options #
#d##########
data_dir = '/home/dan/Hadean/Innovation/CovidABM/id_spatial_sim/data/'
option_list = list(
  make_option(c('-g','--gpwPath'),type="character",default=paste(data_dir,'gpw-v4-population-density-rev11_2020_30_sec_asc',sep=''),help="directory of gpw asc files",metavar="character"),
  make_option(c('-m','--msoaPath'),type="character",default=paste(data_dir,'/msoa_shapefile/Middle_Layer_Super_Output_Areas_(December_2011)_Boundaries.shp',sep=''),help='MSOA shapefile path',metavar='character'),
  make_option(c('-l','--msoaListPath'),type="character",default='./msoaLists/leicstershire_msoa.csv',help='path for CSV of MSOA ids to use',metavar='character'),
  make_option(c('-o','--outPath'),type="character",default='./map.asc',help='Output path',metavar='character'),
  make_option(c("-f", "--fcb"), action = "store_true", default = FALSE,help = "Bool to use facebook data rather than Columbia")
)
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

#d#################
#d Load world pop #
#d#################
#d Create a raster, c, to compare with a region

#d This file is linked in line 3.
if (opt$fcb){
  c_merged <- raster(read.asciigrid('../../data/population_gbr_2019-07-01.asc'))
} else{
  c2 <- raster(read.asciigrid(paste(opt$gpwPath,"/gpw_v4_population_density_rev11_2020_30_sec_2.asc",sep='')))
  c3 <- raster(read.asciigrid(paste(opt$gpwPath,"/gpw_v4_population_density_rev11_2020_30_sec_3.asc",sep='')))
  #d Merge their raster's into one raster.
  #d Rasters seem to be simpler versions of ascii graphs that make them way more maliable.
  c_merged <- merge(c2,c3)
  rm(c2,c3) #d remove the mega loaded files to save space
}

#d#####################################
#d Load MSOA shapefiles #
#d#####################################
#d Linked line 5
shp <- st_read(opt$msoaPath)
shpLL <- st_transform(shp, "+proj=longlat +ellps=WGS84 +datum=WGS84")

#d##############################
#d Loop through the MSOAs read #
#d##############################
geom <- list()
i <- 1 #d an index used
y <- read.csv(opt$msoaListPath)['msoa11cd'][,]
for (msoa in y){
  geom[[i]] <- shpLL[shpLL$msoa11cd == msoa,]$geometry[[1]][[1]][1][[1]]
  i <- i + 1
}

#d e is used as a method to contrain the min rectangle to crop
p <- c()
e <- matrix(nrow = 2, ncol = 2)
  
#d originally 10k each, change to Inf
print('... creating polygon...')
e[1,1] = Inf
e[1,2] = -Inf
e[2,1] = Inf
e[2,2] = -Inf
for (g in geom) {
  p <- c(p, Polygon(g))
  e[1,1] = min(e[1,1], min(g[,1]))
  e[1,2] = max(e[1,2], max(g[,1]))
  e[2,1] = min(e[2,1], min(g[,2]))
  e[2,2] = max(e[2,2], max(g[,2]))
}
  
#d Don't really understand this bit
ps <- Polygons(p, "j")
sp <- SpatialPolygons(c(ps))
  
#d####################################
#d Only take the local authority pop #
#d####################################
c <- as(crop(c_merged, extent(e)), 'SpatialGridDataFrame')
grid <- c[!is.na(over(c, sp)),] #d Crops(?)
#d plot(grid)
writeRaster(raster(grid), opt$outPath, overwrite = TRUE)
