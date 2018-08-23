def getMonthFoodMaterialList(request):
    from bs4 import BeautifulSoup
    import json
    import urllib.request
    import urllib.parse
    request_json = request.get_json()
    mon = '01'
    if request.args and 'mon' in request.args:
        mon = request.args.get('mon')
    web_url = "http://koreanfood.rda.go.kr/kfi/foodMonth/list?menuId=PS03599&mon"+mon
    with urllib.request.urlopen(web_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        all_divs = soup.find_all("div",{'class':'foodlist'})
        for i in range(3):
            if i == 0:
                children = all_divs[0].findChildren("dd" , recursive=True)
                resText = ""
                for child in children:
                    resText = resText + child.contents[0] + " "
    return resText
    
