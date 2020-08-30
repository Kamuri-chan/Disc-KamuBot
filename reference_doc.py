def read_doc(arg):
    from bs4 import BeautifulSoup
    import requests

    def extract_str(string, unwanted_char=[]):
        chars = []
        for char in range(0, len(string)):
            try:
                number = int(string[char])
            except Exception:
                if (string[char] not in unwanted_char):
                    chars.append(string[char])
        if len(chars) > 0:
            value = (''.join(chars)).lower()
            return value
        else:
            return None

    fix_url = "https://docs.python.org/3/reference"
    index = "/index.html"
    url = fix_url + index

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # q = input("O que você quer procurar?? ").strip()
    q = arg

    results = soup.findAll('li', class_="toctree-l1")

    for result in results:
        other_res = result.findAll('li', class_="toctree-l2")
        for element in other_res:
            if q in element.text:
                # print(element.text)
                name = extract_str(element.text, [' ', '.'])
                url_find = element.find('a', href=True)
                url_find = url_find['href']

    new_url = fix_url + "/" + url_find
    page = requests.get(new_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.findAll('div', id=True)

    findit = ""

    for i in results:
        a = extract_str(i['id'], [' ', '-', '.'])
        if a == name:
            findit = i

    if (len(findit.text) > 1999):
        k = []
        j = []
        for i in range(len(findit.text)):
            if i < 1000:
                k.append(findit.text[i])
            else:
                j.append(findit.text[i])

        b = (''.join(k))
        c = (''.join(j))

        return (b, c)
    else:
        return (findit.text)
