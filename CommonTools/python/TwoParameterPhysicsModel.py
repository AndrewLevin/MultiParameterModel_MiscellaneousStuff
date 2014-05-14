from MultiParameterModel_MiscellaneousStuff.CommonTools.AnomalousCouplingModel import *
import ROOT as r
import os

#this model is in the equal couplings scenario of HISZ or something similar
#it does the old style limits of setting the other parameter to zero
class TwoParameterPhysicsModel(AnomalousCouplingModel):
    def __init__(self):
        AnomalousCouplingModel.__init__(self)
        self.channels = ['channel_name']
        self.processes = ['WWewk']
        self.pois = ['param1','param2']
        
    def buildScaling(self,process,channel):        
        scalerName = process

        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch1(param1,param2,"'+self.scaling_filename+'","aQGC_scaling1")')
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch2(param1,param2,"'+self.scaling_filename+'","aQGC_scaling2")')
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch3(param1,param2,"'+self.scaling_filename+'","aQGC_scaling3")')
        self.modelBuilder.factory_('RooTwoParameterModelScaling::Scaling_WWewk_ch4(param1,param2,"'+self.scaling_filename+'","aQGC_scaling4")')  

        return scalerName
        

my_2d_model = TwoParameterPhysicsModel()

