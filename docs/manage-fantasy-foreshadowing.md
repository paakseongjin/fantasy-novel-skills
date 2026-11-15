# 복선·비밀·회수 관리

[가이드 홈](index.md) · [스킬 목록](catalog.md) · [설치 안내](installation.md)

`manage-fantasy-foreshadowing` — 실제로 제시한 단서와 앞으로의 계획을 나누고, 비밀이 누구에게 언제 공개되는지 관리합니다. 반전의 근거가 충분한지 확인하거나 미회수 단서를 정리할 때 사용하세요.

[Gemini ZIP](../dist/gemini/manage-fantasy-foreshadowing.zip) · [Claude ZIP](../dist/claude/manage-fantasy-foreshadowing.zip) · [ChatGPT ZIP](../dist/chatgpt/manage-fantasy-foreshadowing.zip) · [지침 원본](../skills/manage-fantasy-foreshadowing/SKILL.md)

## 준비할 자료

| 항목 | 전달할 내용 |
|---|---|
| 실제 원고 | 단서가 등장한 회차와 문장 |
| 비밀의 진실 | 작가가 확정한 내용과 아직 미정인 내용 |
| 정보 공개 상태 | 독자와 인물 각각이 아는 사실 |
| 회수 조건 | 공개할 시점, 숨겨야 할 기간, 변경 가능한 구간 |

## 요청 예시

```text
manage-fantasy-foreshadowing으로 아래 1~8화의 단서를 정리해 줘.
실제 문장이 있는 단서와 앞으로 넣을 계획을 구분해 줘.
각 항목에 위치, 독자의 해석 가능성, 인물별 지식, 회수 상태를 적어 줘.
9화 반전과 연결할 수 있는 후보만 제안하고 과거 원고는 수정하지 마.
원고에서 확인하지 못한 단서는 배치 완료로 기록하지 마.
[원고 / 비밀의 진실 / 반전 계획]
```

## 받게 되는 결과

단서의 근거 위치, 공개 상태, 회수 후보와 남은 질문을 정리합니다. 계획표의 내용이 이미 원고에 반영된 사실처럼 보이지 않게 상태를 확인하세요.

## 결과 확인

- 독자에게 보인 단서와 인물이 아는 정보가 구분되는가?
- 반전이 기존 단서와 양립하며 뒤늦은 새 규칙에만 기대지 않는가?
- 아직 쓰지 않은 장면이 과거의 근거로 제시되지 않는가?

## 작업 경계

모든 사물과 대사를 복선으로 해석하지 않습니다. 의도된 여운과 미해결 요소가 모두 회수 오류인 것은 아닙니다.

## 다음 작업

[회차 구성](structure-serial-chapters.md)으로 공개 순서를 배치하고, 확정 사실과 충돌하는지는 [정전 검토](audit-fantasy-canon.md)로 확인합니다.

## 참고 양식

[예시 4개와 작업 양식](../skills/manage-fantasy-foreshadowing/references/examples-and-template.md)

예시의 인물·규칙은 설명용 창작입니다. 실제 작품에는 채택한 내용만 적용하세요.
