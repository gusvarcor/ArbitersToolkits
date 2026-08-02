# Esquema XML de la FIDE

## Objetivo

Documentar completamente la estructura del archivo XML oficial distribuido por la FIDE.

Este documento servirá como referencia para:

- Importador SQLite
- Validación
- Estadísticas
- Smart Name Intelligence
- Consultas futuras

---

## Archivo oficial

URL

https://ratings.fide.com/download/players_list_xml.zip

Archivo XML

players_list_xml_foa.xml

---

## Política de ArbitersToolkits

ArbitersToolkits NO importará únicamente los campos utilizados por la interfaz.

Se importarán TODOS los campos presentes en el XML oficial.

Los campos que actualmente no sean utilizados permanecerán almacenados para futuras funcionalidades.

Nunca se descartará información oficial publicada por la FIDE.

---

## Campos

| XML | SQLite | Tipo | Descripción | Importar |
|------|--------|------|-------------|-----------|
| | | | | |

---

## Observaciones

Pendiente de analizar completamente el XML.