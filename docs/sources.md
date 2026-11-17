# 공식 문서와 창작 참고 자료

[가이드 홈](index.md) · [설치 안내](installation.md) · [검증 범위](maintenance.md)

**2026-11-18**에 서비스 기능과 설치 경로를 공식 문서로 확인했습니다. 창작 자료는 작가가 공개한 인터뷰·강의·저술을 중심으로, 적용한 위치와 해석 범위를 정리합니다.

## 서비스와 스킬 형식의 공식 근거

| 공식 자료 | 이 가이드에서 확인한 내용 | 적용 범위 |
|---|---|---|
| [Google: Gemini Apps 스킬](https://support.google.com/gemini/answer/17094296?hl=en) | 파일 업로드, 활성화·자동 적용, 다른 스킬 참조, 교체 | Gemini Apps. CLI의 명령과 구분 |
| [Anthropic: Claude 스킬 사용](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | 코드 실행·파일 생성, 업로드와 활성화 | 계정·조직 설정 확인 |
| [Anthropic: 통합 Plugins 화면](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page) | Customize에서 Plugins로 이름 변경, 대화의 + 및 `/` | 계정·조직에 따라 적용 시점이 다름 |
| [Anthropic: 사용자 지정 스킬 작성](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) | 스킬 폴더를 포함하는 ZIP, 모델의 여러 스킬 자동 선택 | 스킬이 다른 스킬을 직접 호출하는 방식은 지원되지 않음 |
| [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) | 이용 대상, Skills 메뉴와 업로드 검사 | 대상 계정·워크스페이스. 업로드 수용 형식은 화면에서 확인 |
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | 이름·설명·지침 구조, ChatGPT의 `@` 선택 | Codex의 호출 방법은 문서에서 별도로 설명 |
| [OpenAI: Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) | 프로젝트 지침과 파일 자료 | 네이티브 스킬과 별도 방식 |
| [GitHub: 소스 아카이브 다운로드](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) | Code → Download ZIP은 선택한 브랜치의 저장소 스냅샷 | 압축을 푼 뒤 `dist/`에서 개별 파일 선택 |
| [GitHub: Copilot CLI Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | `SKILL.md` 구조와 Copilot CLI의 스킬 검색 경로 | 이 저장소에서 `skills/`는 배포용 원본 위치. Copilot CLI의 기본 프로젝트 검색 위치는 `.github/skills/`, `.claude/skills/`, `.agents/skills/` |
| [Agent Skills 규격](https://agentskills.io/specification) | 이름·설명·참조 구조와 단계적 자료 읽기 | 플랫폼별 세부 수용 여부는 별도 확인 |

문서의 등록 단계는 위 자료를 기준으로 작성했습니다. 정확한 노출 메뉴·기능 제공 여부는 사용하는 계정에서 확인하세요. 어떤 창작 스킬을 어떤 순서로 조합할지는 이 저장소가 설계한 규칙이며, 공식 문서의 보증이나 추천 조합을 뜻하지 않습니다.

## 창작 원리의 참고 자료

작가가 본인의 방법과 경험을 설명한 대목을 요약했습니다. 아래 스킬의 한국어 예문과 연재 절차는 이 팩에서 새로 만들었습니다.

| 지역·작가 | 공개 자료에서 읽을 대목 | 스킬에 반영한 방법 |
|---|---|---|
| 한국 · 전민희 | 중요 사건을 미리 잡아도 집필 중 장면의 길이는 달라진다. 첫머리를 여러 번 바꾸며 뒤의 연결도 맞췄고, 완성한 한 권을 나누어 연재한 경험도 있다. [채널예스 인터뷰](https://ch.yes24.com/Article/Details/37794) | [장편 구성](plan-fantasy-longform.md)의 고정 사건과 유동 구간, [도입부](lower-opening-barrier.md)의 시작 장면 비교, [연재 정체](prevent-serial-drag.md)의 비축분 |
| 한국 · 김보영 | 청각이 없는 세계에 습관적인 소리 표현이 남은 것을 퇴고에서 발견했다. 낯선 설정을 독자가 이야기 속에서 받아들이도록 하는 문제를 고민했다. [채널예스 인터뷰](https://ch.yes24.com/Article/Details/33852) | [장면 사례](../skills/write-fantasy-prose/references/scene-craft.md)의 감각·시점과 관찰에서 행동으로 이어지는 사례 |
| 한국 · 싱숑 | 공동 집필에서 서로의 다른 작법을 인정하며 원고를 검토하는 과정과 마감을 이야기했다. [매경이코노미 인터뷰](https://www.mk.co.kr/news/all/10830213) | [회차 인계](workflow.md#6-공개-전-확인하고-다음-작업에-넘기기)에서 선택과 수정 이유를 공유하는 방식 |
| 일본 · 카즈키 미야 | 다음 갱신분의 필수 요소를 플롯에서 뽑아 순서를 바꾸고 대화를 붙이는 작업을 설명했다. 갱신 주기를 자신의 생활에 맞춰 잡았으면 좋았겠다고 돌아봤다. [소설가가 되자에 실린 인터뷰](https://ncode.syosetu.com/n3654cm/15/) | [회차 카드](structure-serial-chapters.md)의 필수 사건 배치와 [연재 정체](prevent-serial-drag.md)의 마감·비축분 제약 |
| 일본 · 우에하시 나호코 | 두 인물의 여정을 따라 이야기가 퍼졌고, 한 인물이 행복해질 방법을 찾으며 썼다고 돌아봤다. [신초샤 특설 사이트 대담](https://www.shinchosha.co.jp/moribito/) | [장편 구성](plan-fantasy-longform.md)의 탐색형 집필과 [장면 사례](../skills/write-fantasy-prose/references/scene-craft.md)의 인물별 이해관계 |
| 중국 · 위안예(爱潜水的乌贼) | 속편을 새 독자도 읽을 수 있도록 기존 정보를 다시 주되, 설명이 반복되면 속도가 느려지는 점을 이야기했다. [중국작가망 인터뷰](https://www.chinawriter.com.cn/n1/2025/0107/c404024-40396807.html) | [도입부](lower-opening-barrier.md)의 새 부와 속편에서 첫 선택을 이해하는 데 필요한 정보 |
| 영어권 · 어슐러 K. 르 귄 | 문장의 역할에 맞춰 길고 짧은 문장을 유연하게 쓴다. [작가 공식 사이트의 작법 대화](https://www.ursulakleguin.com/bvc-navigating-the-ocean-of-story-session-1-part-3) | [문체 카드](../skills/write-fantasy-prose/references/VOICE_CARD.md)와 [한국어 퇴고](refine-natural-korean.md)의 작품별 호흡 |
| 영어권 · 브랜던 샌더슨 | 작품이 독자에게 형성하는 기대, 그 기대를 향한 진척, 결말에서의 보상을 플롯의 한 관점으로 제시한다. [2025년 플롯 강의](https://www.brandonsanderson.com/blogs/blog/brandon-sandersons-2025-guide-to-plot-lecture-2) | [회차 구성](structure-serial-chapters.md)에서 조용한 화에도 의미 있는 변화나 부분적인 답을 점검 |

위 방법은 작업 상황에 따라 고릅니다. 개요를 먼저 짜거나 장면을 쓰면서 다음 국면을 발견할 수 있고, 짧은 단서나 관계의 변화로도 독자에게 진척을 보여 줄 수 있습니다. 각 작가의 연재 경험은 특정 갱신 주기나 성과를 보장하는 규칙으로 쓰지 않습니다.

### 함께 참고한 자료

| 참고 자료 | 이 팩에서 참고한 관점 | 적용 경계 |
|---|---|---|
| [헤밍웨이 인터뷰 — The Paris Review](https://www.theparisreview.org/interviews/4825/the-art-of-fiction-no-21-ernest-hemingway) | 알고 있는 것을 선택적으로 생략하는 방식 | 설명을 전부 없애라는 규칙이 아닙니다. |
| [체호프 편지 — Project Gutenberg](https://www.gutenberg.org/files/6408/6408-h/6408-h.htm) | 절제된 감정 표현과 구체적 관찰 | 모든 감정을 행동만으로 묘사하지 않습니다. |
| [체호프, The Sea-Gull](https://dev.gutenberg.org/cache/epub/1754/pg1754-images.html) | 선택된 작은 세부가 만드는 장면 | 등장인물의 말을 작가의 절대적인 작법 법칙으로 단정하지 않습니다. |
| [르 귄, Steering the Craft](https://www.ursulakleguin.com/steering-the-craft) | 서술의 소리·리듬·시점에 대한 주의 | 영어 문장 규칙을 한국어에 그대로 적용하지 않습니다. |
| [오웰, Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/) | 상투적인 표현과 모호한 문장의 경계 | 소설의 의도적인 모호함·비유까지 제거하지 않습니다. |
| [Wrede, Fantasy Worldbuilding Questions — 저자 공식 사이트](https://pcwrede.com/pcw-wp/fantasy-worldbuilding-%20questions/) | 세계 요소 사이의 연결을 묻는 접근 | 집필 전에 모든 질문에 답할 의무는 없습니다. |
| [Sanderson's First Law](https://www.brandonsanderson.com/blogs/blog/sandersons-first-law) | 마법으로 갈등을 해결할 때 독자의 이해를 고려 | 소프트 매직과 설명되지 않는 신비도 허용합니다. |
| [Sanderson's Second Law](https://www.brandonsanderson.com/blogs/blog/sandersons-second-law) | 마법의 한계·제약이 만드는 서사 | 모든 능력에 기억·수명 소모를 붙이지 않습니다. |


르 귄의 링크는 도서 안내 페이지이며 책 전문을 제공하는 링크가 아닙니다. Wrede 자료는 세계 요소 사이의 관계를 검토하는 참고 관점으로 사용하며, 모든 질문에 답해야 한다는 절차로 만들지 않습니다.

## 예시와 독자 반응 자료의 해석

세계관 번호 예시 216개는 명칭 48개와 설계·검토 카드 168개입니다. 서로 독립적인 허구 사례이며, 완성 세계관 216개나 현실의 역사·언어·종교 사실을 뜻하지 않습니다. 이름의 전 세계적 미사용 여부를 검증한 목록도 아닙니다.

연재 점검 스킬은 공개 후기에서 관찰한 경향을 작업 관점으로 활용합니다. 무작위 표본이나 작품별 성과 예측 모델이 아니며, 이 가이드는 이탈률·성공률을 제시하지 않습니다. 실제 작품을 검토할 때는 제공된 원고와 실제 독자 반응을 근거로 삼고 취향 차이와 구조 문제를 구분합니다.

## 확인 수준

공식 문서 확인, 배포 파일 검사, 실제 서비스의 등록·모델 실행은 다른 확인 단계입니다. 파일 검사를 통과한 사실을 모든 계정에서의 실행 성공으로 확대하지 않습니다. 검사 항목은 [패키지 검증](maintenance.md), 사용자 확인 방법은 [빠른 시작](quickstart.md)에 있습니다.
