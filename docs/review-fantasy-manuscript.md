# 원고 편집·진단

[가이드 홈](index.md) · [스킬 목록](catalog.md) · [설치 안내](installation.md)

`review-fantasy-manuscript` — 이미 쓴 원고의 인과, 장면 기능과 독자 이해를 근거 중심으로 진단합니다. 어딘가 어색하지만 문제를 특정하기 어려울 때 시작점으로 사용할 수 있습니다.

[Gemini ZIP](../dist/gemini/review-fantasy-manuscript.zip) · [Claude ZIP](../dist/claude/review-fantasy-manuscript.zip) · [ChatGPT ZIP](../dist/chatgpt/review-fantasy-manuscript.zip) · [지침 원본](../skills/review-fantasy-manuscript/SKILL.md)

## 준비할 자료

| 항목 | 전달할 내용 |
|---|---|
| 원고 범위 | 검토할 회차·장면과 버전 |
| 의도 | 독자가 알아야 할 것과 느끼길 바라는 정서 |
| 관련 맥락 | 앞뒤 사건과 필요한 확정 설정 |
| 수정 조건 | 진단만인지, 최소 수정 제안까지인지 |

## 요청 예시

```text
review-fantasy-manuscript로 아래 1~3화를 진단해 줘.
인과가 끊기는 곳, 장면의 역할이 겹치는 곳, 독자가 이해하기 어려운 곳을 봐 줘.
각 문제에 원문 위치, 영향과 최소 수정 방향을 적어 줘.
취향 차이와 실제 이해 문제를 구분하고 우선 문제 3개부터 알려 줘.
지금은 원고를 다시 쓰지 마.
[원고 / 장르와 독자에게 약속한 경험]
```

## 받게 되는 결과

고쳐야 할 위치와 이유, 영향과 우선순위를 받습니다. 단순히 “몰입감이 약하다”는 평가보다 어떤 정보나 선택의 연결이 부족한지 확인하세요.

## 결과 확인

- 진단마다 확인 가능한 원문 근거가 있는가?
- 장르·의도에 맞는 표현을 개인 취향만으로 오류 취급하지 않는가?
- 수정 방향이 문제보다 크게 작품 전체를 바꾸지 않는가?

## 작업 경계

설정집 없이 정전 전체를 검증한 것으로 보지 않습니다. 구체적 자료 대조와 문장 교정은 각각의 전문 작업입니다.

## 다음 작업

확인된 문제만 [회차 구성](structure-serial-chapters.md), [관계 갈등](write-character-conflict.md), [한국어 퇴고](refine-natural-korean.md) 등 담당 스킬로 넘깁니다.

## 참고 양식

[예시 4개와 작업 양식](../skills/review-fantasy-manuscript/references/examples-and-template.md)

예시의 인물·규칙은 설명용 창작입니다. 실제 작품에는 채택한 내용만 적용하세요.
