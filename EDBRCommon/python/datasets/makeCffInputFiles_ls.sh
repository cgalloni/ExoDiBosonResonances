#!/bin/sh

### Output directory for the lists ###

OUTPUTDIR=$USER
mkdir -p $OUTPUTDIR

### Location of CMGtuples ###

MAINDIRMC=/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1d/Summer12/
MAINDIRDATA=/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/productionV1d/Run2012/
#MAINDIRMC=/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/santanas/production0312/Summer12/CA8/
#MAINDIRDATA=/store/group/phys_exotica/leptonsPlusJets/ExoDiBosonResonances/CMGtuple/santanas/production0312/Run2012/CA8/



### Make lists for DATA ###

### List for XWW
#for sample in SingleMu_Run2012A_13Jul2012_xww  SingleMu_Run2012A_recover_xww SingleMu_Run2012B_13Jul2012_xww SingleMu_Run2012C_24Aug2012_xww SingleMu_Run2012C_PromptReco_xww SingleMu_Run2012C_EcalRecove_xww  SingleMu_Run2012D_PromptReco_xww  SingleElectron_Run2012A_13Jul2012_xww SingleElectron_Run2012A_recover_xww SingleElectron_Run2012B_13Jul2012_xww SingleElectron_Run2012C_24Aug2012_xww SingleElectron_Run2012C_EcalRecove_xww   SingleElectron_Run2012C_PromptReco_xww SingleElectron_Run2012D_PromptReco_xww 
### List for XZZ
#DoubleMu_Run2012A_13Jul2012 DoubleMu_Run2012A_recover DoubleMu_Run2012B_13Jul2012 DoubleMu_Run2012C_24Aug2012 DoubleMu_Run2012C_PRv2 DoubleMu_Run2012D_PRv1 DoublePhotonHighPt_Run2012B_13Jul2012  DoublePhotonHighPt_Run2012C_24Aug2012 DoublePhotonHighPt_Run2012C_PRv2 DoublePhotonHighPt_Run2012D_PRv1 Photon_Run2012A_13Jul2012 Photon_Run2012A_recover

for sample in  DoubleMu_Run2012A_13Jul2012 DoubleMu_Run2012A_recover DoubleMu_Run2012B_13Jul2012 DoubleMu_Run2012C_24Aug2012 DoubleMu_Run2012C_PRv2 DoubleMu_Run2012D_PRv1 DoublePhotonHighPt_Run2012B_13Jul2012  DoublePhotonHighPt_Run2012C_24Aug2012 DoublePhotonHighPt_Run2012C_PRv2 DoublePhotonHighPt_Run2012D_PRv1 Photon_Run2012A_13Jul2012 Photon_Run2012A_recover
do
    echo $MAINDIRDATA/$sample
	cmsLs $MAINDIRDATA/$sample | grep .root | awk '{print $5}'  > tmp.txt
    python makeCffInputFiles_ls.py tmp.txt $OUTPUTDIR/cmgTuple_${sample}_cff.py
done

### Make lists for MC ###

