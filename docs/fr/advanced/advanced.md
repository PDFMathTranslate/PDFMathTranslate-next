[**Options avancées**](./introduction.md) > **Options avancées** _(actuel)_

---

<h3 id="toc">Table des matières</h3>

- [Arguments de ligne de commande](#arguments-de-ligne-de-commande)
- [Guide de configuration de la limitation de débit](#guide-de-configuration-de-la-limitation-de-débit)
- [Traduction partielle](#traduction-partielle)
- [Spécifier les langues source et cible](#spécifier-les-langues-source-et-cible)
- [Traduire avec exceptions](#traduire-avec-exceptions)
- [Invite personnalisée](#invite-personnalisée)
- [Configuration personnalisée](#configuration-personnalisée)
- [Ignorer le nettoyage](#ignorer-le-nettoyage)
- [Cache de traduction](#cache-de-traduction)
- [Déploiement en tant que services publics](#déploiement-en-tant-que-services-publics)
- [Authentification et page d'accueil](#authentification-et-page-daccueil)
- [Support de glossaire](#support-de-glossaire)

---

#### Arguments de ligne de commande

Exécutez la commande de traduction dans la ligne de commande pour générer le document traduit `example-mono.pdf` et le document bilingue `example-dual.pdf` dans le répertoire de travail actuel. Utilisez Google comme service de traduction par défaut. Plus de services de traduction supportés peuvent être trouvés [HERE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

Dans le tableau suivant, nous listons toutes les options avancées pour référence :

##### Arguments

| Option                          | Fonction                                                                               | Exemple                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Chemin local du fichier PDF                                                            | `pdf2zh ~/local.pdf`                                                                                                 |
| `liens`                         | Fichiers en ligne                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | Répertoire de sortie pour les fichiers                                                             | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | Utiliser un [**service spécifique**](./Documentation-of-Translation-Services.md) pour la traduction | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | Afficher le message d'aide et quitter                                                             | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | Chemin vers le fichier de configuration                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | Intervalle de rapport de progression en secondes                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | Utiliser le niveau de journalisation de débogage                                                                | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | Interagir avec l'interface graphique                                                                      | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | Télécharge et vérifie uniquement les ressources requises puis quitte                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | Générer un package d'assets hors ligne dans le répertoire spécifié                     | `pdf2zh example.pdf --generate-offline-assets /chemin`                                                                 |
| `--restore-offline-assets`      | Restaurer le package d'assets hors ligne depuis le répertoire spécifié                            | `pdf2zh example.pdf --restore-offline-assets /chemin`                                                                  |
| `--version`                     | Afficher la version puis quitter                                                                 | `pdf2zh --version`                                                                                                   |
| `--pages`                       | Traduction partielle du document                                                           | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | Le code de la langue source                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | Le code de la langue cible                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | Longueur minimale du texte à traduire                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | Adresse hôte du service RPC pour l'analyse de la mise en page des documents                                  |                                                                                                                      |
| `--qps`                         | Limite de QPS pour le service de traduction                                                      | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | Ignorer le cache de traduction                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | Invite système personnalisée pour la traduction. Utilisée pour `/no_think` dans Qwen 3                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | Nombre maximum de travailleurs pour le pool de traduction. Si non défini, utilisera le qps comme nombre de travailleurs | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | Désactiver l'extraction automatique du glossaire                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | Remplace la famille de police principale pour le texte traduit. Choix : 'serif' pour les polices serif, 'sans-serif' pour les polices sans-serif, 'script' pour les polices script/italiques. Si non spécifié, utilise une sélection automatique de police basée sur les propriétés du texte original. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | Ne pas générer de fichiers PDF bilingues                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | Ne pas générer de fichiers PDF monolingues                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | Modèle de police pour identifier le texte des formules                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | Modèle de caractères pour identifier le texte des formules                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | Forcer la division des lignes courtes en différents paragraphes                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | Facteur de seuil de division pour les lignes courtes                                                 |                                                                                                                      |
| `--skip-clean`                  | Ignorer l'étape de nettoyage du PDF                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        | Dans le mode PDF double, prioriser le placement de la page traduite                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | Désactiver la traduction de texte enrichi                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | Activer toutes les options d'amélioration de la compatibilité                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | Utiliser le mode pages alternées pour les PDF doubles                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | Mode de filigrane pour les fichiers PDF                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | Nombre maximum de pages par partie pour la traduction divisée                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | Traduire le texte des tableaux (expérimental)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | Ignorer la détection des documents scannés                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | Forcer le texte traduit à être noir et ajouter un fond blanc                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | Activer le contournement automatique de l'OCR. Si un document est détecté comme étant fortement scanné, cette option tentera d'activer le traitement OCR et ignorera toute détection de scan ultérieure. Voir la documentation pour plus de détails. (par défaut : False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page` | Inclure uniquement les pages traduites dans le PDF de sortie. Efficace uniquement lorsque --pages est utilisé. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | Glossaire personnalisé pour la traduction.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |
| `--save-auto-extracted-glossary`| enregistrer le glossaire extrait automatiquement.                                                | `pdf2zh example.pdf --save-auto-extracted-glossary`                                                                   |
| `--no-merge-alternating-line-numbers` | Désactive la fusion des numéros de ligne alternatifs et des paragraphes de texte dans les documents avec numéros de ligne | `pdf2zh example.pdf --no-merge-alternating-line-numbers` |
| `--no-remove-non-formula-lines` | Désactive la suppression des lignes non-formules dans les zones de paragraphe                          | `pdf2zh example.pdf --no-remove-non-formula-lines`                                                                    |
| `--non-formula-line-iou-threshold` | Définir le seuil IoU pour identifier les lignes non-formules (0.0-1.0)                     | `pdf2zh example.pdf --non-formula-line-iou-threshold 0.85`                                                            |
| `--figure-table-protection-threshold` | Définir le seuil de protection pour les figures et les tableaux (0.0-1.0). Les lignes à l'intérieur des figures/tableaux ne seront pas traitées | `pdf2zh example.pdf --figure-table-protection-threshold 0.95` |
| `--skip-formula-offset-calculation` | Ignorer le calcul du décalage des formules pendant le traitement | `pdf2zh example.pdf --skip-formula-offset-calculation`                                                                |


##### Arguments de l'interface graphique

| Option                          | Fonction                               | Exemple                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Activer le mode partage                | `pdf2zh --gui --share`                          |
| `--auth-file`                   | Chemin vers le fichier d'authentification        | `pdf2zh --gui --auth-file /chemin`                |
| `--welcome-page`                | Chemin vers le fichier HTML de bienvenue          | `pdf2zh --gui --welcome-page /chemin`             |
| `--enabled-services`            | Services de traduction activés           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Désactiver la saisie sensible de l'interface graphique | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | Désactiver l'enregistrement automatique de la configuration | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | Port de l'interface Web                             | `pdf2zh --gui --server-port 7860`               |

[⬆️ Retour en haut](#toc)

---

#### Guide de configuration des limites de débit

Lors de l'utilisation des services de traduction, une configuration appropriée des limites de débit est cruciale pour éviter les erreurs d'API et optimiser les performances. Ce guide explique comment configurer les paramètres `--qps` et `--pool-max-worker` en fonction des différentes limitations des services en amont.

> [!TIP]
>
> Il est recommandé que le pool_size ne dépasse pas 1000. Si le pool_size calculé par la méthode suivante dépasse 1000, veuillez utiliser 1000.

##### Limitation du taux RPM (Requêtes Par Minute)

Lorsque le service en amont a des limitations RPM, utilisez le calcul suivant :

**Formule de calcul :**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Le facteur de 10 est un coefficient empirique qui fonctionne généralement bien pour la plupart des scénarios.

### TEXTE ORIGINAL

**Exemple :**
Si votre service de traduction a une limite de 600 RPM :
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Limitation des connexions simultanées

Lorsque le service en amont a des limitations de connexions simultanées (comme le service officiel GLM), utilisez cette approche :

**Formule de calcul :**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Exemple :**
Si votre service de traduction autorise 50 connexions simultanées :
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Meilleures pratiques

> [!TIP]
> - Commencez toujours avec des valeurs conservatrices et augmentez-les progressivement si nécessaire
> - Surveillez les temps de réponse et les taux d'erreur de votre service
> - Différents services peuvent nécessiter différentes stratégies d'optimisation
> - Prenez en compte votre cas d'utilisation spécifique et la taille des documents lors de la configuration de ces paramètres


[⬆️ Retour en haut](#toc)

---

#### Traduction partielle

Utilisez le paramètre `--pages` pour traduire une partie d'un document.

- Si les numéros de page sont consécutifs, vous pouvez l'écrire comme ceci :

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` inclut toutes les pages après la page 25. Si votre document comporte 100 pages, cela équivaut à `25-100`.
> 
> De même, `-25` inclut toutes les pages avant la page 25, ce qui équivaut à `1-25`.

- Si les pages ne sont pas consécutives, vous pouvez utiliser une virgule `,` pour les séparer.

Par exemple, si vous souhaitez traduire la première et la troisième page, vous pouvez utiliser la commande suivante :

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Si les pages incluent à la fois des plages consécutives et non consécutives, vous pouvez également les connecter avec une virgule, comme ceci :

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Cette commande traduira la première page, la troisième page, les pages 10 à 20, et toutes les pages de 25 jusqu'à la fin.


[⬆️ Retour en haut](#toc)

---

#### Spécifier les langues source et cible

Voir [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Retour en haut](#toc)

---

#### Traduire avec exceptions

Utiliser des expressions régulières pour spécifier les polices de formule et les caractères à préserver :

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Conserve par défaut les polices `Latex`, `Mono`, `Code`, `Italic`, `Symbol` et `Math` :

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Retour en haut](#toc)

---

#### Invite personnalisée

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Invite système personnalisée pour la traduction. Elle est principalement utilisée pour ajouter l'instruction '/no_think' de Qwen 3 dans l'invite.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Retour en haut](#toc)

---

#### Configuration personnalisée

Il existe plusieurs façons de modifier et d'importer le fichier de configuration.

> [!NOTE]
> **Hiérarchie des fichiers de configuration**
>
> Lors de la modification d'un même paramètre à l'aide de différentes méthodes, le logiciel appliquera les modifications selon l'ordre de priorité ci-dessous.
>
> Les modifications de rang supérieur remplaceront celles de rang inférieur.
>
> **cli/gui > env > fichier de configuration utilisateur > fichier de configuration par défaut**

- Modification de la configuration via **Arguments de ligne de commande**

Pour la plupart des cas, vous pouvez directement passer vos paramètres souhaités via les arguments de ligne de commande. Veuillez vous référer à [Arguments de ligne de commande](#cmd) pour plus d'informations.

Par exemple, si vous souhaitez activer une fenêtre d'interface graphique, vous pouvez utiliser la commande suivante :

```bash
pdf2zh_next --gui
```

- Modification de la configuration via **Variables d'environnement**

Vous pouvez remplacer le `--` dans les arguments de ligne de commande par `PDF2ZH_`, connecter les paramètres en utilisant `=`, et remplacer `-` par `_` comme variables d'environnement.

Par exemple, si vous souhaitez activer une fenêtre d'interface graphique, vous pouvez utiliser la commande suivante :

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Fichier de **configuration** spécifié par l'utilisateur

Vous pouvez spécifier un fichier de configuration en utilisant l'argument de ligne de commande ci-dessous :

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Si vous n'êtes pas sûr du format du fichier de configuration, veuillez vous référer au fichier de configuration par défaut décrit ci-dessous.

- **Fichier de configuration par défaut**

Le fichier de configuration par défaut se trouve dans `~/.config/pdf2zh`.  
Veuillez ne pas modifier les fichiers de configuration dans le répertoire `default`.  
Il est fortement recommandé de se référer au contenu de ce fichier de configuration et d'utiliser **Configuration personnalisée** pour implémenter votre propre fichier de configuration.

> [!TIP]
> - Par défaut, pdf2zh 2.0 enregistre automatiquement la configuration actuelle dans `~/.config/pdf2zh/config.v3.toml` chaque fois que vous cliquez sur le bouton de traduction dans l'interface graphique. Ce fichier de configuration sera chargé par défaut au prochain démarrage.
> - Les fichiers de configuration dans le répertoire `default` sont générés automatiquement par le programme. Vous pouvez les copier pour les modifier, mais veuillez ne pas les modifier directement.
> - Les fichiers de configuration peuvent inclure des numéros de version tels que "v2", "v3", etc. Ce sont **des numéros de version des fichiers de configuration**, **et non** le numéro de version de pdf2zh lui-même.


[⬆️ Retour en haut](#toc)

---

#### Ignorer le nettoyage

Lorsque ce paramètre est défini sur True, l'étape de nettoyage du PDF sera ignorée, ce qui peut améliorer la compatibilité et éviter certains problèmes de traitement des polices.

Utilisation :

```bash
pdf2zh_next example.pdf --skip-clean
```

Ou en utilisant des variables d'environnement :

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Lorsque `--enhance-compatibility` est activé, Ignorer le nettoyage est automatiquement activé.

---

#### Cache de traduction

PDFMathTranslate met en cache les textes traduits pour augmenter la vitesse et éviter les appels API inutiles pour les mêmes contenus. Vous pouvez utiliser l'option `--ignore-cache` pour ignorer le cache de traduction et forcer une nouvelle traduction.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Retour en haut](#toc)

---

#### Déploiement en tant que services publics

Lors du déploiement d'une interface graphique pdf2zh sur des services publics, vous devez modifier le fichier de configuration comme décrit ci-dessous.

> [!WARNING]
>
> Ce projet n'a pas été audité professionnellement pour la sécurité et peut contenir des vulnérabilités de sécurité. Veuillez évaluer les risques et prendre les mesures de sécurité nécessaires avant de déployer sur des réseaux publics.


> [!TIP]
> - Lors d'un déploiement public, disable_gui_sensitive_input et disable_config_auto_save doivent tous deux être activés.
> - Séparez les différents services disponibles avec des *virgules anglaises* <kbd>,</kbd> .

Une configuration utilisable est la suivante :

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Retour en haut](#toc)

---

#### Authentification et page d'accueil

Lors de l'utilisation de l'Authentification et de la page d'accueil pour spécifier quel utilisateur doit utiliser l'interface Web et personnaliser la page de connexion :

exemple auth.txt
Chaque ligne contient deux éléments, le nom d'utilisateur et le mot de passe, séparés par une virgule.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

exemple welcome.html

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
> La page d'accueil fonctionnera uniquement si le fichier d'authentification n'est pas vide.
> Si le fichier d'authentification est vide, il n'y aura pas d'authentification. :)

Une configuration utilisable est la suivante :

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Retour en haut](#toc)

---

#### Prise en charge du glossaire

PDFMathTranslate prend en charge la table de glossaire. Le fichier de tables de glossaire doit être un fichier `csv`.
Il y a trois colonnes dans le fichier. Voici un exemple de fichier de glossaire :

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | ML automatique  | fr   |
| a,a    | a       | fr   |
| "      | "       | fr   |


Pour les utilisateurs de la ligne de commande :
Vous pouvez utiliser plusieurs fichiers pour le glossaire. Et les différents fichiers doivent être séparés par `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Pour les utilisateurs de WebUI :

Vous pouvez maintenant télécharger votre propre fichier de glossaire. Après avoir téléchargé le fichier, vous pouvez le consulter en cliquant sur son nom et le contenu s'affichera ci-dessous.

[⬆️ Retour en haut](#toc)

<div align="right"> 
<h6><small>Une partie du contenu de cette page a été traduite par GPT et peut contenir des erreurs.</small></h6>