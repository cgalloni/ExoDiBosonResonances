import FWCore.ParameterSet.Config as cms
maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ('PoolSource',fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_10_1_NYG.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_11_1_4mT.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_1_1_xOy.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_2_1_b6e.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_3_1_JTp.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_4_1_gLM.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_5_1_6eK.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_6_1_WLr.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_7_1_yEw.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_8_1_yJI.root',
       '/store/cmst3/group/exovv/bonato/EDBR_PATtuple_edbr_20131015_RSGZZPythia_20131015_090830/bonato/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola/EDBR_PATtuple_edbr_20131015_RSGZZPythia/1b325ddfb984c14533be7920e22baeef/RSGravitonToZZToLLJJ_kMpl005_M-1750_TuneZ2star_8TeV-pythia6-tauola__Summer12_DR53X-PU_S10_START53_V7A-v1__AODSIM_9_1_CZ7.root' 
]);