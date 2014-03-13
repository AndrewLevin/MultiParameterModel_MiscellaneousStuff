from MultiParameterModel_MiscellaneousStuff.CommonTools.AnomalousCouplingModel import *
import ROOT as r
import os

#this model is in the equal couplings scenario of HISZ or something similar
#it does the old style limits of setting the other parameter to zero
class OneParameterPhysicsModel(AnomalousCouplingModel):
    def __init__(self):
        AnomalousCouplingModel.__init__(self)
        self.processes = ['WWewk']
        self.channels  = ['WV_atgc_semileptonic']
        self.pois      =  ['param']
        self.anomCoupSearchWindows = {'param':['-1.25','1.25']}
        
        self.verbose = False

    def buildScaling(self,process,channel):        
        scalerName = process
        
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch1(param,"~/nd_limit/CMSSW_6_1_1/src/MultiParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling1")')
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch2(param,"~/nd_limit/CMSSW_6_1_1/src/MultiParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling2")')
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch3(param,"~/nd_limit/CMSSW_6_1_1/src/MultiParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling3")')
        self.modelBuilder.factory_('RooOneParameterModelScaling::Scaling_WWewk_ch4(param,"~/nd_limit/CMSSW_6_1_1/src/MultiParameterModel_MiscellaneousStuff/CommonTools/test/aQGC_grids_refined.root","aQGC_scaling4")')        

        return scalerName
        

my_1d_model = OneParameterPhysicsModel()

