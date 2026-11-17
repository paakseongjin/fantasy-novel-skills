# 판타지 소설 스킬

**세계관 구상부터 장편 구성, 회차 집필, 퇴고와 설정 검토까지.** 한국어 판타지·웹소설 작업에 필요한 지침을 ChatGPT, Claude, Gemini에서 사용할 수 있는 스킬로 제공합니다.

[빠른 시작](docs/quickstart.md) · [설치 안내](docs/installation.md) · [스킬 다운로드](docs/catalog.md) · [전체 사용 가이드](docs/index.md)

## 무엇을 할 수 있나요?

설정과 원고, 원하는 작업을 전달하면 해당 스킬이 작업 기준과 순서를 안내합니다. 여러 작업을 연결할 때는 **`route-fantasy-writing`**이 필요한 전문 스킬을 고르고 단계별 결과를 이어 줍니다. 문장 하나를 다듬는 일부터 다음 회차를 구성하고 쓰는 일까지, 요청한 범위에 맞춰 사용할 수 있습니다.

| 지금 필요한 작업 | 시작할 스킬 | 자세히 보기 |
|---|---|---|
| 자연어 요청으로 여러 작업을 연결 | `route-fantasy-writing` | [스킬 조합·라우팅](docs/route-fantasy-writing.md) |
| 지리·마법·국가가 연결된 세계 설계 | `build-fantasy-world` | [세계관 설계](docs/worldbuilding.md) |
| 장편의 사건과 결말 구성 | `plan-fantasy-longform` | [장편 플롯](docs/plan-fantasy-longform.md) |
| 다음 화의 목표·장면·끝맺음 구성 | `structure-serial-chapters` | [회차 구성](docs/structure-serial-chapters.md) |
| 장면이나 회차의 실제 본문 집필 | `write-fantasy-prose` | [본문 집필](docs/write-fantasy-prose.md) |
| 한 장면의 인물 동기·관계 갈등 보완 | `write-character-conflict` | [인물 심리·관계 갈등](docs/write-character-conflict.md) |
| 인물별 대사·말투·호칭 보완 | `craft-character-dialogue` | [대사·인물별 말투](docs/craft-character-dialogue.md) |
| 공간·감각·동선 묘사 보완 | `write-immersive-scenes` | [공간·감각·동선 묘사](docs/write-immersive-scenes.md) |
| 사건과 말투를 유지하며 문장 퇴고 | `refine-natural-korean` | [한국어 퇴고](docs/refine-natural-korean.md) |
| 확정 설정과 원고의 모순 확인 | `audit-fantasy-canon` | [정전·연속성 검토](docs/audit-fantasy-canon.md) |
| 프롤로그·초반의 정보 부담 줄이기 | `lower-opening-barrier` | [초반 진입장벽](docs/lower-opening-barrier.md) |
| 중후반 반복과 보상 지연 줄이기 | `prevent-serial-drag` | [중후반 연재 정체](docs/prevent-serial-drag.md) |
| 여러 구간의 하차 위험과 수정 순서 점검 | `audit-dropout-risks` | [하차 위험 점검](docs/audit-dropout-risks.md) |

[전체 26개 스킬과 다운로드](docs/catalog.md)에서 인물 성장, 복선, 전투, 독자 애착 등 다른 작업도 찾을 수 있습니다.

## 처음 사용한다면

1. **작업 하나를 고릅니다.** 문장 퇴고부터 시험하려면 `refine-natural-korean`만 있으면 됩니다.
2. **사용 환경에 맞는 자료를 추가합니다.** Gemini와 Claude는 개별 ZIP을 사용합니다. ChatGPT에서는 Skills 업로드가 제공되는지 확인하거나 프로젝트 지침과 문서를 추가합니다. [설치 안내](docs/installation.md)
3. **원고와 보존 조건을 함께 전달합니다.** 아래처럼 작은 요청으로 시작하세요.

```text
refine-natural-korean을 적용해 다음 문장의 번역투와 호응만 다듬어 줘.
사건, 시점, 가능성의 의미는 유지하고 수정 본문만 보여 줘.

그는 그 문을 개방하는 것이 가능했으나 끝내 손잡이에 손을 대지 않았다.
```

가능성을 실제 행동으로 바꾸지 않았는지 확인합니다. 설치부터 첫 결과 확인까지의 설명은 [빠른 시작](docs/quickstart.md)에 있습니다.

### 여러 작업을 연결하려면

