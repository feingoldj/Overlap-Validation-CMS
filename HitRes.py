import ROOT
f = ROOT.TFile("HitResRadial.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file
c = ROOT.TCanvas()#Makes a canvas to draw stuff
t.Draw("hitX[0] - predX[0] - (hitX[1] - predX[1])>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/RadT_Hits2."+ext)

f = ROOT.TFile("HitRes.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file
c = ROOT.TCanvas()#Makes a canvas to draw stuff
t.Draw("hitX[0] - predX[0] - (hitX[1] - predX[1])>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/ConT_Hits2."+ext)


f = ROOT.TFile("HitResRadial.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file
c = ROOT.TCanvas()#Makes a canvas to draw stuff
t.Draw("hitX[0] - predX[0]>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/RadT_Hits1."+ext)

f = ROOT.TFile("HitRes.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file
c = ROOT.TCanvas()#Makes a canvas to draw stuff
t.Draw("hitX[0] - predX[0]>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/ConT_Hits1."+ext)

#plots on realData

f = ROOT.TFile("HitRes_realData.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file                        
c = ROOT.TCanvas()#Makes a canvas to draw stuff                                          
t.Draw("hitX[0] - predX[0]>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_Hits1."+ext)

f = ROOT.TFile("HitRes_realData.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file                        
c = ROOT.TCanvas()#Makes a canvas to draw stuff                                          
t.Draw("hitX[0] - predX[0] - (hitX[1] - predX[1])>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_Hits2."+ext)

#plots on realData w/ positive Radial misalignment

f = ROOT.TFile("HitRes_realData_Radial.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file                                    
c = ROOT.TCanvas()#Makes a canvas to draw stuff                                                      
t.Draw("hitX[0] - predX[0]>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_posRadial_Hits1."+ext)

f = ROOT.TFile("HitRes_realData_Radial.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file                                      
c = ROOT.TCanvas()#Makes a canvas to draw stuff                                                       
t.Draw("hitX[0] - predX[0] - (hitX[1] - predX[1])>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_posRadial_Hits2."+ext)

#plots on readData w/ negative Radial misalignment

f = ROOT.TFile("HitRes_realData_negRadial.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file                                                                         
c = ROOT.TCanvas()#Makes a canvas to draw stuff                                                                                           
t.Draw("hitX[0] - predX[0]>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_negRadial_Hits1."+ext)

f = ROOT.TFile("HitRes_realData_negRadial.root")
t = f.Get("analysis/Overlaps")#opens the tree from the ROOT file                                                                          
c = ROOT.TCanvas()#Makes a canvas to draw stuff                                                                                     
t.Draw("hitX[0] - predX[0] - (hitX[1] - predX[1])>>h(100,-0.1,0.1)", "(subdetID == 5) && abs(modualZ_[0] - modualZ_[1]) < 0.5")
for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_negRadial_Hits2."+ext)

#plots on real data w/ positive radial misalignment using phi 

import math 

f = ROOT.TFile("HitRes_realData_Radial.root")
t = f.Get("analysis/Overlaps")
c = ROOT.TCanvas()

h = ROOT.TH1F("h", "h", 100, -.1, .1)

hitPhi0 = math.atan2(t.hitY[0], t.hitX[0])
hitPhi1 = math.atan2(t.hitY[1], t.hitX[1])
predPhi0 = math.atan2(t.predY[0], t.predX[0])
predPhi1 = math.atan2(t.predY[1], t.predX[1])
modulePhi0 = math.atan2(t.modualY_[0], t.modualX_[0]) #module was mispelled in creating the root file. 
modulePhi1 = math.atan2(t.modualY_[1], t.modualX_[1])

if modulePhi0 > modulePhi1:
    hitPhiA = hitPhi1
    hitPhiB = hitPhi0
    predPhiA = predPhi1
    predPhiB = predPhi0
else:
    hitPhiA = hitPhi0
    hitPhiB = hitPhi1
    predPhiA = predPhi0
    predPhiB = predPhi1

print(hitPhiA)
print(hitPhiB)
print(predPhiA)
print(predPhiB)


moduleR0 = math.sqrt(t.modualX_[0]**2 + t.modualY_[0]**2)
moduleR1 = math.sqrt(t.modualX_[1]**2 + t.modualY_[1]**2)
r = 0.5*(moduleR0 + moduleR1)

for entry in t:
    h.Fill((hitPhiA - predPhiA - (hitPhiB - predPhiB))*r)

h.Draw()

for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_posRadial_Hits2_Phi_2."+ext)
