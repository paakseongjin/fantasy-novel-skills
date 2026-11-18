# 설치 및 사용: Gemini · Claude · ChatGPT

[가이드 홈](index.md) · [빠른 시작](quickstart.md) · [다운로드](catalog.md)

**2026-11-18**에 서비스별 설치 안내를 공식 문서와 대조했습니다. 계정·워크스페이스·앱 버전에 따라 표시되는 메뉴가 다를 수 있습니다. 실제 계정에서는 등록 후 [첫 요청](quickstart.md#3-첫-요청을-보내세요)으로 확인하세요.

## 1. 파일 내려받기

| 사용하는 환경 | 선택할 파일 | 이 저장소의 파일 구조 |
|---|---|---|
| Gemini Apps | [dist/gemini](../dist/gemini)의 개별 ZIP | ZIP 루트에 `SKILL.md`, 필요하면 `references/` |
| Claude | [dist/claude](../dist/claude)의 개별 ZIP | 스킬명 폴더 안에 `SKILL.md`와 참고 자료 |
| ChatGPT Skills 업로드 가능 계정 | [dist/chatgpt](../dist/chatgpt)의 배포 ZIP | 스킬명 폴더 안에 `SKILL.md`와 참고 자료. 업로드 형식은 계정 화면에서 확인 |
| ChatGPT 프로젝트 | [프로젝트 지침](../platforms/chatgpt/project-instructions.md) + [단일 문서](../dist/chatgpt-project) | 지침 복사와 문서 업로드 |

설치 파일을 열어 보면 `SKILL.md` 끝에 해당 서비스의 적용 지침이 있습니다. Gemini Apps는 업로드한 참고 파일과 활성 스킬, Claude는 스킬 폴더와 상대 경로, ChatGPT Skills는 현재 대화에서 선택한 스킬과 제공된 자료를 기준으로 작업합니다.

개별 ZIP은 [스킬 목록](catalog.md)의 링크를 열고 파일 화면의 **Download raw file** 버튼으로 저장합니다. 저장소에서 **Code → Download ZIP**을 누르면 선택한 브랜치 전체가 내려받아집니다. 압축을 풀고 `dist`에서 서비스별 개별 스킬 파일을 찾으세요. [GitHub의 소스 아카이브 안내](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)

[장편 7개 묶음](../downloads/fantasy-longform-seven-skills.zip)과 [연재 점검 4개 묶음](../downloads/fantasy-webnovel-serial-skills.zip)도 먼저 풀고 사용할 서비스의 개별 파일을 선택합니다.

## 2. Gemini Apps

Google 공식 안내는 스킬의 자동 적용과 여러 스킬의 조합을 지원하며, 스킬 지침에서 다른 스킬을 참조할 수 있다고 설명합니다. [공식 도움말](https://support.google.com/gemini/answer/17094296?hl=en)

1. [Gemini 웹 앱](https://gemini.google.com/)에서 사이드바 **Customize → Skills**를 엽니다. Customize가 보이지 않으면 More를 확인합니다. 파일을 올려 등록하는 경로는 웹 앱에서 이용합니다.
2. **Create → Upload**를 선택하고 Gemini용 개별 ZIP을 엽니다.
3. **Upload**를 누르고 이름·설명·지침과 참고 자료를 확인한 뒤 **Create**로 등록합니다.
4. 활성화 상태를 확인합니다. 새 대화의 입력창에 `/`를 입력해 스킬을 고릅니다. 화면에 새 단축키가 적용됐다면 `@`를 사용합니다.

성인 계정이 필요합니다. Keep Activity를 끈 상태에서도 스킬 자체는 사용할 수 있으며, 연결 앱 기능의 이용 조건은 별개입니다. 이 팩의 기본 집필 작업은 대화에 제공한 자료로 수행할 수 있습니다.

여러 작업을 연결하려면 필요한 전문 스킬과 [라우터 ZIP](../dist/gemini/route-fantasy-writing.zip)을 각각 등록합니다. 같은 이름이 이미 있으면 **More → Replace skill**을 선택하고 저장합니다. 참고 자료를 갱신할 때는 해당 스킬의 전체 ZIP을 다시 올립니다.

## 3. Claude

Claude는 사용자 지정 스킬 폴더를 ZIP으로 업로드하는 방식을 안내합니다. 새 화면에서는 사이드바의 **Customize**가 **Plugins**로 바뀌고, 통합 화면에서 스킬을 찾을 수 있습니다. Anthropic은 Enterprise의 전환을 2026년 11월 30일로 안내합니다. [사용 안내](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [패키지 구조](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [통합 화면 안내](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

1. 개인 계정은 **Settings → Capabilities**에서 코드 실행·파일 생성을 켭니다. 갱신된 설정에서는 **Create and edit files**로 표시됩니다. Team·Enterprise의 조직 설정은 관리자가 **Organization settings → Plugins & skills → Policy**에서 확인합니다.
2. **Customize → Skills**를 엽니다. 새 화면에서는 **Plugins**를 열고 스킬을 찾습니다. 사용자 지정 스킬을 추가하는 메뉴에서 **Create skill → Upload a skill**을 선택합니다.
3. Claude용 개별 ZIP을 업로드합니다. ZIP 안의 스킬명 폴더에 `SKILL.md`가 있어야 합니다.
4. 목록에서 활성화한 뒤 스킬 이름과 작업을 프롬프트에 적습니다. 새 화면에서는 대화 입력창의 **+** 또는 `/`로 스킬을 고를 수도 있습니다. 적용 여부는 응답과 화면에서 확인합니다.

Team·Enterprise에서는 조직 정책에 따라 생성·업로드 또는 코드 실행이 제한될 수 있습니다. 메뉴가 없거나 비활성 상태면 계정 설정과 조직 권한을 확인하세요. 스킬이 활성화되어도 실제 요청 결과는 검토해야 합니다.

## 4. ChatGPT

### Skills 메뉴가 제공되는 계정

공식 도움말은 대상 Business·Enterprise·Healthcare·Edu 사용자의 이용을 안내하며, 워크스페이스 설정과 제공 여부에 따라 접근이 달라집니다. [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

1. 사이드바 **Plugins → Skills**로 이동합니다.
2. **Create → Upload from your computer**를 엽니다.
3. 업로드 화면에서 형식을 확인하고 ZIP을 받을 경우 ChatGPT용 개별 ZIP을 선택합니다. 다른 형식이 표시되면 화면의 안내를 따릅니다. 원본과 참고 자료를 함께 쓰는 대안으로 아래의 프로젝트 방식도 있습니다. 공식 도움말은 컴퓨터 업로드 절차를 안내하며, 이 팩의 ZIP 수용 여부는 실제 화면에서 확인해야 합니다.
4. 업로드 검사와 등록 상태를 확인한 뒤 입력창에서 `@`로 스킬을 선택하고 작업을 요청합니다. [스킬 사용·형식 안내](https://learn.chatgpt.com/docs/build-skills)

검사에서 검토 필요나 차단으로 표시되면 화면의 사유를 확인하세요.

### 프로젝트에 자료로 추가하는 방식

스킬 메뉴가 없다면 프로젝트의 지침·자료 기능을 사용할 수 있습니다. 프로젝트에서 사용할 수 있는 기능과 파일 수는 계정과 요금제에 따릅니다. [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) · [파일 업로드 형식](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt)

1. 새 프로젝트를 열고 **더보기(···) → 프로젝트 설정(Project settings)**에서 [프로젝트 지침](../platforms/chatgpt/project-instructions.md)을 붙여 넣습니다.
2. 소스 영역의 **소스 추가(Add sources)**에서 [프로젝트용 문서](../dist/chatgpt-project) 중 필요한 `.md` 파일을 추가합니다.
3. 작품의 설정집, 공개본 발췌, 회차 인계, 문체 카드를 필요한 만큼 별도 자료로 추가합니다.
4. “업로드한 write-fantasy-prose.md 자료를 적용해…”처럼 요청합니다.

단일 문서 안에는 원본 지침과 참고 자료가 함께 있습니다. 상대 경로의 파일을 읽으라는 지시는 해당 문서의 같은 이름을 가진 자료 절을 참고한다는 뜻입니다. 선택형 세계관 8개의 프로젝트 문서는 별도로 생성하지 않으므로 통합형 문서의 관련 분야를 이용하세요.

프로젝트에서는 업로드한 문서 이름으로 지침을 요청합니다. 라우터 문서와 함께 해당 작업에 필요한 전문 문서도 추가합니다.

## 5. 설치 확인과 갱신

등록 후 [빠른 시작의 확인 예제](quickstart.md)를 실행합니다. 목록에 이름이 표시되는지, 필요한 참고 자료가 읽히는지, 결과가 요청 조건을 지키는지를 따로 확인하세요.

GitHub 파일은 등록된 스킬에 자동 동기화되지 않습니다. 새 ZIP으로 해당 서비스의 교체 절차를 따르고, 프로젝트 방식에서는 이전 문서와 새 문서가 혼재하지 않게 정리합니다. 구체적인 교체·복구 순서는 [업데이트 안내](versions.md)에 있습니다.

등록이 안 되거나 호출되지 않으면 [문제 해결](troubleshooting.md)을 확인하세요. 서비스 제공 조건의 근거와 이 저장소의 검증 범위는 [공식 자료](sources.md)와 [패키지 검증](maintenance.md)에 정리되어 있습니다.
