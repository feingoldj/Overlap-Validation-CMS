import ROOT
import math
import style

def plot(tree_file_name, hist_name):
    f = ROOT.TFile(tree_file_name)
    t = f.Get("analysis/Overlaps")
    
    h = ROOT.TH1F(hist_name, hist_name, 100, -1000, 1000)
    
    h.SetDirectory(0)

    for entry in t:
        if not ((t.subdetID == 5) and (abs(t.modualZ_[0] - t.modualZ_[1]) < 0.5)):
            print("flag")
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

        A = 10000*(residualA - residualB)
        h.Fill(A)
    return h

#create histogram stack
hstack = ROOT.THStack("hstack","hstack")

#create legend
legend = ROOT.TLegend(.6, .7, .9, .9)
#legend style
legend.SetBorderSize(0)
legend.SetFillStyle(0)

hdefault = plot("Data.root", "Data")
hpositive = plot("Data_posRadial.root", "Data_posRadial")
hnegative = plot("Data_negRadial.root", "Data_negRadial")

hdefault.SetLineColor(2) #red
hpositive.SetLineColor(4) #blue
hnegative.SetLineColor(ROOT.kGreen+3) #dark green

hstack.Add(hdefault)
hstack.Add(hpositive)
hstack.Add(hnegative)


      
legend.AddEntry(hdefault, "#epsilon = 0", "l") 
legend.AddEntry(0, "mean = {:+.1f} #mum".format(hdefault.GetMean()).replace("-","#minus").replace("+"\
,"#plus"),"")
legend.AddEntry(hpositive, "#epsilon = #plus5e-4", "l")  
legend.AddEntry(0, "mean = {:+.1f} #mum".format(hpositive.GetMean()).replace("-","#minus").replace("+"\
,"#plus"), "")
legend.AddEntry(hnegative, "#epsilon = #minus5e-4", "l") 
legend.AddEntry(0, "mean = {:+.1f} #mum".format(hnegative.GetMean()).replace("-","#minus").replace("+","#plus"), "")

#THStack was originally designed for stack plots where each histogram has the previous ones added to it, "nostack" avoids that.

c = ROOT.TCanvas()
hstack.Draw("nostack")
legend.Draw()

#have to do this AFTER hstack.Draw().  Otherwise the axes don't exist yet and you get a segmentation fault
hstack.GetXaxis().SetTitle("hit_{A} - pred_{A} - (hit_{B} - pred_{B}) (#mum)")
hstack.GetYaxis().SetTitle("number of events")
hstack.GetXaxis().SetNdivisions(404)

save_as_file_name = "hStack_Data_TOB"

for ext in "png", "eps", "root", "pdf":
        c.SaveAs("/eos/home-j/jfeingol/www/OverlapAlignmentValidation/Radial/"+save_as_file_name+"." +ext)



#print("Entered data_posRadial")
#plot("HitRes_realData_Radial.root", "data_posRadial")
#print("Entered data_negRadial")
#plot("HitRes_realData_negRadial.root", "data_negRadial")
#print("Entered data")
#plot("HitRes_realData.root", "data")
#print("Entered MC_Radial")
#plot("HitResRadial.root","MC_posRadial")
#print("Entered MC")
#plot("HitRes1.root","MC")
#print("Entered MC_negRadial")
#plot("HitRes_MC_negRadial.root","MC_negRadial") 


