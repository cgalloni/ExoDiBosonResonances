import FWCore.ParameterSet.Config as cms

readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                                                noEventSort = cms.untracked.bool(True),
                                                duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                                                fileNames = readFiles
                                                )
readFiles.extend([
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_10_1_342.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_11_1_FZF.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_12_1_6V4.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_13_1_Nbv.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_37p.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_dc9.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_YE0.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_OgX.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_bjf.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_jL8.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_oLo.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_4p4.root',
       '/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/qili/EDBR_PATtuple_20130307_SignalBulkWW_20130307_093556/qili/BulkG_WW_lvjj_c0p2_M2000-JHU-v1/EDBR_PATtuple_edbr_BulkWW/0cebe449841078f6c01c2b31222fdcfb/BulkG_WW_lvjj_c0p2_M2000-JHU-v1__qili-BulkG_WW_lvjj_c0p2_M2000-JHU-AODSIM-v1-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_ptZ.root',
       ])
