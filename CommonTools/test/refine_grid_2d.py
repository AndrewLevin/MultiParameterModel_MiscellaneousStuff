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

print "input file: "+ sigFile
print "output file: "+ output_file_name

outfile_newF = TFile.Open(output_file_name,'RECREATE')

sigFile = TFile.Open(sigFile)

for key in sigFile.GetListOfKeys():
    anom_th2d=key.ReadObj()
    if type(anom_th2d)!=TH2D:
        print "expecting a TH2D, exiting"
        sys.exit(0)

#sigObj='aQGC_scaling1'

#theBaseData = TH2F('theBaseData_'+section+'_'+str(i),'Base Histogram for RooDataHist',
#                   nGridParBins,par1GridMin,par1GridMax,
#                   nGridParBins,par2GridMin,par2GridMax)

    #theBaseData = sigFile.Get(sigObj)

    par1GridMin=anom_th2d.GetXaxis().GetBinLowEdge(1)
    par2GridMin=anom_th2d.GetYaxis().GetBinLowEdge(1)
    par1GridMax=anom_th2d.GetXaxis().GetBinUpEdge(anom_th2d.GetNbinsX())
    par2GridMax=anom_th2d.GetYaxis().GetBinUpEdge(anom_th2d.GetNbinsY())
    print "par1GridMin:"+str(par1GridMin)
    print "par1GridMax:"+str(par1GridMax)
    
    func = TF2('fittingFunction','[0] + [1]*x + [2]*y + [3]*x*y + [4]*x*x + [5]*y*y',
               par1GridMin,par1GridMax,
               par2GridMin,par2GridMax)
    
    anom_th2d.Fit(func,'R0','')
    
    newFormatInput = TH2D(anom_th2d.GetName()
                      ,anom_th2d.GetTitle(),
                      nGridPointsForNewF,par1GridMin,par1GridMax,
                      nGridPointsForNewF,par2GridMin,par2GridMax)


    for bin_x in range(1,nGridPointsForNewF+1):
        for bin_y in range(1,nGridPointsForNewF+1):
            par1_value=newFormatInput.GetXaxis().GetBinCenter(bin_x)
            par2_value=newFormatInput.GetYaxis().GetBinCenter(bin_y)
            yield_bin=func.GetParameter(0)+func.GetParameter(1)*par1_value+func.GetParameter(2)*par2_value+func.GetParameter(3)*par1_value*par2_value+func.GetParameter(4)*par1_value*par1_value+func.GetParameter(5)*par2_value*par2_value
            newFormatInput.SetBinContent(bin_x,bin_y,yield_bin)
            
    outfile_newF.cd()
    newFormatInput.Write()
            
