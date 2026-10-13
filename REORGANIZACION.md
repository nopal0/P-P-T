# Reorganización por responsabilidades

Se trabajó sobre los archivos existentes, sin restaurar versiones anteriores. El
`git status` inicial estaba limpio. No se encontraron archivos `AGENTS.md`; el
README solo contenía el título. No se hicieron commits ni push.

## Traslados

| Origen | Elemento | Destino |
| --- | --- | --- |
| `persistencia/catalogo_json.py` | `leerDiccJ` | `persistencia/jugadores_json.py` |
| `modelos/jugador.py` | `PC` y `ObtenerCreditos` | `servicios/tienda.py` |
| `modelos/jugador.py` | `ComprarCreditos` | `servicios/tienda.py` |
| `modelos/jugador.py` | `MostrarDatos` | `interfaz/menu_principal.py` |
| `modelos/jugador.py` | `MainCompra` | `interfaz/entradas.py` |
| `modelos/jugador.py` | `LabComprobarPuntosNoSeanNegativosGeneral` | `laboratorio/experimentos_jugador.py` |
| `modelos/jugador.py` | `LabRestarYComprobarPuntos` | `laboratorio/experimentos_jugador.py` |
| `modelos/jugador.py` | `LabSumarYComprobarPuntos` | `laboratorio/experimentos_jugador.py` |
| `modelos/jugador.py` | `LabCreditosComprobarPositivoGeneral` | `laboratorio/experimentos_jugador.py` |
| `modelos/jugador.py` | `LabRestatYComprobarCreditos` | `laboratorio/experimentos_jugador.py` |
| `persistencia/jugadores.json` | Archivo vacío completo | `datos/jugadores_vacio.json` |

El catálogo ya estaba en `config/`, los registros en `datos/` y los scripts
manuales en `laboratorio/`; no necesitaron moverse. Se conservan los tres archivos
JSON byte por byte. El archivo vacío recibió otro nombre para conservarlo sin
sobrescribir el `datos/jugadores.json` que contiene `{}`.

## Estructura de código y datos

```text
main.py
README.md
REORGANIZACION.md
interfaz/
    entradas.py
    menu_principal.py
    menu_compra.py
modelos/
    jugador.py
servicios/
    tienda.py
persistencia/
    catalogo_json.py
    jugadores_json.py
config/
    packs_compras.json
datos/
    jugadores.json
    jugadores_vacio.json
laboratorio/
    mainpruebas.py
    lab.py
    experimentos_jugador.py
```

También permanecen la carpeta vacía `test/` y las cachés `__pycache__/` previas.

## Conexiones y equivalencias

- `MainMenuCompras` llama a `ObtenerCreditos(PuntosAPagar)` del servicio. Sigue
  mostrando paquetes, capturando un precio y mostrando el resultado de la
  consulta. No descuenta puntos ni agrega créditos.
- `PC = leerDicc()` se trasladó con la consulta a la tienda: sigue cargándose una
  vez al importar ese módulo. `MostrarPaquetes` conserva su lectura independiente
  en cada llamada. Importar el modelo por sí solo ya no lee archivos.
- `j.ComprarCreditos(p)` equivale a `ComprarCreditos(j, p)`. La función recibe
  explícitamente el jugador y conserva las dos llamadas existentes, incluido su
  posible error. No se completó la compra.
- `j.MostrarDatos()` equivale a `MostrarDatos(j)`. Se trasladaron las mismas tres
  impresiones al menú principal, sin incorporarlas al flujo actual.
- `j.LabNombre(argumentos)` equivale a `LabNombre(j, argumentos)`. Las referencias
  entre funciones experimentales se actualizaron para pasar el mismo jugador.
  Se conservan sus cálculos, condiciones y retornos.
- `j.MainCompra()` equivale a `MainCompra()`: `self` no se utilizaba. Conserva
  `int(input(""))`, sin devolución del valor ni reintentos.
- `laboratorio/mainpruebas.py` utiliza las nuevas funciones de presentación y
  coordinación. Las restantes operaciones siguen llamándose sobre la instancia.
- Las lecturas usan rutas relativas a la ubicación del módulo mediante
  `Path(__file__)`, hacia `config/packs_compras.json` y `datos/jugadores.json`.
  Antes buscaban ambos nombres en el directorio de trabajo, donde no estaban.
  No se añadieron operaciones de escritura.
- `main.py` conserva la llamada global a `MainMenuCompras()`, incluso al
  importarlo. Se quitó su importación innecesaria del modelo.

El constructor, `CrearId`, `ObtenerPuntos`, `RestarPuntos`, `CambiarPuntos`,
`PerderPuntos`, `ComprobarYRestar`, `ComprobarPuntosCompra` y `SumarCRestarP`
permanecen en `jugador`: dependen de su estado. Se mantienen también las
impresiones mezcladas con las mutaciones; separarlas requeriría dividir métodos,
fuera del traslado completo solicitado. `v()` continúa como función vacía en el
menú de compra porque no tiene una responsabilidad implementada que trasladar.

