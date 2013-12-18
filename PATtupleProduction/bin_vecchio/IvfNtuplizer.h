#ifndef IvfNtuplizer_H
#define IvfNtuplizer_H

#include "NtupleBranches.h"

using namespace NtupleBranches;

namespace IvfNtuplizer {

  void fillIvfBranches( void ){
  
    nivfSVs = (*numberOfivfSVs)[0];
    for( int v = 0; v < nivfSVs; ++v ){
      ivf_vtxE       .push_back((*ivfSVE	)[v]);
      ivf_vtxMass    .push_back((*ivfSVMass	)[v]);
      ivf_vtxPt      .push_back((*ivfSVPt	)[v]);
      ivf_vtxEta     .push_back((*ivfSVEta	)[v]);
      ivf_vtxPhi     .push_back((*ivfSVPhi	)[v]);
      ivf_vtxX       .push_back((*ivfSVX	)[v]);
      ivf_vtxY       .push_back((*ivfSVY	)[v]);
      ivf_vtxZ       .push_back((*ivfSVZ	)[v]);
      ivf_vtxXerr    .push_back((*ivfSVXerr	)[v]);
      ivf_vtxYerr    .push_back((*ivfSVYerr	)[v]);
      ivf_vtxZerr    .push_back((*ivfSVZerr	)[v]);      
      ivf_numTracksSV.push_back((*ivfSVNumTracks)[v]);  
      TVector3 vtx3d   ((*ivfSVX   )[v],(*ivfSVY   )[v],(*ivfSVZ   )[v]); ivf_vtx3dL   .push_back(vtx3d.Mag()	);
      TVector3 vtxErr3d((*ivfSVXerr)[v],(*ivfSVYerr)[v],(*ivfSVZerr)[v]); ivf_vtx3dLerr.push_back(vtxErr3d.Mag());	
      TVector2 vtx2d   ((*ivfSVX   )[v],(*ivfSVY   )[v]); ivf_vtx2dL   .push_back(vtx2d.Mod()	);
      TVector2 vtxErr2d((*ivfSVXerr)[v],(*ivfSVYerr)[v]); ivf_vtx2dLerr.push_back(vtxErr2d.Mod());
    }

    for( size_t t = 0; t < ivfTracksVtxIndex->size(); ++t ){
      ivfTrack_ndof    .push_back((*ivfTracksNdof    )[t]);
      ivfTrack_nhits   .push_back((*ivfTracksNhits   )[t]);
      ivfTrack_vtxIndex.push_back((*ivfTracksVtxIndex)[t]);
      ivfTrack_chi2    .push_back((*ivfTracksChi2    )[t]);
      ivfTrack_dxy     .push_back((*ivfTracksDxy     )[t]);
      ivfTrack_dxyErr  .push_back((*ivfTracksDxyError)[t]);
      ivfTrack_dz      .push_back((*ivfTracksDz      )[t]);
      ivfTrack_dzErr   .push_back((*ivfTracksDzError )[t]);
      ivfTrack_eta     .push_back((*ivfTracksEta     )[t]);
      ivfTrack_phi     .push_back((*ivfTracksPhi     )[t]);
      ivfTrack_pt      .push_back((*ivfTracksPt      )[t]);
    }
  
  }

}

#endif // IvfNtuplizer_H
