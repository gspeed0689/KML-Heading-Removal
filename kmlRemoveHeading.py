#KML Remove Heading Value Script ver 0.0.1
#This script will replace all the <heading> node
#values with 0
from xml.dom import minidom as xdmd
import argparse, sys

def main(fname):
    print("opening %s" % fname)
    kmlFile = open(fname, "r")
    print("parsing xml document")
    kmlDocObj = xdmd.parse(kmlFile)
    headingElem = kmlDocObj.getElementsByTagName("heading")
    print("found %s heading tags" % len(headingElem))
    c = 0
    for i in headingElem:
        i.firstChild.nodeValue = '0'
        c += 1
        sys.stdout.write("\rupdated %s instances" % c)
        sys.stdout.flush()
    print("\nfinished updating headings\nnow writing xml back to file")
    kmlUFile = open(fname + "hr", "w")
    kmlUFile.write(kmlDocObj.toxml(encoding="utf-8"))
    kmlUFile.close()
    kmlFile.close()

def cmdLine():
    parser = argparse.ArgumentParser(description='Remove heading values in a kml file')
    parser.add_argument('-f', '--filename', help="file name")
    args = parser.parse_args()
    fname = args.filename
    main(fname)

cmdLine()
