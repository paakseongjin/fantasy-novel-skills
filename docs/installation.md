# 설치 및 사용: Gemini · Claude · ChatGPT

[가이드 홈](index.md) · [빠른 시작](quickstart.md) · [다운로드](catalog.md)

공식 안내 확인일: **2026-11-15**. 이 문서는 웹 화면의 등록 절차를 기준으로 합니다. 계정·워크스페이스·앱 버전에 따라 표시되는 메뉴가 다를 수 있습니다.

## 1. 파일 내려받기

| 사용하는 환경 | 선택할 파일 | 이 저장소의 파일 구조 |
|---|---|---|
| Gemini Apps | [dist/gemini](../dist/gemini)의 개별 ZIP | ZIP 루트에 `SKILL.md`, 필요하면 `references/` |
| Claude | [dist/claude](../dist/claude)의 개별 ZIP | 스킬명 폴더 안에 `SKILL.md`와 참고 자료 |
| ChatGPT Skills | [dist/chatgpt](../dist/chatgpt)의 개별 ZIP | 스킬명 폴더 안에 `SKILL.md`와 참고 자료 |
| ChatGPT 프로젝트 | [프로젝트 지침](../platforms/chatgpt/project-instructions.md) + [단일 문서](../dist/chatgpt-project) | 지침 복사와 문서 업로드 |

개별 ZIP은 [스킬 목록](catalog.md)의 링크를 열어 내려받습니다. **Code → Download ZIP**으로 저장소 전체를 받았다면 압축을 풀고 `dist`에서 개별 ZIP을 찾으세요. [장편 7개 묶음](../downloads/fantasy-longform-seven-skills.zip)과 [연재 점검 4개 묶음](../downloads/fantasy-webnovel-serial-skills.zip)도 먼저 풀어야 합니다. 바깥 묶음은 등록 파일이 아닙니다.

## 2. Gemini Apps

