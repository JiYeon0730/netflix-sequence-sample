# netflix-sequence-sample
넷플릭스 시나리오 기반 소프트웨어 모델링 및 샘플 코드

sequenceDiagram
    participant User
    participant App
    participant AuthServer
    participant ContentServer

    User->>App: 앱 실행
    App->>AuthServer: 로그인 요청
    AuthServer-->>App: 로그인 성공 응답
    App-->>User: 홈 화면 표시

    User->>App: 콘텐츠 탐색
    App->>ContentServer: 영화 목록 요청
    ContentServer-->>App: 영화 목록 전달
    App-->>User: 영화 목록 표시

    User->>App: 영화 선택 및 시청 요청
    App->>ContentServer: 스트리밍 시작 요청
    ContentServer-->>App: 스트리밍 데이터 전송
    App-->>User: 영화 재생

[시퀀스 다이어그램] (https://github.com/JiYeon0730/netflix-sequence-sample/blob/main/Editor%20_%20Mermaid%20Chart-2025-05-20-155017.png?raw=true)
