#ifndef JetsNtuplizer_H
#define JetsNtuplizer_H

#include "NtupleBranches.h"

using namespace NtupleBranches;

namespace JetsNtuplizer{

  void fillJetsBranches( void ){

    /////////////////////////////////////////////////////////////////////////////////////  
    nrecoJets = 0;
    for ( size_t j = 0; j < allJetsPFPt->size(); ++j ){
      if( (*allJetsPFPt)[j] <= 20 ) continue;  
      nrecoJets++; 
      recoJet_pt	   .push_back((*allJetsPFPt		  )[j]);     
      recoJet_eta	   .push_back((*allJetsPFEta		  )[j]);     
      recoJet_mass	   .push_back((*allJetsPFMass		  )[j]);     
      recoJet_phi	   .push_back((*allJetsPFPhi		  )[j]);     
      recoJet_e 	   .push_back((*allJetsPFE		  )[j]);     
      recoJet_csv	   .push_back((*allJetsPFCSV		  )[j]); 
      recoJet_tchp         .push_back((*allJetsPFTCHP             )[j]);    
      recoJet_chf	   .push_back((*allJetsPFChf		  )[j]);     
      recoJet_nhf	   .push_back((*allJetsPFNhf		  )[j]);     
      recoJet_cef	   .push_back((*allJetsPFCef		  )[j]);     
      recoJet_nef	   .push_back((*allJetsPFNef		  )[j]);     
      recoJet_chm	   .push_back((*allJetsPFChm		  )[j]);     
      recoJet_nm	   .push_back((*allJetsPFNm		  )[j]);     
      recoJet_flavour	   .push_back((*allJetsPFFlavour	  )[j]);     
      recoJet_charge	   .push_back((*allJetsPFCharge 	  )[j]);     
      recoJet_nconstituents.push_back((*allJetsPFNconstituents    )[j]);     
      recoJet_nTracksSV    .push_back((*SecondaryVerticesNumTracks)[j]);     
      recoJet_vtxMass	   .push_back((*SecondaryVerticesMass	  )[j]);     
      recoJet_vtxPt	   .push_back((*SecondaryVerticesPt	  )[j]);     
      recoJet_vtxPhi	   .push_back((*SecondaryVerticesPhi	  )[j]);     
      recoJet_vtxEta	   .push_back((*SecondaryVerticesEta	  )[j]);     
      recoJet_vtxE	   .push_back((*SecondaryVerticesE	  )[j]);     
      recoJet_vtxX	   .push_back((*SecondaryVerticesX	  )[j]);     
      recoJet_vtxY	   .push_back((*SecondaryVerticesY	  )[j]);     
      recoJet_vtxZ	   .push_back((*SecondaryVerticesZ	  )[j]);     
      recoJet_vtxXerr	   .push_back((*SecondaryVerticesXerr	  )[j]);     
      recoJet_vtxYerr	   .push_back((*SecondaryVerticesYerr	  )[j]);     
      recoJet_vtxZerr	   .push_back((*SecondaryVerticesZerr	  )[j]);     
      recoJet_vtx3dL	   .push_back((*SecondaryVertices3dL	  )[j]);     
      recoJet_vtx2dL	   .push_back((*SecondaryVertices2dL	  )[j]);     
    
      TVector3 jetVtxErr3d((*SecondaryVerticesXerr)[j],(*SecondaryVerticesYerr)[j],(*SecondaryVerticesZerr)[j]);
      TVector2 jetVtxErr2d((*SecondaryVerticesXerr)[j],(*SecondaryVerticesYerr)[j]);
    
      recoJet_vtx3dLerr.push_back(jetVtxErr3d.Mag());
      recoJet_vtx2dLerr.push_back(jetVtxErr2d.Mod());
    }    

    int index = 0;
    for( size_t t = 0; t < allJetsPFTracksJetIndex->size(); ++t ){
      index = (*allJetsPFTracksJetIndex)[t];
      if( (*allJetsPFPt)[index] <= 20 ) continue;
      jetTrack_jetIndex.push_back((*allJetsPFTracksJetIndex)[t]);    
      jetTrack_chi2    .push_back((*allJetsPFTracksChi2    )[t]);
      jetTrack_ndof    .push_back((*allJetsPFTracksNdof    )[t]);
      jetTrack_dxy     .push_back((*allJetsPFTracksDxy     )[t]);
      jetTrack_dxyErr  .push_back((*allJetsPFTracksDxyErr  )[t]);
      jetTrack_dz      .push_back((*allJetsPFTracksDz	   )[t]);     
      jetTrack_dzErr   .push_back((*allJetsPFTracksDzErr   )[t]);     
      jetTrack_eta     .push_back((*allJetsPFTracksEta     )[t]);    
      jetTrack_phi     .push_back((*allJetsPFTracksPhi     )[t]);
      jetTrack_pt      .push_back((*allJetsPFTracksPt	   )[t]);   
      jetTrack_nhits   .push_back((*allJetsPFTracksNhits   )[t]);      
    }

    /////////////////////////////////////////////////////////////////////////////////////    
    nak5CHSprunedJets = 0;    
    for( size_t j = 0; j < AK5CHSprunedPt->size(); ++j ){
      if( (*AK5CHSprunedPt)[j] <= 20 ) continue;
      nak5CHSprunedJets++;
      ak5CHSprunedJet_pt     .push_back((*AK5CHSprunedPt     )[j]);
      ak5CHSprunedJet_eta    .push_back((*AK5CHSprunedEta    )[j]);
      ak5CHSprunedJet_mass   .push_back((*AK5CHSprunedMass   )[j]);
      ak5CHSprunedJet_phi    .push_back((*AK5CHSprunedPhi    )[j]);
      ak5CHSprunedJet_e      .push_back((*AK5CHSprunedE      )[j]);
      ak5CHSprunedJet_csv    .push_back((*AK5CHSprunedCSV    )[j]);
      ak5CHSprunedJet_flavour.push_back((*AK5CHSprunedFlavour)[j]);
      ak5CHSprunedJet_charge .push_back((*AK5CHSprunedCharge )[j]);
    }
    
    nak5CHSprunedSubjets = 0;    
    for( size_t j = 0; j < AK5CHSprunedPt->size(); ++j ){
      if( (*AK5CHSprunedPt)[j] <= 20 ) continue;
      nak5CHSprunedSubjets++;
      ak5CHSprunedSubjet_pt	.push_back((*AK5CHSprunedSubjetsPt     )[j]);
      ak5CHSprunedSubjet_eta	.push_back((*AK5CHSprunedSubjetsEta    )[j]);
      ak5CHSprunedSubjet_mass	.push_back((*AK5CHSprunedSubjetsMass   )[j]);
      ak5CHSprunedSubjet_phi	.push_back((*AK5CHSprunedSubjetsPhi    )[j]);
      ak5CHSprunedSubjet_e	.push_back((*AK5CHSprunedSubjetsE      )[j]);
      ak5CHSprunedSubjet_csv	.push_back((*AK5CHSprunedSubjetsCSV    )[j]);
      ak5CHSprunedSubjet_flavour.push_back((*AK5CHSprunedSubjetsFlavour)[j]);
      ak5CHSprunedSubjet_charge .push_back((*AK5CHSprunedSubjetsCharge )[j]);
    }
    
    nca8CHSprunedJets = 0;    
    for( size_t j = 0; j < CA8CHSprunedPt->size(); ++j ){
      if( (*CA8CHSprunedPt)[j] <= 20 ) continue;
      nca8CHSprunedJets++;
      ca8CHSprunedJet_pt     .push_back((*CA8CHSprunedPt     )[j]);
      ca8CHSprunedJet_eta    .push_back((*CA8CHSprunedEta    )[j]);
      ca8CHSprunedJet_mass   .push_back((*CA8CHSprunedMass   )[j]);
      ca8CHSprunedJet_phi    .push_back((*CA8CHSprunedPhi    )[j]);
      ca8CHSprunedJet_e      .push_back((*CA8CHSprunedE      )[j]);
      ca8CHSprunedJet_csv    .push_back((*CA8CHSprunedCSV    )[j]);
      ca8CHSprunedJet_flavour.push_back((*CA8CHSprunedFlavour)[j]);
      ca8CHSprunedJet_charge .push_back((*CA8CHSprunedCharge )[j]);
    }
    
    nca8CHSprunedSubjets = 0;    
    for( size_t j = 0; j < CA8CHSprunedPt->size(); ++j ){
      if( (*CA8CHSprunedPt)[j] <= 20 ) continue;
      nca8CHSprunedSubjets++;
      ca8CHSprunedSubjet_pt	.push_back((*CA8CHSprunedSubjetsPt     )[j]);
      ca8CHSprunedSubjet_eta	.push_back((*CA8CHSprunedSubjetsEta    )[j]);
      ca8CHSprunedSubjet_mass	.push_back((*CA8CHSprunedSubjetsMass   )[j]);
      ca8CHSprunedSubjet_phi	.push_back((*CA8CHSprunedSubjetsPhi    )[j]);
      ca8CHSprunedSubjet_e	.push_back((*CA8CHSprunedSubjetsE      )[j]);
      ca8CHSprunedSubjet_csv	.push_back((*CA8CHSprunedSubjetsCSV    )[j]);
      ca8CHSprunedSubjet_flavour.push_back((*CA8CHSprunedSubjetsFlavour)[j]);
      ca8CHSprunedSubjet_charge .push_back((*CA8CHSprunedSubjetsCharge )[j]);
    }  
    
    
    
  }

}

#endif // JetsNtuplizer_H
