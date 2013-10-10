import FWCore.ParameterSet.Config as cms

cmgFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    noEventSort = cms.untracked.bool(True),
                    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                    fileNames = cmgFiles
                   )

cmgFiles.extend([
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_10_1_i43.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_11_1_rCs.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_12_1_4nN.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_13_1_PLi.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_14_1_JFd.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_15_1_3qV.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_16_1_uqK.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_17_1_XYp.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_18_1_SgE.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_19_1_62T.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_1_1_FGx.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_20_1_CXl.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_21_1_5XO.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_2_1_N3R.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_3_1_XPk.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_4_1_yrj.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_5_1_cbE.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_6_1_HAY.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_7_1_OQz.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_8_1_gCx.root',
    '/store/cmst3/group/exovv/santanas/EDBR_PATtuple_edbr_zz_20130605_Summer12MC_BulkGravitonsWW_20130916_175629/santanas/BulkG_WW_inclusive_c0p2_M1200_GENSIM/EDBR_PATtuple_edbr_zz_20130605/1b325ddfb984c14533be7920e22baeef/BulkG_WW_inclusive_c0p2_M1200_GENSIM__shuai-BulkG_WW_inclusive_c0p2_M1200_AODSIM-2c74483358b1f8805e5601fc325d256c__USER_9_1_8W6.root',
    ])