Google 공식 안내는 스킬의 자동 적용과 여러 스킬의 조합을 지원하며, 스킬 지침에서 다른 스킬을 참조할 수 있다고 설명합니다. [공식 도움말](https://support.google.com/gemini/answer/17094296?hl=en)

1. 웹 사이드바에서 **Customize → Skills**를 엽니다. Customize가 보이지 않으면 More를 확인합니다.
2. **Create → Upload**를 선택하고 Gemini용 개별 ZIP을 업로드합니다.
3. 이름·설명·지침과 참고 자료를 확인한 뒤 **Create**로 등록합니다.
4. 활성화 상태를 확인하고 새 대화에서 스킬 이름과 작업을 명시합니다. `/` 또는 갱신된 화면의 `@`로 선택할 수도 있습니다.

성인 계정이 필요합니다. Keep Activity를 끈 상태에서도 스킬 자체는 사용할 수 있으며, 연결 앱 기능의 이용 조건은 별개입니다. 이 팩의 기본 집필 작업은 대화에 제공한 자료로 수행할 수 있습니다.

기존 창작 스킬 17개를 등록했다면 [라우터 ZIP](../dist/gemini/route-fantasy-writing.zip)만 추가할 수 있습니다. 같은 이름이 이미 있으면 해당 스킬의 **More → Replace skill**로 교체하세요. 참고 파일을 변경할 때는 전체 스킬을 다시 업로드합니다.

## 3. Claude

Claude는 사용자 지정 스킬 폴더를 ZIP으로 업로드하는 방식을 안내합니다. 코드 실행·파일 생성 기능과 조직의 스킬 이용 설정을 먼저 확인합니다. [사용 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [패키지 구조](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

1. 개인 계정은 **Settings → Capabilities**에서 코드 실행·파일 생성을 켭니다. 갱신된 설정에서는 **Create and edit files**로 표시될 수 있습니다.
2. **Customize → Skills**에서 추가 버튼 → **Create skill → Upload a skill**을 선택합니다.
3. Claude용 개별 ZIP을 업로드합니다. ZIP 안의 스킬명 폴더에 `SKILL.md`가 있어야 합니다.
4. 목록에서 활성화한 뒤 스킬 이름을 지정해 작은 작업을 요청합니다.

Team·Enterprise에서는 조직 정책에 따라 생성·업로드 또는 코드 실행이 제한될 수 있습니다. 메뉴가 없거나 비활성 상태면 계정 설정과 조직 권한을 확인하세요. 스킬이 활성화되어도 실제 요청 결과는 검토해야 합니다.

## 4. ChatGPT

### Skills 메뉴가 제공되는 계정

공식 도움말은 대상 Business·Enterprise·Healthcare·Edu 사용자의 이용을 안내하며, 워크스페이스 설정과 제공 여부에 따라 접근이 달라집니다. [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

1. 사이드바 **Plugins → Skills**로 이동합니다.
2. **Create → Upload from your computer**를 엽니다.
3. 업로드 화면에서 지원하는 방식으로 ChatGPT용 파일을 등록합니다. ZIP을 받지 않는 화면에서는 압축을 풀고 제공되는 파일·폴더 또는 편집 방식을 따릅니다.
4. 업로드 검사와 등록 상태를 확인한 뒤 스킬 이름을 지정해 요청합니다. 선택 메뉴가 있으면 `@`로 지정할 수 있습니다. [스킬 사용·형식 안내](https://learn.chatgpt.com/docs/build-skills)

이 저장소의 ZIP 구조 검사와 실제 ChatGPT 업로드 수용 여부는 별개의 확인 항목입니다. 검사에서 검토 필요나 차단으로 표시되면 화면의 사유를 확인하세요.

### 프로젝트에 자료로 추가하는 방식

스킬 메뉴가 없다면 프로젝트의 지침·자료 기능을 사용할 수 있습니다. 프로젝트에서 사용할 수 있는 기능과 파일 수는 계정 설정에 따릅니다. [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)

1. 새 프로젝트를 만들고 [프로젝트 지침](../platforms/chatgpt/project-instructions.md)을 지침 칸에 붙여 넣습니다.
2. [프로젝트용 문서](../dist/chatgpt-project)에서 필요한 `.md` 파일을 자료로 추가합니다.
3. 작품의 설정집과 원고를 별도 자료로 추가합니다.
4. “업로드한 write-fantasy-prose.md 자료를 적용해…”처럼 요청합니다.

단일 문서 안에는 원본 지침과 참고 자료가 함께 있습니다. 상대 경로의 파일을 읽으라는 지시는 해당 문서의 같은 이름을 가진 자료 절을 참고한다는 뜻입니다. 선택형 세계관 8개의 프로젝트 문서는 별도로 생성하지 않으므로 통합형 문서의 관련 분야를 이용하세요.

이 방식은 네이티브 스킬 등록이 아닙니다. 라우터 문서를 사용할 때도 다른 전문 지침을 프로젝트에 제공해야 합니다.

## 5. 설치 확인과 갱신

등록 후 [빠른 시작의 확인 예제](quickstart.md)를 실행합니다. 목록에 이름이 표시되는지, 필요한 참고 자료가 읽히는지, 결과가 요청 조건을 지키는지를 따로 확인하세요.

GitHub 파일은 등록된 스킬에 자동 동기화되지 않습니다. 새 ZIP으로 해당 서비스의 교체 절차를 따르고, 프로젝트 방식에서는 이전 문서와 새 문서가 혼재하지 않게 정리합니다. 구체적인 교체·복구 순서는 [업데이트 안내](versions.md)에 있습니다.

등록이 안 되거나 호출되지 않으면 [문제 해결](troubleshooting.md)을 확인하세요. 서비스 제공 조건의 근거와 이 저장소의 검증 범위는 [공식 자료](sources.md)와 [패키지 검증](maintenance.md)에 정리되어 있습니다.
