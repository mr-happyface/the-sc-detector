#!/usr/bin/env/ Python3.8
import tkinter as tk
import urllib.request

def the_command():
    site = site_url.get()
    print("scanning website, please wait...")
    fp = urllib.request.urlopen(site)
    mybytes = fp.read()


  
    mystr = mybytes.decode("utf8")
    fp.close()
    a = mystr.count("advertorial")
    b = mystr.count("paid post")
    c = mystr.count("presented by")
    d = mystr.count("sponsored by")
    e = mystr.count("partnered with")
    f = mystr.count("promoted")
    g = mystr.count("affiliated with")
    h = mystr.count("powered by")
    i = mystr.count("We earn a commission for products purchased through some links in this article")
    j = mystr.count("sponsored content",)
    k = mystr.count("sponsored")
    l = mystr.count("advertorial")
    m = mystr.count("paid announcement")
    n = mystr.count("branded content")
    o = mystr.count("promoted post")

    dr1 = mystr.count(">advertorial<")
    dr2 = mystr.count(">sponsored content<")
    dr3 = mystr.count(">paid post<")
    dr4 = mystr.count(">paid article<")
    dr5 = mystr.count(">promoted content<")
    dr6 = mystr.count(">branded content<")
  
    if l == 1:
        bonus_points = 1000
    if 1 < l:
        bonus_points = 1000 * l
  
  #points system
    a_pt = a * 100
    b_pt = b * 50
    c_pt = c * 25
    d_pt = d * 35
    e_pt = e * 20
    f_pt = f * 10
    g_pt = g * 5
    h_pt = h * 30
    i_pt = i * 55
    j_pt = j * 45
    k_pt = k * 10
    m_pt = m * 10
    n_pt = n * 60
    o_pt = o * 75
    print("advertorial: ", a)
    print("paid post: ", b)
    print("presented by: ", c)
    print("sponsored by: ", d)
    print("partnered with: ", e)
    print("promoted: ", f)
    print("affiliated with: ", g)
    print("powered by: ", h)
    print("commisions they earned: ", i)
    print("sponsored content: ", j)
    print("sponsored: ", k)
    print("paid annoucement: ", m)
      
  #total points equation
    total_score = a_pt + b_pt + c_pt + d_pt + e_pt + f_pt + h_pt + i_pt + j_pt + k_pt + m_pt + n_pt + o_pt + bonus_points
  
    dead_ringers = dr1 + dr2 + dr3 + dr4 + dr5 + dr6

    print("total score: ", total_score)
    if 0 < dead_ringers:
        print("definetly sponsered content")
    if dead_ringers == 0:
        if 2000 < total_score:
            print("extremely likley sponsered content")
        if 50 < total_score < 100:
            print("might be sponsered content")
        if 100 < total_score < 2000:
            print("most likely sponsered content")
        if 0 < total_score < 50:
            print("unlilkley it's sponsered content")
        if total_score == 0:
            print("probably not sponsered content")

root = tk.Tk()


tk.Label(root, text="Input thing:").grid(row=0)
site_url = tk.Entry(root)
site_url.grid(row=0, column=1)

tk.Button(root, text="QUIT", fg="red", command=quit).grid(row=2, column=0, sticky=tk.W, pady=4)

tk.Button(root, text='show', command=the_command).grid(row=2, column=1, sticky=tk.W, pady=4)


root.mainloop()
