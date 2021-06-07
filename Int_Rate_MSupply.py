#!python3

import sys ,os , requests
import time, json
import matplotlib.pyplot as plt
import Money_Supply_FRED as msf
import numpy as np

# This library retrieves and relies on data coming from FRED API
# Attributes
# List containing the three datasets to plot/analyze
#data_s_s =["DGS1","MANMM101USA657S","MABMM301USA657S"]
data_s_s =["DGS1","M1","M2"]
#DGS1 represents the 1-yr-Treasury Note
#M1 is the M1 money stock while M2 is M2 money stock

def growth_rate(id):

    #Put all data together in lists and dictionaries
    ob,ds,vs = msf.obtain_observations(id)
    # Cleaning up the "."
    #vs = [item.replace('.', '0') for item in vs]
    delta = 365 # 365 days like a year cycle
    pointer = 0
    #Initialize end lists
    final_values = list()
    final_date = list()
    while pointer <= len(ds):

        if (pointer+delta) <= len(ds):

            v_0 = float(vs[pointer])
            v_1 = float(vs[pointer+delta])
            if v_0 != 0:
                g = (v_1-v_0)/(v_0)
            else:
                g = v_1
            pointer = pointer + delta
            final_values.append(g)
            final_date.append(ds[pointer])
            print(g)
        else:
            end = len(ds)-1
            v_0 = float(vs[pointer])
            v_1 = float(vs[end])
            if v_0 != 0:
                g = (v_1-v_0)/(v_0)
            else:
                g = v_1
            g = (v_1 - v_0) / (v_0)
            final_values.append(g)
            final_date.append(ds[end])
            break



    return final_date, final_values

def constant_maturity(id, range):

    ob, ds, vs = msf.obtain_observations(id)
    delta = 365
    max = len(ds)-1
    samples_total = delta*int(range)
    min = max - samples_total
    ds = ds[min:max]
    vs= vs[min:max]
    pointer = 0
    vx=list()
    for index in vs:
        if index == ".":
            vx.append(0.0)
        else:
            vx.append(float(index))
        pointer = pointer + 1
    return ds,vx

def main():

    #fs,fv=growth_rate(data_s_s[0])
    fs,fv=constant_maturity(data_s_s[0],3)
    msf.plot_single(fs, fv, "date range", "%", "1yr treasury note")

if __name__ == "__main__":
    main()