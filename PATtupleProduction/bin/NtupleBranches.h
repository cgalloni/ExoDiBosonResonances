#ifndef NtupleBranches_H
#define NtupleBranches_H

#include <DataFormats/PatCandidates/interface/Jet.h>
#include "DataFormats/FWLite/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "TTree.h"
//#include "Candidate.h"
/* Lepton libraries */
#include <DataFormats/PatCandidates/interface/Electron.h>
#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/PatCandidates/interface/Tau.h>
#include <DataFormats/MuonReco/interface/Muon.h>
//#include <DataFormats/ElectronReco/interface/Electron.h>
//#include </DataFormats/EgammaCandidates/interface/Electron.h>

//#include <DataFormats/Candidate.h>
/*here we declare the input and output variables*/

namespace NtupleBranches {

//=================================================================================================================== 
  /* output tree variables*/
    
    int 	       nrecoJets		 ;
    std::vector<float> recoJet_pt		 ;
    std::vector<float> recoJet_eta		 ;
    std::vector<float> recoJet_mass		 ;
    std::vector<float> recoJet_e		 ;
    std::vector<float> recoJet_phi		 ;

    /* lep variables */

    int   	     nrecoLep	                 ;
    std::vector<int  > recoLep_type              ;
    std::vector<float> recoLep_charge            ;
    std::vector<float> recoLep_e                 ;
    std::vector<float> recoLep_eta               ;
    std::vector<float> recoLep_mass              ;
    std::vector<float> recoLep_pt                ;
    std::vector<float> recoLep_phi               ;
    // std::vector<float> recoLep_dxy               ;
    //std::vector<float> recoLep_dz                ;
      
//=================================================================================================================== 
  /* input variables*/
  
  edm::Handle<std::vector<pat::Jet> > jets;
  edm::Handle<std::vector<pat::Electron> > ele;
  edm::Handle<std::vector<pat::Muon> > muo;
  edm::Handle<std::vector<pat::Tau> > tau;
  /* labels */
  
  edm::InputTag jetLabel("selectedPatJetsCA8CHSprunedForBoostedTaus");
  edm::InputTag eleLabel("patElectronsWithTriggerBoosted");
  edm::InputTag muoLabel("patMuonsWithTriggerBoosted");
  edm::InputTag tauLabel("selectedPatTausBoosted");
//===================================================================================================================      
  void branch( TTree* tree ){
  
    tree->Branch( "nrecoJets"	, &nrecoJets	);         
    tree->Branch( "recoJet_pt"  , &recoJet_pt	);            
    tree->Branch( "recoJet_eta" , &recoJet_eta  );            
    tree->Branch( "recoJet_mass", &recoJet_mass );     
    tree->Branch( "recoJet_phi" , &recoJet_phi  );            
    tree->Branch( "recoJet_e"	, &recoJet_e	);        

    /*  lepton */

    /*  Electron*/
    tree->Branch( "nrecoLep"		    , &nrecoLep 		 );     
    tree->Branch( "recoLep_type"  	    , &recoLep_type		 );
    tree->Branch( "recoLep_charge"	    , &recoLep_charge		 );
   tree->Branch( "recoLep_e"		    , &recoLep_e		 );
    tree->Branch( "recoLep_eta"		    , &recoLep_eta		 );
    tree->Branch( "recoLep_mass"  	    , &recoLep_mass		 );
    tree->Branch( "recoLep_pt"		    , &recoLep_pt		 ); 
    tree->Branch( "recoLep_phi"		    , &recoLep_phi		 );
    // tree->Branch( "recoLep_dxy"		    , &recoLep_dxy		 );
    //tree->Branch( "recoLep_dz"		    , &recoLep_dz		 );
  
  }

//===================================================================================================================        
  void getEventByLabels( edm::EventBase const & event ){

    event.getByLabel(jetLabel, jets);
    event.getByLabel(eleLabel, ele);
    event.getByLabel(muoLabel, muo);
    event.getByLabel(tauLabel, tau);
  }


//=================================================================================================================== 
  void reset( void ){
           
    recoJet_pt  .clear();
    recoJet_eta .clear();
    recoJet_mass.clear();
    recoJet_phi .clear();
    recoJet_e	.clear();
    
    recoLep_type.clear(); 
    recoLep_charge.clear();
    recoLep_e.clear();
    recoLep_eta.clear(); 
    recoLep_mass.clear(); 
    recoLep_pt.clear(); 
    recoLep_phi.clear(); 
    //  recoLep_dxy.clear(); 
    // recoLep_dz.clear(); 
    
  }
  
}

#endif // NtupleBranches_H