### List for XWW
#for sample in TTBAR_xww TTBARpowheg_xww WZ_xww ZZ_xww  WW_xww WJetsPt50To70_xww WJetsPt70To100_xww WJetsPt100_xww WJetsPt180_xww DYJetsPt50To70_xww DYJetsPt70To100_xww  DYJetsPt100_xww BulkG_WW_lvjj_c1p0_M1000_xww BulkG_WW_lvjj_c1p0_M1500_xww BulkG_WW_lvjj_c1p0_M600_xww RSG_WW_lvjj_c0p2_M1000_xww RSG_WW_lvjj_c0p2_M1500_xww RSG_WW_lvjj_c0p2_M600_xww SingleTopBarSchannel_xww SingleTopBarTWchannel_xww SingleTopBarTchannel_xww SingleTopSchannel_xww SingleTopTWchannel_xww SingleTopTchannel_xww BulkG_WW_lvjj_c0p2_M1000_xww BulkG_WW_lvjj_c0p2_M1100_xww  BulkG_WW_lvjj_c0p2_M1200_xww BulkG_WW_lvjj_c0p2_M1300_xww BulkG_WW_lvjj_c0p2_M1400_xww BulkG_WW_lvjj_c0p2_M1500_xww BulkG_WW_lvjj_c0p2_M1600_xww BulkG_WW_lvjj_c0p2_M1700_xww BulkG_WW_lvjj_c0p2_M1800_xww BulkG_WW_lvjj_c0p2_M1900_xww BulkG_WW_lvjj_c0p2_M2000_xww BulkG_WW_lvjj_c0p2_M2100_xww BulkG_WW_lvjj_c0p2_M2200_xww BulkG_WW_lvjj_c0p2_M2300_xww BulkG_WW_lvjj_c0p2_M2400_xww BulkG_WW_lvjj_c0p2_M2500_xww BulkG_WW_lvjj_c0p2_M600_xww BulkG_WW_lvjj_c0p2_M700_xww BulkG_WW_lvjj_c0p2_M800_xww BulkG_WW_lvjj_c0p2_M900_xww
### List for XZZ
# TTBAR DYJetsPt50To70 DYJetsPt70To100 DYJetsPt100 WW WZ ZZ BulkG_ZZ_lljj_c0p2_M600 BulkG_ZZ_lljj_c0p2_M700 BulkG_ZZ_lljj_c0p2_M800 BulkG_ZZ_lljj_c0p2_M900 BulkG_ZZ_lljj_c0p2_M1000 BulkG_ZZ_lljj_c0p2_M1100 BulkG_ZZ_lljj_c0p2_M1300 BulkG_ZZ_lljj_c0p2_M1400 BulkG_ZZ_lljj_c0p2_M1500 BulkG_ZZ_lljj_c0p2_M1700 BulkG_ZZ_lljj_c0p2_M1800 BulkG_ZZ_lljj_c0p2_M1900 BulkG_ZZ_lljj_c1p0_M1000 BulkG_ZZ_lljj_c1p0_M1500 BulkG_ZZ_lljj_c1p0_M600 RSG_ZZ_lljj_c0p05_M1000 RSG_ZZ_lljj_c0p2_M1000 RSG_ZZ_lljj_c0p2_M1500

for sample in  TTBARpowheg  DYJetsPt50To70 DYJetsPt70To100 DYJetsPt100 WJetsPt100 WW WZ ZZ BulkG_ZZ_lljj_c0p2_M600 BulkG_ZZ_lljj_c0p2_M700 BulkG_ZZ_lljj_c0p2_M800 BulkG_ZZ_lljj_c0p2_M900 BulkG_ZZ_lljj_c0p2_M1000 BulkG_ZZ_lljj_c0p2_M1100 BulkG_ZZ_lljj_c0p2_M1200 BulkG_ZZ_lljj_c0p2_M1300 BulkG_ZZ_lljj_c0p2_M1400 BulkG_ZZ_lljj_c0p2_M1500 BulkG_ZZ_lljj_c0p2_M1600 BulkG_ZZ_lljj_c0p2_M1700 BulkG_ZZ_lljj_c0p2_M1800 BulkG_ZZ_lljj_c0p2_M1900 BulkG_ZZ_lljj_c0p2_M2000 BulkG_ZZ_lljj_c1p0_M1000 BulkG_ZZ_lljj_c1p0_M1500 BulkG_ZZ_lljj_c1p0_M600 RSG_ZZ_lljj_c0p05_M1000 RSG_ZZ_lljj_c0p2_M1000 RSG_ZZ_lljj_c0p2_M1500
do
echo $MAINDIRMC/$sample
cmsLs $MAINDIRMC/$sample | grep .root | awk '{print $5}'  > tmp.txt
python makeCffInputFiles_ls.py tmp.txt $OUTPUTDIR/cmgTuple_${sample}_cff.py
done

### Remove tmp file ###

rm -f tmp.txt
