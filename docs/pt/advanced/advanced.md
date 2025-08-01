[**Opções avançadas**](./introduction.md) > **Opções avançadas** _(atual)_

---

<h3 id="toc">Índice</h3>

- [Argumentos da Linha de comando](#argumentos-da-linha-de-comando)
- [Tradução parcial](#tradução-parcial)
- [Especificar idiomas de origem e destino](#especificar-idiomas-de-origem-e-destino)
- [Traduzir com exceções](#traduzir-com-exceções)
- [Prompt personalizado](#prompt-personalizado)
- [Configuração personalizada](#configuração-personalizada)
- [Pular limpeza](#pular-limpeza)
- [Cache de tradução](#cache-de-tradução)
- [Implantação como serviços públicos](#implantação-como-serviços-públicos)
- [Autenticação e página de boas-vindas](#autenticação-e-página-de-boas-vindas)
- [Suporte ao glossário](#suporte-ao-glossário)

---

#### Argumentos da Linha de comando

Execute o comando de tradução na linha de comando para gerar o documento traduzido `example-mono.pdf` e o documento bilíngue `example-dual.pdf` no diretório de trabalho atual. Use o Google como serviço de tradução padrão. Mais serviços de tradução suportados podem ser encontrados [AQUI](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../images/cmd_light.svg" width="580px"  alt="cmd"/>

Na tabela a seguir, listamos todas as opções avançadas para referência:

##### Argumentos

| Opção                          | Função                                                                               | Exemplo                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Caminho local do arquivo PDF                                                                    | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | Arquivos online                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | Diretório de saída para os arquivos                                                    | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | Usar [**serviço específico**](./Documentation-of-Translation-Services.md) para tradução | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | Mostrar mensagem de ajuda e sair                                                       | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | Caminho para o arquivo de configuração                                                | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | Intervalo de relatório de progresso em segundos                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | Usar nível de log de depuração                                                                | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | Interagir com a GUI                                                                      | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | Apenas baixa e verifica os ativos necessários e depois sai                            | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | Gerar pacote de recursos offline no diretório especificado                             | `pdf2zh example.pdf --generate-offline-assets /path`                                                                 |
| `--restore-offline-assets`      | Restaurar pacote de recursos offline do diretório especificado                            | `pdf2zh example.pdf --restore-offline-assets /path`                                                                  |
| `--version`                     | Mostrar versão e sair                                                                  | `pdf2zh --version`                                                                                                   |
| `--pages`                       | Tradução parcial do documento                                                           | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | O código do idioma de origem                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | O código do idioma de destino                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | Comprimento mínimo do texto para tradução                                              | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | Endereço do host do serviço RPC para análise de layout de documento                   |                                                                                                                      |
| `--qps`                         | Limite de QPS para o serviço de tradução                                               | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | Ignorar cache de tradução                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | Prompt personalizado do sistema para tradução. Usado para `/no_think` em Qwen 3                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | Número máximo de workers para o pool de tradução. Se não definido, usará qps como o número de workers | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | Desativar extração automática do glossário                                             | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | Substitui a família de fontes primária para o texto traduzido. Opções: 'serif' para fontes serifadas, 'sans-serif' para fontes sem serifa, 'script' para fontes script/itálicas. Se não especificado, usa seleção automática de fonte baseada nas propriedades do texto original. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | Não gerar arquivos PDF bilíngues                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | Não gerar arquivos PDF monolíngues                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | Padrão de fonte para identificar texto de fórmula                                       | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | Padrão de caracteres para identificar texto de fórmula                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | Forçar a divisão de linhas curtas em parágrafos diferentes                             | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | Fator de limite de divisão para linhas curtas                                                 |                                                                                                                      |
| `--skip-clean`                  | Pular etapa de limpeza do PDF                                                          | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        | No modo de PDF duplo, prioriza a colocação da página traduzida         | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | Desativar tradução de texto rico                                                      | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | Ativar todas as opções de aprimoramento de compatibilidade                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | Usar modo de páginas alternadas para PDF dual                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | Modo de saída de marca d'água para arquivos PDF                                        | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | Número máximo de páginas por parte para tradução dividida                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | Traduzir texto de tabela (experimental)                                               | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | Pular detecção de documentos digitalizados                                             | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | Forçar o texto traduzido a ser preto e adicionar fundo branco                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | Ativar solução alternativa de OCR automática. Se um documento for detectado como altamente digitalizado, isso tentará ativar o processamento de OCR e pular a detecção adicional de digitalização. Consulte a documentação para obter detalhes. (padrão: False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page`| Incluir apenas páginas traduzidas no PDF de saída. Efetivo apenas quando --pages é usado. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | Glossário personalizado para tradução.                                                | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |
| `--save-auto-extracted-glossary`| salvar glossário extraído automaticamente.                                                | `pdf2zh example.pdf --save-auto-extracted-glossary`                                                                   |


##### Argumentos da GUI

| Opção                          | Função                               | Exemplo                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Habilitar modo de compartilhamento    | `pdf2zh --gui --share`                          |
| `--auth-file`                   | Caminho para o arquivo de autenticação        | `pdf2zh --gui --auth-file /path`                |
| `--welcome-page`                | Caminho para o arquivo html de boas-vindas          | `pdf2zh --gui --welcome-page /path`             |
| `--enabled-services`            | Serviços de tradução ativados           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Desativar entrada sensível da GUI      | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | Desativar salvamento automático de configuração | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | Porta do WebUI                             | `pdf2zh --gui --server-port 7860`               |

[⬆️ Voltar ao topo](#toc)

---

#### Tradução parcial

Use o parâmetro `--pages` para traduzir uma parte de um documento.

- Se os números das páginas forem consecutivos, você pode escrever assim:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` inclui todas as páginas após a página 25. Se o seu documento tiver 100 páginas, isso é equivalente a `25-100`.
> 
> Da mesma forma, `-25` inclui todas as páginas antes da página 25, o que é equivalente a `1-25`.

- Se as páginas não forem consecutivas, você pode usar uma vírgula `,` para separá-las.

Por exemplo, se você deseja traduzir a primeira e a terceira páginas, pode usar o seguinte comando:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Se as páginas incluírem intervalos consecutivos e não consecutivos, você também pode conectá-los com uma vírgula, assim:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Este comando irá traduzir a primeira página, a terceira página, as páginas 10-20 e todas as páginas de 25 até o final.


[⬆️ Voltar ao topo](#toc)

---

#### Especificar idiomas de origem e destino

Veja [Códigos do idioma do Google](https://developers.google.com/admin-sdk/directory/v1/languages), [Códigos do idioma do DeepL](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Voltar ao topo](#toc)

---

#### Traduzir com exceções

Use regex para especificar fontes de fórmulas e caracteres que precisam ser preservados:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Preservar as fontes `Latex`, `Mono`, `Code`, `Italic`, `Symbol` e `Math` por padrão:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Voltar ao topo](#toc)

---

#### Prompt personalizado

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Prompt personalizado do sistema para tradução. É usado principalmente para adicionar a instrução '/no_think' do Qwen 3 no prompt.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Voltar ao topo](#toc)

---

#### Configuração personalizada

Existem várias maneiras de modificar e importar o arquivo de configuração.

> [!NOTE]
> **Hierarquia do Arquivo de Configuração**
>
> Ao modificar o mesmo parâmetro usando métodos diferentes, o software aplicará as alterações de acordo com a ordem de prioridade abaixo.
>
> Modificações de prioridade mais alta substituirão as de prioridade mais baixa.
>
> **cli/gui > env > arquivo de configuração do usuário > arquivo de configuração padrão**

- Modificando a configuração via **Argumentos da Linha de comando**

Na maioria dos casos, você pode passar diretamente as configurações desejadas através dos argumentos da linha de comando. Consulte [Argumentos da Linha de comando](#cmd) para obter mais informações.

Por exemplo, se você deseja habilitar uma janela GUI, pode usar o seguinte comando:

```bash
pdf2zh_next --gui
```

- Modificando a configuração via **Variáveis de Ambiente**

Você pode substituir o `--` nos argumentos da linha de comando por `PDF2ZH_`, conectar parâmetros usando `=` e substituir `-` por `_` como variáveis de ambiente.

Por exemplo, se você quiser habilitar uma janela GUI, pode usar o seguinte comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../images/ev_light.svg" width="580px"  alt="env"/>

- Arquivo de **Configuração** Especificado pelo Usuário

Você pode especificar um arquivo de configuração usando o argumento da linha de comando abaixo:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Se você não tiver certeza sobre o formato do arquivo de configuração, consulte o arquivo de configuração padrão descrito abaixo.

- **Arquivo de Configuração Padrão**

O arquivo de configuração padrão está localizado em `~/.config/pdf2zh`. 
Por favor, não modifique os arquivos de configuração no diretório `default`. 
É altamente recomendado consultar o conteúdo deste arquivo de configuração e usar **Configuração personalizada** para implementar seu próprio arquivo de configuração.

> [!TIP]
> - Por padrão, o pdf2zh 2.0 salva automaticamente a configuração atual em `~/.config/pdf2zh/config.v3.toml` cada vez que você clica no botão de tradução na GUI. Este arquivo de configuração será carregado por padrão na próxima inicialização.
> - Os arquivos de configuração no diretório `default` são gerados automaticamente pelo programa. Você pode copiá-los para modificação, mas por favor não os modifique diretamente.
> - Os arquivos de configuração podem incluir números de versão como "v2", "v3", etc. Estes são **números de versão do arquivo de configuração**, **não** o número de versão do pdf2zh em si.


[⬆️ Voltar ao topo](#toc)

---

#### Pular limpeza

Quando este parâmetro for definido como True, a etapa de limpeza do PDF será ignorada, o que pode melhorar a compatibilidade e evitar alguns problemas de processamento de fontes.

Uso:

```bash
pdf2zh_next example.pdf --skip-clean
```

Ou usando variáveis de ambiente:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Quando `--enhance-compatibility` está ativado, Pular limpeza é automaticamente habilitado.

---

#### Cache de tradução

O PDFMathTranslate armazena em cache os textos traduzidos para aumentar a velocidade e evitar chamadas de API desnecessárias para conteúdos idênticos. Você pode usar a opção `--ignore-cache` para ignorar o cache de tradução e forçar uma nova tradução.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Voltar ao topo](#toc)

---

#### Implantação como serviços públicos

Ao implantar um pdf2zh GUI em serviços públicos, você deve modificar o arquivo de configuração conforme descrito abaixo.

> [!TIP]
> - Ao implantar publicamente, tanto `disable_gui_sensitive_input` quanto `disable_config_auto_save` devem ser ativados.
> - Separe diferentes serviços disponíveis com *vírgulas em inglês* <kbd>,</kbd> .

Uma configuração utilizável é a seguinte:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Voltar ao topo](#toc)

---

#### Autenticação e página de boas-vindas

Ao usar Autenticação e página de boas-vindas para especificar qual usuário deve usar a Web UI e personalizar a página de login:

exemplo auth.txt
Cada linha contém dois elementos, nome de usuário e senha, separados por uma vírgula.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

exemplo welcome.html

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
> A página de boas-vindas funcionará apenas se o arquivo de autenticação não estiver em branco.
> Se o arquivo de autenticação estiver em branco, não haverá autenticação. :)

Uma configuração utilizável é a seguinte:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Voltar ao topo](#toc)

---

#### Suporte ao glossário

O PDFMathTranslate suporta a tabela de glossário. O arquivo da tabela de glossário deve ser um arquivo `csv`.
Há três colunas no arquivo. Aqui está um arquivo de glossário de demonstração:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自动 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |


Para usuários da CLI:
Você pode usar vários arquivos para o glossário. E arquivos diferentes devem ser separados por `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Para usuários da WebUI:

Agora você pode enviar seu próprio arquivo de glossário. Após enviar o arquivo, você pode verificá-lo clicando no nome e o conteúdo será exibido abaixo.

[⬆️ Voltar ao topo](#toc)

<div align="right"> 
<h6><small>Parte do conteúdo desta página foi traduzida pelo GPT e pode conter erros.</small></h6>