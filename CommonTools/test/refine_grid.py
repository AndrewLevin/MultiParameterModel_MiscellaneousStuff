#! /usr/bin/env python

import sys
import os

import ROOT
from ROOT import TFile, TF2, TH2D

nGridPointsForNewF=20

#sigFile='/home/anlevin/UserCode/VBS/smurf/histo_nice8TeV_fm1fm2.root'
#output_file_name='input_forNewF_fm1fm2'

if (len(sys.argv) != 3):
    print "format: python.py refine_grid input_file_name output_file_name"
    print "exiting"
    sys.exit(0)

sigFile=sys.argv[1]
output_file_name=sys.argv[2]

print "using input_file: "+ sigFile
print "using output_file: "+ output_file_name

sigObj='bin_content_lam_dk_1'

sigFile = TFile.Open(sigFile)

par1GridMin=-2.5
par2GridMin=-2.5
par1GridMax=2.5
par2GridMax=2.5

#theBaseData = TH2F('theBaseData_'+section+'_'+str(i),'Base Histogram for RooDataHist',
#                   nGridParBins,par1GridMin,par1GridMax,
#                   nGridParBins,par2GridMin,par2GridMax)

theBaseData = sigFile.Get(sigObj)

#sigObj.Draw(par2Name+'_grid:'+par1Name+'_grid >> theBaseData_'+section+'_'+str(i),'','goff')
    
func = TF2('fittingFunction','[0] + [1]*x + [2]*y + [3]*x*y + [4]*x*x + [5]*y*y',
           par1GridMin,par1GridMax,
           par2GridMin,par2GridMax)

theBaseData.Fit(func,'R0','')

#getattr(ws,'import')(theBaseData)

outfile_newF = TFile.Open(output_file_name,'RECREATE')

newFormatInput = TH2D('bin_content_lam_dk_1'
                      ,'bincontent',
                      nGridPointsForNewF,par1GridMin,par1GridMax,
                      nGridPointsForNewF,par2GridMin,par2GridMax)


for bin_x in range(1,nGridPointsForNewF+1):
    for bin_y in range(1,nGridPointsForNewF+1):
        par1_value=newFormatInput.GetXaxis().GetBinCenter(bin_x)
        par2_value=newFormatInput.GetYaxis().GetBinCenter(bin_y)
        yield_bin=func.GetParameter(0)+func.GetParameter(1)*par1_value+func.GetParameter(2)*par2_value+func.GetParameter(3)*par1_value*par2_value+func.GetParameter(4)*par1_value*par1_value+func.GetParameter(5)*par2_value*par2_value
        newFormatInput.SetBinContent(bin_x,bin_y,yield_bin)
        
newFormatInput.Clone('bin_content_lam_dg_1').Write()

newFormatInput.Clone('bin_content_dk_dg_1').Write()

newFormatInput.Write()
