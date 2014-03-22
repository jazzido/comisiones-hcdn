comisiones-hcdn
===============

Scraper para los [datos de Labor de Comisiones](http://www1.hcdn.gov.ar/labordecomision/qryfrmlc.asp) publicados por la [Honorable Cámara de Diputados de la Nación Argentina](http://www1.hcdn.gov.ar/)

## Uso

  - `wget "http://www1.hcdn.gov.ar/labordecomision/search_result.asp?giro_giradoA=&odanno=&pageorig=1&condictytram=false&whichpage=1" -O labor.html`
  - `python scraper.py labor.html > labor.json`

## Licencia

MIT

Copyright © 2014 — Manuel Aristarán
