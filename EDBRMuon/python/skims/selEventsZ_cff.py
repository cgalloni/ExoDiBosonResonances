import FWCore.ParameterSet.Config as cms

ZmmCand = cms.EDFilter(
    "CmgDiMuonSelector",
    src = cms.InputTag("cmgDiMuon"),
    cut = cms.string( "getSelection(\"cuts_zmumu\")&& getSelection(\"cuts_charge\")" )
    )

selectedZmmCandFilter = cms.EDFilter("CandViewCountFilter",
   src = cms.InputTag('ZmmCand'),
   minNumber = cms.uint32(0)
 )


selectedZMMSequence = cms.Sequence(ZmmCand+selectedZmmCandFilter)

