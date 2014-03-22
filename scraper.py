import sys, re
from pprint import pprint
from datetime import datetime

from bs4 import BeautifulSoup

TRAMITE_RE = re.compile('background-color:#(E6F1FF|EFEFEF)')
LINK_RE = re.compile("javascript:OpenWindow\('([^']+)',700,400\)")
TIPO_RE = re.compile("\d+ - ([^:]+)")

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
                tramite_tipo = re.search(TIPO_RE, tag.string).group(1)
            elif 'style' in tag.attrs and re.search(TRAMITE_RE, tag['style']):
                desc = tag.find('div')

                if desc is None and tramite_tipo != 'VARIOS':
                    tag = tag.next_sibling
                    continue
                else:
                    desc = tag

                reunion['tramites'].append({
                    'tipo': tramite_tipo,
                    'descripcion': ''.join(desc.strings),
                    'expediente': desc.find('a').string if desc.find('a') else None,
                    '_color': re.search(TRAMITE_RE, tag['style']).group(1)
                })
            elif 'style' in tag.attrs and tag['style'] == 'text-align:center;font-weight:bold':
                if len(reunion['tramites']) > 0:
                    # esto es porque un 'resultado de votacion' a veces se aplica
                    # a un conjunto de dictamenes
                    # (aparecen con el mismo color)
                    k = None
                    for t in reversed(reunion['tramites']):
                        if k is None or k == t['_color'] + t['tipo']:
                            t['votacion'] = tag.string
                            k = t['_color'] + t['tipo']
                        else:
                            break

            tag = tag.next_sibling

        for t in reunion['tramites']: del t['_color']
        reuniones.append(reunion)

    return reuniones

if __name__ == '__main__':
    pprint(scrape(sys.argv[1]))
    #scrape(sys.argv[1])
