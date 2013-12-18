import FWCore.ParameterSet.Config as cms

process = cms.PSet(
    fileNames	= cms.vstring(),                    
    maxEvents	= cms.int32(-1),
    outputEvery = cms.uint32(1000),
    outputFile  = cms.string('test.root'),
    )

