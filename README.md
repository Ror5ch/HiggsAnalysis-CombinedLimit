HiggsAnalysis-CombinedLimit
===========================

### Datacards (dummy) for test

http://stash.osgconnect.net/+knam/dummy.tar.gz

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
### Test commands
```
tar -xzvf dummy.tar.gz

ulimit -s unlimited

text2workspace.py -m 125 dummy_card.txt.cmb -P HiggsAnalysis.CombinedLimit.SpinZeroStructure_FL1:hzzAnomalousCouplingsFromHistogramsNonSMEFT --PO fL1 --PO fL1Zg --PO fa2 --PO fa3 --PO fL1asPOI --PO fL1ZgasPOIrelative --PO fa2asPOIrelative --PO fa3asPOIrelative --PO allowPMF -o test.root
``` 
