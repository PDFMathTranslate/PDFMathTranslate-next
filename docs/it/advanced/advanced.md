[**Opzioni avanzate**](./introduction.md) > **Opzioni avanzate** _(current)_

---

<h3 id="toc">Indice</h3>

- [Argomenti della riga di comando](#argomenti-della-riga-di-comando)
- [Guida alla configurazione del rate limiting](#guida-alla-configurazione-del-rate-limiting)
- [Traduzione parziale](#traduzione-parziale)
- [Specificare le lingue di origine e di destinazione](#specificare-le-lingue-di-origine-e-di-destinazione)
- [Tradurre con eccezioni](#tradurre-con-eccezioni)
- [Prompt personalizzato](#prompt-personalizzato)
- [Configurazione personalizzata](#configurazione-personalizzata)
- [Salta la pulizia](#salta-la-pulizia)
- [Cache delle traduzioni](#cache-delle-traduzioni)
- [Distribuzione come servizi pubblici](#distribuzione-come-servizi-pubblici)
- [Autenticazione e pagina di benvenuto](#autenticazione-e-pagina-di-benvenuto)
- [Supporto per il glossario](#supporto-per-il-glossario)

---

#### Argomenti della riga di comando

Esegui il comando di traduzione nella riga di comando per generare il documento tradotto `example-mono.pdf` e il documento bilingue `example-dual.pdf` nella directory di lavoro corrente. Utilizza Google come servizio di traduzione predefinito. Altri servizi di traduzione supportati possono essere trovati [QUI](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

Nella tabella seguente, elenchiamo tutte le opzioni avanzate per riferimento:

##### Argomenti

| Opzione                          | Funzione                                                                               | Esempio                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Percorso locale del file PDF                                                           | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | File online                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | Directory di output per i file                                                             | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | Utilizzare [**servizio specifico**](./Documentation-of-Translation-Services.md) per la traduzione | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | Mostra il messaggio di aiuto ed esce                                                             | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | Percorso del file di configurazione                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | Intervallo di report di avanzamento in secondi                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | Usa il livello di registrazione debug                                                                | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | Interagisci con la GUI                                                                      | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | Solo scarica e verifica gli asset richiesti e poi esce                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | Genera il pacchetto di risorse offline nella directory specificata                             | `pdf2zh example.pdf --generate-offline-assets /path`                                                                 |
| `--restore-offline-assets`      | Ripristina il pacchetto di risorse offline dalla directory specificata                            | `pdf2zh example.pdf --restore-offline-assets /percorso`                                                                  |
| `--version`                     | Mostra la versione e poi esci                                                                 | `pdf2zh --version`                                                                                                   |
| `--pages`                       | Traduzione parziale del documento                                                    | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | Il codice della lingua di origine                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | Il codice della lingua di destinazione                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | Lunghezza minima del testo da tradurre                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | Indirizzo host del servizio RPC per l'analisi del layout del documento                                  |                                                                                                                      |
| `--qps`                         | Limite QPS per il servizio di traduzione                                               | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | Ignora la cache delle traduzioni                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | Prompt di sistema personalizzato per la traduzione. Utilizzato per `/no_think` in Qwen 3                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | Numero massimo di lavoratori per il pool di traduzione. Se non impostato, verrà utilizzato qps come numero di lavoratori | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | Disabilita l'estrazione automatica del glossario                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | Sovrascrive il tipo di carattere principale per il testo tradotto. Opzioni: 'serif' per caratteri con grazie, 'sans-serif' per caratteri senza grazie, 'script' per caratteri corsivi/stilizzati. Se non specificato, utilizza la selezione automatica del carattere basata sulle proprietà del testo originale. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | Non generare file PDF bilingui                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | Non generare file PDF monolingua                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | Modello di carattere per identificare il testo della formula                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | Modello di caratteri per identificare il testo della formula                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | Forza la divisione di righe brevi in paragrafi diversi                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | Fattore di soglia di divisione per righe brevi                                                 |                                                                                                                      |
| `--skip-clean`                  | Salta il passaggio di pulizia del PDF                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        | Priorità alla pagina tradotta in modalità PDF doppia                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | Disabilita la traduzione del testo formattato                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | Abilita tutte le opzioni di miglioramento della compatibilità                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | Utilizza la modalità pagine alternate per PDF duali                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | Modalità di output della filigrana per file PDF                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | Numero massimo di pagine per parte per la traduzione divisa                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | Tradurre il testo della tabella (sperimentale)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | Salta il rilevamento dei documenti scansionati                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | Forza il testo tradotto a essere nero e aggiunge uno sfondo bianco                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | Abilita la soluzione automatica OCR. Se un documento viene rilevato come pesantemente scansionato, questo tenterà di abilitare l'elaborazione OCR e salterà ulteriori rilevamenti di scansione. Consultare la documentazione per i dettagli. (predefinito: False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page` | Includi solo le pagine tradotte nel PDF di output. Efficace solo quando viene utilizzato --pages. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | Glossario personalizzato per la traduzione.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |
| `--save-auto-extracted-glossary`| salva il glossario estratto automaticamente.                                                | `pdf2zh example.pdf --save-auto-extracted-glossary`                                                                   |
| `--no-merge-alternating-line-numbers` | Disabilita l'unione dei numeri di riga alternati e dei paragrafi di testo nei documenti con numeri di riga | `pdf2zh example.pdf --no-merge-alternating-line-numbers` |
| `--no-remove-non-formula-lines` | Disabilita la rimozione delle righe non di formula all'interno delle aree di paragrafo                          | `pdf2zh example.pdf --no-remove-non-formula-lines`                                                                    |
| `--non-formula-line-iou-threshold` | Imposta la soglia IoU per identificare le righe non formule (0.0-1.0)                     | `pdf2zh example.pdf --non-formula-line-iou-threshold 0.85`                                                            |
| `--figure-table-protection-threshold` | Imposta la soglia di protezione per figure e tabelle (0.0-1.0). Le righe all'interno di figure/tabelle non verranno elaborate | `pdf2zh example.pdf --figure-table-protection-threshold 0.95` |
| `--skip-formula-offset-calculation` | Salta il calcolo dell'offset della formula durante l'elaborazione | `pdf2zh example.pdf --skip-formula-offset-calculation`                                                                |


##### Argomenti GUI

| Opzione                          | Funzione                               | Esempio                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Abilita la modalità di condivisione    | `pdf2zh --gui --share`                          |
| `--auth-file`                   | Percorso del file di autenticazione        | `pdf2zh --gui --auth-file /percorso`                |
| `--welcome-page`                | Percorso del file html di benvenuto          | `pdf2zh --gui --welcome-page /percorso`             |
| `--enabled-services`            | Servizi di traduzione abilitati           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Disabilita l'input sensibile della GUI            | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | Disabilita il salvataggio automatico della configurazione | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | Porta WebUI                             | `pdf2zh --gui --server-port 7860`               |

[⬆️ Torna all'inizio](#toc)

---

#### Guida alla configurazione del limite di velocità

Quando si utilizzano i servizi di traduzione, una corretta configurazione del limite di velocità è fondamentale per evitare errori API e ottimizzare le prestazioni. Questa guida spiega come configurare i parametri `--qps` e `--pool-max-worker` in base alle diverse limitazioni del servizio upstream.

> [!TIP]
>
> Si consiglia che il pool_size non superi 1000. Se il pool_size calcolato con il seguente metodo supera 1000, si prega di utilizzare 1000.

##### Limitazione della velocità RPM (Richieste al minuto)

Quando il servizio upstream ha limitazioni RPM, utilizza il seguente calcolo:

**Formula di calcolo:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Il fattore 10 è un coefficiente empirico che generalmente funziona bene per la maggior parte degli scenari.

**Esempio:**
Se il tuo servizio di traduzione ha un limite di 600 RPM:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Limitazione delle connessioni simultanee

Quando il servizio upstream ha limitazioni di connessione simultanea (come il servizio ufficiale GLM), utilizza questo approccio:

**Formula di calcolo:**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Esempio:**
Se il tuo servizio di traduzione consente 50 connessioni simultanee:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Best Practices

> [!TIP]
> - Inizia sempre con valori conservativi e aumenta gradualmente se necessario
> - Monitora i tempi di risposta del tuo servizio e i tassi di errore
> - Servizi diversi possono richiedere strategie di ottimizzazione diverse
> - Considera il tuo caso d'uso specifico e la dimensione del documento quando imposti questi parametri


[⬆️ Torna all'inizio](#toc)

---

#### Traduzione parziale

Utilizzare il parametro `--pages` per tradurre una parte di un documento.

- Se i numeri di pagina sono consecutivi, puoi scriverlo così:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` include tutte le pagine successive alla pagina 25. Se il tuo documento ha 100 pagine, questo è equivalente a `25-100`.
> 
> Allo stesso modo, `-25` include tutte le pagine precedenti alla pagina 25, che è equivalente a `1-25`.

- Se le pagine non sono consecutive, puoi usare una virgola `,` per separarle.

Ad esempio, se vuoi tradurre la prima e la terza pagina, puoi usare il seguente comando:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Se le pagine includono sia intervalli consecutivi che non consecutivi, puoi anche collegarli con una virgola, in questo modo:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Questo comando tradurrà la prima pagina, la terza pagina, le pagine da 10 a 20 e tutte le pagine da 25 alla fine.


[⬆️ Torna all'inizio](#toc)

---

#### Specificare le lingue di origine e di destinazione

Vedi [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Torna all'inizio](#toc)

---

#### Tradurre con eccezioni

Utilizza le espressioni regolari per specificare i caratteri e i font delle formule che devono essere preservati:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Preserva i caratteri `Latex`, `Mono`, `Code`, `Italic`, `Symbol` e `Math` per impostazione predefinita:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Torna all'inizio](#toc)

---

#### Prompt personalizzato

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Prompt di sistema personalizzato per la traduzione. Viene principalmente utilizzato per aggiungere l'istruzione '/no_think' di Qwen 3 nel prompt.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Torna all'inizio](#toc)

---

#### Configurazione personalizzata

Esistono diversi modi per modificare e importare il file di configurazione.

> [!NOTE]
> **Gerarchia dei file di configurazione**
>
> Quando si modifica lo stesso parametro utilizzando metodi diversi, il software applicherà le modifiche secondo l'ordine di priorità riportato di seguito.
>
> Le modifiche con priorità più alta sovrascriveranno quelle con priorità più bassa.
>
> **cli/gui > env > file di configurazione utente > file di configurazione predefinito**

- Modifica della configurazione tramite **Argomenti della riga di comando**

Nella maggior parte dei casi, puoi passare direttamente le impostazioni desiderate attraverso gli argomenti della riga di comando. Per ulteriori informazioni, consulta [Argomenti della riga di comando](#cmd).

Ad esempio, se desideri abilitare una finestra GUI, puoi utilizzare il seguente comando:

```bash
pdf2zh_next --gui
```

- Modifica della configurazione tramite **Variabili d'ambiente**

Puoi sostituire il `--` negli argomenti della riga di comando con `PDF2ZH_`, collegare i parametri utilizzando `=` e sostituire `-` con `_` come variabili d'ambiente.

Ad esempio, se vuoi abilitare una finestra GUI, puoi utilizzare il seguente comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- File di **Configurazione** specificato dall'utente

È possibile specificare un file di configurazione utilizzando l'argomento della riga di comando seguente:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Se non sei sicuro del formato del file di configurazione, consulta il file di configurazione predefinito descritto di seguito.

- **File di configurazione predefinito**

Il file di configurazione predefinito si trova in `~/.config/pdf2zh`.  
Si prega di non modificare i file di configurazione nella directory `default`.  
Si consiglia vivamente di fare riferimento al contenuto di questo file di configurazione e utilizzare **Configurazione personalizzata** per implementare il proprio file di configurazione.

> [!TIP]
> - Per impostazione predefinita, pdf2zh 2.0 salva automaticamente la configurazione corrente in `~/.config/pdf2zh/config.v3.toml` ogni volta che si fa clic sul pulsante di traduzione nella GUI. Questo file di configurazione verrà caricato per impostazione predefinita al prossimo avvio.
> - I file di configurazione nella directory `default` vengono generati automaticamente dal programma. È possibile copiarli per modificarli, ma si prega di non modificarli direttamente.
> - I file di configurazione possono includere numeri di versione come "v2", "v3", ecc. Questi sono **numeri di versione del file di configurazione**, **non** il numero di versione di pdf2zh stesso.


[⬆️ Torna all'inizio](#toc)

---

#### Salta pulizia

Quando questo parametro è impostato su True, il passaggio di pulizia del PDF verrà saltato, il che può migliorare la compatibilità ed evitare alcuni problemi di elaborazione dei caratteri.

Utilizzo:

```bash
pdf2zh_next example.pdf --skip-clean
```

Oppure utilizzando le variabili d'ambiente:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Quando `--enhance-compatibility` è abilitato, Salta pulizia viene automaticamente abilitato.

---

#### Cache delle traduzioni

PDFMathTranslate memorizza nella cache i testi tradotti per aumentare la velocità ed evitare chiamate API non necessarie per contenuti identici. Puoi utilizzare l'opzione `--ignore-cache` per ignorare la cache delle traduzioni e forzare una nuova traduzione.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Torna all'inizio](#toc)

---

#### Distribuzione come servizi pubblici

Quando si distribuisce un'interfaccia grafica pdf2zh su servizi pubblici, è necessario modificare il file di configurazione come descritto di seguito.

> [!WARNING]
>
> Questo progetto non è stato sottoposto a un controllo professionale per la sicurezza e potrebbe contenere vulnerabilità. Si prega di valutare i rischi e adottare le necessarie misure di sicurezza prima di distribuire su reti pubbliche.


> [!TIP]
> - Quando si distribuisce pubblicamente, sia disable_gui_sensitive_input che disable_config_auto_save dovrebbero essere abilitati.
> - Separare i diversi servizi disponibili con *virgole inglesi* <kbd>,</kbd> .

Una configurazione utilizzabile è la seguente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Torna all'inizio](#toc)

---

#### Autenticazione e pagina di benvenuto

Quando si utilizza Autenticazione e pagina di benvenuto per specificare quale utente può utilizzare Web UI e personalizzare la pagina di accesso:

esempio auth.txt
Ogni riga contiene due elementi, nome utente e password, separati da una virgola.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

esempio welcome.html

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
> La pagina di benvenuto funzionerà solo se il file di autenticazione non è vuoto.
> Se il file di autenticazione è vuoto, non ci sarà alcuna autenticazione. :)

Una configurazione utilizzabile è la seguente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Torna all'inizio](#toc)

---

#### Supporto del glossario

PDFMathTranslate supporta la tabella del glossario. Il file delle tabelle del glossario dovrebbe essere un file `csv`.
Ci sono tre colonne nel file. Ecco un file di glossario demo:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自动 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |


Per gli utenti CLI:
È possibile utilizzare più file per il glossario. E i diversi file dovrebbero essere separati da `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Per gli utenti di WebUI:

Ora puoi caricare il tuo file del glossario. Dopo aver caricato il file, puoi verificarlo cliccando sul suo nome e il contenuto verrà visualizzato di seguito.

[⬆️ Torna all'inizio](#toc)

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>