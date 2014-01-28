import pyroot_logon
import limits
import os
import sys

from array import *


from ROOT import *

norm_sig_sm = -1
norm_bkg = -1
norm_obs = -1

basepath = '%s/src/CombinedEWKAnalysis/CommonTools/data/WV_semileptonic'%os.environ['CMSSW_BASE']

f=TFile('wwssll_nsign1.input_8TeV.root')
#f = TFile('observable_distributions.root')

data_obs = f.Get('data_obs')

theWS = RooWorkspace('ss_ww_wspace', 'ss_ww_wspace')

observable = theWS.factory('observable[1100,2000]')

vars = RooArgList(observable)

for key in f.GetListOfKeys():
    th1d_shape=key.ReadObj()
    if type(th1d_shape)!=TH1D:
        print "expecting a TH1D, exiting"
        sys.exit(0)
    roodh = RooDataHist(th1d_shape.GetName(),
                          th1d_shape.GetTitle(),
                          vars,
                          th1d_shape)
    if th1d_shape.GetName() == "histo_WWewk":
        ww_ewk_dh=roodh
    getattr(theWS, 'import')(roodh)

param1 = theWS.factory('param1[0.,-0.15, 0.15]')
param2 = theWS.factory('param2[0.,-0.1,0.1]')

varSet = RooArgSet(observable)

ww_ewk_pdf = RooHistFunc('ww_ewk_pdf',
                         'ww_ewk_pdf',
                         varSet,
                         ww_ewk_dh)

aQGCPdf = RooTwoParameterModelPdf('aqgc_2d',
                                 'aqgc_2d',
                                 observable,
                                 param1,
                                 param2,                                 
                                 ww_ewk_pdf,
                                 '/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/input_forNewF.root')

getattr(theWS, 'import')(aQGCPdf)

theWS.Print()

fout = TFile('ss_ww_shapes.root', 'recreate')
theWS.Write()
fout.Close()

### make the card for this channel and plane ID
card = """
# Simple counting experiment, with one signal and a few background processes 
imax 1  number of channels
jmax * number of background
kmax * number of nuisance parameters
Observation 1.999427
shapes *   *   ./ss_ww_shapes.root  ss_ww_wspace:histo_$PROCESS ss_ww_wspace:histo_$PROCESS_$SYSTEMATIC
shapes data_obs * ./ss_ww_shapes.root  ss_ww_wspace:histo_WWewk 
shapes WWewk * ./ss_ww_shapes.root ss_ww_wspace:aqgc_2d
bin wwssll8TeV wwssll8TeV wwssll8TeV wwssll8TeV wwssll8TeV wwssll8TeV
process WWewk WWqcd WZ WS VVV Wjets
process 0 1 2 3 4 5
rate  1.999   0.017   0.555   0.219   0.072   0.411
lumi_8TeV                               lnN  1.026 1.026 1.026 1.026 1.026   -  
CMS_eff_l                                   shape   - 1.000 1.000 1.000 1.000   -  
CMS_p_scale_l                                   shape   - 1.000 1.000 1.000 1.000   -  
CMS_scale_met                        shape   - 1.000 1.000 1.000 1.000   -  
CMS_scale_j                          shape   - 1.000 1.000 1.000 1.000   -  
pdf_qqbar                              lnN   1.073 1.068 1.069   -     -     -  
QCDscale_WWewk		               lnN   1.050   -     -     -     -     -  
QCDscale_WWqcd		               lnN    -   1.160   -     -     -     -  
QCDscale_VV		               lnN    -     -   1.100   -     -     -  
CMS_wwss_WZ3l                          lnN    -     -   1.010   -     -     -  
CMS_wwss_WZNLOBounding               shape    -     -   1.000   -     -     -  
CMS_wwss_MVAWSBounding               shape    -     -     -   1.000   -     -  
QCDscale_VVV		               lnN    -     -     -     -   1.500   -  
CMS_FakeRate                           lnN    -     -     -     -	    -   1.360
CMS_wwss_MVAWBounding                shape    -     -	-     -     -   1.000
CMS_wwssll_MVAWWqcdStatBounding_8TeV_Bin0           shape    -   1.000   -     -     -	  -  
CMS_wwssll_MVAWZStatBounding_8TeV_Bin0                shape    -	 -   1.000   -     -	  -  
CMS_wwssll_MVAWSStatBounding_8TeV_Bin0                shape    -	 -     -   1.000   -	  -  
CMS_wwssll_MVAVVVStatBounding_8TeV_Bin0              shape    -	 -     -     -   1.000   -  
CMS_wwssll_MVAWjetsStatBounding_8TeV_Bin0             shape    -	 -     -     -     -   1.000

"""

print card

cardfile = open('ss_ww_datacard.txt','w')
cardfile.write(card)
cardfile.close
