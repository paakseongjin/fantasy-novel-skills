# 설치 및 사용: ChatGPT · Claude · Gemini

공식 안내 확인일: **2026-11-14**. 웹에서 등록한 뒤 사용하는 절차를 기준으로 합니다. 계정·워크스페이스·앱에 따라 메뉴와 동기화 범위가 다릅니다. 실제 사용자 계정에 설치한 결과를 보증하는 문서는 아닙니다.

## 1. 파일 내려받기

장편 창작 신규 7개만 필요하다면 [장편 스킬 묶음](../downloads/fantasy-longform-seven-skills.zip)을 내려받을 수 있습니다. 웹소설 연재 점검 4개만 필요하다면 [웹소설 연재 스킬 묶음](../downloads/fantasy-webnovel-serial-skills.zip)을 사용하세요. 바깥 ZIP을 풀어 서비스별 개별 ZIP을 각각 등록하세요. 프로젝트용 문서도 포함됩니다.

1. 로그인한 GitHub에서 이 저장소를 엽니다. 비공개 저장소 접근 권한이 필요합니다.
2. **Code → Download ZIP**으로 저장소 전체를 내려받아 풉니다. 저장소 ZIP 자체는 스킬 업로드 파일이 아닙니다.
3. [스킬 목록](catalog.md)에서 필요한 스킬을 고르고, 서비스에 맞는 `dist` 폴더의 **개별 ZIP**을 선택합니다. 개별 ZIP은 다시 압축하지 않습니다.
4. 기본 스킬은 집필·세계관·장편 7개·웹소설 연재 4개를 합쳐 17개입니다. 세계관 통합형 대신 분야별 8개 중 필요한 것만 골라도 됩니다.

| 서비스/방식 | 파일 | 패키지 구조 |
|---|---|---|
| ChatGPT 스킬 업로드 메뉴가 있는 계정 | [dist/chatgpt](../dist/chatgpt) | 스킬명 폴더 안에 SKILL.md와 참고 파일 |
| ChatGPT 프로젝트 방식 | [프로젝트 지침](../platforms/chatgpt/project-instructions.md) + [단일 문서](../dist/chatgpt-project) | 지침 복사 + Markdown 업로드 |
| Claude 사용자 지정 스킬 | [dist/claude](../dist/claude) | 스킬명 폴더 안에 SKILL.md와 참고 파일 |
| Gemini Apps 스킬 | [dist/gemini](../dist/gemini) | ZIP 최상위에 SKILL.md와 references |

## 2. ChatGPT

### 스킬 업로드 메뉴가 있는 경우

OpenAI 도움말은 대상 Business·Enterprise·Healthcare·Edu 계정에서의 제공을 설명합니다. 모든 개인 요금제와 앱에서 동일하게 제공된다고 가정하지 마세요.

1. 사이드바 **Plugins → Skills → Create → Upload from your computer**를 엽니다.
2. `dist/chatgpt/<스킬명>.zip`을 선택하고 화면의 등록 절차를 완료합니다.
3. 새 대화에서 스킬 이름과 작업을 명시하고 아래 확인 예제로 동작을 점검합니다.

ChatGPT ZIP은 표준 SKILL.md 폴더를 묶은 배포물입니다. 공식 도움말은 업로드 메뉴를 안내하지만 이 ZIP을 실제 계정에서 시험한 것은 아닙니다. 파일 선택창에서 ZIP을 받지 않으면 압축을 풀어 제공되는 폴더 업로드/편집 방식으로 등록하거나 아래 프로젝트 방식을 사용하세요. 다른 OpenAI 제품에서의 설치가 웹·앱에 자동 동기화된다고 가정하지 않습니다.

### 스킬 메뉴가 없는 경우: 프로젝트 지침·자료

