from CombinedEWKAnalysis.CommonTools.AnomalousCouplingModel import *
import ROOT as r
import os

basepath = '%s/src/CombinedEWKAnalysis/CommonTools/data/WV_semileptonic'%os.environ['CMSSW_BASE']
#filename = '%s/ATGC_shape_coefficients.root'%basepath  
#filename = '%s/signal_WV.root'%basepath  

#this model is in the equal couplings scenario of HISZ or something similar
#it does the old style limits of setting the other parameter to zero
class HagiwaraAndZeppenfeldTwoDimensionalModel(AnomalousCouplingModel):
    def __init__(self):
        print "andrew debug hagiwara 1"
        AnomalousCouplingModel.__init__(self)
        print "andrew debug hagiwara 2"
        self.processes = ['WWewk']
        self.channels  = ['WV_atgc_semileptonic']
        self.pois      =  ['param1','param2']
        self.anomCoupSearchWindows = {'param1':['-2.5','2.5'],
                                      'param2':['-2.5','2.5'] }
        
        self.verbose = False

    def buildScaling(self,process,channel):        
        scalerName = process
        filename = '/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/input_forNewF.root'  
       
              
#        f = r.TFile('%s/mu_boosted.root'%basepath,'READ')
        print "basepath"
        print basepath
        
        f = r.TFile('%s/ch1_boosted.root'%(basepath),'READ')
#        SM_diboson_shape = f.Get('diboson').Clone('SM_wv_semil_mu_shape_for_scale')
        SM_diboson_shape = f.Get('diboson').Clone('SM_wv_semil_ch1_shape_for_scale')
        SM_diboson_shape.SetDirectory(0)
        print "buildScaling f.ls()"
        f.ls()
        f.Close()
        self.modelBuilder.out._import(SM_diboson_shape)
        SM_diboson_shape_dhist = r.RooDataHist('DHIST_SM_wv_semil_ch1_shape_for_scale',
                    'DHIST_SM_wv_semil_ch1_shape_for_scale',
                    r.RooArgList(self.modelBuilder.out.var('observable')),
                    self.modelBuilder.out.obj('SM_wv_semil_ch1_shape_for_scale'))
        self.modelBuilder.out._import(SM_diboson_shape_dhist)
#        self.modelBuilder.factory_('RooHistFunc::Scaling_base_pdf_%s({observable},DHIST_SM_wv_semil_mu_shape_for_scale)'%(scalerName))
        self.modelBuilder.factory_('RooHistFunc::Scaling_base_pdf_WWewk({observable},DHIST_SM_wv_semil_ch1_shape_for_scale)')          
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk(observable,param1,param2,Scaling_base_pdf_%s,"%s")'%(scalerName,filename))

        return scalerName
        

model_2d_hag_zep = HagiwaraAndZeppenfeldTwoDimensionalModel()

