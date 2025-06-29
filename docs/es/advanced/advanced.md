[**Opciones avanzadas**](./introduction.md) > **Opciones avanzadas** _(actual)_

---

<h3 id="toc">Tabla de Contenidos</h3>

- [Argumentos de línea de comandos](#argumentos-de-línea-de-comandos)
  - [Argumentos](#argumentos)
  - [Argumentos de GUI](#argumentos-de-gui)
- [Traducción parcial](#traducción-parcial)
- [Especificar idiomas de origen y destino](#especificar-idiomas-de-origen-y-destino)
- [Traducir con excepciones](#traducir-con-excepciones)
- [Prompt personalizado](#prompt-personalizado)
- [Configuración personalizada](#configuración-personalizada)
- [Omitir limpieza](#omitir-limpieza)
- [Caché de traducción](#caché-de-traducción)
- [Despliegue como servicios públicos](#despliegue-como-servicios-públicos)
- [Autenticación y página de bienvenida](#autenticación-y-página-de-bienvenida)
- [Soporte de glosario](#soporte-de-glosario)

---

#### Argumentos de la línea de comandos

Ejecuta el comando de traducción en la línea de comandos para generar el documento traducido `example-mono.pdf` y el documento bilingüe `example-dual.pdf` en el directorio de trabajo actual. Utiliza Google como el servicio de traducción predeterminado. Puedes encontrar más servicios de traducción soportados [AQUÍ](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../images/cmd_light.svg" width="580px"  alt="cmd"/>

En la siguiente tabla, enumeramos todas las opciones avanzadas como referencia:

##### Argumentos

| Opción                          | Función                                                                               | Ejemplo                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Ruta local del archivo PDF                                                             | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | Archivos en línea                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | Directorio de salida para los archivos                                                             | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | Usar [**servicio específico**](./Documentación-de-servicios-de-traducción.md) para traducción | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | Mostrar mensaje de ayuda y salir                                                             | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | Ruta al archivo de configuración                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | Intervalo de informe de progreso en segundos                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | Usar nivel de registro de depuración                                                | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | Interactuar con la interfaz gráfica de usuario (GUI)                                                                      | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | Solo descargar y verificar los recursos necesarios y luego salir                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | Generar paquete de recursos sin conexión en el directorio especificado                             | `pdf2zh example.pdf --generate-offline-assets /path`                                                                 |
| `--restore-offline-assets`      | Restaurar el paquete de recursos sin conexión desde el directorio especificado                            | `pdf2zh example.pdf --restore-offline-assets /ruta`                                                                  |
| `--version`                     | Mostrar la versión y luego salir                                                                 | `pdf2zh --version`                                                                                                   |
| `--pages`                       | Traducción parcial del documento                                                      | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | El código del idioma de origen                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | El código del idioma de destino                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | Longitud mínima del texto a traducir                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | Dirección del host del servicio RPC para el análisis de diseño de documentos                                  |                                                                                                                      |
| `--qps`                         | Límite de QPS para el servicio de traducción                                                      | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | Ignorar caché de traducción                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | Prompt personalizado del sistema para traducción. Usado para `/no_think` en Qwen 3                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | Número máximo de trabajadores para el grupo de traducción. Si no se establece, se usará qps como el número de trabajadores | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | Desactivar la extracción automática del glosario                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | Anula la familia de fuentes principal para el texto traducido. Opciones: 'serif' para fuentes serif, 'sans-serif' para fuentes sans-serif, 'script' para fuentes de script/cursivas. Si no se especifica, utiliza la selección automática de fuentes basada en las propiedades del texto original. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | No generar archivos PDF bilingües                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | No generar archivos PDF monolingües                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | Patrón de fuente para identificar texto de fórmulas                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | Patrón de caracteres para identificar texto de fórmulas                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | Forzar la división de líneas cortas en diferentes párrafos                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | Factor de umbral de división para líneas cortas                                                 |                                                                                                                      |
| `--skip-clean`                  | Omitir el paso de limpieza del PDF                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        |  En modo PDF dual, coloca primero la página traducida                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | Deshabilitar la traducción de texto enriquecido                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | Activar todas las opciones de mejora de compatibilidad                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | Usar el modo de páginas alternas para PDF dual                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | Modo de salida de marca de agua para archivos PDF                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | Máximo de páginas por parte para traducción dividida                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | Traducir texto de tablas (experimental)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | Omitir detección de escaneado                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | Forzar que el texto traducido sea negro y añadir un fondo blanco                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | Habilita la solución automática para OCR. Si se detecta que un documento está muy escaneado, intentará habilitar el procesamiento OCR y omitirá la detección adicional de escaneo. Consulta la documentación para más detalles. (predeterminado: False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page`| Solo incluir las páginas traducidas en el PDF de salida. Solo es efectivo cuando se usa --pages. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | Glosario personalizado para la traducción.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |

##### Argumentos de GUI

| Opción                          | Función                               | Ejemplo                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Habilitar modo de compartir           | `pdf2zh --gui --share`                          |
| `--auth-file`                   | Ruta al archivo de autenticación      | `pdf2zh --gui --auth-file /ruta`                |
| `--welcome-page`                | Ruta al archivo html de bienvenida    | `pdf2zh --gui --welcome-page /ruta`             |
| `--enabled-services`            | Servicios de traducción habilitados   | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Deshabilitar entrada sensible en GUI  | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | Deshabilitar guardado automático de configuración | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | Puerto de la WebUI                    | `pdf2zh --gui --server-port 7860`               |

[⬆️ Volver al inicio](#toc)

---

#### Traducción parcial

Utiliza el parámetro `--pages` para traducir una porción de un documento.

- Si los números de página son consecutivos, puedes escribirlo así:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` incluye todas las páginas posteriores a la página 25. Si tu documento tiene 100 páginas, esto equivale a `25-100`.
> 
> Del mismo modo, `-25` incluye todas las páginas anteriores a la página 25, lo que equivale a `1-25`.

- Si las páginas no son consecutivas, puedes usar una coma `,` para separarlas.

Por ejemplo, si quieres traducir la primera y tercera página, puedes usar el siguiente comando:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Si las páginas incluyen rangos consecutivos y no consecutivos, también puedes conectarlos con una coma, así:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Este comando traducirá la primera página, la tercera página, las páginas 10-20 y todas las páginas desde la 25 hasta el final.

[⬆️ Volver al inicio](#toc)

---

#### Especificar idiomas de origen y destino

Consulta los [Códigos de idioma de Google](https://developers.google.com/admin-sdk/directory/v1/languages) y los [Códigos de idioma de DeepL](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Volver al inicio](#toc)

---

#### Traducir con excepciones

Usa expresiones regulares para especificar las fuentes de fórmulas y los caracteres que deben preservarse:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Conserva las fuentes `Latex`, `Mono`, `Code`, `Italic`, `Symbol` y `Math` por defecto:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Volver al inicio](#toc)

---

#### Prompt personalizado

<!-- Nota: Actualmente no se admite el mensaje del sistema. Consulta [este cambio](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Mensaje del sistema personalizado para la traducción. Se utiliza principalmente para agregar la instrucción '/no_think' de Qwen 3 en el mensaje.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Volver al inicio](#toc)

---

#### Configuración personalizada

Existen múltiples formas de modificar e importar el archivo de configuración.

> [!NOTE]
> **Jerarquía del archivo de configuración**
>
> Al modificar el mismo parámetro utilizando diferentes métodos, el software aplicará los cambios según el orden de prioridad a continuación.
>
> Las modificaciones de mayor prioridad anularán las de menor prioridad.
>
> **cli/gui > env > archivo de configuración del usuario > archivo de configuración predeterminado**

- Modificación de la configuración mediante **argumentos de la línea de comandos**

En la mayoría de los casos, puedes pasar directamente tus configuraciones deseadas a través de argumentos de la línea de comandos. Consulta [Argumentos de la línea de comandos](#cmd) para más información.

Por ejemplo, si deseas habilitar una ventana GUI, puedes usar el siguiente comando:

```bash
pdf2zh_next --gui
```

- Modificación de la configuración mediante **variables de entorno**

<!-- TODO Colocar una ilustración de variables de entorno aquí -->

Puedes reemplazar los `--` en los argumentos de la línea de comandos con `PDF2ZH_`, conectar parámetros usando `=` y reemplazar `-` con `_` como variables de entorno.

Por ejemplo, si deseas habilitar una ventana GUI, puedes usar el siguiente comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../images/ev_light.svg" width="580px"  alt="env"/>

- Archivo de **configuración** especificado por el usuario

Puedes especificar un archivo de configuración utilizando el siguiente argumento de la línea de comandos:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Si no está seguro del formato del archivo de configuración, consulte el archivo de configuración predeterminado que se describe a continuación.

- **Archivo de configuración predeterminado**

El archivo de configuración predeterminado se encuentra en `~/.config/pdf2zh`.  
Por favor, no modifiques los archivos de configuración en el directorio `default`.  
Se recomienda encarecidamente consultar el contenido de este archivo de configuración y utilizar **Archivo de configuración especificado por el usuario** para implementar tu propio archivo de configuración.

> [!TIP]
> - Por defecto, pdf2zh 2.0 guarda automáticamente la configuración actual en `~/.config/pdf2zh/config.v3.toml` cada vez que haces clic en el botón de traducción en la GUI. Este archivo de configuración se cargará por defecto en el próximo inicio.
> - Los archivos de configuración en el directorio `default` son generados automáticamente por el programa. Puedes copiarlos para modificarlos, pero por favor no los modifiques directamente.
> - Los archivos de configuración pueden incluir números de versión como "v2", "v3", etc. Estos son **números de versión del archivo de configuración**, **no** el número de versión de pdf2zh en sí.

[⬆️ Volver al inicio](#toc)

---

#### Omitir limpieza

Cuando este parámetro se establece en True, se omitirá el paso de limpieza del PDF, lo que puede mejorar la compatibilidad y evitar algunos problemas de procesamiento de fuentes.

Uso:

```bash
pdf2zh_next example.pdf --skip-clean
```

O utilizando variables de entorno:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Cuando `--enhance-compatibility` está habilitado, Skip clean se activa automáticamente.

---

#### Caché de traducción

PDFMathTranslate almacena en caché los textos traducidos para aumentar la velocidad y evitar llamadas API innecesarias para los mismos contenidos. Puedes usar la opción `--ignore-cache` para ignorar la caché de traducción y forzar la retraducción.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Volver al inicio](#toc)

---

#### Despliegue como servicios públicos

Al desplegar una GUI de pdf2zh en servicios públicos, debes modificar el archivo de configuración como se describe a continuación.

> [!TIP]
> - Al desplegar públicamente, tanto `disable_gui_sensitive_input` como `disable_config_auto_save` deben estar habilitados.
> - Separa diferentes servicios disponibles con *comas en inglés* <kbd>,</kbd> .

Una configuración utilizable es la siguiente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Volver al inicio](#toc)

---

#### Autenticación y página de bienvenida

Al usar Autenticación y página de bienvenida para especificar qué usuario utilizará la Interfaz de Usuario Web y personalizar la página de inicio de sesión:

ejemplo auth.txt
Cada línea contiene dos elementos, nombre de usuario y contraseña, separados por una coma.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

ejemplo welcome.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Simple HTML</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my simple HTML page.</p>
</body>
</html>
```

> [!NOTE]
> La página de bienvenida funcionará solo si el archivo de autenticación no está en blanco.
> Si el archivo de autenticación está en blanco, no habrá autenticación. :)

Una configuración utilizable es la siguiente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Volver al inicio](#toc)

---

#### Soporte de glosario

PDFMathTranslate admite la tabla de glosario. El archivo de tablas de glosario debe ser un archivo `csv`.
Hay tres columnas en el archivo. Aquí hay un archivo de glosario de demostración:

| fuente | objetivo  | tgt_lng |
|--------|---------|---------|
| AutoML | ML automático  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |

Para usuarios de la línea de comandos:
Puedes usar múltiples archivos para el glosario. Y los diferentes archivos deben separarse con `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Para usuarios de WebUI:

Ahora puedes subir tu propio archivo de glosario. Después de subir el archivo, puedes verificar su contenido haciendo clic en su nombre y el contenido se mostrará debajo.

[⬆️ Volver al inicio](#toc)

<div align="right"> 
<h6><small>Parte del contenido de esta página ha sido traducido por GPT y puede contener errores.</small></h6>