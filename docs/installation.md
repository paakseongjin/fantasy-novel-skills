# 설치 및 사용: 웹과 앱

기준일: 2026-11-14. 다음은 서비스별로 다른 등록 방식입니다. ZIP의 형식이 다르므로 해당 서비스의 파일을 사용하세요. 다운로드와 설치 후 계정에서 인식 여부를 직접 확인해야 합니다.

## 공통 준비

GitHub에서 저장소를 열고 **Code → Download ZIP**으로 전체를 내려받아 압축을 풉니다. 비공개 저장소이므로 로그인된 계정으로 접근해야 합니다. `dist`의 ZIP은 다시 풀지 않고 해당 서비스에 업로드합니다. GitHub의 ZIP 파일 화면에서 다운로드 버튼을 이용해 개별 ZIP을 받아도 됩니다. 모바일에서는 파일 앱에서 다운로드한 파일의 위치를 확인하세요.

| 서비스 | 등록 형태 | 파일 |
|---|---|---|
| Gemini Apps | 스킬별 ZIP 업로드 | `dist/gemini/` |
| Claude | 사용자 지정 스킬별 ZIP 업로드 | `dist/claude/` |
| ChatGPT | 프로젝트 지침 + 프로젝트 자료 | `platforms/chatgpt/` 및 `skills/` |

## Gemini 웹 및 모바일 앱

Google 안내상 스킬 이용에는 성인 계정, 로그인 및 Gemini 앱 활동 사용 설정이 필요합니다. 제공 국가·계정·메뉴는 달라질 수 있습니다.

1. 웹에서 Gemini → 메뉴 → Customize(맞춤설정) → Skills(스킬)로 이동합니다. 메뉴가 안 보이면 더보기를 확인합니다.
2. Create → Upload를 선택하고 `dist/gemini/write-fantasy-prose.zip`을 등록합니다. 검토 후 저장합니다.
3. 같은 방법으로 `dist/gemini/audit-fantasy-canon.zip`을 등록합니다. ZIP의 최상위에는 `SKILL.md`가 있습니다.
4. 대화에서 `/` 또는 지원되는 경우 `@`를 입력해 스킬을 선택하거나 이름을 명시해 요청합니다. 활성화된 스킬은 관련 작업에 자동으로 사용될 수도 있습니다.
5. 모바일 앱에서는 등록된 스킬을 사용합니다. Google의 안내상 파일·폴더 업로드는 웹에서 진행하며, 참고 파일을 갱신하려면 전체 스킬을 다시 업로드해야 합니다. 모바일 앱에서 메뉴가 다르면 웹에서 설정하세요.

## Claude 웹 및 앱

1. 개인 계정에서 설정 → Capabilities(기능) → 코드 실행 및 파일 생성(또는 파일 만들기 및 편집)을 켭니다. 조직 계정은 관리자 정책을 확인합니다.
2. Customize → Skills → 추가/업로드에서 `dist/claude/write-fantasy-prose.zip`을 업로드하고 활성화합니다.
3. `dist/claude/audit-fantasy-canon.zip`도 같은 방식으로 등록합니다. Claude ZIP은 최상위에 스킬 폴더가 있고 그 안에 `SKILL.md`가 있습니다.
4. 새 대화에서 스킬 이름과 작업을 명시하고 결과의 적용 여부를 확인합니다. 모바일·데스크톱의 업로드 메뉴 제공 여부는 계정과 앱 버전에 따라 확인하세요. 메뉴가 없으면 웹에서 등록 후 앱에서 사용을 확인합니다.
5. 원고와 확정 설정은 프로젝트 지식에 따로 넣습니다. Claude는 프로젝트 내 다른 대화의 내용을 자동으로 공유하지 않으므로 필요한 내용은 프로젝트 지식에 추가해야 합니다.

## ChatGPT 웹 및 앱

ChatGPT 대화에서 다음은 **프로젝트 지침과 참고 자료를 사용하는 구성**이며, Claude/Gemini의 스킬 ZIP을 설치하는 절차가 아닙니다.

1. 새 프로젝트를 만들고 프로젝트 메뉴 `···` → 프로젝트 설정/지침을 엽니다.
2. `platforms/chatgpt/project-instructions.md` 내용을 복사해 프로젝트 지침에 붙여 넣고 저장합니다.
3. 프로젝트 자료에 `skills/write-fantasy-prose/SKILL.md`와 `skills/audit-fantasy-canon/SKILL.md`를 추가합니다. 이름이 같으므로 다운로드할 때 각각 `write-fantasy-prose.md`, `audit-fantasy-canon.md`로 구분하세요. 각각의 `references` 문서도 필요한 것을 개별로 추가합니다. ZIP을 자료로 넣으면 내부 파일이 자동 인식된다고 가정하지 마세요.
4. 작품별 확정 세계관과 해당 원고를 별도 자료로 추가합니다. 자료 제목·버전·승인 상태를 구분합니다.
5. 프로젝트 대화에서 “집필 지침을 사용해…” 또는 “설정 감사 지침을 사용해…”라고 요청합니다. 모바일과 웹에서 같은 프로젝트를 열어 사용하되 설정 메뉴는 버전에 따라 다를 수 있습니다.

## 확인과 갱신

각 서비스에서 동일한 짧은 시험을 합니다: `확정 설정: 마법은 기억 하나를 소모한다. 원고: 아무 대가 없이 사용했다. 감사 지침으로 두 근거와 확인할 예외를 제시해 줘.` 확인된 충돌 후보로 다루고 예외 유무를 확인하는지 점검하세요. 새 설정을 자동 확정하지 않는지도 확인합니다. 실제 활용에는 관련 정전과 원고를 제공해야 합니다.

GitHub에서 파일을 변경해도 이미 등록한 스킬이나 프로젝트 자료에 자동 반영된다고 가정하지 마세요. 최신 ZIP을 내려받아 서비스의 갱신 절차를 따르고, ChatGPT 프로젝트 자료도 교체한 뒤 다시 시험하세요.

## 공식 자료

- [Google: Gemini 앱 스킬 생성 및 관리](https://support.google.com/gemini/answer/17094296?hl=en)
- [Anthropic: Claude에서 스킬 사용](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Anthropic: 사용자 지정 스킬 만들기](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Anthropic: 프로젝트 관리](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [OpenAI: ChatGPT 프로젝트](https://help.openai.com/ko-kr/articles/10169521-projects-in-chatgpt)