## Comprobaciones y resultados

- Python 3.14.7: compilación de los 11 archivos `.py` e importación de los 8
  módulos sin flujo interactivo, correctas. Se usaron `compile()` y `-B` para no
  modificar las cachés existentes.
- Se capturaron los archivos de trabajo antes de editar. La comparación ejecutó
  254 casos con el código previo y posterior: ninguna diferencia en tipos y
  valores devueltos, mensajes, entradas solicitadas, excepciones ni estado.
  Incluyó precios 10, 25 y 50, cero, precio inexistente, cinco entradas inválidas,
  ambos menús, conversiones, constructor, operaciones de estado y funciones
  trasladadas, además de los scripts manuales.
- Los nueve métodos conservados en la clase mantienen el mismo árbol sintáctico
  que antes, ignorando espacios y posiciones en el archivo.
- Los tres JSON mantienen exactamente sus bytes. La comprobación comparó el
  archivo vacío anterior con su nueva ubicación `datos/jugadores_vacio.json`.
- Lecturas e importaciones desde un directorio ajeno al proyecto, correctas.
  Ejecución real de `main.py` con precio 10: mostró los paquetes y el valor 25.
- `git diff --check` pasó. No hubo modificaciones en los `.pyc` versionados.

**Límite de la comparación:** ejecutar el `main.py` original fallaba antes de
mostrar el menú con `FileNotFoundError`, pues el lector buscaba el catálogo en la
raíz. Para comparar la lógica previa se redirigieron únicamente sus aperturas
de `packs_compras.json` y `jugadores.json` a los archivos existentes en `config/`
y `datos/`, sin editar el código capturado. Esta adaptación permite comparar
el flujo que estaba bloqueado por las rutas, pero no equivale a afirmar que el
programa original arrancaba correctamente sin ella.

Se confirmó que `laboratorio/lab.py` mantiene su `TypeError` al llamar al módulo
como clase y que `laboratorio/mainpruebas.py` mantiene su `AttributeError` por
`PuntosPerdidos`. Este último impide ejecutar las instrucciones posteriores del
script completo; las operaciones trasladadas se comprobaron también por separado.
Los auxiliares de comparación quedaron en una carpeta temporal, fuera del proyecto.

## Errores y trabajo manual pendiente

| Ubicación | Comportamiento previo conservado | Pista |
| --- | --- | --- |
| `jugador.ComprobarYRestar` | Usa `jugador.PuntosPerdidos`, que no existe; falla también la coordinación de compra con saldo suficiente. | Revisar su relación con `PPerdidos` y con el precio recibido. |
| `ValidarQueSeaLetra` | `str(input())` acepta números y cualquier cadena. | Definir qué caracteres son válidos y cómo comprobarlos. |
| `jugador.__init__` | `idi == float(idi)` admite decimales y rechaza cadenas numéricas. | Definir el tipo de ID y validar ese tipo. |
| `jugador.RestarPuntos` | Compara el valor con la clase `int`, admite negativos y solo devuelve un cálculo. | Revisar tipo, signo y contrato de retorno frente a modificación de estado. |
| `jugador.SumarCRestarP` | Rechaza créditos mayores de 50 aunque el catálogo ofrece 80 y 150; admite argumentos negativos. | Revisar reglas y validaciones cuando trabajes la lógica. |
| `Lab*` | Las comprobaciones excluyen cero; una resta puede dar negativo. | Decidir límites antes de modificar condiciones. |
| `LabSumarYComprobarPuntos` | Solo evalúa `print`, sin imprimir ni sumar. | Definir la operación que falta. |
| `LabRestatYComprobarCreditos` | Calcula `NC` pero no lo devuelve ni modifica créditos. | Elegir el efecto deseado. |
| `MainCompra` | Lee un entero, pierde el valor al terminar y falla con texto inválido. | Decidir retorno y validación cuando implementes ese flujo. |
| `laboratorio/lab.py` | Importa un módulo y lo llama como clase: `TypeError`. | Revisar la importación de la clase `jugador`. |
| `datos/jugadores_vacio.json` | Está vacío; no contiene JSON válido. | Decidir si conservarlo como experimento o darle un contenido válido. |

`CrearId` ya existía: se conservó su cálculo, sin integrarlo al constructor ni al
flujo. No se implementaron guardado, nuevas reglas de IDs ni una compra completa.
Para ejecutar los scripts manuales con las importaciones del proyecto, usar
`python -B -m laboratorio.mainpruebas` o `python -B -m laboratorio.lab` desde la
raíz; ambos siguen teniendo los errores lógicos indicados.
