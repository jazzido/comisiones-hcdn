comisiones-hcdn
===============

Scraper para los [datos de Labor de Comisiones](http://www1.hcdn.gov.ar/labordecomision/qryfrmlc.asp) publicados por la [Honorable Cámara de Diputados de la Nación Argentina](http://www1.hcdn.gov.ar/)

## Uso

  - `wget "http://www1.hcdn.gov.ar/labordecomision/search_result.asp?giro_giradoA=&odanno=&pageorig=1&condictytram=false&whichpage=1" -O labor.html`
  - `python scraper.py labor.html > labor.json`

## Salida

```json
[{

    "fecha": "2013-11-19T00:00:00",
    "tramites": [
        {
            "descripcion": "RESOLUCION (6785-D-2013)\n DESIGNAR CON EL NOMBRE DE \"MAESTRO ALFREDO BRAVO\" A LA SALA DE \nREUNIONES DEL EDIFICIO ANEXO \"C\", SEGUNDO PISO, DE LA CALLE BARTOLOME \nMITRE 1848.",
            "votacion": "Aprobado por unanimidad sin modificaciones",
            "expediente": "6785-D-2013",
            "tipo": "DICTAMEN"
        },
        {
            "descripcion": "RESOLUCION (7239-D-2013)\n EXPRESAR RECONOCIMIENTO A LOS DIPUTADOS NACIONALES QUE ASUMIERON SU \nMANDATO EL DIA 10 DE DICIEMBRE DE 1983, Y HACER ENTREGA DE UN DIPLOMA DE\n HONOR Y UNA MEDALLA CONMEMORATIVA, CON LA INSCRIPCION \"1983 - 2013 30 \nAÑOS DE DEMOCRACIA\".",
            "votacion": "Aprobado por unanimidad sin modificaciones",
            "expediente": "7239-D-2013",
            "tipo": "DICTAMEN"
        }
    ],
    "comision": "PETICIONES, PODERES Y REGLAMENTO"

},
{

    "fecha": "2013-11-20T00:00:00",
    "tramites": [
        {
            "descripcion": "DECLARACION (6307-D-2013)\n EXPRESAR BENEPLACITO POR LA PARTICIPACION DE LA PROVINCIA DEL CHUBUT EN\n LA \"FERIA DE TURISMO DE LAS AMERICAS (ABAV)\", QUE SE REALIZA DEL 4 AL 8\n DE SEPTIEMBRE DE 2013 EN SAN PABLO, BRASIL.",
            "votacion": "Aprobado\n por unanimidad con modificaciones en los términos del articulo 114 del \nreglamento de la H. Cámara como Proyecto de Resolución",
            "expediente": "6307-D-2013",
            "tipo": "DICTAMEN"
        },
        {
            "descripcion": "RESOLUCION (6326-D-2013)\n DECLARAR DE INTERES DE LA H. CAMARA LA PARTICIPACION DE LA PROVINCIA \nDEL CHUBUT EN LA \"FERIA INTERNACIONAL DE TURISMO (FIT)\", A REALIZARSE \nDEL 14 AL 17 DE SETIEMBRE DE 2013 EN LA CIUDAD AUTONOMA DE BUENOS AIRES.",
            "votacion": "Aprobado por unanimidad con modificaciones en los términos del articulo 114 del reglamento de la H. Cámara",
            "expediente": "6326-D-2013",
            "tipo": "DICTAMEN"
        },
        {
            "descripcion": "RESOLUCION (6471-D-2013)\n EXPRESAR BENEPLACITO POR LA FIRMA DEL CONVENIO DE OBRAS ENTRE EL \nGOBIERNO DE LA PROVINCIA DE MISIONES, EL MINISTERIO DE TURISMO DE LA \nNACION Y EL BANCO INTERAMERICANO DE DESARROLLO -BID- EN LAS MISIONES \nJESUITICAS DE SAN IGNACIO, PROVINCIA DE MISIONES, REALIZADO EL DIA 9 DE \nSEPTIEMBRE DE 2013.",
            "votacion": "Aprobado por unanimidad sin modificaciones en los términos del articulo 114 del reglamento de la H. Cámara",
            "expediente": "6471-D-2013",
            "tipo": "DICTAMEN"
        },
        {
            "descripcion": "RESOLUCION (6570-D-2013) EXPRESAR BENEPLACITO POR LA PARTICIPACION DE LA PROVINCIA DEL CHUBUT EN LA \"RED INCUBAR TURISMO\". ",
            "votacion": "Aprobado por unanimidad con modificaciones en los términos del articulo 114 del reglamento de la H. Cámara",
            "expediente": "6570-D-2013",
            "tipo": "DICTAMEN"
        },
    ],
    "comision": "TURISMO"
}]

```

## Licencia

MIT

Copyright © 2014 — Manuel Aristarán
