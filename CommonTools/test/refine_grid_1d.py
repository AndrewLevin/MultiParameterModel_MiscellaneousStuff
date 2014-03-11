#! /usr/bin/env python

import sys
import os

import ROOT
from ROOT import TFile, TF1, TH1D

nGridPointsForNewF=20

if (len(sys.argv) != 3):
    print "format: python.py refine_grid_1d.py input_file_name output_file_name"
    print "exiting"
    sys.exit(0)

sigFile=sys.argv[1]
output_file_name=sys.argv[2]

print "input file: "+ sigFile
print "output file: "+ output_file_name

outfile_newF = TFile.Open(output_file_name,'RECREATE')

sigFile = TFile.Open(sigFile)

for key in sigFile.GetListOfKeys():
    anom_th1d=key.ReadObj()
    if type(anom_th1d)!=TH1D:
        print "expecting a TH1D, exiting"
        sys.exit(0)

    par1GridMin=anom_th1d.GetXaxis().GetBinLowEdge(1)
    par1GridMax=anom_th1d.GetXaxis().GetBinUpEdge(anom_th1d.GetNbinsX())
    print "par1GridMin:"+str(par1GridMin)
    print "par1GridMax:"+str(par1GridMax)
    
    func = TF1('fittingFunction','[0] + [1]*x + [2]*x*x,
               par1GridMin,par1GridMax)
        
    anom_th1d.Fit(func,'R0','')
    
    newFormatInput = TH1D(anom_th1d.GetName()
                      ,anom_th1d.GetTitle(),
                      nGridPointsForNewF,par1GridMin,par1GridMax)

    for bin_x in range(1,nGridPointsForNewF+1):
            par1_value=newFormatInput.GetXaxis().GetBinCenter(bin_x)
            yield_bin=func.GetParameter(0)+func.GetParameter(1)*par1_value+func.GetParameter(2)*par1_value*par1_value
            newFormatInput.SetBinContent(bin_x,yield_bin)
            
    outfile_newF.cd()
    newFormatInput.Write()
            
