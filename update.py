# -*- coding: utf-8 -*-
# Update atom feed, md docs in index
import requests, os, subprocess
from xml.etree import ElementTree as ET

def download_md(url):
    html = requests.get(url)
    slice_start = html.url.find("Marchearth")
    namelist = html.url.split("/")

    if namelist[2] == "raw.githubusercontent.com":
        for i in range(0,len(namelist)):
            if namelist[i] == "Marchearth":
                i += 1
                filename = namelist[i]

        filename += ".html"
        write_file = open(filename, "w")
        write_file.truncate()
        write_file.write(html.text.encode('utf-8'))

    else:
        filename = "feed.xml"
        write_file = open(filename, "w")
        write_file.write(html.content)


download_md("https://raw.githubusercontent.com/Marchearth/BotterLord/master/README.md")
download_md("https://raw.githubusercontent.com/Marchearth/marchearth.github.io/master/README.md")
download_md("https://github.com/marchearth.atom")

def git_commit():
    commands = \
    """\
    echo Auto content updater: &\
    git add -A &\
    git commit -a -m "Auto content update. (Srs.Bot-Website/update.py)" --no-edit &\
    git push
    """
    process = subprocess.Popen(commands,stdout=subprocess.PIPE, shell=True, universal_newlines=True)
    print process.stdout.read()

git_commit()