1. 새 프로젝트를 만들고 프로젝트 지침을 엽니다.
2. [project-instructions.md](../platforms/chatgpt/project-instructions.md) 본문을 붙여 넣고 저장합니다.
3. `dist/chatgpt-project`의 필요한 `.md` 파일을 자료에 올립니다. 처음에는 `build-fantasy-world.md`, `write-fantasy-prose.md`, `audit-fantasy-canon.md`부터 시작해도 됩니다.
4. 원고·확정 설정·연표는 작품명과 버전을 표시한 별도 자료로 추가합니다.
5. 프로젝트 안에서 `build-fantasy-world 자료의 명칭 지침을 적용해…`처럼 요청합니다.

단일 문서에는 스킬 본문과 참고 파일이 함께 들어 있습니다. 같은 이름의 SKILL.md 여러 개를 올리거나 상대 폴더 경로를 재현할 필요가 없습니다. 이 방식은 네이티브 설치와 별개이며 자동 호출·모든 자료의 완전한 열람을 보장하지 않습니다. 웹·앱에서 같은 프로젝트를 열어 자료가 보이는지 확인하세요.

## 3. Claude

1. 설정 **Capabilities**에서 코드 실행·파일 생성 기능을 활성화합니다. 이 팩에 실행 코드는 없지만 Claude 스킬 기능에는 해당 설정이 요구됩니다.
2. **Customize → Skills**에서 추가/생성 → 스킬 업로드를 선택합니다.
3. `dist/claude/<스킬명>.zip`을 업로드하고 활성화합니다. ZIP 안의 첫 폴더가 스킬명이고 그 안에 SKILL.md가 있습니다.
4. 새 대화에서 스킬 이름을 지정해 요청하고 작품별 정전·원고도 제공합니다.
5. 앱에 등록 메뉴가 없으면 웹에서 진행한 뒤, 사용할 앱에서 스킬이 보이고 적용되는지 확인합니다.

## 4. Gemini Apps

1. 성인 계정으로 로그인한 뒤 웹의 **Customize → Skills → Create → Upload**를 엽니다. Customize가 없으면 More를 확인합니다.
2. `dist/gemini/<스킬명>.zip`을 업로드합니다. ZIP 최상위에 SKILL.md가 있습니다.
3. 내용을 검토하고 Create로 등록합니다.
4. 대화에서 `/` 또는 갱신된 단축키 `@`로 스킬을 선택하거나 이름을 명시해 요청합니다.
5. 참고 자료를 수정했으면 참고 파일이 포함된 전체 스킬을 다시 업로드합니다.

Google은 웹·모바일·Mac 앱의 스킬을 안내합니다. **Keep Activity를 꺼도 스킬은 사용할 수 있습니다.** 다만 이에 의존하는 Connected Apps 기능은 제한됩니다. 이 팩은 외부 연결 없이 작동하는 Markdown 지침·예시입니다.

## 5. 설치 확인과 갱신

```text
audit-fantasy-canon을 적용해 다음을 검토해 줘.
확정 설정: 마법 한 번에 기억 하나를 소모한다.
원고: 주인공은 아무 대가 없이 마법을 사용했다.
충돌 후보의 두 근거와 확인해야 할 예외를 제시해 줘.
새 예외를 만들어 확정하지 마.
```

```text
refine-natural-korean을 적용해 다음 문장을 다듬어 줘.
“그는 문을 열 수 있었다. 그러나 끝내 손잡이에 손을 대지 않았다.”
가능성을 실제 행동으로 바꾸지 말고 수정한 본문만 출력해 줘.
```

GitHub 변경은 설치된 스킬에 자동 반영되지 않습니다. 최신 파일을 내려받아 기존 항목의 갱신 절차를 따르고 중복 활성화를 피하세요. 프로젝트 방식은 기존 자료를 최신 `.md`로 교체합니다. 작품 정전·원고는 별도로 관리합니다.

## 공식 자료

- [OpenAI: Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI: Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- [Anthropic: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Anthropic: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Google: Create & manage skills for Gemini Apps](https://support.google.com/gemini/answer/17094296?hl=en)
