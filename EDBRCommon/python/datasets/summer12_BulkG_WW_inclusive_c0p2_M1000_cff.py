import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_10_1_D8R.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_11_1_94y.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_12_1_6kj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_13_1_BDQ.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_14_1_pz6.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_15_1_Po0.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_16_1_ZEu.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_17_1_BEy.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_18_1_mWn.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_19_1_ZrY.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_1_1_fC0.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_20_1_Fji.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_21_1_vsy.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_2_1_ckJ.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_3_1_OBX.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_4_1_nVW.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_5_1_yPj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_6_1_Ptj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_7_1_hUX.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_8_1_Kly.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_jjjj_c0p2_M1000-JHU/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_jjjj_c0p2_M1000-JHU__qili-BulkG_WW_jjjj_c0p2_M1000-JHU-AODSIM-c8f8ed334db8a7d6f56c62266b1dfa5b__USER_9_1_AiP.root',
    ])