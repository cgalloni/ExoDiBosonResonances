#ifndef GenParticlesNtuplizer_H
#define GenParticlesNtuplizer_H

#include "NtupleBranches.h"

using namespace NtupleBranches;

namespace GenParticlesNtuplizer {

  void fillGenParticlesBranches( void ){
  
    /////////////////////////////////////////////////////////////////////////////////////
    for ( size_t q = 0; q < MCHiggsPdgId->size(); ++q ){

      genH_charge.push_back((*MCHiggsCharge)[q]);
      genH_e	 .push_back((*MCHiggsE     )[q]);
      genH_eta   .push_back((*MCHiggsEta   )[q]);
      genH_pdgId .push_back((*MCHiggsPdgId )[q]);
      genH_phi   .push_back((*MCHiggsPhi   )[q]);
      genH_pt	 .push_back((*MCHiggsPt    )[q]);
      genH_status.push_back((*MCHiggsStatus)[q]);
      genH_mass  .push_back((*MCHiggsMass  )[q]);
      
    }
    ngenH = genH_charge.size();          	 

    /////////////////////////////////////////////////////////////////////////////////////
    std::vector<int> bquarks   ;
    std::vector<int> bbarquarks;
    for ( size_t q = 0; q < MCHiggsBQuarkPdgId->size(); ++q ){
      if ( (*MCHiggsBQuarkPdgId)[q] == 5 ) bquarks.push_back(q);
      else if ( (*MCHiggsBQuarkPdgId)[q] == -5 ) bbarquarks.push_back(q);
    }  

    for ( size_t i = 0; i < bquarks.size(); ++i ){
  
        int q = bquarks[i];
        hgenB_charge.push_back((*MCHiggsBQuarkCharge)[q]);
        hgenB_e     .push_back((*MCHiggsBQuarkE	    )[q]);
        hgenB_eta   .push_back((*MCHiggsBQuarkEta   )[q]);
        hgenB_pdgId .push_back((*MCHiggsBQuarkPdgId )[q]);
        hgenB_phi   .push_back((*MCHiggsBQuarkPhi   )[q]);
        hgenB_pt    .push_back((*MCHiggsBQuarkPt    )[q]);
	hgenB_mass  .push_back((*MCHiggsBQuarkMass  )[q]);
        hgenB_status.push_back((*MCHiggsBQuarkStatus)[q]);
	
    }
    for ( size_t i = 0; i < bbarquarks.size(); ++i ){
      
        int q = bbarquarks[i];
        hgenBbar_charge.push_back((*MCHiggsBQuarkCharge)[q]);
        hgenBbar_e     .push_back((*MCHiggsBQuarkE     )[q]);
        hgenBbar_eta   .push_back((*MCHiggsBQuarkEta   )[q]);
        hgenBbar_pdgId .push_back((*MCHiggsBQuarkPdgId )[q]);
        hgenBbar_phi   .push_back((*MCHiggsBQuarkPhi   )[q]);
        hgenBbar_pt    .push_back((*MCHiggsBQuarkPt    )[q]);
	hgenBbar_mass  .push_back((*MCHiggsBQuarkMass  )[q]);
        hgenBbar_status.push_back((*MCHiggsBQuarkStatus)[q]);
	
    }
    
    nhgenB    = hgenB_charge.size();
    nhgenBbar = hgenBbar_charge.size();
    
    /////////////////////////////////////////////////////////////////////////////////////
    bquarks.clear();
    bbarquarks.clear();
    for ( size_t q = 0; q < MCbquarksPdgId->size(); ++q ){
      if ( (*MCbquarksMotherID)[q] != 25 && (*MCbquarksPdgId)[q] == 5 ) bquarks.push_back(q);
      else if ( (*MCbquarksMotherID)[q] != 25 && (*MCbquarksPdgId)[q] == -5 ) bbarquarks.push_back(q);
    }
    ngenB = bquarks.size();
    ngenBbar = bbarquarks.size();
    for ( size_t i = 0; i < bquarks.size(); ++i ){	     
      genB_charge.push_back((*MCbquarksCharge  )[bquarks[i]]);
      genB_e	 .push_back((*MCbquarksE       )[bquarks[i]]);
      genB_eta   .push_back((*MCbquarksEta     )[bquarks[i]]);
      genB_pdgId .push_back((*MCbquarksPdgId   )[bquarks[i]]);
      genB_phi   .push_back((*MCbquarksPhi     )[bquarks[i]]);
      genB_pt	 .push_back((*MCbquarksPt      )[bquarks[i]]);
      genB_mass  .push_back((*MCbquarksMass    )[bquarks[i]]);
      genB_status.push_back((*MCbquarksStatus  )[bquarks[i]]);
      genB_mother.push_back((*MCbquarksMotherID)[bquarks[i]]);	 
    }      
    for ( size_t i = 0; i < bbarquarks.size(); ++i ){
      genBbar_charge.push_back((*MCbquarksCharge  )[bbarquarks[i]]);
      genBbar_e     .push_back((*MCbquarksE	  )[bbarquarks[i]]);
      genBbar_eta   .push_back((*MCbquarksEta	  )[bbarquarks[i]]);
      genBbar_pdgId .push_back((*MCbquarksPdgId   )[bbarquarks[i]]);
      genBbar_phi   .push_back((*MCbquarksPhi	  )[bbarquarks[i]]);
      genBbar_pt    .push_back((*MCbquarksPt	  )[bbarquarks[i]]);
      genBbar_mass  .push_back((*MCbquarksMass    )[bbarquarks[i]]);
      genBbar_status.push_back((*MCbquarksStatus  )[bbarquarks[i]]);
      genBbar_mother.push_back((*MCbquarksMotherID)[bbarquarks[i]]);  
    }      
    /*if( ngenB != 0){      
      int bIndex = bquarks[0];
      for ( size_t i = 0; i < bquarks.size(); ++i ){	     
        if ( (*MCbquarksPt)[bquarks[i]] >= (*MCbquarksPt)[bIndex] ) bIndex = bquarks[i];
      }
      genB_charge.push_back((*MCbquarksCharge  )[bIndex]);
      genB_e	 .push_back((*MCbquarksE       )[bIndex]);
      genB_eta   .push_back((*MCbquarksEta     )[bIndex]);
      genB_pdgId .push_back((*MCbquarksPdgId   )[bIndex]);
      genB_phi   .push_back((*MCbquarksPhi     )[bIndex]);
      genB_pt	 .push_back((*MCbquarksPt      )[bIndex]);
      genB_mass  .push_back((*MCbquarksMass    )[bIndex]);
      genB_status.push_back((*MCbquarksStatus  )[bIndex]);
      genB_mother.push_back((*MCbquarksMotherID)[bIndex]);
      ngenB = genB_charge.size();	 
    }
    if( ngenBbar != 0 ){      
      int bbarIndex = bbarquarks[0];
      for ( size_t i = 0; i < bbarquarks.size(); ++i ){
        if ( (*MCbquarksPt)[bbarquarks[i]] >= (*MCbquarksPt)[bbarIndex] ) bbarIndex = bbarquarks[i];
      }
      genBbar_charge.push_back((*MCbquarksCharge  )[bbarIndex]);
      genBbar_e     .push_back((*MCbquarksE	  )[bbarIndex]);
      genBbar_eta   .push_back((*MCbquarksEta	  )[bbarIndex]);
      genBbar_pdgId .push_back((*MCbquarksPdgId   )[bbarIndex]);
      genBbar_phi   .push_back((*MCbquarksPhi	  )[bbarIndex]);
      genBbar_pt    .push_back((*MCbquarksPt	  )[bbarIndex]);
      genBbar_mass  .push_back((*MCbquarksMass    )[bbarIndex]);
      genBbar_status.push_back((*MCbquarksStatus  )[bbarIndex]);
      genBbar_mother.push_back((*MCbquarksMotherID)[bbarIndex]); 
      ngenBbar = genBbar_charge.size(); 
    }*/

    for ( size_t q = 0; q < MCWPdgId->size(); ++q ){

      if ( 11 <= abs((*MCWDauOneID)[q]) && abs((*MCWDauOneID)[q]) <= 16 ){
      	genW_charge = (*MCWCharge)[q];
      	genW_e      = (*MCWE	 )[q];
      	genW_eta    = (*MCWEta   )[q];
      	genW_pdgId  = (*MCWPdgId )[q];
      	genW_phi    = (*MCWPhi   )[q];
      	genW_pt     = (*MCWPt	 )[q];
	genW_mass   = (*MCWMass  )[q];
      	genW_status = (*MCWStatus)[q];
      }
      
    }

    for ( size_t q = 0; q < MCWleptonPdgId->size(); ++q ){

      genWlep_charge = (*MCWleptonCharge)[q];
      genWlep_e      = (*MCWleptonE	)[q];
      genWlep_eta    = (*MCWleptonEta	)[q];
      genWlep_pdgId  = (*MCWleptonPdgId )[q];
      genWlep_phi    = (*MCWleptonPhi	)[q];
      genWlep_pt     = (*MCWleptonPt	)[q];
      genWlep_mass   = (*MCWleptonMass  )[q];
      genWlep_status = (*MCWleptonStatus)[q];
      
    }

    for ( size_t q = 0; q < MCWneutrinoPdgId->size(); ++q ){

      genWnu_charge = (*MCWneutrinoCharge)[q];
      genWnu_e      = (*MCWneutrinoE	 )[q];
      genWnu_eta    = (*MCWneutrinoEta   )[q];
      genWnu_pdgId  = (*MCWneutrinoPdgId )[q];
      genWnu_phi    = (*MCWneutrinoPhi   )[q];
      genWnu_pt     = (*MCWneutrinoPt	 )[q];
      genWnu_status = (*MCWneutrinoStatus)[q];
      
    }

    for ( size_t q = 0; q < MCWstarPdgId->size(); ++q ){

      genWstar_charge = (*MCWstarCharge)[q];
      genWstar_e      = (*MCWstarE     )[q];
      genWstar_eta    = (*MCWstarEta   )[q];
      genWstar_pdgId  = (*MCWstarPdgId )[q];
      genWstar_phi    = (*MCWstarPhi   )[q];
      genWstar_pt     = (*MCWstarPt    )[q];
      genWstar_status = (*MCWstarStatus)[q];
      
    }
      
  }

}

#endif // GenParticlesNtuplizer_H
