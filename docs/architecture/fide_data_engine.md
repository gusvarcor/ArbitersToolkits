# FIDE Data Engine (FDE)

**Versión:** 1.0  
**Estado:** Diseño  
**Proyecto:** ArbitersToolkits

---

# 1. Propósito

El **FIDE Data Engine (FDE)** es el subsistema responsable de obtener, validar, almacenar y mantener actualizada toda la información oficial publicada por la Federación Internacional de Ajedrez (FIDE).

El FDE constituye la única fuente oficial de datos dentro de ArbitersToolkits. Ningún otro módulo descargará información directamente desde FIDE ni manipulará archivos XML oficiales.

Su misión es transformar los datos oficiales en información estructurada, optimizada y preparada para ser utilizada por el resto del sistema.

---

# 2. Objetivos

El FDE tiene los siguientes objetivos principales:

- Descargar automáticamente las listas oficiales de FIDE.
- Validar la integridad de los archivos descargados.
- Importar la información a SQLite.
- Mantener un historial de versiones mensuales.
- Generar diccionarios auxiliares.
- Generar estadísticas utilizadas por otros motores.
- Servir como fuente única de datos para todo ArbitersToolkits.

---

# 3. Principios de diseño

El FDE se basa en los siguientes principios:

## Fuente única de verdad

El archivo XML oficial de FIDE es la única fuente de información.

Todo lo demás se genera automáticamente.

```
XML Oficial
      │
      ▼
SQLite
      │
      ▼
Diccionarios
      │
      ▼
Estadísticas
      │
      ▼
Motores del sistema
```

---

## Automatización

Todo el proceso debe ejecutarse automáticamente.

No deberá existir intervención manual para:

- importar
- reconstruir índices
- reconstruir diccionarios
- reconstruir estadísticas

---

## Independencia

El FDE no conocerá nada acerca de:

- Smart Name Intelligence
- Buscador Masivo
- Normas FIDE
- Herramientas Arbitrales

Su única responsabilidad será administrar datos.

---

# 4. Fuente oficial de datos

El FDE utilizará exclusivamente el archivo:

**Combined XML**

publicado mensualmente por FIDE.

Este archivo contiene:

- Rating Standard
- Rating Rapid
- Rating Blitz

por lo que no será necesario descargar tres archivos independientes.

---

# 5. Flujo general

```
Nueva Lista FIDE

        │

        ▼

Descarga

        │

        ▼

Validación

        │

        ▼

Importación SQLite

        │

        ▼

Reconstrucción de índices

        │

        ▼

Generación de diccionarios

        │

        ▼

Generación de estadísticas

        │

        ▼

Validación final

        │

        ▼

Datos disponibles
```

---

# 6. Componentes

El FDE estará compuesto por los siguientes módulos.

## Downloader

Responsable de localizar y descargar el XML oficial.

---

## Validator

Valida:

- XML correcto
- tamaño
- fecha
- integridad

---

## Importer

Convierte el XML en registros SQLite.

---

## Updater

Actualiza la base existente.

Determina:

- jugadores nuevos
- modificaciones
- bajas

---

## Dictionary Builder

Genera automáticamente:

- nombres.json
- apellidos.json
- estadísticas de nombres
- estadísticas de apellidos

---

## Statistics Builder

Genera estadísticas utilizadas por otros motores.

Ejemplos:

- frecuencia de nombres
- frecuencia de apellidos
- federaciones
- títulos
- sexo
- países

---

## Integrity Checker

Comprueba consistencia de la base.

Ejemplos:

- IDs repetidos
- nombres vacíos
- ratings inválidos

---

## Version Manager

Mantiene un historial completo de las versiones mensuales.

---

# 7. Estructura de directorios

```
data/

    downloads/

        2026-08/

            combined.xml

        2026-09/

            combined.xml

    sqlite/

        current.db

        archive/

            players_2026_08.db

            players_2026_09.db

    dictionaries/

        nombres.json

        apellidos.json

        estadisticas_nombres.json

        estadisticas_apellidos.json
```

---

# 8. Relación con otros subsistemas

```
                   FIDE

                     │

                     ▼

          FIDE DATA ENGINE

                     │

      ┌──────────────┼──────────────┐

      ▼              ▼              ▼

 SQLite        Diccionarios    Estadísticas

      │              │              │

      └──────────────┼──────────────┘

                     ▼

          Smart Name Intelligence

                     │

                     ▼

           Buscador Masivo

                     │

                     ▼

      Herramientas Arbitrales
```

---

# 9. Responsabilidades

El FDE **sí debe**:

- descargar
- validar
- importar
- actualizar
- generar diccionarios
- generar estadísticas
- versionar datos

---

El FDE **nunca debe**:

- interpretar nombres
- calcular normas
- realizar búsquedas inteligentes
- generar emparejamientos
- mostrar interfaces gráficas

---

# 10. Filosofía

Todos los módulos del proyecto deberán depender del FIDE Data Engine.

Nunca deberán depender directamente de archivos XML ni de recursos externos.

Esto garantiza una arquitectura desacoplada, mantenible y preparada para crecer durante muchos años.
