# Contributing to the Project

> [!CAUTION]
>
> The current project maintainers are researching automated documentation internationalization. Therefore, any PRs related to documentation internationalization/translation will NOT be accepted!
>
> Please do NOT submit PRs related to documentation internationalization/translation!

Thank you for your interest in this project! Before you start contributing, please take some time to read the following guidelines to ensure your contribution can be smoothly accepted.

## Types of Contributions Not Accepted

1. Documentation internationalization/translation
2. Contributions related to core infrastructure, such as HTTP API, etc.
3. Issues explicitly marked as "No help needed" (including issues in the [Byaidu/PDFMathTranslate](Byaidu/PDFMathTranslate) and the [PDFMathTranslate/PDFMathTranslate-next](PDFMathTranslate/PDFMathTranslate-next) repository).
4. Other contributions deemed inappropriate by the maintainers.
5. Contributing documentation, but changing the documentation in languages other than English.
6. PRs that require modifying PDF files.
7. PRs that modify the `pdf2zh_next/gui_translation.yaml` file.

Please do NOT submit PRs related to the above types.

> [!NOTE]
>
> If you want to contribute documentation, please **only modify the English version of the documentation**. Other language versions are translated by contributors themselves.

## Contribution Process

1. Fork this repository and clone it locally.
2. Create a new branch: `git checkout -b feature/<feature-name>`.
3. Develop and ensure your code meets the requirements.
4. Commit your code:
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```
5. Push to your repository: `git push origin feature/<feature-name>`.
6. Create a PR on GitHub, provide a detailed description, and request a review from [@awwaawwa](https://github.com/awwaawwa).
7. Ensure all automated checks pass.

> [!TIP]
>
> You do not need to wait until your development is fully complete to create a PR. Creating one early allows us to review your implementation and provide suggestions.
>
> If you have any questions about the source code or related matters, please contact the maintainer at aw@funstory.ai.
>
> Resource files for version 2.0 are shared with [BabelDOC](https://github.com/funstory-ai/BabelDOC). The code for downloading related resources is in BabelDOC. If you want to add new resource files, please contact the BabelDOC maintainer at aw@funstory.ai.

## Basic Requirements

<h4 id="sop">1. Workflow</h4>

   - Please fork from the `main` branch and develop on your forked branch.
   - When submitting a Pull Request (PR), provide a detailed description of your changes.
   - If your PR does not pass automated checks (indicated by `checks failed` and a red cross), please review the corresponding `details` and modify your submission to ensure the new PR passes all checks.


<h4 id="dev&test">2. Development and Testing</h4>

   - Use the command `pip install -e .` for development and testing.


<h4 id="format">3. Code Formatting</h4>

   - Configure the `pre-commit` tool and enable `black` and `flake8` for code formatting.


<h4 id="requpdate">4. Dependency Updates</h4>

   - If you introduce new dependencies, please update the dependency list in the `pyproject.toml` file in a timely manner.


<h4 id="docupdate">5. Documentation Updates</h4>

   - If you add new command-line options, please update the list of command-line options in all language versions of the `README.md` file accordingly.


<h4 id="commitmsg">6. Commit Messages</h4>

   - Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), for example: `feat(translator): add openai`.


<h4 id="codestyle">7. Coding Style</h4>

   - Ensure your submitted code adheres to basic coding style standards.
   - Use either snake_case or camelCase for variable naming.


<h4 id="doctypo">8. Documentation Formatting</h4>

   - For `README.md` formatting, please follow the [Chinese Copywriting Guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines).
   - Ensure that both English and Chinese documentation are always up to date; other language documentation updates are optional.

## Adding a Translation Engine

1. Add a new translator configuration class in the `pdf2zh/config/translate_engine_model.py` file.
2. Add an instance of the new translator configuration class to the `TRANSLATION_ENGINE_SETTING_TYPE` type alias in the same file.
3. Add the new translator implementation class in the `pdf2zh/translator/translator_impl` folder.

> [!NOTE]
>
> This project does not intend to support any translation engines with an RPS (requests per second) lower than 4. Please do not submit support for such engines.
> The following types of translators will also not be integrated:
> - Translators that have been discontinued by upstream maintainers (such as deeplx)
> - Translators with large dependencies (such as those depending on pytorch)
> - Unstable translators
> - Translator Based on Reverse Engineering API
>
> When you are unsure whether a translator meets the requirements, you can send an issue to discuss with the maintainers.

## Project Structure

- **config folder**: Configuration system.
- **translator folder**: Translator-related implementations.
- **gui.py**: Provides the GUI interface.
- **const.py**: Some constants.
- **main.py**: Provides the command-line tool.
- **high_level.py**: High-level interfaces based on BabelDOC.
- **http_api.py**: Provides HTTP API (not started).

Ask AI to understand the project: [DeepWiki](https://deepwiki.com/PDFMathTranslate/PDFMathTranslate-next)

## Contact Us

If you have any questions, please submit feedback via Issue or join our Telegram Group. Thank you for your contribution!

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) sponsors monthly Pro membership codes for active contributors to this project. For details, please see: [BabelDOC/PDFMathTranslate Contributor Reward Rules](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/)