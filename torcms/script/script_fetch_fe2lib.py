# -*- coding: utf-8 -*-

import os
import sys
import zipfile
import urllib.request


den_dir = './static/f2elib'

if os.path.exists(den_dir):
    pass
else:
    os.mkdir(den_dir)

def fetch_file(url, filename , outdir = False):
    print('fetch ...')
    print(' ' * 4 +  url)

    urllib.request.urlretrieve(url, os.path.join(den_dir, filename))

    if outdir:
        zip_file = os.path.join(den_dir, filename)
        f = zipfile.ZipFile(zip_file, 'r')
        for zfile in f.namelist():
            f.extract(zfile, os.path.join(den_dir, outdir))


def get_jquery():
    # jquery_url = 'https://code.jquery.com/jquery-3.1.1.min.js'
    jquery_url = 'http://cdn.bootcss.com/jquery/3.1.1/jquery.min.js'
    qian, hou = os.path.split(jquery_url)
    fetch_file(jquery_url, hou)

def get_leaflet():
    leaflet_url = 'http://cdn.leafletjs.com/leaflet/v1.0.1/leaflet.zip'


    qian, hou = os.path.split(leaflet_url)
    fetch_file(leaflet_url, hou, outdir = 'leaflet')




def get_ol3():

    # ol3_url = 'https://github.com/openlayers/ol3/releases/download/v3.18.2/v3.18.2-dist.zip'

    # qian, hou = os.path.split(ol3_url)
    # fetch_file(ol3_url, hou, outdir='ol3')

    tdir = os.path.join(den_dir, 'ol3')
    if os.path.exists(tdir):
        pass
    else:
        os.mkdir(tdir)

    ol3_css  = 'http://cdn.bootcss.com/ol3/3.18.2/ol.css'
    fetch_file(ol3_css, 'ol3/ol.css')


    ol3_js = 'http://cdn.bootcss.com/ol3/3.18.2/ol.js'
    fetch_file(ol3_js, 'ol3/ol.js')

def run_fetch_f2elib():
    get_leaflet()
    get_jquery()
    get_ol3()



