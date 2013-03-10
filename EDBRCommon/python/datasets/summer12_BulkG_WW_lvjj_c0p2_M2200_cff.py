import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2200-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2200-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2200-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_Ehj.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2200-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2200-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2200-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_Gob.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2200-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2200-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2200-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_Qgk.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2200-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2200-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2200-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_JYf.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2200-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2200-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2200-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_MmQ.root',
       ])
