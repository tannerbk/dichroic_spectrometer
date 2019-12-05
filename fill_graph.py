import ROOT

MIN_CONTENT = 275

def transmission_45deg():

    # transmission for 45deg
    h = ROOT.TGraphErrors()

    wavelength = [385, 405, 450, 505, 555, 630]
    transmission = [95.2, 91.8, 92.9, 29.8, 0.33, 0.12]
    error = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
    lerror = [6, 7.5, 10, 15, 20, 7]
    for i in range(len(wavelength)):
        l = wavelength[i]
        t = transmission[i]
        h.SetPoint(i, l, t/100.0)
        h.SetPointError(i, lerror[i], error[i])

    h.SetMarkerStyle(20)

    return h

def transmission_0deg():

    # transmission for 0deg
    h = ROOT.TGraphErrors()

    wavelength = [385, 405, 450, 505, 555, 630]
    transmission = [96.2, 92.1, 95.2, 97.6, 29.1, 0.01]
    error = [0.04, 0.04, 0.04, 0.04, 0.04, 0.04]
    lerror = [6, 7.5, 10, 15, 20, 7]
    for i in range(len(wavelength)):
        l = wavelength[i]
        t = transmission[i]
        h.SetPoint(i, l, t/100.0)
        h.SetPointError(i, lerror[i], error[i])

    h.SetMarkerStyle(20)

    return h

def fill(data):

    h = ROOT.TGraph()
    d = []
    l = []
    count = 0
    for wavelength, intensity in data:
        h.SetPoint(count, wavelength, intensity)
        d.append(intensity)
        l.append(wavelength)
        count+=1

    return h, d, l

def one_hist(data):

    h = ROOT.TH1D("","",4000,0,1000)

    for wavelength, intensity in data:
        b = h.FindBin(wavelength)
        h.SetBinContent(b, intensity)

    return h

def hist(d, l_nf):

    g_r0  = ROOT.TH1D("","",4000,0,1000)
    g_r15 = ROOT.TH1D("","",4000,0,1000)
    g_r30 = ROOT.TH1D("","",4000,0,1000)
    g_r45 = ROOT.TH1D("","",4000,0,1000)
    g_r60 = ROOT.TH1D("","",4000,0,1000)
    g_r75 = ROOT.TH1D("","",4000,0,1000)

    d_nf, d_0, d_15, d_30, d_45, d_60, d_75 = d

    for i in range(len(d_nf)):
        no_filter = d_nf[i]
        deg0  = d_0[i]
        deg15 = d_15[i]
        deg30 = d_30[i]
        deg45 = d_45[i]
        deg60 = d_60[i]
        deg75 = d_75[i]

        rat0 = 0
        rat15 = 0
        rat30 = 0
        rat45 = 0
        rat60 = 0
        rat75 = 0
        if deg0 > MIN_CONTENT:
            rat0  = deg0/no_filter
        if deg15 > MIN_CONTENT:
            rat15 = deg15/no_filter
        if deg30 > MIN_CONTENT:
            rat30 = deg30/no_filter
        if deg45 > MIN_CONTENT:
            rat45 = deg45/no_filter
        if deg60 > MIN_CONTENT:
            rat60 = deg60/no_filter
        if deg75 > MIN_CONTENT:
            rat75 = deg75/no_filter

        wavelength = l_nf[i]

        b = g_r0.FindBin(wavelength)

        g_r0.SetBinContent(b, rat0)
        g_r15.SetBinContent(b, rat15)
        g_r30.SetBinContent(b, rat30)
        g_r45.SetBinContent(b, rat45)
        g_r60.SetBinContent(b, rat60)
        g_r75.SetBinContent(b, rat75)

    return g_r0, g_r15, g_r30, g_r45, g_r60, g_r75
