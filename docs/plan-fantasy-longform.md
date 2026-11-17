# 장편 구성·플롯 설계

[가이드 홈](index.md) · [스킬 목록](catalog.md) · [설치 안내](installation.md)

`plan-fantasy-longform` — 작품 전체의 사건을 주인공의 선택과 결과로 연결합니다. 시작과 결말은 있지만 중간이 비어 있거나, 이야기 단위가 서로 따로 움직일 때 사용하세요.

[Gemini ZIP](../dist/gemini/plan-fantasy-longform.zip) · [Claude ZIP](../dist/claude/plan-fantasy-longform.zip) · [ChatGPT ZIP](../dist/chatgpt/plan-fantasy-longform.zip) · [지침 원본](../skills/plan-fantasy-longform/SKILL.md)

## 준비할 자료

| 항목 | 전달할 내용 |
|---|---|
| 작품의 약속 | 장르·독자층·주인공의 장기 목표 |
| 기존 구조 | 확정 사건, 결말, 이미 쓴 구간 |
| 설계 범위 | 전체 구성인지 특정 이야기 단위인지, 대략적인 길이 |
| 변경 조건 | 새 사건 허용 여부와 유지해야 할 관계·결말 |

## 요청 예시

```text
plan-fantasy-longform을 적용해 장편의 사건 구조를 설계해 줘.
전제: 주인공은 금지된 역사 기록을 찾아 고향의 누명을 벗기려 한다.
확정 결말: 진실을 공개하지만 원래의 신분은 되찾지 못한다.
이번 작업: 시작부터 결말까지 큰 이야기 단위 5개.
각 단위의 목표, 주인공의 선택, 대가, 다음 갈등의 원인을 연결해 줘.
회차별 상세 개요나 본문은 아직 쓰지 마.
[확정 설정과 기존 줄거리]
```

## 받게 되는 결과

사건 목록에 그치지 않고 앞선 선택이 다음 상황을 만드는 구조안을 받습니다. 확정 사건과 새로 제안한 사건, 아직 결정하지 않은 분기를 나누어 검토하세요.

## 결과 확인

- 각 이야기 단위가 끝날 때 인물이나 상황이 실제로 달라지는가?
- 중간 사건이 결말의 선택을 준비하며, 우연만으로 다음 사건에 넘어가지 않는가?
- 작가가 고정한 결말과 기존 원고가 유지되는가?

## 작업 경계

한 회차의 장면 배치와 본문 집필은 별도 작업입니다. 모든 장편에 같은 회차 수나 기승전결 비율을 적용하지 않습니다.

## 다음 작업

중요 사건을 먼저 정하는 방식과, 장면을 쓰면서 인물의 다음 선택을 발견하는 방식을 작품에 맞춰 쓸 수 있습니다. [장편 예시의 계획과 탐색](../skills/plan-fantasy-longform/references/examples-and-template.md#계획과-탐색을-오가는-법)을 참고하세요.

[인물 성장](design-character-arcs.md)으로 사건에 따른 변화의 계기를 잡고, [회차 구성](structure-serial-chapters.md)으로 실제 연재 단위에 나눌 수 있습니다.

## 참고 양식

[예시 4개와 작업 양식](../skills/plan-fantasy-longform/references/examples-and-template.md)

예시의 인물·규칙은 설명용 창작입니다. 실제 작품에는 채택한 내용만 적용하세요.
