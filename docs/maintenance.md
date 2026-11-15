# 패키지 생성과 검증

## 편집할 원본

| 위치 | 역할 |
|---|---|
| skills/스킬명 | 기본 17개 SKILL.md와 참고 양식 |
| skills/build-fantasy-world/references | 세계관 지침·예시의 단일 원본 |
| config/worldbuilding-modules.json | 선택형 8개 본문과 포함할 참고 파일 목록 |
| platforms/chatgpt/project-instructions.md | 프로젝트에 붙여 넣는 지침 |
| scripts/build_packages.py | 플랫폼별 ZIP·프로젝트 문서 생성 |
| scripts/validate_repository.py | 문서 경로·예시 개수·생성물 일치 확인 |
| dist | 배포용 생성물. 직접 수정하지 않습니다. |

## 명령

Python 3.9 이상, 표준 라이브러리만 필요합니다. 저장소 최상위에서 실행하세요.

```bash
python scripts/build_packages.py
python scripts/build_packages.py --check
python scripts/validate_repository.py
```

빌더는 파일 정렬·ZIP 타임스탬프를 고정합니다. 같은 Python/zlib 환경과 원본에서 같은 바이트를 생성합니다. 다른 압축 라이브러리 버전에서 바이트가 달라질 가능성은 있으므로 소스 내용 일치도 함께 확인합니다. 오래된 예상 밖 dist 파일을 자동 삭제하지 않고 오류로 보고합니다.

## 검증하는 항목

- 스킬명 형식·길이, 설명 길이, 필수 메타데이터
- 각 독립 패키지 안의 참고 파일 존재와 상대 경로
- ZIP 압축 해제 무결성 및 원본과의 바이트 일치
- 플랫폼별 최상위 폴더 구조
- 기본 17개·선택형 8개·ZIP 75개·프로젝트 문서 17개
- 세계관 8개 예시 파일의 고유 번호와 총 216개; 장편 스킬 예시 28개·웹소설 연재 스킬 예시 16개는 별도
- 저장소 Markdown 상대 링크 대상 존재
- 생성물의 재생성 일치와 SHA-256 manifest

`dist/manifest.json`의 live_platform_installation_tested는 false입니다. 로컬 형식 검사는 실제 ChatGPT·Claude·Gemini 계정의 설치 성공이나 모델 실행을 뜻하지 않습니다. 계정 등록 후 [짧은 확인 예제](installation.md#5-설치-확인과-갱신)를 실행하세요.

기존 집필·정전 감사 스킬과 legacy 원본은 이번 통합에서 내용이 변경되지 않았습니다. 세계관 자료는 배포 형식 안내를 공통화한 출처 문서 외에 기존 내용을 유지합니다.
