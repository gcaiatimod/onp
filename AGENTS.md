# AGENTS.md — Instrucciones obligatorias

Antes de modificar cualquier archivo del proyecto, leer y cumplir TODAS las reglas de GUIA-SCSS.md.

## Reglas que no se negocian

### 1. `poncho/modules/` NO SE TOCA
Todo el contenido de `scss/poncho/modules/` es dependencia del framework.
- No modificar, eliminar ni agregar archivos ahí.
- Solo se importan desde el SCSS principal.

### 2. Prohibido crear variables SCSS propias
- Usar exclusivamente las variables definidas dentro de `poncho/modules/`.
- Si el valor exacto no existe, usar la variable más cercana.
- Si ninguna variable coincide, hardcodear el valor con `// TODO:` comentado.
- **No crear `$variables-propias`**.

### 3. Todo bajo un scope único
- Nunca escribir selectores sueltos en la raíz. Todo anidado bajo un scope (ej: `.pasos-internacionales`).
- Modificadores y estados con `&` dentro del scope.

### 4. Media queries con scope repetido
- Cada media query debe repetir el scope completo adentro.

### 5. `@extend` prohibido — usar `@mixin`

### 6. `!important` solo como último recurso

### 7. Source maps
El archivo `.css.map` vincula el CSS compilado con el SCSS original. Sirve para debuggear desde DevTools viendo la fuente SCSS real.

### 8. Comentarios
| Formato | Sale en CSS | Para qué |
|---------|-------------|----------|
| `/* texto */` | Sí | Títulos de sección, delimitadores de bloque |
| `// texto` | No | Notas internas, FIXMEs, decisiones de diseño |

### 9. Selectores concatenados
Si hay que apuntar a elementos sin clase propia, hacerlo siempre dentro del scope. No encadenar más de 3 clases utilitarias.

### 10. Excepciones (fuera del scope)
Si es inevitable salir del scope (modales que Bootstrap mueve al body, containers de Drupal), documentar con comentario `// Excepción: ...`.

### 11. Mobile first
Sin media query = mobile. Breakpoints para pantallas más grandes.

## Orden del archivo SCSS
1. Imports de `poncho/modules/` (solo esos, no agregar otros)
2. Scope con estilos
3. Media queries al final

## Checklist antes de terminar
- [ ] Usé variables de Poncho, no valores fijos (o hardcode con `// TODO`)
- [ ] No toqué `poncho/modules/` (archivos, contenido ni estructura)
- [ ] No creé variables propias
- [ ] Todo anidado bajo scope único
- [ ] Media queries repiten el scope
- [ ] Sin `@extend`
- [ ] `!important` solo si inevitable
- [ ] Orden correcto: imports → estilos → media queries
- [ ] Source map generado (`.css.map`)
- [ ] Excepciones documentadas con `// Excepción: ...`

## Compilación
```bash
sass scss/estilos-pasos.scss css/estilos-pasos.css
sass --watch scss/estilos-pasos.scss:css/estilos-pasos.css
sass -s compressed scss/estilos-pasos.scss css/estilos-pasos.css
```
