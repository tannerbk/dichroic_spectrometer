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
    except:
        sys.exit(help())

    gr0_365, gr15_365, gr30_365, gr45_365, gr60_365, gr75_365 = plot_365(False, dirname1)
    gr0_405, gr15_405, gr30_405, gr45_405, gr60_405, gr75_405 = plot_405(False, dirname2)
    gr0_white, gr15_white, gr30_white, gr45_white, gr60_white, gr75_white = plot_white(False, dirname3)

    gr0deg = transmission_0deg()
    gr45deg = transmission_45deg()

    g_r0  = ROOT.TH1D("","",4000,0,1000)
    g_r15 = ROOT.TH1D("","",4000,0,1000)
    g_r30 = ROOT.TH1D("","",4000,0,1000)
    g_r45 = ROOT.TH1D("","",4000,0,1000)
    g_r60 = ROOT.TH1D("","",4000,0,1000)
    g_r75 = ROOT.TH1D("","",4000,0,1000)

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

    c3 = ROOT.TCanvas("c3","c3",800,600)

    g_r0.GetXaxis().SetTitle("Wavelength (nm)")
    g_r0.GetYaxis().SetTitle("Transmission (%)")
    g_r0.GetXaxis().SetLabelFont(132)
    g_r0.GetYaxis().SetLabelFont(132)
    g_r0.GetYaxis().SetTitleFont(132)
    g_r0.GetXaxis().SetTitleFont(132)
    g_r0.GetYaxis().SetTitleOffset(1.4)
    g_r0.GetXaxis().SetRangeUser(350.0, 750.0)
    g_r0.GetYaxis().SetRangeUser(0.0, 1.25)
    g_r0.SetStats(0)

    g_r0.SetLineColor(ROOT.kRed)
    g_r0.SetMarkerColor(ROOT.kRed)

    g_r15.SetLineColor(ROOT.kBlue)
    g_r15.SetMarkerColor(ROOT.kBlue)

    g_r30.SetLineColor(ROOT.kViolet)
    g_r30.SetMarkerColor(ROOT.kViolet)

    g_r45.SetLineColor(ROOT.kCyan)
    g_r45.SetMarkerColor(ROOT.kCyan)

    g_r60.SetLineColor(ROOT.kGreen)
    g_r60.SetMarkerColor(ROOT.kGreen)

    g_r75.SetLineColor(ROOT.kGray)
    g_r75.SetMarkerColor(ROOT.kGray)

    g_r0.Draw("")
    g_r15.Draw("same")
    g_r30.Draw("same")
    g_r45.Draw("same")
    g_r60.Draw("same")
    g_r75.Draw("same")

    t1 = ROOT.TLegend(0.55, 0.55, 0.85, 0.85)
    t1.SetTextFont(132)
    t1.SetBorderSize(0)
    t1.AddEntry(g_r0, "0 Degrees", "l")
    t1.AddEntry(g_r15, "15 Degrees", "l")
    t1.AddEntry(g_r30, "30 Degrees", "l")
    t1.AddEntry(g_r45, "45 Degrees", "l")
    t1.AddEntry(g_r60, "60 Degrees", "l")
    t1.AddEntry(g_r75, "75 Degrees", "l")
    t1.Draw("same")

    c3.Update()

    c4 = ROOT.TCanvas("c4","c4",800,600)

    #g_r0.Draw("")
    #gr0deg.SetLineColor(ROOT.kBlack)
    #gr0deg.SetMarkerColor(ROOT.kBlack)
    #gr0deg.Draw("P same")

    g_r45.Draw("")
    gr45deg.SetLineColor(ROOT.kBlack)
    gr45deg.SetMarkerColor(ROOT.kBlack)
    gr45deg.Draw("P same")

    c4.Update()

    filename = sys.argv[4]

    f  = open(filename, "w")

    for i in range(g_r0.GetNbinsX()):
        wavelength = g_r0.GetBinCenter(i)

        transmission0  = g_r0.GetBinContent(i)
        transmission15 = g_r15.GetBinContent(i)
        transmission30 = g_r30.GetBinContent(i)
        transmission45 = g_r45.GetBinContent(i)
        transmission60 = g_r60.GetBinContent(i)
        transmission75 = g_r75.GetBinContent(i)

        if(wavelength > 350 and wavelength < 750):
            f.write("0, %f, %f\n" % (wavelength, transmission0))
            f.write("15, %f, %f\n" % (wavelength, transmission15))
            f.write("30, %f, %f\n" % (wavelength, transmission30))
            f.write("45, %f, %f\n" % (wavelength, transmission45))
            f.write("60, %f, %f\n" % (wavelength, transmission60))
            f.write("75, %f, %f\n" % (wavelength, transmission75))

    raw_input()
