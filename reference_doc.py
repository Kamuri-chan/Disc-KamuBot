def print_multiple_str(lista):
    lista1 = []
    resto = []
    i = 0
    for q in lista:
        i += 1
        if i < 2001:
            lista1.append(q)
        elif i > 2001:
            resto.append(q)

    if len(lista) > 0:
        has_char = True
    else:
        has_char = False
    return lista1, resto, has_char


def read_doc(arg):
    from bs4 import BeautifulSoup
    import requests

    def extract_str(string, unwanted_char=[]):
        chars = []
        for char in range(0, len(string)):
            try:
                int(string[char])
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

    to_find = extract_str(arg, [".", '-'])

    results = soup.findAll('li', class_="toctree-l1")
    try:
        for result in results:
            other_res = result.findAll('li', class_="toctree-l2")
            for element in other_res:
                f = extract_str(element.text, [' ', '.', '-'])
                if to_find in f:
                    name = extract_str(element.text, [' ', '.', ','])
                    url_find = element.find('a', href=True)
                    url_find = url_find['href']

        new_url = fix_url + "/" + url_find
        page = requests.get(new_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.findAll('div', id=True)

        contents = []
        n_encontrado = True
        for result in results:
            formatted_str = extract_str(result['id'], [' ', '-', '.', ','])
            if formatted_str == name:
                n_encontrado = False
                sections = result.findAll('div', class_="section")
                for section in sections:
                    contents.append(section.text)
                findit = result.text
            elif n_encontrado:
                if formatted_str == "identifiers":
                    sections = result.findAll('div', class_="section")
                    for section in sections:
                        contents.append(section.text)
                    findit = result.text

        to_return = []
        if contents:
            for content in contents:
                if (len(content) > 2000):
                    has_char = True
                    while has_char:
                        chars, content, has_char = print_multiple_str(content)
                        to_return.append(chars)
                    return to_return
                else:
                    return contents
        else:
            if len(findit) > 2000:
                has_char = True
                while has_char:
                    chars, findit, has_char = print_multiple_str(findit)
                    to_return.append(chars)
                return to_return
            else:
                return findit
    except NameError:
        return "Error! Não consegui encontrar nada!"
