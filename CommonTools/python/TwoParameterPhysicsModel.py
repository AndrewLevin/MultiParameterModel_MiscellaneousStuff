from TwoParameterModel_MiscellaneousStuff.CommonTools.AnomalousCouplingModel import *
import ROOT as r
import os

basepath = '%s/src/CombinedEWKAnalysis/CommonTools/data/WV_semileptonic'%os.environ['CMSSW_BASE']
#filename = '%s/ATGC_shape_coefficients.root'%basepath  
#filename = '%s/signal_WV.root'%basepath  

#this model is in the equal couplings scenario of HISZ or something similar
#it does the old style limits of setting the other parameter to zero
class HagiwaraAndZeppenfeldTwoDimensionalModel(AnomalousCouplingModel):
    def __init__(self):
        AnomalousCouplingModel.__init__(self)
        self.processes = ['WWewk']
        self.channels  = ['WV_atgc_semileptonic']
        self.pois      =  ['param1','param2']
        self.anomCoupSearchWindows = {'param1':['-3.75','3.75'],
                                      'param2':['-1.25','1.25'] }
        
        self.verbose = False

    def buildScaling(self,process,channel):        
        scalerName = process
        filename = '/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_refined.root'  
        f = r.TFile(filename,'READ')
        #yield_scaling1=f.Get("aQGC_scaling1").Clone("aQGC_scaling1_new")
        #yield_scaling2=f.Get("aQGC_scaling2").Clone("aQGC_scaling2_new")
        #yield_scaling3=f.Get("aQGC_scaling3").Clone("aQGC_scaling3_new")
        #yield_scaling4=f.Get("aQGC_scaling4").Clone("aQGC_scaling4_new")

        #self.modelBuilder.out._import(yield_scaling1)
        #self.modelBuilder.out._import(yield_scaling2)
        #self.modelBuilder.out._import(yield_scaling3)
        #self.modelBuilder.out._import(yield_scaling4)

        
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch1(param1,param2,"~/2d_limit/CMSSW_6_1_1/src/TwoParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling1")')
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch2(param1,param2,"~/2d_limit/CMSSW_6_1_1/src/TwoParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling2")')
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch3(param1,param2,"~/2d_limit/CMSSW_6_1_1/src/TwoParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling3")')
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch4(param1,param2,"~/2d_limit/CMSSW_6_1_1/src/TwoParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling4")')        
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch1(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign1_refined.root","aQGC_scaling1")')
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch2(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign1_refined.root","aQGC_scaling2")')
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch3(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign1_refined.root","aQGC_scaling3")')
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch4(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign1_refined.root","aQGC_scaling4")')
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch5(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign2_refined.root","aQGC_scaling1")')
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch6(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign2_refined.root","aQGC_scaling2")')
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch7(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign2_refined.root","aQGC_scaling3")')
        #self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch8(param1,param2,"/home/anlevin/2d_limit_fw/CMSSW_6_1_1/src/CombinedEWKAnalysis/CommonTools/test/aQGC_grids_sign2_refined.root","aQGC_scaling4")')


        return scalerName
        

my_2d_model = HagiwaraAndZeppenfeldTwoDimensionalModel()

