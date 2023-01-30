# PastelBot
## 개발하기
- `errors`, `logs` 디렉토리 생성
- 데이터베이스 생성
- `.env.example`을 복사해 `.env`파일 생성
    ```py
    TOKEN="토큰"
    DATABASE="데이터베이스 파일"
    TEST_GUILD_ID=[테스트 서버 ID]
    DEV_GUILD_ID=[개발용 서버 ID]
    ```
- 가상환경 구축 후 `requirements.txt`를 활용해 디펜던시 설치
### 개발 시 주의사항
- `main`: 개발용 브랜치, 직접 커밋 금지
- `release`: 배포용 브랜치, 직접 커밋 금지
- 개발 시 아래의 룰을 따라서 브랜치 생성 후 `main` 브랜치로 PR
    - 버그 수정: `bug/이름`
    - 기능 추가 & 보수: `feature/이름`
    - 기타 코드 개선 작업 등: `maintain/이름`
