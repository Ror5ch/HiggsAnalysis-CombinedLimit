HiggsAnalysis-CombinedLimit
===========================

### Datacards

/hdfs/store/user/knam/forYurii

### Setup
```
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src
cmsenv
git clone git@github.com:Ror5ch/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
git fetch origin
git checkout HTTHZZ
cd ../..
scram b -j 8
```
### Commands (for fL1)
```
tar -xzvf datacards_fL1.tar.gz
tar -xzvf datacards_HZZ.tar.gz

ulimit -s unlimited

combineCards.py htt_*.txt hzz4l_*.txt >& fL1_HTTHZZ_years.txt.cmb 
text2workspace.py -m 125 fL1_HTTHZZ_years.txt.cmb -P HiggsAnalysis.CombinedLimit.SpinZeroStructure_FL1:hzzAnomalousCouplingsFromHistogramsNonSMEFT --PO fL1 --PO fL1Zg --PO fa2 --PO fa3 --PO fL1asPOI --PO fL1ZgasPOIrelative --PO fa2asPOIrelative --PO fa3asPOIrelative --PO allowPMF -o fL1_HTTHZZ_years.root
```
### Commands (for the others)
Every setup is the same as fL1, you just need to change options for text2workspace as follows:
```
text2workspace.py -m 125 fL1Zg_HTTHZZ_years.txt.cmb -P HiggsAnalysis.CombinedLimit.SpinZeroStructure_FL1Zg:hzzAnomalousCouplingsFromHistogramsNonSMEFT --PO fL1 --PO fL1Zg --PO fa2 --PO fa3 --PO fL1asPOIrelative --PO fL1ZgasPOI --PO fa2asPOIrelative --PO fa3asPOIrelative --PO allowPMF -o fL1Zg_HTTHZZ_years.root
text2workspace.py -m 125 fa2_HTTHZZ_years.txt.cmb -P HiggsAnalysis.CombinedLimit.SpinZeroStructure_FA2:hzzAnomalousCouplingsFromHistogramsNonSMEFT --PO fL1 --PO fL1Zg --PO fa2 --PO fa3 --PO fL1asPOIrelative --PO fL1ZgasPOIrelative --PO fa2asPOI --PO fa3asPOIrelative --PO allowPMF -o fa2_HTTHZZ_years.root
text2workspace.py -m 125 fa3_HTTHZZ_years.txt.cmb -P HiggsAnalysis.CombinedLimit.SpinZeroStructure_FA3:hzzAnomalousCouplingsFromHistogramsNonSMEFT --PO fL1 --PO fL1Zg --PO fa2 --PO fa3 --PO fL1asPOIrelative --PO fL1ZgasPOIrelative --PO fa2asPOIrelative --PO fa3asPOI --PO allowPMF -o fa3_HTTHZZ_years.root
``` 