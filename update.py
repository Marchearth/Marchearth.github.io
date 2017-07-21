# Update atom feed, md docs in index
import urllib2
import requests

def download_md(url):
    html = urllib2.urlopen(url).read
    html = requests.get(url)
    slice_start = html.url.find("Marchearth")
    namelist = html.url.split("/")
    print namelist
    print len(namelist)

    if namelist[2] == "raw.githubusercontent.com":
        for i in range(0,len(namelist)):
            if namelist[i] == "Marchearth":
                i += 1
                filename = namelist[i]
        filename += ".html"
    else:
        filename = "feed.xml"

    write_file = open(filename, "w")
    write_file.truncate()
    write_file.write(html.text)
    print write_file
    print html.text

download_md("https://raw.githubusercontent.com/Marchearth/BotterLord/master/README.md")
download_md("https://raw.githubusercontent.com/Marchearth/marchearth.github.io/master/README.md")
download_md("github.com/marchearth.atom")
