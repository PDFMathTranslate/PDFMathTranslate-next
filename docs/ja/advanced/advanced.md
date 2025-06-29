[**高度な設定**](./introduction.md) > **高度な設定** _(現在)_

---

<h3 id="toc">目次</h3>

- [コマンドライン引数](#コマンドライン引数)
  - [引数](#引数)
  - [GUI引数](#gui引数)
- [部分翻訳](#部分翻訳)
- [ソース言語とターゲット言語の指定](#ソース言語とターゲット言語の指定)
- [例外付き翻訳](#例外付き翻訳)
- [カスタムプロンプト](#カスタムプロンプト)
- [カスタム設定](#カスタム設定)
- [クリーニングのスキップ](#クリーニングのスキップ)
- [翻訳キャッシュ](#翻訳キャッシュ)
- [公開サービスとしてのデプロイ](#公開サービスとしてのデプロイ)
- [認証とウェルカムページ](#認証とウェルカムページ)
- [用語集サポート](#用語集サポート)

---

#### コマンドライン引数

コマンドラインで翻訳コマンドを実行し、現在の作業ディレクトリに翻訳済みドキュメント `example-mono.pdf` とバイリンガルドキュメント `example-dual.pdf` を生成します。デフォルトの翻訳サービスとしてGoogleを使用します。その他のサポート翻訳サービスは[こちら](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services)で確認できます。

<img src="./../images/cmd_light.svg" width="580px"  alt="cmd"/>

以下の表に、すべての高度なオプションを参考としてリストアップします:

##### 引数

| オプション                          | 機能                                                                               | 例                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | ローカルPDFファイルのパス                                                                    | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | オンラインファイル                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | ファイルの出力ディレクトリ                                                             | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | 翻訳に[**特定のサービス**](./翻訳サービスドキュメント.md)を使用する | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | ヘルプメッセージを表示して終了                                                             | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | 設定ファイルへのパス                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | 進捗レポートの間隔（秒単位）                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | デバッグログレベルを使用                                                                 | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | GUIと対話する                                                                      | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | 必要なアセットをダウンロードして検証した後、終了する                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | 指定されたディレクトリにオフラインアセットパッケージを生成する                             | `pdf2zh example.pdf --generate-offline-assets /path`                                                                 |
| `--restore-offline-assets`      | 指定されたディレクトリからオフラインアセットパッケージを復元する                            | `pdf2zh example.pdf --restore-offline-assets /path`                                                                  |
| `--version`                     | バージョンを表示して終了                                                                 | `pdf2zh --version`                                                                                                   |
| `--pages`                       | ドキュメントの部分翻訳                                                           | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | ソース言語のコード                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | ターゲット言語のコード                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | 翻訳する最小テキスト長                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | ドキュメントレイアウト分析用のRPCサービスホストアドレス                                  |                                                                                                                      |
| `--qps`                         | 翻訳サービスのQPS制限                                                      | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | 翻訳キャッシュを無視する                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | 翻訳用のカスタムシステムプロンプト。Qwen 3の`/no_think`で使用されます                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | 翻訳プールの最大ワーカー数。設定されていない場合、qpsをワーカー数として使用します | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | 自動用語集抽出を無効化                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | 翻訳テキストのプライマリフォントファミリーを上書きします。選択肢: 'serif'（セリフ体）、'sans-serif'（サンセリフ体）、'script'（スクリプト/イタリック体）。指定しない場合、元のテキストのプロパティに基づいて自動的にフォントが選択されます。 | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | バイリンガルPDFファイルを出力しない                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | 単一言語のPDFファイルを出力しない                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | 数式テキストを識別するためのフォントパターン                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | 数式テキストを識別するための文字パターン                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | 短い行を強制的に異なる段落に分割する                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | 短い行の分割閾値係数                                                 |                                                                                                                      |
| `--skip-clean`                  | PDFのクリーニングステップをスキップ                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        | デュアルPDFモードで翻訳ページを優先的に配置                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | リッチテキスト翻訳を無効にする                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | すべての互換性向上オプションを有効にする                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | デュアルPDF用に交互ページモードを使用する                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | PDFファイルの透かし出力モード                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | 分割翻訳におけるパートごとの最大ページ数                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | テーブルテキストを翻訳（実験的機能）                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | スキャンされた文書の検出をスキップ                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | 翻訳されたテキストを強制的に黒色にし、白い背景を追加する                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | 自動OCR回避策を有効にします。文書が重度にスキャンされていると検出された場合、OCR処理を有効にし、さらなるスキャン検出をスキップしようとします。詳細はドキュメントを参照してください。（デフォルト: False） | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page`| 出力PDFに翻訳済みのページのみを含めます。--pagesが使用されている場合にのみ有効です。 | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | 翻訳用のカスタム用語集。                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |

##### GUI引数

| オプション                          | 機能                               | 例                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | 共有モードを有効化                    | `pdf2zh --gui --share`                          |
| `--auth-file`                   | 認証ファイルのパス        | `pdf2zh --gui --auth-file /path`                |
| `--welcome-page`                | ウェルカムページのHTMLファイルのパス          | `pdf2zh --gui --welcome-page /path`             |
| `--enabled-services`            | 有効化された翻訳サービス           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | GUIの機密入力無効化            | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | 設定の自動保存無効化 | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | WebUIポート                             | `pdf2zh --gui --server-port 7860`               |

[⬆️ トップに戻る](#toc)

---

#### 部分翻訳

`--pages` パラメータを使用して、ドキュメントの一部を翻訳します。

- ページ番号が連続している場合、以下のように記述できます:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` は25ページ以降のすべてのページを含みます。ドキュメントが100ページある場合、これは `25-100` と同じです。
> 
> 同様に、`-25` は25ページより前のすべてのページを含み、これは `1-25` と同じです。

- ページが連続していない場合は、カンマ `,` を使用してページを区切ることができます。

たとえば、最初と3番目のページを翻訳したい場合は、次のコマンドを使用できます：

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- ページに連続した範囲と非連続した範囲の両方が含まれている場合、それらをカンマで接続することもできます。例：

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

このコマンドは、最初のページ、3ページ目、10～20ページ、および25ページ以降のすべてのページを翻訳します。

[⬆️ トップに戻る](#toc)

---

#### ソース言語とターゲット言語を指定する

[Google 言語コード](https://developers.google.com/admin-sdk/directory/v1/languages)、[DeepL 言語コード](https://developers.deepl.com/docs/resources/supported-languages)を参照してください

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ トップに戻る](#toc)

---

#### 例外付き翻訳

正規表現を使用して、保持する必要のある数式フォントと文字を指定します：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

デフォルトで `Latex`、`Mono`、`Code`、`Italic`、`Symbol`、`Math` フォントを保持します:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ トップに戻る](#toc)

---

#### カスタムプロンプト

<!-- Note: システムプロンプトは現在サポートされていません。詳細は[この変更](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637)をご覧ください。 -->

翻訳用のカスタムシステムプロンプト。主にQwen 3の'/no_think'指示をプロンプトに追加するために使用されます。

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ トップに戻る](#toc)

---

#### カスタム設定

設定ファイルを変更およびインポートする方法は複数あります。

> [!NOTE]
> **設定ファイルの階層**
>
> 同じパラメータを異なる方法で変更する場合、ソフトウェアは以下の優先順位に従って変更を適用します。
>
> 上位の変更は下位の変更を上書きします。
>
> **cli/gui > env > ユーザー設定ファイル > デフォルト設定ファイル**

- **コマンドライン引数**による設定変更

ほとんどの場合、コマンドライン引数を通じて直接設定を指定できます。詳細は[コマンドライン引数](#cmd)を参照してください。

例えば、GUIウィンドウを有効にするには、次のコマンドを使用します:

```bash
pdf2zh_next --gui
```

- **環境変数**による設定変更

<!-- TODO ここに環境変数の図を配置 -->

コマンドライン引数の `--` を `PDF2ZH_` に置き換え、パラメータを `=` で接続し、`-` を `_` に置き換えて環境変数として使用できます。

例えば、GUIウィンドウを有効にするには、次のコマンドを使用できます:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../images/ev_light.svg" width="580px"  alt="env"/>

- ユーザー指定の **設定ファイル**

以下のコマンドライン引数を使用して設定ファイルを指定できます:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

設定ファイルの形式がわからない場合は、以下のデフォルト設定ファイルを参照してください。

- **デフォルト設定ファイル**

デフォルト設定ファイルは `~/.config/pdf2zh` にあります。
`default` ディレクトリ内の設定ファイルは変更しないでください。
この設定ファイルの内容を参照し、**ユーザー指定設定ファイル**を使用して独自の設定ファイルを実装することを強く推奨します。

> [!TIP]
> - デフォルトでは、pdf2zh 2.0はGUIで翻訳ボタンをクリックするたびに現在の設定を`~/.config/pdf2zh/config.v3.toml`に自動保存します。この設定ファイルは次回起動時にデフォルトで読み込まれます。
> - `default`ディレクトリ内の設定ファイルはプログラムによって自動生成されます。修正用にコピーすることは可能ですが、直接編集しないでください。
> - 設定ファイルには「v2」「v3」などのバージョン番号が含まれる場合があります。これらは**設定ファイルのバージョン番号**であり、pdf2zh自体のバージョン番号では**ありません**。

[⬆️ トップに戻る](#toc)

---

#### クリーンをスキップ

このパラメータをTrueに設定すると、PDFのクリーニングステップがスキップされ、互換性が向上し、一部のフォント処理の問題を回避できます。

使い方:

```bash
pdf2zh_next example.pdf --skip-clean
```

または環境変数を使用する:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> `--enhance-compatibility` が有効な場合、Skip clean は自動的に有効になります。

---

#### 翻訳キャッシュ

PDFMathTranslateは翻訳済みのテキストをキャッシュし、同じ内容に対する不必要なAPI呼び出しを避けつつ速度を向上させます。`--ignore-cache`オプションを使用すると、翻訳キャッシュを無視して強制的に再翻訳を行えます。

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ トップに戻る](#toc)

---

#### 公開サービスとしてのデプロイ

公開サービスでpdf2zh GUIをデプロイする場合、以下のように設定ファイルを変更する必要があります。

> [!TIP]
> - 公開デプロイ時には、`disable_gui_sensitive_input` と `disable_config_auto_save` の両方を有効にする必要があります。
> - 利用可能な異なるサービスは*英語のカンマ* <kbd>,</kbd> で区切ってください。

使用可能な設定例は以下の通りです：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ トップに戻る](#toc)

---

#### 認証とウェルカムページ

認証とウェルカムページを使用して、どのユーザーがWeb UIを使用するかを指定し、ログインページをカスタマイズする場合:

例 auth.txt
各行には、ユーザー名とパスワードの2つの要素が含まれ、カンマで区切られています。

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
> 認証ファイルが空白でない場合のみ、ウェルカムページが機能します。
> 認証ファイルが空白の場合、認証は行われません。 :)

使用可能な設定は以下の通りです：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ トップに戻る](#toc)

---

#### 用語集サポート

PDFMathTranslateは用語集テーブルをサポートしています。用語集テーブルのファイルは`csv`形式である必要があります。  
ファイルには3つの列があります。以下はデモ用の用語集ファイルです:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自動 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |

CLIユーザー向け:
複数のファイルを用語集として使用できます。異なるファイルは `,` で区切る必要があります。

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

WebUIユーザー向け:

独自の用語集ファイルをアップロードできるようになりました。ファイルをアップロード後、ファイル名をクリックすると内容が下に表示されますので確認できます。

[⬆️ トップに戻る](#toc)

<div align="right"> 
<h6><small>このページの一部のコンテンツはGPTによって翻訳されており、エラーが含まれている可能性があります。</small></h6>