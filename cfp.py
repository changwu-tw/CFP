#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import tablib

from bs4 import BeautifulSoup


id_list = [ 2660, 2099, 6046, 2103, 2114, 2670, 399, 1430, 3090, 1330,
            2609, 1947, 2186, 2152, 1294, 1138, 3023, 2339, 2980 ]

URL_PATTERN = 'http://www.wikicfp.com/cfp/program?id={}'

headers = ('Conference', 'Date', 'Location', 'Deadline')


def parsePage(id):
    r = requests.get(URL_PATTERN.format(id))
    bs = BeautifulSoup(r.text.encode('utf-8')).findAll('table')[5]
    tr_doms = bs.findAll('tr')[1:3]

    conf_name = tr_doms[0].findAll('td')[0].text

    td_doms = tr_doms[1].findAll('td')
    conf_date = td_doms[0].text
    conf_locaton = td_doms[1].text
    paper_date = td_doms[2].text

    return (conf_name, conf_date, conf_locaton, paper_date)


def main():
    conf_info = []
    for id in id_list:
        conf_info.append(parsePage(id))

    data = tablib.Dataset(*conf_info, headers=headers)
    with open('cfp.xlsx', 'wb') as f:
        f.write(data.xlsx)


if __name__ == '__main__':
    main()
