#!/bin/sh -x
################################################################################
####  UNIX Script Documentation Block
#                      .                                             .
# Script name:         copyefsoifiles.sh
# Script description:  copy files required for EFSOI from COMROT 
#
# Author:        Andrew Eichmann  Org: NCEP/EMC     Date: 2021-03-05 
#
# Abstract: This script copies the files required to run EFSOI executable
#           from COMROT that has generated 24/30 hour forecasts to staging
#           directory for testing purposes 
#
# $Id$
#
# Attributes:
#   Language: POSIX shell
#   Machine: Hera
#
################################################################################



COMROT=
STGDIR=

EDATE=2019111818
NENS=20
NDATE=/scratch1/NCEPDEV/global/Fanglin.Yang/save/VRFY/vsdb/nwprod/util/exec/ndate

PDATE=`${NDATE} -6 ${EDATE}`
VDATE=`${NDATE} +24 ${EDATE}`

EDATECYC="${EDATE:8:2}"
PDATECYC="${PDATE:8:2}"
VDATECYC="${VDATE:8:2}"

EDATEDIR=enkfgdas."${EDATE:0:8}"
PDATEDIR=enkfgdas."${PDATE:0:8}"
VDATEDIR=enkfgdas."${VDATE:0:8}"


echo $PDATE
echo $VDATE
echo $EDATECYC
echo $EDATEDIR

# set up 30 hour forecast

cd $STGDIR

if [ -d "$PDATEDIR" ]; then
    echo "$PDATEDIR exists."
else 
    echo "$PDATEDIR does not exist, creating it"
    mkdir $PDATEDIR
fi

cd $PDATEDIR

if [ -d "$PDATECYC" ]; then
    echo "$PDATECYC exists."
else 
    echo "$PDATECYC does not exist, creating it"
    mkdir $PDATECYC
fi

cd $PDATECYC

cp -vi $COMROT/$PDATEDIR/$PDATECYC/gdas.t${PDATECYC}z.atmf030.ensmean.* .
cp -vi $COMROT/$PDATEDIR/$PDATECYC/gdas.t${PDATECYC}z.atmf006.ensmean.* .


# set up 24 hour forecast

cd $STGDIR

if [ -d "$EDATEDIR" ]; then
    echo "$EDATEDIR exists."
else 
    echo "$EDATEDIR does not exist, creating it"
    mkdir $EDATEDIR
fi

cd $EDATEDIR

if [ -d "$EDATECYC" ]; then
    echo "$EDATECYC exists."
else 
    echo "$EDATECYC does not exist, creating it"
    mkdir $EDATECYC
fi

cd $EDATECYC

cp -vi $COMROT/$EDATEDIR/$EDATECYC/gdas.t${EDATECYC}z.atmf024.ensmean.* .
cp -vi $COMROT/$EDATEDIR/$EDATECYC/gdas.t${EDATECYC}z.atmf006.ensmean.* .
cp -vi $COMROT/$EDATEDIR/$EDATECYC/gdas.t${EDATECYC}z.abias_int.ensmean .



imem=1
while [[ $imem -le $NENS ]]; do
   member="mem"`printf %03i $imem`
   
   if [ -d "$member" ]; then
       echo "$member exists."
   else 
       echo "$member does not exist, creating it"
       mkdir $member
   fi

   cd $member

   cp -vi $COMROT/$EDATEDIR/$EDATECYC/$member/gdas.t${EDATECYC}z.atmf024.nemsio .  
   cp -vi $COMROT/$EDATEDIR/$EDATECYC/$member/gdas.t${EDATECYC}z.atmf024s.nemsio .  
 
   cd ..
   
   (( imem = $imem + 1 ))
done




