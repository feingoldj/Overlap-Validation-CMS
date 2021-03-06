import ROOT
import math

def plot(tree_file_name, save_as_file_name):
    f = ROOT.TFile(tree_file_name)
    t = f.Get("analysis/Overlaps")
    c = ROOT.TCanvas()
    h = ROOT.TH1F("h", "h", 100, -0.1, 0.1)


    for entry in t:
        if not ((t.subdetID == 1) and (abs(t.modualZ_[0] - t.modualZ_[1]) < 0.5)):
     
            continue
    
        modulePhi0 = math.atan2(t.modualY_[0], t.modualX_[0]) #module was mispelled in creating the root file.   
        modulePhi1 = math.atan2(t.modualY_[1], t.modualX_[1])
        
        if modulePhi0 > modulePhi1:
            hitXA = t.hitX[1]
            hitXB = t.hitX[0]
            predXA = t.predX[1]
            predXB = t.predX[0]
            deltaPhiA = t.deltaphi_[1]
            deltaPhiB = t.deltaphi_[0]
        else:
            hitXA = t.hitX[0]
            hitXB = t.hitX[1]
            predXA = t.predX[0]
            predXB = t.predX[1]
            deltaPhiA = t.deltaphi_[0]
            deltaPhiB = t.deltaphi_[1]
        
        residualA = hitXA - predXA
        residualB = hitXB - predXB
        if deltaPhiA < 0:
            residualA *= -1
        if deltaPhiB < 0:
            residualB *= -1 
        h.Fill(residualA - residualB)
    
    h.Draw()
    for ext in "png", "eps", "root", "pdf":
        c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/Radial/"+save_as_file_name+"." +ext)


plot("Data_collisions.root","Data_collisions_BPix")

print("Entered data_posRadial")
#plot("HitRes_realData_Radial.root", "data_posRadial")
print("Entered data_negRadial")
#plot("HitRes_realData_negRadial.root", "data_negRadial")
print("Entered data")
#plot("HitRes_realData.root", "data")
print("Entered MC_Radial")
#plot("HitResRadial.root","MC_posRadial")
print("Entered MC")
#plot("HitRes1.root","MC")
print("Entered MC_negRadial")
#plot("HitRes_MC_negRadial.root","MC_negRadial") 

f = ROOT.TFile("HitRes_realData_Radial.root")
t = f.Get("analysis/Overlaps")
c = ROOT.TCanvas()

h = ROOT.TH1F("h", "h", 100, -0.1, 0.1)

for entry in t:
    #hitPhi0 = math.atan2(t.hitY[0], t.hitX[0])
    #hitPhi1 = math.atan2(t.hitY[1], t.hitX[1])
    #predPhi0 = math.atan2(t.predY[0], t.predX[0])
    #predPhi1 = math.atan2(t.predY[1], t.predX[1])
    modulePhi0 = math.atan2(t.modualY_[0], t.modualX_[0]) #module was mispelled in creating the root file.    
    modulePhi1 = math.atan2(t.modualY_[1], t.modualX_[1])
    
    #print("-------------")
    #print(hitPhi0)
    #print(hitPhi1)
    #print(predPhi0)
    #print(predPhi1)
    #print(modulePhi0)
    #print(modulePhi1)
    #print("-------------")

    if modulePhi0 > modulePhi1:
        hitXA = t.hitX[1]
        hitXB = t.hitX[0]
        predXA = t.predX[1]
        predXB = t.predX[0]
    else:
        hitXA = t.hitX[0]
        hitXB = t.hitX[1]
        predXA = t.predX[0]
        predXB = t.predX[1]
    
    #moduleR0 = math.sqrt(t.modualX_[0]**2 + t.modualY_[0]**2)
    #moduleR1 = math.sqrt(t.modualX_[1]**2 + t.modualY_[1]**2)
    #r = 0.5*(moduleR0 + moduleR1)
    #print("this is r")
    #print(r)
    #print("this is delta phi")
    #print((hitPhiA - predPhiA - (hitPhiB - predPhiB)))

    h.Fill((hitXA - predXA - (hitXB - predXB)))

h.Draw()

for ext in "png", "eps", "root", "pdf":
    c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/realData_posRadial_Hits2_Phi_2."+ext)


