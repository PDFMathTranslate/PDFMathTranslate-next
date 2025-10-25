[**고급 옵션**](./introduction.md) > **고급 옵션** _(현재)_

---

<h3 id="목차">목차</h3>

- [명령줄 인수](#명령줄 - 인수)
- [속도 제한 구성 가이드](#속도 - 제한 - 구성 - 가이드)
- [부분 번역](#부분 - 번역)
- [소스 및 대상 언어 지정](#소스 - 및 - 대상 - 언어 - 지정)
- [예외와 함께 번역](#예외와 - 함께 - 번역)
- [사용자 정의 프롬프트](#사용자 - 정의 - 프롬프트)
- [사용자 정의 구성](#사용자 - 정의 - 구성)
- [정리 건너뛰기](#정리 - 건너뛰기)
- [번역 캐시](#번역 - 캐시)
- [공용 서비스로 배포](#공용 - 서비스로 - 배포)
- [인증 및 환영 페이지](#인증 - 및 - 환영 - 페이지)
- [용어집 지원](#용어집 - 지원)

---

#### 명령줄 인수

명령줄에서 번역 명령을 실행하여 현재 작업 디렉터리에 번역된 문서 `example-mono.pdf` 와 이중 언어 문서 `example-dual.pdf` 를 생성합니다. 기본 번역 서비스로 Google 을 사용합니다. 더 많은 지원되는 번역 서비스는 [여기](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services) 에서 확인할 수 있습니다.

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

다음 표에서는 참조용으로 모든 고급 옵션을 나열합니다:

##### 인수

| 옵션                          | 기능                                                                               | 예시                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `files`                         | 로컬 `PDF` 파일 경로                                                                    | `pdf2zh ~/local.pdf`                                                                                                 |
| `links`                         | 온라인 파일                                                                           | `pdf2zh http://arxiv.org/paper.pdf`                                                                                  |
| `--output`                      | 출력 파일 디렉토리                                                             | `pdf2zh example.pdf --output /outputpath`                                                                            |
| `--<Services>`                  | 번역을 위해 [**특정 서비스**](./Documentation-of-Translation-Services.md) 사용 | `pdf2zh example.pdf --openai`<br>`pdf2zh example.pdf --deepseek`                                                     |
| `--help`, `-h`                  | 도움말 메시지를 표시하고 종료                                                             | `pdf2zh -h`                                                                                                          |
| `--config-file`                 | 구성 파일 경로                                                         | `pdf2zh --config-file /path/to/config/config.toml`                                                                   |
| `--report-interval`             | 진행 보고 간격 (초 단위)                                                    | `pdf2zh example.pdf --report-interval 5`                                                                             |
| `--debug`                       | 디버그 로깅 레벨 사용                                                                 | `pdf2zh example.pdf --debug`                                                                                         |
| `--gui`                         | GUI 와 상호 작용                                                                      | `pdf2zh --gui`                                                                                                       |
| `--warmup`                      | 필요한 자산만 다운로드하고 검증한 후 종료                                     | `pdf2zh example.pdf --warmup`                                                                                        |
| `--generate-offline-assets`     | 지정된 디렉터리에 오프라인 자산 패키지 생성                             | `pdf2zh example.pdf --generate-offline-assets /path`                                                                 |
| `--restore-offline-assets`      | 지정된 디렉터리에서 오프라인 자산 패키지 복원                            | `pdf2zh example.pdf --restore-offline-assets /path`                                                                  |
| `--version`                     | 버전 표시 후 종료                                                                       | `pdf2zh --version`                                                                                                   |
| `--pages`                       | 문서의 부분 번역                                                           | `pdf2zh example.pdf --pages 1,2,1-,-3,3-5`                                                                           |
| `--lang-in`                     | 소스 언어의 코드                                                            | `pdf2zh example.pdf --lang-in en`                                                                                    |
| `--lang-out`                    | 대상 언어의 코드                                                            | `pdf2zh example.pdf --lang-out zh-CN`                                                                                |
| `--min-text-length`             | 번역할 최소 텍스트 길이                                                       | `pdf2zh example.pdf --min-text-length 5`                                                                             |
| `--rpc-doclayout`               | 문서 레이아웃 분석을 위한 RPC 서비스 호스트 주소                                  |                                                                                                                      |
| `--qps`                         | 번역 서비스의 QPS 제한                                                      | `pdf2zh example.pdf --qps 200`                                                                                       |
| `--ignore-cache`                | 번역 캐시 무시                                                               | `pdf2zh example.pdf --ignore-cache`                                                                                  |
| `--custom-system-prompt`        | 번역을 위한 사용자 정의 시스템 프롬프트. Qwen 3 에서 `/no_think` 에 사용됨                   | `pdf2zh example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--pool-max-worker`             | 번역 풀의 최대 작업자 수. 설정되지 않은 경우 qps 를 작업자 수로 사용합니다 | `pdf2zh example.pdf --pool-max-worker 100`                                                                |
| `--no-auto-extract-glossary`    | 자동 용어집 추출 비활성화                                                          | `pdf2zh example.pdf --no-auto-extract-glossary`                                                                      |
| `--primary-font-family`         | 번역된 텍스트의 기본 글꼴 패밀리를 재정의합니다. 선택 사항: 'serif'는 세리프 글꼴, 'sans-serif'는 산세리프 글꼴, 'script'는 필기체/이탤릭 글꼴입니다. 지정하지 않으면 원본 텍스트 속성을 기반으로 자동 글꼴 선택이 사용됩니다. | `pdf2zh example.pdf --primary-font-family serif` |
| `--no-dual`                     | 이중 언어 PDF 파일 출력 안 함                                                      | `pdf2zh example.pdf --no-dual`                                                                                       |
| `--no-mono`                     | 단일 언어 PDF 파일 출력하지 않음                                                    | `pdf2zh example.pdf --no-mono`                                                                                       |
| `--formular-font-pattern`       | 수식 텍스트를 식별하기 위한 폰트 패턴                                                  | `pdf2zh example.pdf --formular-font-pattern "(MS.*)"`                                                                |
| `--formular-char-pattern`       | 수식 텍스트를 식별하기 위한 문자 패턴                                             | `pdf2zh example.pdf --formular-char-pattern "(MS.*)"`                                                                |
| `--split-short-line`            | 짧은 줄을 강제로 다른 단락으로 분할                                       | `pdf2zh example.pdf --split-short-line`                                                                              |
| `--short-line-split-factor`     | 짧은 줄 분할 임계값 계수                                                 |                                                                                                                      |
| `--skip-clean`                  | PDF 클리닝 단계 건너뛰기                                                                 | `pdf2zh example.pdf --skip-clean`                                                                                    |
| `--dual-translate-first`        | 듀얼 PDF 모드에서 번역 페이지를 우선적으로 배치합니다                                          | `pdf2zh example.pdf --dual-translate-first`                                                                                            |
| `--disable-rich-text-translate` | 리치 텍스트 번역 비활성화                                                          | `pdf2zh example.pdf --disable-rich-text-translate`                                                                   |
| `--enhance-compatibility`       | 모든 호환성 향상 옵션 활성화                                           | `pdf2zh example.pdf --enhance-compatibility`                                                                         |
| `--use-alternating-pages-dual`  | 듀얼 PDF 를 위한 교대 페이지 모드 사용                                                | `pdf2zh example.pdf --use-alternating-pages-dual`                                                                    |
| `--watermark-output-mode`       | PDF 파일의 워터마크 출력 모드                                                    | `pdf2zh example.pdf --watermark-output-mode "NoWaterMark"`                                                           |
| `--max-pages-per-part`          | 부분 번역을 위한 파트당 최대 페이지 수                                           | `pdf2zh example.pdf --max-pages-per-part 1`                                                                          |
| `--translate-table-text`        | 테이블 텍스트 번역 (실험적 기능)                                                    | `pdf2zh example.pdf --translate-table-text`                                                                          |
| `--skip-scanned-detection`      | 스캔된 문서 감지 건너뛰기                                                                 | `pdf2zh example.pdf --skip-scanned-detection`                                                                        |
| `--ocr-workaround`              | 번역된 텍스트를 강제로 검정색으로 만들고 흰색 배경 추가                             | `pdf2zh example.pdf --ocr-workaround`                                                                                |
| `--auto-enable-ocr-workaround`  | 자동 OCR 해결 방법을 활성화합니다. 문서가 심하게 스캔된 것으로 감지되면 OCR 처리를 시도하고 추가 스캔 감지를 건너뜁니다. 자세한 내용은 문서를 참조하세요. (기본값: False) | `pdf2zh example.pdf --auto-enable-ocr-workaround True`                    |
| `--only-include-translated-page` | 출력 PDF 에 번역된 페이지만 포함합니다. `--pages` 가 사용될 때만 유효합니다. | `pdf2zh example.pdf --pages 1-5 --only-include-translated-page`                                                       |
| `--glossaries`                  | 번역을 위한 사용자 정의 용어집.                                                      | `pdf2zh example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                         |
| `--save-auto-extracted-glossary`| 자동으로 추출된 용어집을 저장합니다.                                                | `pdf2zh example.pdf --save-auto-extracted-glossary`                                                                   |
| `--no-merge-alternating-line-numbers` | 줄 번호가 있는 문서에서 번갈아 나타나는 줄 번호와 텍스트 단락의 병합을 비활성화합니다 | `pdf2zh example.pdf --no-merge-alternating-line-numbers` |
| `--no-remove-non-formula-lines` | 단락 영역 내에서 수식이 아닌 줄 제거 비활성화                          | `pdf2zh example.pdf --no-remove-non-formula-lines`                                                                    |
| `--non-formula-line-iou-threshold` | 비수식 라인 식별을 위한 IoU 임계값 설정 (0.0-1.0)                     | `pdf2zh example.pdf --non-formula-line-iou-threshold 0.85`                                                            |
| `--figure-table-protection-threshold` | 그림과 표에 대한 보호 임계값 설정 (0.0-1.0). 그림/표 내부의 라인은 처리되지 않음 | `pdf2zh example.pdf --figure-table-protection-threshold 0.95` |
| `--skip-formula-offset-calculation` | 처리 중 수식 오프셋 계산 건너뛰기         | `pdf2zh example.pdf --skip-formula-offset-calculation`                                                                |


##### GUI 인수

| 옵션                          | 기능                               | 예시                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | 공유 모드 활성화                    | `pdf2zh --gui --share`                          |
| `--auth-file`                   | 인증 파일 경로        | `pdf2zh --gui --auth-file /path`                |
| `--welcome-page`                | 환영 페이지 HTML 파일 경로          | `pdf2zh --gui --welcome-page /path`             |
| `--enabled-services`            | 활성화된 번역 서비스           | `pdf2zh --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | GUI 민감한 입력 비활성화            | `pdf2zh --gui --disable-gui-sensitive-input`    |
| `--disable-config-auto-save`    | 자동 구성 저장 비활성화 | `pdf2zh --gui --disable-config-auto-save`       |
| `--server-port`                 | WebUI 포트                             | `pdf2zh --gui --server-port 7860`               |

[⬆️ 맨 위로](#toc)

---

#### 속도 제한 구성 가이드

번역 서비스를 사용할 때 적절한 속도 제한 구성은 API 오류를 방지하고 성능을 최적화하는 데 중요합니다. 이 가이드는 다양한 업스트림 서비스 제한에 따라 `--qps` 및 `--pool-max-worker` 매개변수를 구성하는 방법을 설명합니다.

> [!TIP]
>
> `pool_size` 는 1000 을 초과하지 않는 것이 권장됩니다. 아래 방법으로 계산된 `pool_size` 가 1000 을 초과하는 경우 1000 을 사용하세요.

##### RPM (Requests Per Minute) 요청 속도 제한

업스트림 서비스에 RPM 제한이 있을 때 다음 계산을 사용하세요:

**계산 공식:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> 10 이라는 계수는 대부분의 시나리오에서 잘 작동하는 경험적 계수입니다.

**예시:**
번역 서비스의 제한이 600 RPM 인 경우:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### 동시 연결 제한

`Concurrent Connection Limit = (Number of Workers) × (Number of GPUs per Worker) × (Number of Concurrent Requests per GPU)`

**Example:**

- If you have 2 workers (`--workers 2`), each with 1 GPU (`CUDA_VISIBLE_DEVICES=0`), and each GPU handles 2 concurrent requests (`--concurrency 2`), then:
  
  ```bash
  Concurrent Connection Limit = 2 × 1 × 2 = 4
  ```

- If you have 1 worker (`--workers 1`) with 2 GPUs (`CUDA_VISIBLE_DEVICES=0,1`), and each GPU handles 3 concurrent requests (`--concurrency 3`), then:
  
  ```bash
  Concurrent Connection Limit = 1 × 2 × 3 = 6
  ```

**Note:** This calculation assumes each GPU processes requests independently. If your model implementation shares resources across GPUs (e.g., tensor parallelism), adjust accordingly.

---

### TRANSLATED TEXT

업스트림 서비스에 동시 연결 제한이 있는 경우 (예: GLM 공식 서비스), 이 방법을 사용하세요:

**계산 공식:**
`동시 연결 제한 = (작업자 수) × (작업자당 GPU 수) × (GPU 당 동시 요청 수)`

**예시:**

- 작업자가 2 개 (`--workers 2`), 각 작업자에 GPU 가 1 개 (`CUDA_VISIBLE_DEVICES=0`), GPU 당 동시 요청이 2 개 (`--concurrency 2`) 인 경우:
  
  ```bash
  동시 연결 제한 = 2 × 1 × 2 = 4
  ```

- 작업자가 1 개 (`--workers 1`), GPU 가 2 개 (`CUDA_VISIBLE_DEVICES=0,1`), GPU 당 동시 요청이 3 개 (`--concurrency 3`) 인 경우:
  
  ```bash
  동시 연결 제한 = 1 × 2 × 3 = 6
  ```

**참고:** 이 계산은 각 GPU 가 요청을 독립적으로 처리한다고 가정합니다. 모델 구현이 GPU 간 리소스를 공유하는 경우 (예: 텐서 병렬화), 이에 따라 조정하세요.
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

---

### 번역 결과

**예시:**
번역 서비스가 50 개의 동시 연결을 허용하는 경우:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### 모범 사례

> [!TIP]
> - 항상 보수적인 값으로 시작하고 필요에 따라 점진적으로 증가시키세요
> - 서비스의 응답 시간과 오류율을 모니터링하세요
> - 서비스마다 다른 최적화 전략이 필요할 수 있습니다
> - 이러한 매개변수를 설정할 때 특정 사용 사례와 문서 크기를 고려하세요


[⬆️ 맨 위로](#toc)

---

#### 부분 번역

`--pages` 매개변수를 사용하여 문서의 일부를 번역합니다.

- 페이지 번호가 연속적인 경우 다음과 같이 작성할 수 있습니다:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` 는 25 페이지 이후의 모든 페이지를 포함합니다. 문서가 100 페이지인 경우, 이는 `25-100` 과 동일합니다.
> 
> 마찬가지로, `-25` 는 25 페이지 이전의 모든 페이지를 포함하며, 이는 `1-25` 와 동일합니다.

- 페이지가 연속적이지 않은 경우 쉼표 `,` 를 사용하여 구분할 수 있습니다.

예를 들어, 첫 번째와 세 번째 페이지를 번역하려면 다음 명령을 사용할 수 있습니다:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- 페이지에 연속적 및 비연속적 범위가 모두 포함된 경우, 다음과 같이 쉼표로 연결할 수도 있습니다:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

이 명령은 첫 번째 페이지, 세 번째 페이지, 10-20 페이지, 그리고 25 페이지부터 끝까지의 모든 페이지를 번역합니다.

[⬆️ 맨 위로 이동](#toc)

---

#### 소스 및 대상 언어 지정

[Google 언어 코드](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL 언어 코드](https://developers.deepl.com/docs/resources/supported-languages) 참조

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ 맨 위로](#toc)

---

#### 예외와 함께 번역하기

보존해야 할 수식 글꼴과 문자를 지정하기 위해 정규식을 사용합니다:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

기본적으로 `Latex`, `Mono`, `Code`, `Italic`, `Symbol` 및 `Math` 글꼴을 보존합니다:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ 맨 위로](#toc)

---

#### 사용자 정의 프롬프트

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

번역을 위한 사용자 정의 시스템 프롬프트. 주로 프롬프트에 Qwen 3 의 '/no_think' 지시를 추가하는 데 사용됩니다.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ 맨 위로](#toc)

---

#### 사용자 지정 구성

구성 파일을 수정하고 가져오는 방법에는 여러 가지가 있습니다.

> [!NOTE]
> **구성 파일 계층 구조**
>
> 동일한 매개변수를 다른 방법으로 수정할 때, 소프트웨어는 아래의 우선순위에 따라 변경 사항을 적용합니다.
>
> 상위 순위의 수정 사항은 하위 순위의 것을 덮어씁니다.
>
> **cli/gui > env > 사용자 구성 파일 > 기본 구성 파일**

- **명령줄 인수**를 통한 구성 수정

대부분의 경우 원하는 설정을 명령줄 인수를 통해 직접 전달할 수 있습니다. 자세한 내용은 [명령줄 인수](#cmd) 를 참조하세요.

예를 들어 GUI 창을 활성화하려면 다음 명령을 사용할 수 있습니다:

```bash
pdf2zh_next --gui
```

- **환경 변수**를 통한 구성 수정

명령줄 인수에서 `--` 를 `PDF2ZH_` 로 대체하고, `=` 를 사용하여 매개변수를 연결하며, `-` 를 `_` 로 대체하여 환경 변수로 사용할 수 있습니다.

예를 들어, GUI 창을 활성화하려면 다음 명령을 사용할 수 있습니다:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- 사용자 지정 **구성 파일**

아래 명령줄 인수를 사용하여 구성 파일을 지정할 수 있습니다:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

구성 파일 형식이 확실하지 않은 경우 아래 설명된 기본 구성 파일을 참조하세요.

- **기본 구성 파일**

기본 구성 파일은 `~/.config/pdf2zh` 에 위치합니다.  
`default` 디렉토리의 구성 파일은 수정하지 마십시오.  
이 구성 파일의 내용을 참조하고 **사용자 지정 구성 파일**을 사용하여 자신의 구성 파일을 구현하는 것이 강력히 권장됩니다.

> [!TIP]
> - 기본적으로 pdf2zh 2.0 은 GUI 에서 번역 버튼을 클릭할 때마다 현재 구성을 `~/.config/pdf2zh/config.v3.toml` 에 자동으로 저장합니다. 이 구성 파일은 다음 시작 시 기본적으로 로드됩니다.
> - `default` 디렉토리의 구성 파일은 프로그램에 의해 자동으로 생성됩니다. 수정을 위해 복사할 수 있지만 직접 수정하지 마십시오.
> - 구성 파일에는 "v2", "v3" 등의 버전 번호가 포함될 수 있습니다. 이는 **구성 파일 버전 번호**이며, pdf2zh 자체의 버전 번호가 **아닙니다**.


[⬆️ 맨 위로](#toc)

---

#### 클린 건너뛰기

이 매개변수가 True 로 설정되면 PDF 클린 단계가 건너뛰어지며, 이는 호환성을 향상시키고 일부 폰트 처리 문제를 피할 수 있습니다.

사용법:

```bash
pdf2zh_next example.pdf --skip-clean
```

환경 변수를 사용하는 방법:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> `--enhance-compatibility` 가 활성화되면 클린 건너뛰기가 자동으로 활성화됩니다.

---

#### 번역 캐시

PDFMathTranslate 는 번역 속도를 높이고 동일한 내용에 대한 불필요한 API 호출을 방지하기 위해 번역된 텍스트를 캐시합니다. `--ignore-cache` 옵션을 사용하여 번역 캐시를 무시하고 강제로 재번역할 수 있습니다.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ 맨 위로](#toc)

---

#### 공개 서비스로 배포하기

공개 서비스에 pdf2zh GUI 를 배포할 때는 아래 설명대로 구성 파일을 수정해야 합니다.

> [!WARNING]
>
> 이 프로젝트는 보안 전문 감사를 받지 않았으며 보안 취약점이 포함되어 있을 수 있습니다. 공용 네트워크에 배포하기 전에 위험을 평가하고 필요한 보안 조치를 취하세요.


> [!TIP]
> - 공개적으로 배포할 때는 `disable_gui_sensitive_input` 과 `disable_config_auto_save` 를 모두 활성화해야 합니다.
> - 사용 가능한 서비스를 *영어 쉼표* <kbd>,</kbd> 로 구분하세요.

사용 가능한 구성은 다음과 같습니다:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ 맨 위로](#toc)

---

#### 인증 및 환영 페이지

인증 및 환영 페이지를 사용하여 Web UI 를 사용할 사용자를 지정하고 로그인 페이지를 사용자 정의할 때:

예시 auth.txt
각 줄에는 사용자 이름과 비밀번호 두 요소가 쉼표로 구분되어 포함됩니다.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

예시 welcome.html

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
> 인증 파일이 비어 있지 않은 경우에만 환영 페이지가 작동합니다.
> 인증 파일이 비어 있으면 인증이 없습니다. :)

사용 가능한 구성은 다음과 같습니다:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ 맨 위로](#toc)

---

#### 용어집 지원

PDFMathTranslate 는 용어집 테이블을 지원합니다. 용어집 테이블 파일은 `csv` 파일이어야 합니다.  
파일에는 세 개의 열이 있습니다. 다음은 데모 용어집 파일입니다:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 자동 ML  | ko     |
| a,a    | a       | ko     |
| "      | "       | ko     |


CLI 사용자의 경우:
용어집으로 여러 파일을 사용할 수 있습니다. 다른 파일은 `,` 로 구분해야 합니다.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

웹 UI 사용자를 위해:

이제 자신의 용어집 파일을 업로드할 수 있습니다. 파일을 업로드한 후에는 이름을 클릭하여 내용을 확인할 수 있으며, 내용이 아래에 표시됩니다.

[⬆️ 맨 위로 돌아가기](#toc)

<div align="right"> 
<h6><small>이 페이지의 일부 내용은 GPT 에 의해 번역되었으며 오류가 포함될 수 있습니다.</small></h6>