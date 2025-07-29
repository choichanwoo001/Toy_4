# 현재 시스템 파이프라인

## 현재 챗봇 시스템의 처리 흐름

```mermaid
flowchart TD
    A["사용자 입력"] --> B["전처리<br/>Preprocessor"]
    B --> C["대화 기록 가져오기<br/>ConversationManager"]
    C --> D["의도 분류 Agent<br/>ConversationManagementAgent"]
    D --> E{"복합 사건?"}
    E -->|Yes| F["청크 분석<br/>analyze_chunk"]
    E -->|No| G["응답 생성 Agent<br/>ResponseGenerationAgent"]
    F --> H["RAG 검색 Agent<br/>RagAgent"]
    H --> I{"검색 결과 있음?"}
    I -->|Yes| J["응답 생성 Agent<br/>with RAG data"]
    I -->|No| K["응답 생성 Agent<br/>without RAG data"]
    J --> L["대화 저장<br/>ConversationManager"]
    K --> L
    G --> L
```

## 현재 시스템의 문제점

```mermaid
flowchart LR
    A["사용자 입력"] --> B["단순 분류<br/>고정된 로직"]
    B --> C["조건부 검색<br/>의존적 실행"]
    C --> D["템플릿 응답<br/>맥락 무시"]
    D --> E["단순 저장<br/>상태 없음"]
```

## 현재 시스템의 처리 예시

```mermaid
sequenceDiagram
    participant U as 사용자
    participant P as Preprocessor
    participant IA as Intent Agent
    participant RA as RAG Agent
    participant ResA as Response Agent
    participant CM as Conversation Manager
    
    U->>P: "친구와 다퉈서 속상해"
    P->>IA: 전처리된 입력
    IA->>IA: 의도 분류: "단순 감정 표현"
    IA->>ResA: 분류 결과 전달
    ResA->>ResA: 템플릿 기반 응답 생성
    ResA->>U: "힘드셨겠어요"
    ResA->>CM: 대화 저장
```

## 현재 시스템의 한계

1. **단순한 분류**: 복잡한 상황을 단순하게 분류
2. **독립적 실행**: 각 Agent가 서로의 판단을 참고하지 않음
3. **상태 없음**: 이전 대화의 맥락을 제대로 활용하지 못함
4. **고정된 로직**: 상황에 따른 유연한 대응 불가
5. **맥락 무시**: 사용자의 감정 상태나 상황을 고려하지 않음 