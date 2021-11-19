#!/usr/bin/python

import argparse
import json
import lxml.etree
from xmljson import yahoo

def xml2json(tree):
    output = []
    for node in tree.iter():
        if node.tag =='ReportHost':
            attr_name = node.xpath('@name')[0]
            attr_ip = node.xpath('//HostProperties/tag[@name="host-ip"]')[0].text
            attr_rdns = node.xpath('//HostProperties/tag[@name="host-rdns"]')[0].text
            for subnode in node.iter():
                if subnode.tag == 'ReportItem':
                    rptitem = yahoo.data(subnode)
                    rptitem['host_name'] = attr_name
                    rptitem['host_ip'] = attr_ip
                    rptitem['host_rdns'] = attr_rdns
                    output.append(rptitem)
    return(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='Filename of Nessus XML export')
    args = parser.parse_args()
    filename = args.filename
    tree = lxml.etree.parse(filename)
    output = xml2json(tree)
    print("{}".format(json.dumps(output, indent=2)))

