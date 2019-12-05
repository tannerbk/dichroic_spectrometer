import ROOT
import numpy as np
import sys
from fill_graph import fill, hist

def plot_white(plot, dirname):

    data_nf = np.loadtxt(str(dirname) + 'no_filter.txt')
    data_0  = np.loadtxt(str(dirname) + '0deg.txt')
    data_15 = np.loadtxt(str(dirname) + '15deg.txt')
    data_30 = np.loadtxt(str(dirname) + '30deg.txt')
    data_45 = np.loadtxt(str(dirname) + '45deg.txt')
    data_60 = np.loadtxt(str(dirname) + '60deg.txt')
    data_75 = np.loadtxt(str(dirname) + '75deg.txt')

    g_nf, d_nf, l_nf = fill(data_nf)
    g_0,  d_0, l_0   = fill(data_0)
    g_15, d_15, l_15 = fill(data_15)
    g_30, d_30, l_30 = fill(data_30)
    g_45, d_45, l_45 = fill(data_45)
    g_60, d_60, l_60 = fill(data_60)
    g_75, d_75, l_75 = fill(data_75)

    d = [d_nf, d_0, d_15, d_30, d_45, d_60, d_75]
    g_r0, g_r15, g_r30, g_r45, g_r60, g_r75 = hist(d, l_nf)

    if plot:
        c1 = ROOT.TCanvas("c1","c1",800,600)

        g_nf.GetXaxis().SetTitle("Wavelength (nm)")
        g_nf.GetYaxis().SetTitle("Intensity (A.U.)")
        g_nf.GetXaxis().SetLabelFont(132)
        g_nf.GetYaxis().SetLabelFont(132)
        g_nf.GetYaxis().SetTitleFont(132)
        g_nf.GetXaxis().SetTitleFont(132)
        g_nf.GetYaxis().SetTitleOffset(1.3)
        g_nf.GetXaxis().SetRangeUser(300.0, 800.0)
        g_nf.Draw("")

        g_0.SetLineColor(ROOT.kRed)
        g_0.SetMarkerColor(ROOT.kRed)
        g_0.Draw("same")

        g_15.SetLineColor(ROOT.kBlue)
        g_15.SetMarkerColor(ROOT.kBlue)
        g_15.Draw("same")

        g_30.SetLineColor(ROOT.kViolet)
        g_30.SetMarkerColor(ROOT.kViolet)
        g_30.Draw("same")

        g_45.SetLineColor(ROOT.kCyan)
        g_45.SetMarkerColor(ROOT.kCyan)
        g_45.Draw("same")

        g_60.SetLineColor(ROOT.kGreen)
        g_60.SetMarkerColor(ROOT.kGreen)
        g_60.Draw("same")

        g_75.SetLineColor(ROOT.kGray)
        g_75.SetMarkerColor(ROOT.kGray)
        g_75.Draw("same")

        t1 = ROOT.TLegend(0.15, 0.55, 0.4, 0.85)
        t1.SetTextFont(132)
        t1.SetBorderSize(0)
        t1.AddEntry(g_nf, "No filter", "l")
        t1.AddEntry(g_0, "0 Degrees", "l")
        t1.AddEntry(g_15, "15 Degrees", "l")
        t1.AddEntry(g_30, "30 Degrees", "l")
        t1.AddEntry(g_45, "45 Degrees", "l")
        t1.AddEntry(g_60, "60 Degrees", "l")
        t1.AddEntry(g_75, "75 Degrees", "l")
        t1.Draw("same")

        c1.Update()

        c2 = ROOT.TCanvas("c2","c2",800,600)

        g_r0.GetXaxis().SetTitle("Wavelength (nm)")
        g_r0.GetYaxis().SetTitle("Transmission (%)")
        g_r0.GetXaxis().SetLabelFont(132)
        g_r0.GetYaxis().SetLabelFont(132)
        g_r0.GetYaxis().SetTitleFont(132)
        g_r0.GetXaxis().SetTitleFont(132)
        g_r0.GetYaxis().SetTitleOffset(1.4)
        g_r0.GetXaxis().SetRangeUser(400.0, 750.0)
        g_r0.GetYaxis().SetRangeUser(0.0, 1.0)
        g_r0.SetStats(0)

        g_r0.SetLineColor(ROOT.kRed)
        g_r0.SetMarkerColor(ROOT.kRed)
        g_r0.Draw("")

        g_r15.SetLineColor(ROOT.kBlue)
        g_r15.SetMarkerColor(ROOT.kBlue)
        g_r15.Draw("same")

        g_r30.SetLineColor(ROOT.kViolet)
        g_r30.SetMarkerColor(ROOT.kViolet)
        g_r30.Draw("same")

        g_r45.SetLineColor(ROOT.kCyan)
        g_r45.SetMarkerColor(ROOT.kCyan)
        g_r45.Draw("same")

        g_r60.SetLineColor(ROOT.kGreen)
        g_r60.SetMarkerColor(ROOT.kGreen)
        g_r60.Draw("same")

        g_r75.SetLineColor(ROOT.kGray)
        g_r75.SetMarkerColor(ROOT.kGray)
        g_r75.Draw("same")

        c2.Update()

        raw_input()

    return g_r0, g_r15, g_r30, g_r45, g_r60, g_r75

if __name__=='__main__':

    dirname = sys.argv[1]

    plot_white(True, dirname)
