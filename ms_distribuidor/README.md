# Microsoft Store — Distribuidor (`ms_distribuidor`)

Módulo de Odoo 18 para una tienda distribuidora de productos Microsoft en Ecuador.

Es un módulo **100% personalizado**: no hereda ni integra ningún modelo predefinido de Odoo
(`product.template`, `res.partner`, `hr.employee`, `sale.order`, `stock`, `account`, `mail`).
Su única dependencia es `base`.

## Modelos

| Modelo | Descripción |
|---|---|
| `ms.producto` | Producto Microsoft: línea, categoría, versión, specs, precios con IVA |
| `ms.cliente` | Cliente propio (cédula / RUC / pasaporte) |
| `ms.vendedor` | Asesor de la tienda |
| `ms.demo_producto` | Demo o prueba de producto, con flujo borrador → confirmada → realizada |
| `ms.venta` | Venta con secuencia `VENTA/0001` y flujo cotización → confirmada → facturada |

## Cálculo de impuestos

El IVA se calcula en Python, sin el módulo de contabilidad. La tarifa vive en una sola
constante, `IVA_TARIFA` en `models/ms_producto.py`, que `ms.venta` importa:

```python
IVA_TARIFA = 0.15          # IVA vigente en Ecuador

iva_valor    = precio_base * IVA_TARIFA
precio_final = precio_base + iva_valor
```

Los productos tecnológicos **no llevan ICE**: ese impuesto aplica únicamente a vehículos,
alcohol y tabaco, así que el módulo no lo modela.

Ambos campos calculados son `store=True`, condición necesaria para que el total pueda
agregarse en las vistas pivot y graph.

## Menús

```
Microsoft Store
├── Productos
├── Clientes
├── Ventas
├── Demos de producto
├── Vendedores
└── Tablero
    └── Análisis de ventas   (pivot + graph sobre ms.venta)
```

## Instalación

El módulo debe estar en una carpeta del `addons_path` (aquí `C:\odoo-dev\cunstom-addons`).

Primera instalación:

```bash
C:\odoo-dev\venv\Scripts\python.exe C:\odoo-dev\odoo\odoo-bin -c C:\odoo-dev\odoo.conf -d localhost -i ms_distribuidor --stop-after-init
```

Actualizar tras editar código o vistas:

```bash
C:\odoo-dev\venv\Scripts\python.exe C:\odoo-dev\odoo\odoo-bin -c C:\odoo-dev\odoo.conf -d localhost -u ms_distribuidor --stop-after-init
```

Arrancar el servidor:

```bash
C:\odoo-dev\venv\Scripts\python.exe C:\odoo-dev\odoo\odoo-bin -c C:\odoo-dev\odoo.conf -d localhost
```

Luego entra a http://localhost:8069 y busca **Microsoft Store** en el menú de aplicaciones.

## Datos iniciales

`data/ms_datos_iniciales.xml` carga 9 productos, 4 clientes, 3 vendedores, 3 demos y 8 ventas
repartidas en los últimos tres meses, para que el análisis de ventas tenga algo que graficar.

Va marcado con `noupdate="1"`: los registros se crean una sola vez y puedes editarlos o
borrarlos sin que una actualización del módulo los reponga. Las ventas de ejemplo usan
referencias `VENTA/DEMO/NN` para no consumir la secuencia real, así que la primera venta que
crees desde la interfaz será `VENTA/0001`.

## Seguridad

`security/ir.model.access.csv` concede lectura, escritura, creación y borrado sobre los cinco
modelos al grupo `base.group_user` (usuario interno). No hay grupos propios ni reglas de
registro.

## Notas de versión de Odoo

Escrito para **Odoo 18**, lo que implica dos diferencias respecto a ejemplos más antiguos:

- Las vistas de lista usan `<list>`, no `<tree>`.
- La visibilidad condicional se declara directo en el nodo — `invisible="estado != 'borrador'"`
  — en lugar del atributo `attrs`, eliminado desde la versión 17.

## Frontend

El look & feel tipo microsoft.com (Fluent Design, azul `#0078D4`, Segoe UI) **no** se
implementa aquí: este módulo es el backend y usa las vistas estándar de Odoo. La capa visual
va en un frontend Django aparte que consume estos modelos vía XML-RPC.
