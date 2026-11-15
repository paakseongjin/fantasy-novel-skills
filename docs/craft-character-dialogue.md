# 대사·인물별 말투

[가이드 홈](index.md) · [스킬 목록](catalog.md) · [설치 안내](installation.md)

`craft-character-dialogue` — 호칭·존대·어휘·정보를 말하는 방식으로 인물의 목소리를 구분합니다. 대사가 모두 비슷하거나 설명을 위해 억지로 대화하는 느낌일 때 사용하세요.

[Gemini ZIP](../dist/gemini/craft-character-dialogue.zip) · [Claude ZIP](../dist/claude/craft-character-dialogue.zip) · [ChatGPT ZIP](../dist/chatgpt/craft-character-dialogue.zip) · [지침 원본](../skills/craft-character-dialogue/SKILL.md)

## 준비할 자료

| 항목 | 전달할 내용 |
|---|---|
| 화자와 상대 | 관계·지위·존대 방향과 현재 감정 |
| 대화의 목표 | 설득·회피·협상 등 각자가 원하는 결과 |
| 알고 있는 사실 | 말할 수 있는 정보와 숨기는 비밀 |
| 원문과 범위 | 대사만 수정할지 주변 행동도 바꿀지 |

## 요청 예시

```text
craft-character-dialogue로 아래 대사를 다듬어 줘.
대장은 결정을 짧게 전달하고 신입은 근거를 확인하려 한다.
신입은 대장에게 존댓말을 쓴다.
발언의 정보, 인물 관계와 다툼의 결말은 유지해 줘.
반복 말버릇을 붙이지 말고 표현과 질문 방식으로 차이를 내 줘.
대사 외의 새 행동이나 과거사는 추가하지 마.
[대사 원문 / 인물별 지식]
```

## 받게 되는 결과

발언의 의미를 지키면서 인물과 상황에 맞춘 대사를 받습니다. 호칭이나 존대가 달라졌다면 관계 변화의 근거를 확인하세요.

## 결과 확인

- 각 대사를 그 인물이 지금 말할 이유가 있는가?
- 상대가 이미 아는 정보를 독자 설명만을 위해 반복하지 않는가?
- 말투를 구분하려고 불필요한 고어·방언·말버릇을 강요하지 않는가?

## 작업 경계

직접적이고 솔직한 대화도 허용합니다. 모든 대사에 숨은 뜻이나 몸짓을 덧붙이지 않습니다.

## 다음 작업

대사의 표현보다 갈등의 원인이 약하면 [관계 갈등](write-character-conflict.md), 서술문까지 다듬으려면 [한국어 퇴고](refine-natural-korean.md)를 사용하세요.

## 참고 양식

[예시 4개와 작업 양식](../skills/craft-character-dialogue/references/examples-and-template.md)

예시의 인물·규칙은 설명용 창작입니다. 실제 작품에는 채택한 내용만 적용하세요.
