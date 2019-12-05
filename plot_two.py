import ROOT
from plot_365nm_spectrometer_data import plot_365
from plot_405nm_spectrometer_data import plot_405
from plot_white_spectrometer_data import plot_white
from fill_graph import transmission_0deg, transmission_45deg
import sys

def help():

    print "Run the code in the following way:"
    print "python plot_all.py 365nm_dirname 405nm_dirname white_dirname"

if __name__=='__main__':

    try:
        dirname1 = sys.argv[1]
        dirname2 = sys.argv[2]
        dirname3 = sys.argv[3]
        dirname4 = sys.argv[4]
        dirname5 = sys.argv[5]
        dirname6 = sys.argv[6]
    except:
        sys.exit(help())

    gr0_365, gr15_365, gr30_365, gr45_365, gr60_365, gr75_365 = plot_365(False, dirname1)
    gr0_405, gr15_405, gr30_405, gr45_405, gr60_405, gr75_405 = plot_405(False, dirname2)
    gr0_white, gr15_white, gr30_white, gr45_white, gr60_white, gr75_white = plot_white(False, dirname3)

    gr0_365_water, gr15_365_water, gr30_365_water, gr45_365_water, gr60_365_water, gr75_365_water = plot_365(False, dirname4)
    gr0_405_water, gr15_405_water, gr30_405_water, gr45_405_water, gr60_405_water, gr75_405_water = plot_405(False, dirname5)
    gr0_white_water, gr15_white_water, gr30_white_water, gr45_white_water, gr60_white_water, gr75_white_water = plot_white(False, dirname6)

    g_r0  = ROOT.TH1D("","",4000,0,1000)
    g_r15 = ROOT.TH1D("","",4000,0,1000)
    g_r30 = ROOT.TH1D("","",4000,0,1000)
    g_r45 = ROOT.TH1D("","",4000,0,1000)
    g_r60 = ROOT.TH1D("","",4000,0,1000)
    g_r75 = ROOT.TH1D("","",4000,0,1000)

    wg_r0  = ROOT.TH1D("","",4000,0,1000)
    wg_r15 = ROOT.TH1D("","",4000,0,1000)
    wg_r30 = ROOT.TH1D("","",4000,0,1000)
    wg_r45 = ROOT.TH1D("","",4000,0,1000)
    wg_r60 = ROOT.TH1D("","",4000,0,1000)
    wg_r75 = ROOT.TH1D("","",4000,0,1000)

    for i in range(4000):
        wavelength = g_r0.GetBinCenter(i)
        content0 = 0
        content15 = 0
        content30 = 0
        content45 = 0
        content60 = 0
        content75 = 0
        if(wavelength > 350 and wavelength <= 390):
            content0  = gr0_365.GetBinContent(i)
            content15 = gr15_365.GetBinContent(i)
            content30 = gr30_365.GetBinContent(i)
            content45 = gr45_365.GetBinContent(i)
            content60 = gr60_365.GetBinContent(i)
            content75 = gr75_365.GetBinContent(i)
        elif(wavelength > 390 and wavelength < 440):
            content0  = gr0_405.GetBinContent(i)
            content15 = gr15_405.GetBinContent(i)
            content30 = gr30_405.GetBinContent(i)
            content45 = gr45_405.GetBinContent(i)
            content60 = gr60_405.GetBinContent(i)
            content75 = gr75_405.GetBinContent(i)
        else:
            content0  = gr0_white.GetBinContent(i)
            content15 = gr15_white.GetBinContent(i)
            content30 = gr30_white.GetBinContent(i)
            content45 = gr45_white.GetBinContent(i)
            content60 = gr60_white.GetBinContent(i)
            content75 = gr75_white.GetBinContent(i)

        g_r0.SetBinContent(i, content0)
        g_r15.SetBinContent(i, content15)
        g_r30.SetBinContent(i, content30)
        g_r45.SetBinContent(i, content45)
        g_r60.SetBinContent(i, content60)
        g_r75.SetBinContent(i, content75)

    for i in range(4000):
        wavelength = wg_r0.GetBinCenter(i)
        content0 = 0
        content15 = 0
        content30 = 0
        content45 = 0
        content60 = 0
        content75 = 0
        if(wavelength > 350 and wavelength <= 390):
            content0  = gr0_365_water.GetBinContent(i)
            content15 = gr15_365_water.GetBinContent(i)
            content30 = gr30_365_water.GetBinContent(i)
            content45 = gr45_365_water.GetBinContent(i)
            content60 = gr60_365_water.GetBinContent(i)
            content75 = gr75_365_water.GetBinContent(i)
        elif(wavelength > 390 and wavelength < 410):
            content0  = gr0_405_water.GetBinContent(i)
            content15 = gr15_405_water.GetBinContent(i)
            content30 = gr30_405_water.GetBinContent(i)
            content45 = gr45_405_water.GetBinContent(i)
            content60 = gr60_405_water.GetBinContent(i)
            content75 = gr75_405_water.GetBinContent(i)
        else:
            content0  = gr0_white_water.GetBinContent(i)
            content15 = gr15_white_water.GetBinContent(i)
            content30 = gr30_white_water.GetBinContent(i)
            content45 = gr45_white_water.GetBinContent(i)
            content60 = gr60_white_water.GetBinContent(i)
            content75 = gr75_white_water.GetBinContent(i)

        wg_r0.SetBinContent(i, content0)
        wg_r15.SetBinContent(i, content15)
        wg_r30.SetBinContent(i, content30)
        wg_r45.SetBinContent(i, content45)
        wg_r60.SetBinContent(i, content60)
        wg_r75.SetBinContent(i, content75)

    c3 = ROOT.TCanvas("c3","c3",800,600)

    g_r0.GetXaxis().SetTitle("Wavelength (nm)")
    g_r0.GetYaxis().SetTitle("Transmission (%)")
    g_r0.GetXaxis().SetLabelFont(132)
    g_r0.GetYaxis().SetLabelFont(132)
    g_r0.GetYaxis().SetTitleFont(132)
    g_r0.GetXaxis().SetTitleFont(132)
    g_r0.GetYaxis().SetTitleOffset(1.4)
    g_r0.GetXaxis().SetRangeUser(350.0, 750.0)
    g_r0.GetYaxis().SetRangeUser(0.0, 1.05)
    g_r0.SetStats(0)

    R = 20
    g_r0.SetLineColor(ROOT.kBlack)
    g_r0.SetMarkerColor(ROOT.kBlack)
    g_r0.Rebin(R)

    wg_r0.SetLineColor(ROOT.kBlack)
    wg_r0.SetMarkerColor(ROOT.kBlack)
    wg_r0.SetLineStyle(2)
    wg_r0.Rebin(R)
    for i in range(4000):
        g_r0.SetBinContent(i, g_r0.GetBinContent(i)/R)
        wg_r0.SetBinContent(i, wg_r0.GetBinContent(i)/R)

    #g_r15.SetLineColor(ROOT.kBlue)
    #g_r15.SetMarkerColor(ROOT.kBlue)

    #g_r30.SetLineColor(ROOT.kViolet)
    #g_r30.SetMarkerColor(ROOT.kViolet)

    g_r45.SetLineColor(ROOT.kRed)
    g_r45.SetMarkerColor(ROOT.kRed)
    g_r45.Rebin(R)

    wg_r45.SetLineColor(ROOT.kRed)
    wg_r45.SetMarkerColor(ROOT.kRed)
    wg_r45.SetLineStyle(2)
    wg_r45.Rebin(R)
    for i in range(4000):
        g_r45.SetBinContent(i, g_r45.GetBinContent(i)/R)
        wg_r45.SetBinContent(i, wg_r45.GetBinContent(i)/R)

    #g_r60.SetLineColor(ROOT.kGreen)
    #g_r60.SetMarkerColor(ROOT.kGreen)

    #g_r75.SetLineColor(ROOT.kGray)
    #g_r75.SetMarkerColor(ROOT.kGray)

    g_r0.GetXaxis().SetRangeUser(350.0, 750.0)

    g_r0.Draw("")
    wg_r0.Draw("same")
    #g_r15.Draw("same")
    #g_r30.Draw("same")
    g_r45.Draw("same")
    wg_r45.Draw("same")
    #g_r60.Draw("same")
    #g_r75.Draw("same")

    t1 = ROOT.TLegend(0.55, 0.55, 0.85, 0.85)
    t1.SetTextFont(132)
    t1.SetBorderSize(0)
    t1.AddEntry(g_r0, "0 Degrees, Air", "l")
    t1.AddEntry(wg_r0, "0 Degrees, Water", "l")
    #t1.AddEntry(g_r15, "15 Degrees", "l")
    #t1.AddEntry(g_r30, "30 Degrees", "l")
    t1.AddEntry(g_r45, "45 Degrees, Air", "l")
    t1.AddEntry(wg_r45, "45 Degrees, Water", "l")
    #t1.AddEntry(g_r60, "60 Degrees", "l")
    #t1.AddEntry(g_r75, "75 Degrees", "l")
    t1.Draw("same")

    c3.Update()

    raw_input()
