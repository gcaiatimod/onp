# Presupuestos Nacionales — ONP

Aplicación web de navegación presupuestaria de la **Oficina Nacional de Presupuesto (ONP)** del Ministerio de Economía de Argentina.

## Funcionalidades

- **Menú lateral** con 6 categorías principales: Presupuestos, Ejecución, Evaluación, Empresas Públicas, Sistema Presupuestario y Series Estadísticas
- **Subcategorías** desplegables según la categoría seleccionada
- **Resultados simulados** con documentos en formato PDF, RTF y XLS para cada subcategoría
- **Buscador global** que filtra resultados en todas las categorías
- **Filtro por año** (2023–2026) con chips de filtros activos

## Stack

- HTML/CSS/JS vanilla (sin frameworks JS)
- **Poncho** (Sistema de diseño del Gobierno de Argentina) — CSS local
- **Bootstrap 3** (vía CDN de argentina.gob.ar)
- **Font Awesome 4** (vía CDN)
- **SCSS** compilado con Sass, con sourcemaps

## Estructura

```
├── index.html                  # Entrada única (HTML + JS)
├── poncho.css                  # Poncho CSS descargado localmente
├── css/estilos-pasos.css       # SCSS compilado
├── scss/
│   ├── estilos-pasos.scss      # Estilos scoped bajo .presupuestos-nacionales
│   └── poncho/modules/         # Variables y módulos Poncho (no modificar)
├── AGENTS.md                   # Reglas de estilo del proyecto
└── README.md
```

## Compilación SCSS

```bash
sass scss/estilos-pasos.scss css/estilos-pasos.css        # compilar
sass --watch scss/estilos-pasos.scss:css/estilos-pasos.css # watch
sass -s compressed scss/estilos-pasos.scss css/estilos-pasos.css  # producción
```

## Convenciones

- Todo el CSS está scoped bajo `.presupuestos-nacionales`
- Solo se usan variables de Poncho (no crear `$variables-propias`)
- Prohibido `@extend`; usar `@mixin`
- `!important` solo como último recurso
- Mobile first

## Notas

- Los datos del menú están embebidos en `MENU_DATA` dentro de `index.html`
- Los resultados son simulados (datos estáticos en `SIMULATED_RESULTS`)
- Funciona desde protocolo `file://` sin servidor
