#ifndef JetsNtuplizer_H
#define JetsNtuplizer_H

#include "NtupleBranches.h"

using namespace NtupleBranches;

namespace JetsNtuplizer{

  void fillJetsBranches( void ){

   /*here we want to save the jets info*/
    nrecoJets = 0;
    for(unsigned j=0; j<jets->size(); ++j){
      nrecoJets++;
      recoJet_pt  .push_back((*jets)[j].pt()  );
      recoJet_eta .push_back((*jets)[j].eta() );
      recoJet_mass.push_back((*jets)[j].phi() );
      recoJet_phi .push_back((*jets)[j].mass());
    }
         
  }

}

#endif // JetsNtuplizer_H
