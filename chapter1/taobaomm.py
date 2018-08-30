import urllib
import urllib2
import re
import tool
import os

class Spider:

    def __init__(self):
        self.siteURL = "http：//mm.taobao.com/json.request.top_list.htm"
        self.tool = tool.Tool()

    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile();
        items = re.findall(pattern.page)