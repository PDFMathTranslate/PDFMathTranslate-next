[**Opciones avanzadas**](./introduction.md) > **Opciones avanzadas** _(actual)_

---

<h3 id="toc">Tabla de Contenidos</h3>

- [Argumentos de la Línea de comandos](#argumentos-de-la-línea-de-comandos)
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

#### Argumentos de la Línea de comandos

Ejecuta el comando de traducción en la línea de comandos para generar el documento traducido `example-mono.pdf` y el documento bilingüe `example-dual.pdf` en el directorio de trabajo actual. Utiliza Google como servicio de traducción predeterminado. Más servicios de traducción soportados se pueden encontrar [AQUÍ](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../images/cmd_light.svg" width="580px"  alt="cmd"/>

En la siguiente tabla, enumeramos todas las opciones avanzadas para referencia:

##### Argumentos

| Opción                          | Función                                                                               | Ejemplo                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Ruta del archivo PDF local                                                            | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | Archivos en línea                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | Directorio de salida para los archivos                                                | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | Usar [**servicio específico**](./Documentation-of-Translation-Services.md) para traducción | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | Mostrar mensaje de ayuda y salir                                                       | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | Ruta al archivo de configuración                                                       | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | Intervalo de informe de progreso en segundos                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | Usar nivel de registro de depuración                                                   | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | Interactuar con la GUI                                                                 | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | Solo descargar y verificar los recursos requeridos y luego salir                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | Generar paquete de recursos sin conexión en el directorio especificado                 | `pdf2zh example.pdf --generate-offline-assets /ruta`                                                                 |
| `--restore-offline-assets`      | Restaurar el paquete de recursos sin conexión desde el directorio especificado        | `pdf2zh example.pdf --restore-offline-assets /path`                                                                  |
| `--version`                     | Mostrar versión y salir                                                                | `pdf2zh --version`                                                                                                   |
| `--pages`                       | Traducción parcial de documento                                                       | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | El código del idioma de origen                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | El código del idioma de destino                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | Longitud mínima del texto a traducir                                                   | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | Dirección del host del servicio RPC para análisis de diseño de documentos              |                                                                                                                      |
| `--qps`                         | Límite de QPS para el servicio de traducción                                                      | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | Ignorar caché de traducción                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | Prompt personalizado del sistema para traducción. Usado para `/no_think` en Qwen 3                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | Número máximo de trabajadores para el grupo de traducción. Si no se establece, se usará qps como el número de trabajadores | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | Desactivar extracción automática de glosario                                           | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | Anular la familia de fuentes principal para el texto traducido. Opciones: 'serif' para fuentes serif, 'sans-serif' para fuentes sans-serif, 'script' para fuentes script/cursivas. Si no se especifica, utiliza selección automática de fuentes basada en las propiedades del texto original. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | No generar archivos PDF bilingües                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | No generar archivos PDF monolingües                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | Patrón de fuente para identificar texto de fórmulas                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | Patrón de caracteres para identificar texto de fórmulas                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | Forzar la división de líneas cortas en diferentes párrafos                             | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | Factor de umbral de división para líneas cortas                                        |                                                                                                                      |
| `--skip-clean`                  | Omitir paso de limpieza de PDF                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        | En el modo de PDF dual, coloca primero la página traducida                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | Deshabilitar traducción de texto enriquecido                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | Habilitar todas las opciones de mejora de compatibilidad                               | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | Usar modo de páginas alternas para PDF dual                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | Modo de marca de agua para archivos PDF                                                | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | Máximo de páginas por parte para traducción dividida                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | Traducir texto de tablas (experimental)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | Omitir detección de escaneado                                                         | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | Forzar que el texto traducido sea negro y agregar fondo blanco                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | Habilitar solución automática para OCR. Si se detecta que un documento está muy escaneado, intentará habilitar el procesamiento OCR y omitirá la detección de escaneo adicional. Consulte la documentación para más detalles. (predeterminado: False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page`| Incluir solo las páginas traducidas en el PDF de salida. Solo es efectivo cuando se usa --pages. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | Glosario personalizado para la traducción.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |
| `--save-auto-extracted-glossary`| guardar glosario extraído automáticamente.                                                | `pdf2zh example.pdf --save-auto-extracted-glossary`                                                                   |


##### Argumentos de GUI

| Opción                          | Función                                | Ejemplo                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Habilitar modo de compartir            | `pdf2zh --gui --share`                          |
| `--auth-file`                   | Ruta al archivo de autenticación        | `pdf2zh --gui --auth-file /path`                |
| `--welcome-page`                | Ruta al archivo html de bienvenida     | `pdf2zh --gui --welcome-page /path`             |
| `--enabled-services`            | Servicios de traducción habilitados           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Deshabilitar entrada sensible en GUI   | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | Deshabilitar el guardado automático de configuración | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | Puerto de WebUI                        | `pdf2zh --gui --server-port 7860`               |

[⬆️ Volver al inicio](#toc)

---

#### Traducción parcial

Utiliza el parámetro `--pages` para traducir una parte de un documento.

- Si los números de página son consecutivos, puedes escribirlo así:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` incluye todas las páginas después de la página 25. Si tu documento tiene 100 páginas, esto es equivalente a `25-100`.
> 
> De manera similar, `-25` incluye todas las páginas antes de la página 25, lo cual es equivalente a `1-25`.

- Si las páginas no son consecutivas, puedes usar una coma `,` para separarlas.

Por ejemplo, si deseas traducir la primera y tercera página, puedes usar el siguiente comando:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Si las páginas incluyen rangos tanto consecutivos como no consecutivos, también puedes conectarlos con una coma, así:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Este comando traducirá la primera página, la tercera página, las páginas 10-20 y todas las páginas desde la 25 hasta el final.


[⬆️ Volver al inicio](#toc)

---

#### Especificar idiomas de origen y destino

Ver [Códigos de idioma de Google](https://developers.google.com/admin-sdk/directory/v1/languages), [Códigos de idioma de DeepL](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Volver al inicio](#toc)

---

#### Traducir con excepciones

Usar expresiones regulares para especificar fuentes de fórmulas y caracteres que deben preservarse:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Preservar las fuentes `Latex`, `Mono`, `Code`, `Italic`, `Symbol` y `Math` por defecto:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Volver al inicio](#toc)

---

#### Prompt personalizado

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Prompt personalizado del sistema para traducción. Se utiliza principalmente para agregar la instrucción '/no_think' de Qwen 3 en el prompt.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Volver al inicio](#toc)

---

#### Configuración personalizada

Hay múltiples formas de modificar e importar el archivo de configuración.

> [!NOTE]
> **Jerarquía de archivos de configuración**
>
> Al modificar el mismo parámetro utilizando diferentes métodos, el software aplicará los cambios según el orden de prioridad a continuación.
>
> Las modificaciones de mayor prioridad anularán las de menor prioridad.
>
> **cli/gui > env > archivo de configuración de usuario > archivo de configuración predeterminado**

- Modificación de la configuración mediante **Argumentos de la Línea de comandos**

En la mayoría de los casos, puedes pasar directamente tus configuraciones deseadas a través de argumentos de la línea de comandos. Por favor, consulta [Argumentos de la Línea de comandos](#cmd) para más información.

Por ejemplo, si deseas habilitar una ventana GUI, puedes usar el siguiente comando:

```bash
pdf2zh_next --gui
```

- Modificación de la configuración mediante **Variables de entorno**

Puedes reemplazar el `--` en los argumentos de la línea de comandos con `PDF2ZH_`, conectar parámetros usando `=`, y reemplazar `-` con `_` como variables de entorno.

Por ejemplo, si deseas habilitar una ventana GUI, puedes usar el siguiente comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../images/ev_light.svg" width="580px"  alt="env"/>

- Archivo de **Configuración** especificado por el usuario

Puedes especificar un archivo de configuración utilizando el siguiente argumento de la línea de comandos:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Si no estás seguro acerca del formato del archivo de configuración, por favor consulta el archivo de configuración predeterminado descrito a continuación.

- **Archivo de configuración predeterminado**

El archivo de configuración predeterminado se encuentra en `~/.config/pdf2zh`.  
Por favor, no modifiques los archivos de configuración en el directorio `default`.  
Se recomienda encarecidamente consultar el contenido de este archivo de configuración y utilizar **Configuración personalizada** para implementar tu propio archivo de configuración.

> [!TIP]
> - Por defecto, pdf2zh 2.0 guarda automáticamente la configuración actual en `~/.config/pdf2zh/config.v3.toml` cada vez que haces clic en el botón de traducir en la GUI. Este archivo de configuración se cargará por defecto en el próximo inicio.
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
> Cuando `--enhance-compatibility` está habilitado, Omitir limpieza se activa automáticamente.

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
> - Separe diferentes servicios disponibles con *comas en inglés* <kbd>,</kbd> .

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

Cuando se utiliza Autenticación y página de bienvenida para especificar qué usuario utilizará la interfaz web y personalizar la página de inicio de sesión:

ejemplo auth.txt
Cada línea contiene dos elementos, nombre de usuario y contraseña, separados por una coma.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

example welcome.html

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
> La página de bienvenida funcionará solo si el archivo de autenticación no está vacío.
> Si el archivo de autenticación está vacío, no habrá autenticación. :)

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

PDFMathTranslate soporta la tabla de glosario. El archivo de tablas de glosario debe ser un archivo `csv`.
Hay tres columnas en el archivo. Aquí hay un archivo de glosario de demostración:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自动 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |


Para usuarios de CLI:
Puedes usar múltiples archivos para el glosario. Y los diferentes archivos deben estar separados por `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Para usuarios de WebUI:

Ahora puedes subir tu propio archivo de glosario. Después de subir el archivo, puedes verificarlo haciendo clic en su nombre y el contenido se mostrará a continuación.

[⬆️ Volver arriba](#toc)

<div align="right"> 
<h6><small>Parte del contenido de esta página ha sido traducido por GPT y puede contener errores.</small></h6>