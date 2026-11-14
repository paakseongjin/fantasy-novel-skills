# 버전과 중복 정리

## 2026-11-14 — 대화 산출물 통합·3개 플랫폼 배포

- 기존 `write-fantasy-prose`, `audit-fantasy-canon`의 본문과 참고 양식을 보존했습니다.
- 대화에서 작성한 `write-character-conflict`, `write-immersive-scenes`, `refine-natural-korean`을 파일로 수록했습니다.
- `build-fantasy-world`에 8개 분야 지침과 216개 번호 예시, 장르 프리셋 7종, 연결 세계관, 설정집 양식을 수록했습니다.
- 분야별 8개 선택형의 본문·참고 목록은 `config/worldbuilding-modules.json`에서 관리합니다. 예시 원본은 통합형 references 한 곳에 두며, ZIP을 만들 때 필요한 파일만 넣습니다.
- ChatGPT·Claude·Gemini용 개별 ZIP 42개와 ChatGPT 프로젝트용 단일 문서 6개를 생성했습니다. 플랫폼별 ZIP은 같은 지침을 담고 압축 폴더 구조만 다릅니다.
- ChatGPT 안내를 조건부 네이티브 설치+프로젝트 대안으로 수정하고 Gemini 활동 기록을 필수로 안내한 부분을 정정했습니다.
- 기존 문서의 “이번 대화의 스킬팩은 포함되지 않았다”는 설명을 현재 구성으로 교체했습니다.

## 설치 중복을 피하는 기준

| 항목 | 역할과 선택 기준 |
|---|---|
| write-fantasy-prose | 장면·회차의 전체 집필 |
| 심리·장면·한국어 3개 | 특정 문제의 집중 수정. 매번 모두 적용하지 않아도 됩니다. |
| 세계관 통합형 / 분야별 8개 | 동일한 자료를 쓰는 대체 구성. 통합형 1개 또는 필요한 개별형을 선택합니다. |
| audit-fantasy-worldbuilding | 설정 분야 간 인과관계와 장면 반영의 검토 |
| audit-fantasy-canon | 확정 자료·시점·변경 요청·연속성을 근거 중심으로 검증. 같은 충돌을 반복 감사할 필요는 없습니다. |
| legacy/write-fantasy-novels | 이전 통합형 보관용. 현재 기본 스킬과 함께 설치하지 않습니다. |

## 원본과 생성물

`skills`와 `config`를 수정하고 [패키지 생성 명령](maintenance.md)을 실행하세요. `dist`는 생성물이며 별도의 스킬 원본이 아닙니다. 예전 대화의 Gemini 단일 ZIP·8개 묶음 ZIP은 내용을 플랫폼별 개별 ZIP으로 재구성했으므로 중복 압축파일로 보관하지 않습니다. 옛 사용 안내는 설치·세계관·출처 문서로 통합했습니다.

확인 범위는 [검증 문서](maintenance.md)에 명시합니다. 실제 서비스 계정에서의 설치·실행 완료와 패키지 형식 검증은 서로 다릅니다.
