# 공식 문서와 창작 참고 자료

[가이드 홈](index.md) · [설치 안내](installation.md) · [검증 범위](maintenance.md)

기능·설치 안내 확인일: **2026-11-15**. 서비스 기능의 근거와 이 저장소가 설계한 창작 절차를 구분합니다. 이 가이드는 각 제공사의 공식 매뉴얼을 번역·대체하거나 제품의 인증을 표시하는 문서가 아닙니다.

## 서비스와 스킬 형식의 공식 근거

| 공식 자료 | 이 가이드에서 확인한 내용 | 적용 범위 |
|---|---|---|
| [Google: Gemini Apps 스킬](https://support.google.com/gemini/answer/17094296?hl=en) | 파일 업로드, 활성화·자동 적용, 다른 스킬 참조, 교체 | Gemini Apps. CLI의 명령과 구분 |
| [Anthropic: Claude 스킬 사용](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | 코드 실행·파일 생성, 업로드와 활성화 | 계정·조직 설정 확인 |
| [Anthropic: 사용자 지정 스킬 작성](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) | 스킬 폴더를 포함하는 ZIP 구조 | Claude용 패키지 구성 |
| [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) | 이용 대상, Skills 메뉴와 업로드 검사 | 제공 계정·워크스페이스에 한함 |
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | 이름·설명·지침 구조와 명시적·자동 선택 | 제품별 호출 방식 구분 |
| [OpenAI: Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) | 프로젝트 지침과 파일 자료 | 네이티브 스킬과 별도 방식 |
| [GitHub: Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | SKILL.md와 메타데이터, 보조 자료, 요청에 따른 선택 | 공통 형식 참고. 저장소 skills/를 자동 설치 경로로 간주하지 않음 |
| [Agent Skills 규격](https://agentskills.io/specification) | 이름·설명·참조 구조와 단계적 자료 읽기 | 플랫폼별 세부 수용 여부는 별도 확인 |

문서의 등록 단계는 위 자료를 기준으로 작성했습니다. 정확한 노출 메뉴·기능 제공 여부는 사용하는 계정에서 확인하세요. 어떤 창작 스킬을 어떤 순서로 조합할지는 이 저장소가 설계한 규칙이며, 공식 문서의 보증이나 추천 조합을 뜻하지 않습니다.

## 창작 원리의 참고 자료

아래 자료의 일반 원리를 바탕으로 한국어 작업 절차를 구성했습니다. 원문의 전체 질문·문장을 번역한 자료나 특정 작가의 문체 복제 지침은 아닙니다.

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
