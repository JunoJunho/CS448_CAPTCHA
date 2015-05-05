# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2 as ul
# import pdb
def strip_tags(strings):
    string = ''
    for tmp in strings:
        string = string + tmp
    return string


def CAFESEARCHER(searchKey):
    searchKeyword = ul.quote(searchKey)
    cafeList = []
    for i in range(3):
        f = ul.Request(
            "http://search.daum.net/search?w=cafe&m=name&q=" + searchKeyword + "&SortType=4&StoreCafe=&lpp=10&SearchType=tag&ResultType=tab&f=section&page=" + str(
                i))
        f.add_header("Accept-Charset", "windows-949,utf-8;q=0.7,*;q=0.3")
        f.add_header("User-Agent",
                     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.95 ")
        result = ul.urlopen(f).read().decode("utf8")

        soup = BeautifulSoup(result)
        cafes = soup.find('ul', attrs={'id': 'cafeNameResultUL'})
        cafes = cafes.find_all("li")
        for cafe in cafes:
            print cafe
            url = cafe.find('a', attrs={'class': 'f_link_bu f_l'})['href']
            name = cafe.find('a', attrs={'class': 'f_link_bu f_l'}).strings
            name = strip_tags(name)
            desc = cafe.find('p', attrs={'class': 'f_eb desc'}).string
            desc2 = cafe.find('span', attrs={'class': 'f_l'}).stripped_strings
            desc2 = strip_tags(desc2)
            desc2 = desc2[desc2.find(":") - 2:]
            desc2 = desc2.split("|")
            rank = desc2[0]
            members = desc2[1]
            cafeList.append((url, name, desc, rank, members))
    return cafeList


if __name__ == '__main__':
    cafeList = CAFESEARCHER("유학")
    for cafe in cafeList:
        print "##### LIST START #######"
        print cafe[0], cafe[1], cafe[2], cafe[3], cafe[4]
        print "##### LIST END #######'"
