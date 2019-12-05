import ROOT
import numpy as np
import sys
from fill_graph import one_hist

def plot_dichroicon(plot, dirname):

    data_nf = np.loadtxt(str(dirname) + 'no_filter.txt')
    data_0  = np.loadtxt(str(dirname) + '0deg.txt')
    data_d = np.loadtxt(str(dirname) +  'dichroicon.txt')

    g_nf = one_hist(data_nf)
    g_0  = one_hist(data_0)
    g_d  = one_hist(data_d)

    c1 = ROOT.TCanvas("c1","c1",800,600)

    g_nf.SetLineColor(ROOT.kBlack)
    g_nf.SetMarkerColor(ROOT.kBlack)
    g_nf.GetXaxis().SetTitle("Wavelength (nm)")
    g_nf.GetYaxis().SetTitle("A.U")
    g_nf.GetXaxis().SetLabelFont(132)
    g_nf.GetYaxis().SetLabelFont(132)
    g_nf.GetYaxis().SetTitleFont(132)
    g_nf.GetXaxis().SetTitleFont(132)
    g_nf.GetYaxis().SetTitleOffset(1.4)
    g_nf.Draw("")
    g_nf.SetStats(0)

    g_0.SetLineColor(ROOT.kRed)
    g_0.SetMarkerColor(ROOT.kRed)
    g_0.Draw("same")

    g_d.SetLineColor(ROOT.kBlue)
    g_d.SetMarkerColor(ROOT.kBlue)
    g_d.Draw("same")

    g_nf.Scale(1.0/g_nf.Integral())
    g_0.Scale(1.0/g_0.Integral())
    g_d.Scale(1.0/g_d.Integral())

    m1 = g_nf.GetMaximum()
    m2 = g_0.GetMaximum()
    m3 = g_d.GetMaximum()

    g_0.Scale(0.95*m1/m2)
    g_d.Scale(0.98*m1/m3)

    g_nf.GetXaxis().SetRangeUser(350.0, 750.0)
    g_nf.GetYaxis().SetRangeUser(0.0, 0.002)

    t1 = ROOT.TLegend(0.15, 0.55, 0.4, 0.85)
    t1.SetTextFont(132)
    t1.SetBorderSize(0)
    t1.AddEntry(g_nf, "No filter", "l")
    t1.AddEntry(g_0,  "0 Degrees", "l")
    t1.AddEntry(g_d,  "Dichroicon", "l")
    t1.Draw("same")

    c1.Update()

    raw_input()

if __name__=='__main__':

    dirname = sys.argv[1]

    plot_dichroicon(True, dirname)
