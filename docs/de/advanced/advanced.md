[**Erweiterte Optionen**](./introduction.md) > **Erweiterte Optionen** _(aktuell)_

---

<h3 id="toc">Inhaltsverzeichnis</h3>

- [Kommandozeilen-Argumente](#kommandozeilen-argumente)
  - [Argumente](#argumente)
  - [GUI-Argumente](#gui-argumente)
- [Teilweise Übersetzung](#teilweise-übersetzung)
- [Quell- und Zielsprachen angeben](#quell--und-zielsprachen-angeben)
- [Übersetzung mit Ausnahmen](#übersetzung-mit-ausnahmen)
- [Benutzerdefinierte Eingabeaufforderung](#benutzerdefinierte-eingabeaufforderung)
- [Benutzerdefinierte Konfiguration](#benutzerdefinierte-konfiguration)
- [Bereinigung überspringen](#bereinigung-überspringen)
- [Übersetzungscache](#übersetzungscache)
- [Bereitstellung als öffentlicher Dienst](#bereitstellung-als-öffentlicher-dienst)
- [Authentifizierung und Willkommensseite](#authentifizierung-und-willkommensseite)
- [Glossar-Unterstützung](#glossar-unterstützung)

---

#### Kommandozeilen-Argumente

Führen Sie den Übersetzungsbefehl in der Kommandozeile aus, um das übersetzte Dokument `example-mono.pdf` und das zweisprachige Dokument `example-dual.pdf` im aktuellen Arbeitsverzeichnis zu generieren. Verwenden Sie Google als Standard-Übersetzungsdienst. Weitere unterstützte Übersetzungsdienste finden Sie [HIER](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../images/cmd_light.svg" width="580px"  alt="cmd"/>

In der folgenden Tabelle listen wir alle erweiterten Optionen zur Referenz auf:

##### Argumente

| Option                          | Funktion                                                                               | Beispiel                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Lokaler PDF-Dateipfad                                                                    | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | Online-Dateien                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | Ausgabeverzeichnis für Dateien                                                             | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | Verwenden Sie einen [**spezifischen Dienst**](./Dokumentation-der-Übersetzungsdienste.md) für die Übersetzung | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | Hilfe-Nachricht anzeigen und beenden                                                   | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | Pfad zur Konfigurationsdatei                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | Fortschrittsberichtsintervall in Sekunden                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | Debug-Logging-Level verwenden                                                                | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | Interaktion mit der GUI                                                                 | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | Lädt nur die erforderlichen Assets herunter und überprüft sie, bevor das Programm beendet wird                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | Generieren Sie ein Offline-Asset-Paket im angegebenen Verzeichnis                             | `pdf2zh example.pdf --generate-offline-assets /pfad`                                                                 |
| `--restore-offline-assets`      | Stellt das Offline-Asset-Paket aus dem angegebenen Verzeichnis wieder her                            | `pdf2zh example.pdf --restore-offline-assets /pfad`                                                                  |
| `--version`                     | Version anzeigen und beenden                                                                 | `pdf2zh --version`                                                                                                   |
| `--pages`                       | Teilweise Übersetzung des Dokuments                                                           | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | Der Code der Ausgangssprache                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | Der Code der Zielsprache                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | Minimale Textlänge für die Übersetzung                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | RPC-Service-Hostadresse für die Dokumentenlayoutanalyse                                  |                                                                                                                      |
| `--qps`                         | QPS-Limit für den Übersetzungsdienst                                                   | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | Übersetzungscache ignorieren                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | Benutzerdefinierte Systemaufforderung für die Übersetzung. Wird für `/no_think` in Qwen 3 verwendet                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | Maximale Anzahl an Arbeitern für den Übersetzungspool. Falls nicht gesetzt, wird qps als Anzahl der Arbeiter verwendet | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | Deaktiviert die automatische Glossarextraktion                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | Überschreibt die primäre Schriftfamilie für übersetzten Text. Optionen: 'serif' für Serifenschriften, 'sans-serif' für serifenlose Schriften, 'script' für Schreibschrift/kursive Schriften. Falls nicht angegeben, wird automatisch eine Schrift basierend auf den Eigenschaften des Originaltextes ausgewählt. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | Gibt keine zweisprachigen PDF-Dateien aus                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | Gibt keine einsprachigen PDF-Dateien aus                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | Schriftmuster zur Identifizierung von Formeltext                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | Zeichenmuster zur Identifizierung von Formeltext                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | Erzwingt die Aufteilung kurzer Zeilen in verschiedene Absätze                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | Teilungsschwellenwertfaktor für kurze Zeilen                                                 |                                                                                                                      |
| `--skip-clean`                  | Überspringe den Schritt der PDF-Bereinigung                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        |  Im Dual-PDF-Modus die Übersetzungsseite priorisiert platzieren                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | Deaktiviert die Übersetzung von formatiertem Text                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | Aktiviert alle Optionen zur Kompatibilitätsverbesserung                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | Verwenden Sie den Modus für abwechselnde Seiten für duale PDFs                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | Wasserzeichen-Ausgabemodus für PDF-Dateien                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | Maximale Seiten pro Teil für geteilte Übersetzung                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | Tabellentext übersetzen (experimentell)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | Überspringt die Erkennung gescannter Dokumente                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | Erzwingt, dass übersetzter Text schwarz ist und fügt einen weißen Hintergrund hinzu                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | Aktiviert die automatische OCR-Umgehung. Wenn ein Dokument als stark gescannt erkannt wird, wird versucht, die OCR-Verarbeitung zu aktivieren und die weitere Scan-Erkennung zu überspringen. Weitere Details finden Sie in der Dokumentation. (Standard: False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page`| Nur übersetzte Seiten in die Ausgabe-PDF aufnehmen. Wirkt nur, wenn --pages verwendet wird. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | Benutzerdefinierte Glossare für die Übersetzung.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |

##### GUI-Argumente

| Option                          | Funktion                               | Beispiel                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Freigabemodus aktivieren               | `pdf2zh --gui --share`                          |
| `--auth-file`                   | Pfad zur Authentifizierungsdatei       | `pdf2zh --gui --auth-file /pfad`                |
| `--welcome-page`                | Pfad zur Willkommens-HTML-Datei        | `pdf2zh --gui --welcome-page /pfad`             |
| `--enabled-services`            | Aktivierte Übersetzungsdienste         | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | GUI-Eingabe für sensible Daten deaktivieren | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | Automatisches Speichern der Konfiguration deaktivieren | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | WebUI-Port                             | `pdf2zh --gui --server-port 7860`               |

[⬆️ Zurück zum Anfang](#toc)

---

#### Teilweise Übersetzung

Verwenden Sie den Parameter `--pages`, um einen Teil eines Dokuments zu übersetzen.

- Wenn die Seitenzahlen aufeinanderfolgend sind, können Sie es wie folgt schreiben:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` umfasst alle Seiten ab Seite 25. Wenn Ihr Dokument 100 Seiten hat, entspricht dies `25-100`.
> 
> Ebenso umfasst `-25` alle Seiten vor Seite 25, was `1-25` entspricht.

- Wenn die Seiten nicht aufeinanderfolgend sind, können Sie ein Komma `,` verwenden, um sie zu trennen.

Beispiel: Wenn Sie die erste und dritte Seite übersetzen möchten, können Sie den folgenden Befehl verwenden:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Wenn die Seiten sowohl aufeinanderfolgende als auch nicht aufeinanderfolgende Bereiche enthalten, können Sie diese auch mit einem Komma verbinden, wie folgt:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Dieser Befehl übersetzt die erste Seite, die dritte Seite, die Seiten 10-20 und alle Seiten von 25 bis zum Ende.

[⬆️ Zurück zur Startseite](#toc)

---

#### Quell- und Zielsprachen angeben

Siehe [Google-Sprachcodes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL-Sprachcodes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Übersetzen mit Ausnahmen

Verwenden Sie reguläre Ausdrücke, um Formelschriften und Zeichen anzugeben, die erhalten bleiben müssen:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Behalten Sie standardmäßig die Schriftarten `Latex`, `Mono`, `Code`, `Italic`, `Symbol` und `Math` bei:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Benutzerdefinierte Eingabeaufforderung

<!-- Hinweis: Systemprompts werden derzeit nicht unterstützt. Siehe [diese Änderung](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Benutzerdefinierter Systemprompt für die Übersetzung. Er wird hauptsächlich verwendet, um die '/no_think'-Anweisung von Qwen 3 im Prompt hinzuzufügen.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Zurück zur Startseite](#toc)

---

#### Benutzerdefinierte Konfiguration

Es gibt mehrere Möglichkeiten, die Konfigurationsdatei zu ändern und zu importieren.

> [!NOTE]
> **Konfigurationsdatei-Hierarchie**
>
> Wenn derselbe Parameter mit verschiedenen Methoden geändert wird, wendet die Software die Änderungen gemäß der folgenden Prioritätsreihenfolge an.
>
> Höher eingestufte Änderungen überschreiben niedriger eingestufte.
>
> **cli/gui > env > Benutzerkonfigurationsdatei > Standardkonfigurationsdatei**

- Ändern der Konfiguration über **Kommandozeilenargumente**

In den meisten Fällen können Sie Ihre gewünschten Einstellungen direkt über Kommandozeilenargumente übergeben. Weitere Informationen finden Sie unter [Kommandozeilenargumente](#cmd).

Zum Beispiel, wenn Sie ein GUI-Fenster aktivieren möchten, können Sie den folgenden Befehl verwenden:

```bash
pdf2zh_next --gui
```

- Ändern der Konfiguration über **Umgebungsvariablen**

<!-- TODO Hier eine Abbildung der Umgebungsvariablen einfügen -->

Sie können die `--` in Kommandozeilenargumenten durch `PDF2ZH_` ersetzen, Parameter mit `=` verbinden und `-` durch `_` als Umgebungsvariablen ersetzen.

Zum Beispiel, wenn Sie ein GUI-Fenster aktivieren möchten, können Sie den folgenden Befehl verwenden:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../images/ev_light.svg" width="580px"  alt="env"/>

- Benutzerdefinierte **Konfigurationsdatei**

Sie können eine Konfigurationsdatei mit dem folgenden Kommandozeilenargument angeben:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Wenn Sie sich über das Format der Konfigurationsdatei unsicher sind, lesen Sie bitte die unten beschriebene Standardkonfigurationsdatei.

- **Standardkonfigurationsdatei**

Die Standardkonfigurationsdatei befindet sich unter `~/.config/pdf2zh`.  
Bitte ändern Sie die Konfigurationsdateien im Verzeichnis `default` nicht.  
Es wird dringend empfohlen, sich an den Inhalt dieser Konfigurationsdatei zu halten und die **Benutzerdefinierte Konfigurationsdatei** zu verwenden, um Ihre eigene Konfigurationsdatei zu implementieren.

> [!TIP]
> - Standardmäßig speichert pdf2zh 2.0 die aktuelle Konfiguration automatisch in `~/.config/pdf2zh/config.v3.toml` jedes Mal, wenn Sie auf die Übersetzungsschaltfläche in der GUI klicken. Diese Konfigurationsdatei wird beim nächsten Start standardmäßig geladen.
> - Die Konfigurationsdateien im Verzeichnis `default` werden automatisch vom Programm generiert. Sie können sie zur Bearbeitung kopieren, aber bitte ändern Sie sie nicht direkt.
> - Konfigurationsdateien können Versionsnummern wie "v2", "v3" usw. enthalten. Dies sind **Versionsnummern der Konfigurationsdatei**, **nicht** die Versionsnummer von pdf2zh selbst.


[⬆️ Zurück zum Anfang](#toc)

---

#### Bereinigung überspringen

Wenn dieser Parameter auf True gesetzt wird, wird der PDF-Bereinigungsschritt übersprungen, was die Kompatibilität verbessern und einige Schriftverarbeitungsprobleme vermeiden kann.

Verwendung:

```bash
pdf2zh_next example.pdf --skip-clean
```

Oder mit Umgebungsvariablen:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Wenn `--enhance-compatibility` aktiviert ist, wird Skip clean automatisch aktiviert.

---

#### Übersetzungscache

PDFMathTranslate speichert übersetzte Texte zwischen, um die Geschwindigkeit zu erhöhen und unnötige API-Aufrufe für dieselben Inhalte zu vermeiden. Sie können die Option `--ignore-cache` verwenden, um den Übersetzungscache zu ignorieren und eine erneute Übersetzung zu erzwingen.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Bereitstellung als öffentlicher Dienst

Beim Bereitstellen einer pdf2zh-GUI auf öffentlichen Diensten sollten Sie die Konfigurationsdatei wie unten beschrieben anpassen.

> [!TIP]
> - Bei der öffentlichen Bereitstellung sollten sowohl `disable_gui_sensitive_input` als auch `disable_config_auto_save` aktiviert sein.
> - Trennen Sie verschiedene verfügbare Dienste mit *englischen Kommas* <kbd>,</kbd>.

Eine brauchbare Konfiguration sieht wie folgt aus:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Authentifizierung und Willkommensseite

Bei der Verwendung von Authentifizierung und Willkommensseite, um festzulegen, welcher Benutzer die Web-Oberfläche nutzen und die Anmeldeseite anpassen kann:

Beispiel auth.txt
Jede Zeile enthält zwei Elemente, Benutzername und Passwort, getrennt durch ein Komma.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

Beispiel welcome.html

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
> Die Startseite funktioniert nur, wenn die Authentifizierungsdatei nicht leer ist.
> Wenn die Authentifizierungsdatei leer ist, gibt es keine Authentifizierung. :)

Eine brauchbare Konfiguration ist wie folgt:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Unterstützung für das Glossar

PDFMathTranslate unterstützt die Glossartabelle. Die Glossartabellendatei sollte eine `csv`-Datei sein.
Die Datei enthält drei Spalten. Hier ist eine Demo-Glossardatei:

| Quelle | Ziel  | Zielsprache |
|--------|---------|---------|
| AutoML | Automatisiertes ML  | de   |
| a,a    | a       | de   |
| "      | "       | de   |

Für CLI-Benutzer:
Sie können mehrere Dateien für das Glossar verwenden. Unterschiedliche Dateien sollten durch `,` getrennt werden.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Für WebUI-Benutzer:

Sie können jetzt Ihre eigene Glossardatei hochladen. Nachdem Sie die Datei hochgeladen haben, können Sie sie überprüfen, indem Sie auf ihren Namen klicken und der Inhalt wird unten angezeigt.

[⬆️ Zurück zum Anfang](#toc)

<div align="right"> 
<h6><small>Ein Teil des Inhalts dieser Seite wurde von GPT übersetzt und kann Fehler enthalten.</small></h6>