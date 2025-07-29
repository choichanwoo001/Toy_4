# Agent 패턴 파이프라인

## 개선된 챗봇 시스템의 처리 흐름

```mermaid
flowchart TD
    A["사용자 입력"] --> B["전처리<br/>Preprocessor"]
    B --> C["상황 분석<br/>Context Analyzer"]
    C --> D["Intent Agent<br/>상황 기반 의사결정"]
    D --> E["상태 공유<br/>Shared Context"]
    E --> F["RAG Agent<br/>전략적 검색"]
    F --> G["Response Agent<br/>맥락 기반 응답"]
    G --> H["협력 및 피드백<br/>Agent Collaboration"]
    H --> I["대화 저장 + 상태 업데이트<br/>Enhanced Storage"]
```

## Agent 패턴의 개선점

```mermaid
flowchart LR
    A["사용자 입력"] --> B["상황 분석<br/>맥락 이해"]
    B --> C["전략 선택<br/>의사결정"]
    C --> D["협력적 검색<br/>상태 기반"]
    D --> E["맥락 기반 응답<br/>감정 고려"]
    E --> F["상태 업데이트<br/>학습"]
```

## Agent 간 협력 예시

```mermaid
sequenceDiagram
    participant U as 사용자
    participant CA as Context Analyzer
    participant IA as Intent Agent
    participant RA as RAG Agent
    participant ResA as Response Agent
    participant SC as Shared Context
    
    U->>CA: "친구와 다퉈서 속상해"
    CA->>CA: 감정 상태 분석: 민감함
    CA->>IA: 상황 + 감정 정보 전달
    IA->>IA: "복합 사건, 사용자 감정 민감함"
    IA->>SC: 판단 결과 저장
    IA->>RA: 감정/상황 태그 전달
    RA->>RA: "위로 + 조심스러운 조언" 전략 선택
    RA->>ResA: 검색 결과 + 맥락 전달
    ResA->>ResA: 사용자 감정 상태 고려
    ResA->>U: "정말 힘드셨겠어요. 어떤 일이 있었나요?"
    ResA->>SC: 응답 패턴 학습
```

## Agent 패턴의 장점

```mermaid
mindmap
  root((Agent 패턴))
    자율성
      상황 기반 판단
      전략적 선택
      적응적 행동
    협력
      상태 공유
      정보 교환
      상호 보완
    학습
      패턴 인식
      성능 개선
      맥락 이해
    맥락 인식
      감정 상태 고려
      대화 흐름 파악
      개인화 응답
```

## Agent 패턴의 핵심 특징

1. **자율성**: 각 Agent가 상황을 분석하고 최적의 행동을 선택
2. **상태 관리**: Agent들이 자신의 상태와 다른 Agent의 상태를 공유
3. **협력**: Agent들이 서로의 판단을 참고하여 더 정확한 결과 도출
4. **적응성**: 상황에 따라 다른 전략을 사용
5. **학습**: 대화 패턴을 학습하여 점진적으로 개선

## 처리 예시 비교

| 구분 | 현재 시스템 | Agent 패턴 |
|------|------------|------------|
| **입력** | "친구와 다퉈서 속상해" | "친구와 다퉈서 속상해" |
| **분류** | 단순 감정 표현 | 복합 사건 + 감정 민감함 |
| **검색** | 실행 안됨 | 위로 + 조심스러운 조언 |
| **응답** | "힘드셨겠어요" | "정말 힘드셨겠어요. 어떤 일이 있었나요?" |
| **결과** | 표면적인 위로 | 공감 + 구체적 질문 | 