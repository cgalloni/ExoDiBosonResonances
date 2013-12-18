#ifndef LeptonsNtuplizer_H
#define LeptonsNtuplizer_H

#include "NtupleBranches.h"

using namespace NtupleBranches;

namespace LeptonsNtuplizer{

  void fillLeptonsBranches( void ){
  
    for (size_t e = 0; e < allElectronsCharge->size(); ++e){

      recoLep_type	       .push_back(11					  );
      recoLep_charge	       .push_back((*allElectronsCharge  	      )[e]);
      recoLep_e 	       .push_back((*allElectronsE		      )[e]);
      recoLep_eta	       .push_back((*allElectronsEta		      )[e]);
      recoLep_mass	       .push_back((*allElectronsMass		      )[e]);
      recoLep_pt	       .push_back((*allElectronsPt		      )[e]);
      recoLep_phi	       .push_back((*allElectronsPhi		      )[e]);
      recoLep_dxy	       .push_back((*allElectronsPVDxy		      )[e]);
      recoLep_dz	       .push_back((*allElectronsPVDz		      )[e]);
      recoLep_idMVAtrig        .push_back((*allElectronsMvaTrigV0	      )[e]);
      recoLep_looseId	       .push_back((*allElectronsPassesLooseID	      )[e]);
      recoLep_vetoId	       .push_back((*allElectronsPassesVetoID	      )[e]);
      recoLep_tightId	       .push_back((*allElectronsPassesTightID	      )[e]);
      recoLep_trigTightId      .push_back((*allElectronsPassesTrigTightID     )[e]);
      recoLep_pfRhoCorrRelIso  .push_back((*allElectronsPFRhoCorrectedRelIso  )[e]);
      recoLep_pfDeltaCorrRelIso.push_back((*allElectronsPFDeltaCorrectedRelIso)[e]);
      recoLep_pfRelIso         .push_back((*allElectronsPFRelIso	      )[e]);
      recoLep_photonIso        .push_back((*allElectronsChargedHadIso	      )[e]);
      recoLep_neutralHadIso    .push_back((*allElectronsNeutralHadIso	      )[e]);
      recoLep_chargedHadIso    .push_back((*allElectronsPhotonIso	      )[e]);
      recoLep_normChi2         .push_back(-99					  );
      recoLep_isGlobalMuon     .push_back(-99					  );
      recoLep_trackerHits      .push_back(-99					  );
      recoLep_matchedStations  .push_back(-99					  );
      recoLep_pixelHits        .push_back(-99					  );
      recoLep_globalHits       .push_back(-99					  );
  			    
    }

    for (size_t m = 0; m < allMuonsCharge->size(); ++m){

      recoLep_type	       .push_back(13				      );
      recoLep_charge	       .push_back((*allMuonsCharge		  )[m]);
      recoLep_e 	       .push_back((*allMuonsE			  )[m]);
      recoLep_eta	       .push_back((*allMuonsEta 		  )[m]);
      recoLep_mass	       .push_back((*allMuonsMass		  )[m]);
      recoLep_pt	       .push_back((*allMuonsPt  		  )[m]);
      recoLep_phi	       .push_back((*allMuonsPhi 		  )[m]);
      recoLep_dxy	       .push_back((*allMuonsPVDxy		  )[m]);
      recoLep_dz	       .push_back((*allMuonsPVDz		  )[m]);
      recoLep_idMVAtrig        .push_back(-99				      );
      recoLep_looseId	       .push_back(-99				      );
      recoLep_vetoId	       .push_back(-99				      );
      recoLep_tightId	       .push_back(-99				      );
      recoLep_trigTightId      .push_back(-99				      );
      recoLep_pfRhoCorrRelIso  .push_back((*allMuonsPFRhoCorrectedRelIso  )[m]);
      recoLep_pfDeltaCorrRelIso.push_back((*allMuonsPFDeltaCorrectedRelIso)[m]);
      recoLep_pfRelIso         .push_back((*allMuonsPFRelIso		  )[m]);
      recoLep_photonIso        .push_back((*allMuonsChargedHadIso	  )[m]);
      recoLep_neutralHadIso    .push_back((*allMuonsNeutralHadIso	  )[m]);
      recoLep_chargedHadIso    .push_back((*allMuonsPhotonIso		  )[m]);
      recoLep_normChi2         .push_back((*allMuonsNormChi2		  )[m]);
      recoLep_isGlobalMuon     .push_back((*allMuonsIsGlobalMuon	  )[m]);
      recoLep_trackerHits      .push_back((*allMuonsTrackerHits 	  )[m]);
      recoLep_matchedStations  .push_back((*allMuonsMatchedStations	  )[m]);
      recoLep_pixelHits        .push_back((*allMuonsPixelHits		  )[m]);
      recoLep_globalHits       .push_back((*allMuonsGlobalMuonHits	  )[m]);
      
    }

    nrecoLep = recoLep_type.size();
  
  }

}

#endif // LeptonsNtuplizer_H
