# 정전·연속성 검토

[가이드 홈](index.md) · [스킬 목록](catalog.md) · [설치 안내](installation.md)

`audit-fantasy-canon` — 작가가 확정한 설정과 원고를 대조해 시간·지리·능력·인물 지식·소지품 등의 충돌을 확인합니다. 여기서 정전은 작품의 공식적인 사실과 규칙을 뜻합니다.

[Gemini ZIP](../dist/gemini/audit-fantasy-canon.zip) · [Claude ZIP](../dist/claude/audit-fantasy-canon.zip) · [ChatGPT ZIP](../dist/chatgpt/audit-fantasy-canon.zip) · [지침 원본](../skills/audit-fantasy-canon/SKILL.md)

## 준비할 자료

| 항목 | 전달할 내용 |
|---|---|
| 기준 자료 | 작가가 승인한 설정집과 변경 기록 |
| 비교 자료 | 검토할 원고·연표·인물 상태. 독자 공개를 판단할 때는 실제 공개본과 정정 이력 |
| 적용 시점 | 자료 버전, 확정 여부와 유효한 시점 |
| 검토 범위 | 대상 회차·검사 항목과 수정 허용 여부 |

## 요청 예시

```text
audit-fantasy-canon으로 설정집 v2와 12화를 검토해 줘.
인물 지식, 능력 사용 비용과 이동 시간에 집중해 줘.
문제마다 충돌하는 양쪽 근거, 적용 시점, 심각도와 확실성을 따로 적어 줘.
의도된 거짓말과 독자만 아는 비밀은 오류로 단정하지 마.
최소 수정안을 제안하되 원고·설정은 아직 수정하지 마.
[확정 설정 / 변경 이력 / 12화와 관련 회차]
```

## 받게 되는 결과

충돌 후보의 양쪽 근거와 영향 범위, 최소 수정 대안을 받습니다. “확정 충돌”, “조건부 충돌”, “확인 필요”를 구분하고 누락 자료가 있으면 결론의 범위를 제한합니다.

## 결과 확인

- 서로 다른 시점의 사실이나 인물의 오해를 모순으로 오인하지 않는가?
- 문제의 심각성과 근거의 확실성이 별도로 표시되는가?
- 새 예외를 임의로 확정하지 않고 수정 제안으로 남겼는가?
- 작가 확정본과 공개본에 서로 다른 사건이 있으면 양쪽 근거와 영향 회차가 보이는가?

## 작업 경계

“오류 없음”은 검토한 자료와 항목에서 발견하지 못했다는 뜻입니다. 작가의 채택 결정 없이 설정을 확정·소급 변경하지 않습니다.

## 다음 작업

채택한 변경의 적용 시점과 영향받는 회차를 [작품 기록](project-data.md)에 남깁니다. 본문 수정은 변경 조건을 명시해 [집필 스킬](write-fantasy-prose.md)에 요청합니다.

## 참고 양식

[설정집 양식](../skills/audit-fantasy-canon/references/WORLD_BIBLE_TEMPLATE.md) · [연속성 대장](../skills/audit-fantasy-canon/references/CONTINUITY_LEDGER_TEMPLATE.md) · [감사 보고서](../skills/audit-fantasy-canon/references/AUDIT_REPORT_TEMPLATE.md) · [변경 요청서](../skills/audit-fantasy-canon/references/CHANGE_REQUEST_TEMPLATE.md)

예시의 인물·규칙은 설명용 창작입니다. 실제 작품에는 채택한 내용만 적용하세요.
