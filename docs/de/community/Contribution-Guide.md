# Beitrag zum Projekt

> [!CAUTION]
>
> Die aktuellen Projektbetreuer erforschen die automatisierte Internationalisierung der Dokumentation. Daher werden PRs im Zusammenhang mit der Internationalisierung/Übersetzung der Dokumentation NICHT akzeptiert!
>
> Bitte reichen Sie KEINE PRs im Zusammenhang mit der Internationalisierung/Übersetzung der Dokumentation ein!

Vielen Dank für Ihr Interesse an diesem Projekt! Bevor Sie mit Ihrem Beitrag beginnen, nehmen Sie sich bitte etwas Zeit, um die folgenden Richtlinien zu lesen, um sicherzustellen, dass Ihr Beitrag problemlos akzeptiert werden kann.

## Arten von Beiträgen, die nicht akzeptiert werden

1. Dokumentation Internationalisierung/Übersetzung
2. Beiträge im Zusammenhang mit der Kerninfrastruktur, wie z.B. HTTP-API, etc.
3. Issues, die explizit als "No help needed" markiert sind (einschließlich Issues in den Repositories [Byaidu/PDFMathTranslate](Byaidu/PDFMathTranslate) und [PDFMathTranslate/PDFMathTranslate-next](PDFMathTranslate/PDFMathTranslate-next)).
4. Andere Beiträge, die von den Maintainern als unangemessen erachtet werden.
5. Beiträge zur Dokumentation, aber Änderungen an der Dokumentation in anderen Sprachen als Englisch.
6. PRs, die das Ändern von PDF-Dateien erfordern.

Bitte reichen Sie KEINE PRs ein, die sich auf die oben genannten Arten beziehen.

> [!NOTE]
>
> Wenn Sie zur Dokumentation beitragen möchten, **ändern Sie bitte nur die englische Version der Dokumentation**. Andere Sprachversionen werden von den Mitwirkenden selbst übersetzt.

## Beitragsprozess

