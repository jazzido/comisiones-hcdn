import sys, re
from pprint import pprint
from datetime import datetime

from bs4 import BeautifulSoup

TRAMITE_RE = re.compile('background-color:#(E6F1FF|EFEFEF)')
LINK_RE = re.compile("javascript:OpenWindow\('([^']+)',700,400\)")

def scrape(fname):
    with open(fname) as f:
        html = BeautifulSoup(f.read())

    reuniones = []
    for hr in html.find_all('hr'):
        reunion = {
            'fecha': datetime.strptime(hr.find_next_sibling(class_='fecha').string,
                                       '%d/%m/%Y'),
            'comision': hr.find_next_sibling(class_='comisiones').string,
            'tramites': []
        }

        tag = hr.next_sibling
        tramite_tipo = tramite = None

        while tag is not None \
          and tag.name != 'hr':

            if 'class' in tag.attrs and 'tituloItem' in tag['class']:
                tramite_tipo = tag.string
            elif 'style' in tag.attrs and re.search(TRAMITE_RE, tag['style']):
                desc = tag.find('div')
                if desc is None:
                    tag = tag.next_sibling
                    continue

                expedientes = [
                    {
                        'expediente': a.string,
                        'link': re.search(LINK_RE, a['href']).group(1)
                    } for a in desc.find_all('a')
                ]

                reunion['tramites'].append({
                    'tipo': tramite_tipo,
                    'descripcion': ' '.join(desc.stripped_strings),
                    'expedientes': expedientes
                })
            elif 'style' in tag.attrs and tag['style'] == 'text-align:center;font-weight:bold':
                if len(reunion['tramites']) > 0:
                    reunion['tramites'][-1]['resultado'] = tag.string

            tag = tag.next_sibling

        reuniones.append(reunion)

    return reuniones

if __name__ == '__main__':
    pprint(scrape(sys.argv[1]))
    #scrape(sys.argv[1])