필요한 전문 스킬과 함께 `route-fantasy-writing`을 등록하세요. 예를 들어 다음 화의 구성과 본문을 모두 요청하려면 `structure-serial-chapters`와 `write-fantasy-prose`를 준비합니다. 서비스별 조합 방식과 라우터 파일은 [라우터 사용법](docs/route-fantasy-writing.md)에 있습니다.

## 서비스별 이용 방법

| 사용하는 환경 | 받을 자료 | 등록 방식 |
|---|---|---|
| Gemini Apps | [Gemini 개별 ZIP](dist/gemini) | Skills에서 파일 업로드 |
| Claude | [Claude 개별 ZIP](dist/claude) | Skills에서 파일 업로드 |
| ChatGPT Skills 업로드 가능 계정 | [ChatGPT용 배포 ZIP](dist/chatgpt) | Plugins → Skills에서 업로드 형식 확인 |
| ChatGPT 프로젝트 | [프로젝트 지침](platforms/chatgpt/project-instructions.md) + [프로젝트용 문서](dist/chatgpt-project) | 프로젝트 설정에 지침을 붙여 넣고 문서를 소스로 추가 |

메뉴와 이용 조건은 계정·워크스페이스에 따라 다릅니다. 등록 단계와 공식 근거는 [설치 안내](docs/installation.md)에서 확인하세요. 프로젝트 자료 방식은 네이티브 스킬 등록과 별개의 이용 방식입니다.

## 포함된 자료

| 구성 | 수량 | 용도 |
|---|---:|---|
| 기본 창작 스킬 | 17개 | 세계관·구성·집필·수정·검토 |
| 조합·라우팅 스킬 | 1개 | 자연어 요청에 따른 스킬 선택과 인계 |
| 세계관 분야별 선택형 | 8개 | 통합형 대신 필요한 분야만 사용 |
| 서비스별 개별 ZIP | 78개 | 스킬 26개 × 서비스 3종. 업로드 조건은 서비스별 안내 참고 |
| 프로젝트용 단일 문서 | 18개 | 기본 17개와 라우터의 지침·참고 자료 |

세계관 자료에는 **명칭 48개와 설계·검토 예시 168개**, 총 216개의 번호 예시가 있습니다. 장편 스킬의 예시 28개와 연재 점검 예시 16개는 별도입니다. 장르 프리셋 7종, 연결 세계관 예제와 작업 양식도 제공합니다.

세계관 통합형과 선택형은 같은 원본 자료를 활용합니다. 처음에는 `build-fantasy-world` 하나로 시작하고, 특정 분야만 독립적으로 쓰고 싶을 때 선택형을 고르세요.

## 연재 작업에 적용하기

문장 퇴고나 동선 수정은 담당 스킬 하나로 시작합니다. 여러 결과물이 필요하면 라우터를 쓰고, 다음 단계에서 사용할 **근거 위치와 바뀐 상태**만 이어 줍니다. 이어쓰기에는 직전 회차의 끝부분과 이번 장면에 걸리는 확정 설정부터 전달하세요.

- [실전 작업 가이드](docs/workflow.md): 세계관 설계, 다음 화 집필, 수정, 연재 점검 요청 예시
- [작품 자료 관리](docs/project-data.md): 확정 설정, 인물 지식, 복선, 버전과 인계 기록
- [동작 확인 사례](docs/behavior-checks.md): 단일 스킬 선택, 이어쓰기, 설정 예외, 복선 상태
- [문제 해결](docs/troubleshooting.md): 등록 실패, 스킬 미적용, 자료 누락과 과도한 수정

## 작업 범위와 검증

이 자료는 창작 지침과 참고 문서입니다. 스킬 이용에 별도 API 키나 실행 서버를 요구하지 않습니다. 원고·설정은 작가가 제공하고 관리하며, 저장이나 발행은 해당 서비스의 도구와 권한이 있어야 수행할 수 있습니다.

패키지 구조·참조·배포 파일 일치는 검사합니다. 실제 계정의 등록 여부와 모델의 작업 결과는 별도로 확인해야 합니다. GitHub 업데이트는 이미 등록된 스킬에 자동 반영되지 않습니다. [검증 범위](docs/maintenance.md) · [업데이트 안내](docs/versions.md)

이 가이드는 저장소의 사용 설명서입니다. 서비스 제공사의 공식 문서를 참고하되, 각 회사가 이 스킬팩을 제작하거나 보증한다는 뜻은 아닙니다. [공식 문서와 창작 참고 자료](docs/sources.md)