1. Forken Sie dieses Repository und klonen Sie es lokal.
2. Erstellen Sie einen neuen Branch: `git checkout -b feature/<feature-name>`.
3. Entwickeln Sie und stellen Sie sicher, dass Ihr Code den Anforderungen entspricht.
4. Committen Sie Ihren Code:
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```
5. Pushen Sie zu Ihrem Repository: `git push origin feature/<feature-name>`.
6. Erstellen Sie einen PR auf GitHub, geben Sie eine detaillierte Beschreibung an und fordern Sie eine Überprüfung von [@awwaawwa](https://github.com/awwaawwa) an.
7. Stellen Sie sicher, dass alle automatisierten Prüfungen bestanden werden.

> [!TIP]
>
> Sie müssen nicht warten, bis Ihre Entwicklung vollständig abgeschlossen ist, um einen PR zu erstellen. Eine frühzeitige Erstellung ermöglicht es uns, Ihre Implementierung zu überprüfen und Vorschläge zu machen.
>
> Wenn Sie Fragen zum Quellcode oder verwandten Themen haben, wenden Sie sich bitte an den Maintainer unter aw@funstory.ai.
>
> Ressourcendateien für Version 2.0 werden mit [BabelDOC](https://github.com/funstory-ai/BabelDOC) geteilt. Der Code zum Herunterladen der zugehörigen Ressourcen befindet sich in BabelDOC. Wenn Sie neue Ressourcendateien hinzufügen möchten, wenden Sie sich bitte an den BabelDOC-Maintainer unter aw@funstory.ai.

## Grundlegende Anforderungen

<h4 id="sop">1. Arbeitsablauf</h4>

- Bitte forken Sie vom `main`-Branch und entwickeln Sie auf Ihrem geforkten Branch.
   - Geben Sie beim Einreichen eines Pull Requests (PR) eine detaillierte Beschreibung Ihrer Änderungen an.
   - Wenn Ihr PR die automatisierten Prüfungen nicht besteht (angezeigt durch `checks failed` und ein rotes Kreuz), überprüfen Sie bitte die entsprechenden `details` und passen Sie Ihre Einreichung an, um sicherzustellen, dass der neue PR alle Prüfungen besteht.


<h4 id="dev&test">2. Entwicklung und Tests</h4>

- Verwenden Sie den Befehl `pip install -e .` für Entwicklung und Tests.


<h4 id="format">3. Code Formatting</h4>

- Konfigurieren Sie das `pre-commit`-Tool und aktivieren Sie `black` und `flake8` für die Codeformatierung.


<h4 id="requpdate">4. Abhängigkeitsaktualisierungen</h4>

- Wenn Sie neue Abhängigkeiten einführen, aktualisieren Sie bitte die Abhängigkeitsliste in der `pyproject.toml`-Datei zeitnah.


<h4 id="docupdate">5. Dokumentationsaktualisierungen</h4>

- Wenn Sie neue Kommandozeilen-Optionen hinzufügen, aktualisieren Sie bitte die Liste der Kommandozeilen-Optionen in allen Sprachversionen der `README.md`-Datei entsprechend.


<h4 id="commitmsg">6. Commit-Nachrichten</h4>

- Verwenden Sie [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), zum Beispiel: `feat(translator): add openai`.


<h4 id="codestyle">7. Codierungsstil</h4>

- Stellen Sie sicher, dass Ihr eingereichter Code grundlegende Codierungsstilstandards einhält.
   - Verwenden Sie entweder snake_case oder camelCase für die Benennung von Variablen.


<h4 id="doctypo">8. Dokumentationsformatierung</h4>

- Für die Formatierung von `README.md` folgen Sie bitte den [Chinesischen Richtlinien für Texterstellung](https://github.com/sparanoid/chinese-copywriting-guidelines).
   - Stellen Sie sicher, dass sowohl die englische als auch die chinesische Dokumentation immer auf dem neuesten Stand sind; Aktualisierungen der Dokumentation in anderen Sprachen sind optional.

## Hinzufügen einer Übersetzungsmaschine

1. Fügen Sie eine neue Übersetzerkonfigurationsklasse in der Datei `pdf2zh/config/translate_engine_model.py` hinzu.
2. Fügen Sie eine Instanz der neuen Übersetzerkonfigurationsklasse zum Typalias `TRANSLATION_ENGINE_SETTING_TYPE` in derselben Datei hinzu.
3. Fügen Sie die neue Übersetzerimplementierungsklasse im Ordner `pdf2zh/translator/translator_impl` hinzu.

> [!NOTE]
>
> Dieses Projekt beabsichtigt nicht, Übersetzungsmaschinen mit einer RPS (Anfragen pro Sekunde) von weniger als 4 zu unterstützen. Bitte reichen Sie keine Unterstützung für solche Maschinen ein.

## Projektstruktur

- **config folder**: Konfigurationssystem.
- **translator folder**: Implementierungen im Zusammenhang mit Übersetzern.
- **gui.py**: Stellt die GUI-Schnittstelle bereit.
- **const.py**: Einige Konstanten.
- **main.py**: Stellt das Kommandozeilen-Tool bereit.
- **high_level.py**: Hochrangige Schnittstellen basierend auf BabelDOC.
- **http_api.py**: Stellt HTTP-API bereit (nicht gestartet).

## Kontaktieren Sie uns

Wenn Sie Fragen haben, senden Sie bitte Feedback über Issue oder treten Sie unserer Telegram-Gruppe bei. Vielen Dank für Ihren Beitrag!

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) sponsert monatliche Pro-Mitgliedschaftscodes für aktive Mitwirkende an diesem Projekt. Einzelheiten finden Sie unter: [BabelDOC/PDFMathTranslate Contributor Reward Rules](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/)

<div align="right"> 
<h6><small>Ein Teil des Inhalts dieser Seite wurde von GPT übersetzt und kann Fehler enthalten.</small></h6>