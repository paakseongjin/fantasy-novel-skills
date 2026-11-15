# 전투·액션 설계

[가이드 홈](index.md) · [스킬 목록](catalog.md) · [설치 안내](installation.md)

`design-fantasy-action` — 능력과 공간의 제약 안에서 인물이 어떤 선택으로 승패에 이르는지 설계합니다. 전투·추격의 전술, 대응과 대가가 필요한 장면에 사용하세요.

[Gemini ZIP](../dist/gemini/design-fantasy-action.zip) · [Claude ZIP](../dist/claude/design-fantasy-action.zip) · [ChatGPT ZIP](../dist/chatgpt/design-fantasy-action.zip) · [지침 원본](../skills/design-fantasy-action/SKILL.md)

## 준비할 자료

| 항목 | 전달할 내용 |
|---|---|
| 승리 조건 | 격파·탈출·시간 벌기 등 장면의 실제 목표 |
| 전력과 제약 | 능력·사거리·비용·부상·장비 |
| 공간과 시간 | 지형·시야·이동 경로·남은 시간 |
| 고정 결과 | 승패·피해·최종 위치와 새 능력 허용 여부 |

## 요청 예시

```text
design-fantasy-action으로 전투의 행동 순서를 설계해 줘.
목표: 다친 검사가 성문이 열릴 때까지 마법사를 지연시킨다.
공간: 비가 오는 성벽 위의 좁은 통로.
고정 결과: 검사는 살아남고 성문은 열리지만 검을 잃는다.
첨부한 능력과 장비만 사용해 행동, 상대의 대응, 비용과 결과를 연결해 줘.
본문은 아직 쓰지 마.
[능력 규칙 / 부상과 장비 / 공간 조건]
```

## 받게 되는 결과

목표를 달성하려는 행동, 상대의 대응, 소모와 실패 가능성, 다음 행동의 이유가 연결된 설계안을 받습니다.

## 결과 확인

- 상대가 단순히 기다리거나 실수만 반복하지 않는가?
- 승패가 이미 제시한 능력·지형·선택에서 나오는가?
- 사용한 자원과 입은 부상이 후속 행동에 영향을 주는가?

## 작업 경계

새 능력이나 예외를 만들어 고정된 제약을 무시하지 않습니다. 자세한 전술 설계와 실제 본문 작성은 요청에 따라 나눕니다.

## 다음 작업

[본문 집필](write-fantasy-prose.md)로 장면화하고, 위치·지각의 연결은 [공간 묘사](write-immersive-scenes.md)로 보완합니다.

## 참고 양식

[예시 4개와 작업 양식](../skills/design-fantasy-action/references/examples-and-template.md)

예시의 인물·규칙은 설명용 창작입니다. 실제 작품에는 채택한 내용만 적용하세요.
