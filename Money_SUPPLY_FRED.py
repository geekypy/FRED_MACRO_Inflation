#!python3

import sys ,os , requests
import time, json
import matplotlib.pyplot as plt

# Intellectual property of codenthusiast.com
# visit us @ codenthusiast,com
# This library retrieves and relies on data coming from FRED API
# Attributes

api_key="<your key here>"

def category_search_by():

    entry = input("Please introduce keywords: ")
    req1 = "https://api.stlouisfed.org/fred/series/search?search_text="+entry+"&"+api_key+"&file_type=json"
    req = requests.get(req1)
    print(json.loads(req.text)['seriess'])

def data_series_extraction(id):

    req1 = "https://api.stlouisfed.org/fred/series/observations?series_id="+id+"&"+api_key+"&file_type=json"

    print(req1+"\n")
    req = requests.get(req1)
    observations =json.loads(req.text)['observations']
    date_s = list()
    value_s = list()

    for i in observations:

        month = "-04-"
        if month in i['date']:
            date_s.append(i['date'])
            value_s.append(float(i['value']))

    date_s_s = [*range(0,len(date_s))]

    return date_s_s,value_s



def plot_single(date_s,value_s,x_label,y_label,title_s):


     plt.plot(date_s, value_s)
     plt.ylabel(y_label)
     plt.xlabel(x_label)
     plt.title(title_s)
     plt.show()

def plot_multiple(d1,v1,d2,v2):

    plt.plot(d1, v1)
    plt.plot(d2, v2)
    plt.show()

def main():

    #data_series_extraction("WM2NS","From 1980 t0 2021 (May)","Billions of Dollars","M2 United States (Money Stock)")

    dm2,vm2 = data_series_extraction("M2SL")
    dm1,vm1 = data_series_extraction("M1SL")
    plot_multiple(dm1, vm1, dm2, vm2)

    #plot_single(dm2,vm2,"From 1959 t0 2021 (May)", "Billions of Dollars", "M2 United States (Money Stock)")
    #data_series_extraction("M1SL", "From 1959 t0 2021 (May)", "Billions of Dollars", "M1 United States (Money Stock)")

main()
