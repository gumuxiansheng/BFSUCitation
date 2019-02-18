# coding:utf-8

import requests


def grab_from_url(url, cookie_initial):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'Cookie': cookie_initial,
        'Cache-Control': 'max-age=0',
        'Host': 'apps.webofknowledge.com',
        'Proxy-Connection': 'keep-alive',
        'Connection': 'keep-alive',
        'Referer': 'http://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?product=WOS&search_mode=AdvancedSearch&replaceSetId=&goToPageLoc=SearchHistoryTableBanner&SID=7AxcRcd9UhxH81u1Orl&errorQid=1185',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
    }
    data = {'product': 'WOS',
             'search_mode': 'AdvancedSearch',
             'SID': '7AxcRcd9UhxH81u1Orl',
             'input_invalid_notice': '檢索錯誤: 請輸入檢索字詞。',
             'input_invalid_notice_limits': ' <br/>備註: 在捲動方塊中顯示的欄位至少必須與一個其他檢索欄位組合。',
             'action': 'search',
             'replaceSetId': '',
             'goToPageLoc': 'SearchHistoryTableBanner',
             'value(input1)': 'TI=(Social robots for education: A review)',
             'value(searchOp)': 'search',
             'value(select2)': 'LA',
             'value(input2)': '',
             'value(select3)': 'DT',
             'value(input3)': '',
             'value(limitCount)': '14',
             'limitStatus': 'collapsed',
             'ss_lemmatization': 'On',
             'ss_spellchecking': 'Suggest',
             'SinceLastVisit_UTC': '',
             'SinceLastVisit_DATE': '',
             'period': 'Range Selection',
             'range': 'ALL',
             'startYear': '1986',
             'endYear': '2019',
             'editions': 'SSCI',
             'editions': 'AHCI',
             'editions': 'CCR',
             'editions': 'IC',
             'update_back2search_link_param': 'yes',
             'ss_query_language': '',
             'rs_sort_by': 'LC.D;PY.D;AU.A.en;SO.A.en;VL.D;PG.A'}
    res = requests.post(url, headers=headers, data=data)
    res.content
    print res

    return True


def grab_main():
    cookie_initial = 'dotmatics.elementalKey=SLsLWlMhrHnTjDerSrlG; _sp_id.0210=bd0fa84ca40ddf43.1539840966.2.1539849221.1539842259.0f045b20-b147-4f3a-b49c-a2600decda5c; CUSTOMER="Beijing Foreign Studies University"; E_GROUP_NAME="Beijing Foreign Studies University"; SID="7AxcRcd9UhxH81u1Orl"; bm_sz=419AF5F017054BF06B85824FF0FF085F~YAAQNwEPF6hSYuloAQAAQ7fy/gKtNKJ8LiTXSiMD1j3vkYXTprEsSSp+Rz8pjuJOXviq1/IqZe5W6dp5hAys4/jiOnt3+IkEwkF8uUR2Fn+cpxHprBU6faEBReYCaoY2N9V3F5SKOsqImMtKFj+JU1qHxjkLVVVD+0Hq31RdIe/1+yf9cETXWe87OLLyCXfPPsMGFNi/QHM=; _sp_ses.630e=*; ak_bmsc=CAD019DEB604CBDF6B99B42BCE532049170F011D6F5D00003D566A5C3A6FB242~plYNvXLPl7P6dZj9Da8dp7RBQzH0W4RKgpiyU56PXvAUvcTCD+hO5ddngXvPEPWDgz40NWNeOpYKSahqixuR/V7Fia6hwbm+GCdpNExrTTZf8KKT267vnKGqfcsdDAsBUu6XD88sA9pWes8pQWb6vK/1EiyZUdks3dkzb0v0mKzPSWUGyWyRkJGC8vRpkuhNFgajZmWyioNM6gBhdUglfNsjxmFWTL/kLXIigdTNUJlgBfzDKyvxPTw8FDacMtwtZq; _abck=35A0F40E8E262122115979ED180047CC7D38DA35C37200007C1BC85BB6CC6E36~0~+JWXYjWOU8HEZYlr7jISxMhrqizaJVJJZKK/uOCiBTk=~-1~-1; JSESSIONID=F27F68F575552A421866809891B258F7; bm_sv=A7BDF28BE4DE970D93FA764D18A14FFC~WcObxOOE4vt6CUeegojjiHTs9f4a14ERkDt9FD51HILouSAESJDWrSiJySOH6Isdxqkfpjdgg7VaBMveYcr9shp0Dn1IIMR9x2iYbdtI1rhlSL4v/M2N5+We/DUPc6ZdgHgoSy4xvHQ8asM2lFb6SccMYMaGwxcqhyyIMetBb+g=; _sp_id.630e=ba61a8b6-be03-4f11-abb0-52b262626c92.1539934508.23.1550475371.1547368714.d5baa586-75b0-40ec-8023-50aa4f344561'
    grab_from_url('http://apps.webofknowledge.com/WOS_AdvancedSearch.do', cookie_initial)
    return
