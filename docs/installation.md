# 설치와 공통 사용법

이 문서는 Gemini CLI를 기준으로 합니다. Gemini 웹 앱의 사용자 지정 MCP 연결 화면은 스킬 설치 화면이 아닙니다. 웹 앱에서 폴더형 스킬을 직접 설치하거나 references를 자동으로 읽는 기능은 이 저장소에서 검증하지 않았습니다.

## 준비

Git과 Gemini CLI를 설치하고 GitHub 비공개 저장소 읽기 권한으로 인증합니다. 원고 프로젝트의 PowerShell에서 실행하세요.

```powershell
git clone https://github.com/paakseongjin/fantasy-novel-skills.git
New-Item -ItemType Directory -Force .agents/skills | Out-Null
Copy-Item -Recurse fantasy-novel-skills/skills/write-fantasy-prose .agents/skills/
Copy-Item -Recurse fantasy-novel-skills/skills/audit-fantasy-canon .agents/skills/
gemini
```

기존에 같은 이름의 스킬이 있다면 백업하고 차이를 확인한 후 교체하세요. `references` 폴더도 함께 복사해야 합니다. Gemini CLI에서 `/skills`를 실행해 두 스킬의 인식 여부를 확인합니다. 표시되지 않으면 현재 작업 폴더, 경로, 파일명을 확인하고 CLI를 다시 시작하세요. 호출 시 권한 확인이 나타나면 내용을 확인하세요.

## 기본 작업

1. 작품별 폴더에 승인된 설정과 원고를 준비합니다. 자료의 출처와 확정 여부를 명시합니다.
2. 집필 스킬에 장면 목표와 시점, 분량, 기존 설정을 제공합니다.
3. 작성 후 감사 스킬에 원고와 정전 자료를 함께 제공하고 충돌 근거를 요청합니다.
4. 제안은 작가가 검토하고 명시적으로 승인한 뒤 작품 파일에 반영합니다.

스킬은 지침이며 데이터를 자동으로 기억하거나 모든 오류를 검출하지 않습니다. 원고를 변경하기 전 별도 백업을 유지하세요.

Google 참고: [Gemini CLI 에이전트 스킬 실습](https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli?hl=ko) (확인: 2026-11-14).
