# プロジェクトへの貢献

> [!CAUTION]
>
> 現在のプロジェクトメンテナーはドキュメントの自動国際化を研究中です。そのため、ドキュメントの国際化/翻訳に関連するPRは一切受け付けません！
>
> ドキュメントの国際化/翻訳に関連するPRを提出しないでください！

このプロジェクトに興味を持っていただきありがとうございます！貢献を始める前に、以下のガイドラインを読んで、あなたの貢献がスムーズに受け入れられるようにしてください。

## 受け付けない貢献の種類

1. ドキュメントの国際化/翻訳
2. HTTP APIなどのコアインフラストラクチャに関する貢献
3. 「No help needed」と明示的にマークされたIssue（[Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate/issues)リポジトリ内のIssueを含む）。
4. メンテナーが不適切と判断したその他の貢献。

上記の種類に関連するPRは提出しないでください。

## 貢献プロセス

1. このリポジトリをフォークし、ローカルにクローンします。
2. 新しいブランチを作成します: `git checkout -b feature/<feature-name>`.
3. 開発を行い、コードが要件を満たしていることを確認します。
4. コードをコミットします:
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```

5. リポジトリにプッシュ: `git push origin feature/<feature-name>`  
6. GitHubでPRを作成し、詳細な説明を記入して [@awwaawwa](https://github.com/awwaawwa) にレビューを依頼  
7. すべての自動チェックが通過することを確認

> [!TIP]
>
> 開発が完全に完了するまで待つ必要はありません。早期にPRを作成することで、実装をレビューし、提案を提供することができます。
>
> ソースコードや関連事項について質問がある場合は、メンテナーにaw@funstory.aiまでご連絡ください。
>
> バージョン2.0のリソースファイルは[BabelDOC](https://github.com/funstory-ai/BabelDOC)と共有されています。関連リソースをダウンロードするコードはBabelDOCにあります。新しいリソースファイルを追加したい場合は、BabelDOCのメンテナーにaw@funstory.aiまでご連絡ください。

## 基本要件

<h4 id="sop">1. ワークフロー</h4>

- 必ず `main` ブランチからフォークし、フォークしたブランチで開発を行ってください。
   - プルリクエスト（PR）を提出する際は、変更内容の詳細な説明を提供してください。
   - PRが自動チェックに合格しない場合（`checks failed` と赤い十字マークが表示される場合）、対応する `details` を確認し、提出内容を修正して新しいPRがすべてのチェックに合格するようにしてください。


<h4 id="dev&test">2. 開発とテスト</h4>

- 開発とテストには `pip install -e .` コマンドを使用してください。

<h4 id="format">3. コードフォーマット</h4>

- `pre-commit` ツールを設定し、コードフォーマット用に `black` と `flake8` を有効にします。


<h4 id="requpdate">4. 依存関係の更新</h4>

- 新しい依存関係を導入する場合は、`pyproject.toml` ファイル内の依存関係リストを適時更新してください。

<h4 id="docupdate">5. ドキュメント更新</h4>

- 新しいコマンドラインオプションを追加する場合、`README.md`ファイルのすべての言語バージョンにあるコマンドラインオプションのリストを適宜更新してください。

<h4 id="commitmsg">6. コミットメッセージ</h4>

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) を使用してください。例: `feat(translator): add openai`。

<h4 id="codestyle">7. コーディングスタイル</h4>

- 提出するコードが基本的なコーディングスタイル標準に準拠していることを確認してください。
   - 変数名にはスネークケース（snake_case）またはキャメルケース（camelCase）を使用してください。

<h4 id="doctypo">8. ドキュメントフォーマット</h4>

- `README.md` のフォーマットについては、[中国語コピーライティングガイドライン](https://github.com/sparanoid/chinese-copywriting-guidelines) に従ってください。
   - 英語と中国語のドキュメントは常に最新に保つようにしてください。他の言語のドキュメント更新は任意です。

## 翻訳エンジンの追加

1. `pdf2zh/config/translate_engine_model.py` ファイルに新しい翻訳エンジン設定クラスを追加します。
2. 同じファイル内の `TRANSLATION_ENGINE_SETTING_TYPE` 型エイリアスに、新しい翻訳エンジン設定クラスのインスタンスを追加します。
3. `pdf2zh/translator/translator_impl` フォルダに新しい翻訳エンジン実装クラスを追加します。

> [!NOTE]
>
> このプロジェクトは、RPS（1秒あたりのリクエスト数）が4未満の翻訳エンジンをサポートする意図はありません。そのようなエンジンのサポートを提出しないでください。

## プロジェクト構造

- **config folder**: 設定システム。
- **translator folder**: 翻訳関連の実装。
- **gui.py**: GUIインターフェースを提供。
- **const.py**: いくつかの定数。
- **main.py**: コマンドラインツールを提供。
- **high_level.py**: BabelDOCベースの高レベルインターフェース。
- **http_api.py**: HTTP APIを提供（未開始）。

## お問い合わせ

ご質問がある場合は、Issueを通じてフィードバックを提出するか、Telegramグループに参加してください。ご協力ありがとうございます！

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) は、このプロジェクトの積極的な貢献者に対して月額Proメンバーシップコードをスポンサーしています。詳細については、[BabelDOC/PDFMathTranslate 貢献者報酬規則](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/)をご覧ください。

<div align="right"> 
<h6><small>このページの一部のコンテンツはGPTによって翻訳されており、エラーが含まれている可能性があります。</small></h6>