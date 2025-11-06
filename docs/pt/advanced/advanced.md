[**Opções avançadas**](./introduction.md) > **Opções avançadas** _(atual)_

---

<h3 id="toc">Índice</h3>

- [Argumentos da Linha de Comando](#argumentos-da-linha-de-comando)
- [Guia de Configuração de Limitação de Taxa](#guia-de-configuração-de-limitação-de-taxa)
- [Tradução parcial](#tradução-parcial)
- [Especificar idiomas de origem e destino](#especificar-idiomas-de-origem-e-destino)
- [Traduzir com exceções](#traduzir-com-exceções)
- [Prompt personalizado](#prompt-personalizado)
- [Configuração personalizada](#configuração-personalizada)
- [Pular limpeza](#pular-limpeza)
- [Cache de tradução](#cache-de-tradução)
- [Implantação como serviços públicos](#implantação-como-serviços-públicos)
- [Autenticação e página de boas-vindas](#autenticação-e-página-de-boas-vindas)
- [Suporte a Glossário](#suporte-a-glossário)

---

#### Argumentos da Linha de Comando

Execute o comando de tradução na linha de comando para gerar o documento traduzido `example-mono.pdf` e o documento bilíngue `example-dual.pdf` no diretório de trabalho atual. Use o Google como o serviço de tradução padrão. Mais serviços de tradução suportados podem ser encontrados [AQUI](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

Na tabela a seguir, listamos todas as opções avançadas para referência:

##### Argumentos

| Opção                          | Função                                                                               | Exemplo                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | Caminho do arquivo PDF local                                                                    | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | Arquivos online                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | Diretório de saída para os arquivos                                                     | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | Usar [**serviço específico**](./Documentation-of-Translation-Services.md) para tradução | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | Mostrar mensagem de ajuda e sair                                                             | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | Caminho para o arquivo de configuração                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | Intervalo de relatório de progresso em segundos                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | Usar nível de registro de depuração                                                                | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | Interagir com a GUI                                                                      | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | Apenas baixar e verificar os ativos necessários e depois sair                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | Gerar pacote de recursos offline no diretório especificado                             | `pdf2zh example.pdf --generate-offline-assets /path`                                                                 |
| `--restore-offline-assets`      | Restaurar pacote de ativos offline do diretório especificado                            | `pdf2zh example.pdf --restore-offline-assets /path`                                                                  |
| `--version`                     | Mostrar versão e sair                                                                  | `pdf2zh --version`                                                                                                   |
| `--pages`                       | Tradução parcial do documento                                                           | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | O código do idioma de origem                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | O código do idioma de destino                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | Comprimento mínimo do texto para traduzir                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | Endereço do host do serviço RPC para análise de layout de documento                                  |                                                                                                                      |
| `--qps`                         | Limite de QPS para o serviço de tradução                                                      | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | Ignorar cache de tradução                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | Prompt personalizado do sistema para tradução. Usado para `/no_think` em Qwen 3                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | Número máximo de trabalhadores para o pool de tradução. Se não definido, será usado qps como o número de trabalhadores | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | Desativar extração automática do glossário                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | Substitui a família de fontes primária para o texto traduzido. Opções: 'serif' para fontes serifadas, 'sans-serif' para fontes sem serifa, 'script' para fontes script/itálicas. Se não especificado, usa seleção automática de fonte baseada nas propriedades do texto original. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | Não gerar arquivos PDF bilíngues                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | Não gerar arquivos PDF monolíngues                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | Padrão de fonte para identificar texto de fórmula                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | Padrão de caracteres para identificar texto de fórmula                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | Forçar a divisão de linhas curtas em parágrafos diferentes                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | Fator de limite de divisão para linhas curtas                                                 |                                                                                                                      |
| `--skip-clean`                  | Pular etapa de limpeza do PDF                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        | Priorizar a colocação da página traduzida no modo de PDF duplo                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | Desativar tradução de texto rico                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | Ativar todas as opções de aprimoramento de compatibilidade                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | Usar o modo de páginas alternadas para PDF duplo                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | Modo de saída de marca d'água para arquivos PDF                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | Número máximo de páginas por parte para tradução dividida                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | Traduzir texto de tabela (experimental)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | Pular detecção de digitalização                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | Forçar o texto traduzido a ser preto e adicionar fundo branco                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | Ativar solução alternativa automática de OCR. Se um documento for detectado como altamente digitalizado, isso tentará ativar o processamento de OCR e pular a detecção adicional de digitalização. Consulte a documentação para obter detalhes. (padrão: Falso) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page`| Incluir apenas páginas traduzidas no PDF de saída. Eficaz apenas quando --pages é usado. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | Glossário personalizado para tradução.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |
| `--save-auto-extracted-glossary`| salvar o glossário extraído automaticamente.                                                | `pdf2zh example.pdf --save-auto-extracted-glossary`                                                                   |
| `--no-merge-alternating-line-numbers` | Desativa a fusão de números de linha alternados e parágrafos de texto em documentos com números de linha | `pdf2zh example.pdf --no-merge-alternating-line-numbers` |
| `--no-remove-non-formula-lines` | Desativar a remoção de linhas não relacionadas a fórmulas dentro de áreas de parágrafo                          | `pdf2zh example.pdf --no-remove-non-formula-lines`                                                                    |
| `--non-formula-line-iou-threshold` | Define o limite de IoU para identificar linhas não-fórmula (0.0-1.0)                     | `pdf2zh example.pdf --non-formula-line-iou-threshold 0.85`                                                            |
| `--figure-table-protection-threshold` | Define o limite de proteção para figuras e tabelas (0.0-1.0). Linhas dentro de figuras/tabelas não serão processadas | `pdf2zh example.pdf --figure-table-protection-threshold 0.95` |
| `--skip-formula-offset-calculation` | Pular o cálculo de deslocamento de fórmulas durante o processamento | `pdf2zh example.pdf --skip-formula-offset-calculation`                                                                |


##### Argumentos da GUI

| Opção                          | Função                               | Exemplo                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Ativar modo de compartilhamento        | `pdf2zh --gui --share`                          |
| `--auth-file`                   | Caminho para o arquivo de autenticação        | `pdf2zh --gui --auth-file /path`                |
| `--welcome-page`                | Caminho para o arquivo HTML de boas-vindas          | `pdf2zh --gui --welcome-page /path`             |
| `--enabled-services`            | Serviços de tradução ativados           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Desativar entrada sensível da GUI            | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | Desativar o salvamento automático de configuração | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | Porta do WebUI                             | `pdf2zh --gui --server-port 7860`               |

[⬆️ Voltar ao topo](#toc)

---

#### Guia de Configuração de Limitação de Taxa

Ao utilizar serviços de tradução, a configuração adequada da limitação de taxa é crucial para evitar erros de API e otimizar o desempenho. Este guia explica como configurar os parâmetros `--qps` e `--pool-max-worker` com base nas diferentes limitações do serviço upstream.

> [!TIP]
>
> É recomendado que o `pool_size` não exceda 1000. Se o `pool_size` calculado pelo método a seguir exceder 1000, por favor, use 1000.

##### Limitação de Taxa RPM (Solicitações Por Minuto)

Quando o serviço upstream tem limitações de RPM, use o seguinte cálculo:

**Fórmula de Cálculo:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> O fator de 10 é um coeficiente empírico que geralmente funciona bem para a maioria dos cenários.

**Exemplo:**
Se o seu serviço de tradução tiver um limite de 600 RPM:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Limitação de Conexões Simultâneas

Quando o serviço upstream tem limitações de conexões simultâneas (como o serviço oficial GLM), use esta abordagem:

**Fórmula de Cálculo:**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Exemplo:**
Se o seu serviço de tradução permitir 50 conexões simultâneas:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Melhores práticas

> [!TIP]
> - Sempre comece com valores conservadores e aumente gradualmente, se necessário
> - Monitore os tempos de resposta e as taxas de erro do seu serviço
> - Diferentes serviços podem exigir diferentes estratégias de otimização
> - Considere seu caso de uso específico e o tamanho do documento ao definir esses parâmetros


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

Veja [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

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

Prompt personalizado do sistema para tradução. Ele é usado principalmente para adicionar a instrução '/no_think' do Qwen 3 no prompt.

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
> Modificações com classificação mais alta substituirão as de classificação mais baixa.
>
> **cli/gui > env > arquivo de configuração do usuário > arquivo de configuração padrão**

- Modificando a Configuração via **Argumentos da Linha de Comando**

Na maioria dos casos, você pode passar diretamente suas configurações desejadas através dos argumentos da linha de comando. Consulte [Argumentos da Linha de Comando](#cmd) para obter mais informações.

Por exemplo, se você deseja habilitar uma janela GUI, pode usar o seguinte comando:

```bash
pdf2zh_next --gui
```

- Modificando a Configuração via **Variáveis de Ambiente**

Você pode substituir o `--` nos argumentos da linha de comando por `PDF2ZH_`, conectar parâmetros usando `=` e substituir `-` por `_` como variáveis de ambiente.

Por exemplo, se você quiser habilitar uma janela GUI, pode usar o seguinte comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Arquivo de **Configuração** Especificado pelo Usuário

Você pode especificar um arquivo de configuração usando o argumento da linha de comando abaixo:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Se você não tiver certeza sobre o formato do arquivo de configuração, consulte o arquivo de configuração padrão descrito abaixo.

- **Arquivo de Configuração Padrão**

O arquivo de configuração padrão está localizado em `~/.config/pdf2zh`.  
Por favor, não modifique os arquivos de configuração no diretório `default`.  
É altamente recomendável consultar o conteúdo deste arquivo de configuração e usar **Configuração personalizada** para implementar seu próprio arquivo de configuração.

> [!TIP]
> - Por padrão, o pdf2zh 2.0 salva automaticamente a configuração atual em `~/.config/pdf2zh/config.v3.toml` cada vez que você clica no botão de tradução na GUI. Este arquivo de configuração será carregado por padrão na próxima inicialização.
> - Os arquivos de configuração no diretório `default` são gerados automaticamente pelo programa. Você pode copiá-los para modificação, mas por favor não os modifique diretamente.
> - Os arquivos de configuração podem incluir números de versão como "v2", "v3", etc. Estes são **números de versão do arquivo de configuração**, **não** o número de versão do pdf2zh em si.


[⬆️ Voltar ao topo](#toc)

---

#### Pular limpeza

Quando este parâmetro é definido como True, a etapa de limpeza do PDF será ignorada, o que pode melhorar a compatibilidade e evitar alguns problemas de processamento de fontes.

Uso:

```bash
pdf2zh_next example.pdf --skip-clean
```

Ou usando variáveis de ambiente:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Quando `--enhance-compatibility` está ativado, Pular limpeza é automaticamente ativado.

---

#### Cache de tradução

O PDFMathTranslate armazena em cache os textos traduzidos para aumentar a velocidade e evitar chamadas desnecessárias à API para conteúdos idênticos. Você pode usar a opção `--ignore-cache` para ignorar o cache de tradução e forçar uma nova tradução.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Voltar ao topo](#toc)

---

#### Implantação como serviços públicos

Ao implantar uma GUI pdf2zh em serviços públicos, você deve modificar o arquivo de configuração conforme descrito abaixo.

> [!WARNING]
>
> Este projeto não foi auditado profissionalmente quanto à segurança e pode conter vulnerabilidades de segurança. Por favor, avalie os riscos e tome as medidas de segurança necessárias antes de implantar em redes públicas.


> [!TIP]
> - Ao implantar publicamente, tanto disable_gui_sensitive_input quanto disable_config_auto_save devem ser ativados.
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
> A página de boas-vindas funcionará apenas se o arquivo de autenticação não estiver vazio.
> Se o arquivo de autenticação estiver vazio, não haverá autenticação. :)

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

#### Suporte ao Glossário

PDFMathTranslate suporta a tabela de glossário. O arquivo da tabela de glossário deve ser um arquivo `csv`.
Há três colunas no arquivo. Aqui está um arquivo de glossário de demonstração:

| origem  | destino  | tgt_lng |
|--------|---------|---------|---------|
| AutoML | ML Automático | pt     |
| a,a    | a       | pt      |
| "      | "       | pt      |


Para usuários da CLI:
Você pode usar vários arquivos para o glossário. E arquivos diferentes devem ser separados por `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Para usuários do WebUI:

Agora você pode enviar seu próprio arquivo de glossário. Após enviar o arquivo, você pode verificar o conteúdo clicando no nome dele, que será exibido abaixo.

[⬆️ Voltar ao topo](#toc)

<div align="right"> 
<h6><small>Parte do conteúdo desta página foi traduzida pelo GPT e pode conter erros.</small></h6>