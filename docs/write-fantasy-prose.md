# 장면·회차 본문 집필

[가이드 홈](index.md) · [스킬 목록](catalog.md) · [설치 안내](installation.md)

`write-fantasy-prose` — 확정한 설정과 장면 목표를 실제 본문으로 작성합니다. 새 장면, 직전 회차의 이어 쓰기, 허용 범위를 정한 장면 재작성에 사용하세요.

[Gemini ZIP](../dist/gemini/write-fantasy-prose.zip) · [Claude ZIP](../dist/claude/write-fantasy-prose.zip) · [ChatGPT ZIP](../dist/chatgpt/write-fantasy-prose.zip) · [지침 원본](../skills/write-fantasy-prose/SKILL.md)

## 준비할 자료

| 항목 | 전달할 내용 |
|---|---|
| 작품 조건 | 장르·시점·목표 분량, 필요한 경우 작품별 문체 카드나 작가가 고른 대표 문단 |
| 관련 자료 | 확정 설정, 직전 공개본 또는 집필 기준 버전, 인물 상태와 영향 있는 정정 |
| 장면 목표 | 원하는 것·장애·선택·고정 결말 |
| 창작 범위 | 새 설정 허용 여부와 공개하지 않을 정보 |

## 요청 예시

```text
write-fantasy-prose로 아래 장면의 초고를 써 줘.
시점: 제자의 3인칭 제한 시점.
목표: 제자가 스승의 배신을 의심하지만 확신하지 못한다.
결말: 제자는 질문을 삼키고 스승의 제안을 받아들인다.
분량: 약 1,500자. 대화와 행동으로 불신을 드러내 줘.
스승만 아는 사실은 직접 서술하지 마.
새 설정이 필요하면 본문 뒤에 미확정 제안으로 분리해 줘.
[확정 설정 / 직전 장면 / 인물별 지식]
```

## 받게 되는 결과

요청한 범위의 초고 또는 수정 본문을 받습니다. 작성 중 새로 생긴 설정 후보와 다음 장면에 이어질 상태가 있다면 확정 여부를 따로 검토하세요.

## 결과 확인

- 시점 인물이 알 수 있는 정보로 서술했는가?
- 선택과 결과가 장면 목표·고정 결말에 이어지는가?
- 앞 장면의 부상·위치·소지품·관계가 유지되는가?
- 시점 인물이 직업이나 관계 때문에 알아챈 것이 새로운 판단이나 행동으로 이어지는가?
- 이전 공개본에서 빠진 단서가 이미 일어난 사건처럼 들어오지 않았는가?

## 작업 경계

작가의 결정 없이 확정 설정을 바꾸거나 제공받지 않은 직전 회차를 읽은 것처럼 이어 쓰지 않습니다. 외부 저장·발행은 본문 생성과 별도 작업입니다.

## 다음 작업

[회차 인계](project-data.md)로 종료 상태를 기록합니다. 문장 문제는 [한국어 퇴고](refine-natural-korean.md), 설정 충돌은 [정전 검토](audit-fantasy-canon.md)로 이어 갈 수 있습니다.

## 참고 양식

[작품별 문체 카드](../skills/write-fantasy-prose/references/VOICE_CARD.md) · [장면을 살리는 사례](../skills/write-fantasy-prose/references/scene-craft.md) · [장면 카드](../skills/write-fantasy-prose/references/SCENE_CARD_TEMPLATE.md) · [원고 점검](../skills/write-fantasy-prose/references/PROSE_CHECK_TEMPLATE.md) · [회차 인계](../skills/write-fantasy-prose/references/CHAPTER_HANDOFF_TEMPLATE.md)

예시의 인물·규칙은 설명용 창작입니다. 실제 작품에는 채택한 내용만 적용하세요.
