#ifndef LeptonsNtuplizer_H
#define LeptonsNtuplizer_H

#include	 "NtupleBranches.h"

using namespace NtupleBranches;

namespace LeptonsNtuplizer{

  void fillLeptonsBranches( void ){

   /* here we want to save the leptons info*/  
    for (size_t e = 0; e < ele->size(); ++e){

      recoLep_type	       .push_back((*ele )[e].pdgId());
      recoLep_charge	       .push_back((*ele)[e].chargeInfo().scPixCharge);
      // recoLep_e 	       .push_back((*ele)[e].e());
      recoLep_eta	       .push_back((*ele)[e].eta());
      recoLep_mass	       .push_back((*ele)[e].mass());
      recoLep_pt	       .push_back((*ele)[e].pt());
      recoLep_phi	       .push_back((*ele)[e].phi());
      // recoLep_dxy	       .push_back((*ele)[e].vertex().fCoordinates().fX());
      //recoLep_dz	       .push_back((*ele)[e].vertex().fCoordinates().fZ());



    }

    for (size_t e = 0; e < muo->size(); ++e){

      recoLep_type	       .push_back((*muo )[e].pdgId());
      recoLep_charge	       .push_back((*muo)[e].charge());
      // recoLep_e 	       .push_back((*muo)[e].e());
      recoLep_eta	       .push_back((*muo)[e].eta());
      recoLep_mass	       .push_back((*muo)[e].mass());
      recoLep_pt	       .push_back((*muo)[e].pt());
      recoLep_phi	       .push_back((*muo)[e].phi());
      // recoLep_dxy	       .push_back((*muo)[e].vertex().fCoordinates().fX());
      //recoLep_dz	       .push_back((*muo)[e].vertex().fCoordinates().fZ());



    }


  }

}

#endif // LeptonsNtuplizer_H
