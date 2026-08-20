# -*- coding: utf-8 -*-
import yaml
import requests
from bs4 import BeautifulSoup

# emoji.demojize

allEmojiUrl = "https://www.emojiall.com/zh-hans/all-emojis"

req = requests.get(allEmojiUrl)

print(req.status_code)

html = BeautifulSoup(req.text)

# groups =  html.find_all('//div[@class=""]')
groups = html.find_all('div',class_='emoji_card_list')
# //div[@class='emoji_card_list'][1]/h2/a
h1dict = []
h2dict = []
h3dict = []
for group in groups:
    h2s = group.find_all('h2')
    for h2 in h2s:
        # print(h2)
        if h2:
            a = h2.find('a')
            sup = a.find('sup')
            a = a.text
            sup = sup.text
            a = a.replace(sup,'')
            # h3s = group.find_all('h3')
            # for h3 in h3s:
            divs = group.find_all('div', class_='list_table')
            # print(divs)
            tmpH2 = []
            for div in divs:
                cols = div.find_all('div', class_='emoji_card')
                for col in cols:
                    emoji = col.find('a',class_='emoji_font').string
                    # print({'emoji':emoji.encode('unicode-escape').decode(), "title":col.find('a',class_='emoji_name').string})
                    tmpH2.append({'emoji':emoji.encode('unicode-escape').decode(), "title":col.find('a',class_='emoji_name').string})
                #print(tmpH2)
            h1dict.append({'group':a.encode('unicode-escape').decode(),'data':tmpH2})

        #print(h1dict)

# print(a)

# with open('./emoji.yaml','w',encoding='utf8') as f:
#     msg = ""
#     for (key,value) in h1dict.items():
#         msg += i['emoji'].encode().decode('unicode-escape')
#         msg += i['title']
#         msg += '\n'
#     f.write(msg)

with open('./emoji.json','w',encoding='utf8') as f:
    groups = '{'
    for j in range(len(h1dict)):
        tmpH1 = h1dict[j]
        tmpH2 = tmpH1['data']
        dataStart = '['
        for t in tmpH2:
            dataEmoji = t['emoji'].encode().decode('unicode-escape')
            # print(dataEmoji)
            dataTitle = t['title']
            tmp = '"emoji":"{emoji}","title":"{title}"'.format(emoji=dataEmoji,title=dataTitle)
            tmp = '{' + tmp + '},'
            dataStart += tmp
        if dataStart[-1] == ',':dataStart=dataStart[:-1]
        data = dataStart + ']'
        groupName = tmpH1['group'].encode().decode('unicode-escape')
        # print(groupName)
        group = '"{name}":{data},'.format(name=groupName,data=data)
        groups += group
        if len(h1dict) == (j + 1):groups=groups[:-1]
    groups += '}'
    f.write(groups)