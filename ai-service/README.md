# AI Service

일기 분석 및 AI 코멘트 생성을 위한 FastAPI 서비스입니다.

## 기능

### 1. 대화 관리 시스템 (Conversation Manager)
- 사용자 입력 분석 및 ASK/REPLY 결정
- 대화 히스토리 관리
- 고급 채팅 기능 (RAG 포함)

### 2. 일기 분석 시스템 (Diary Analyzer) - NEW!
- 일기 전처리 (문법/문맥 정리)
- 의미 단위 청크 분할
- 감정/상황 추출 및 카테고리 매핑
- 유사한 과거 일기 검색
- 관련 조언 검색 및 통합
- 관련 인용문 검색
- AI 코멘트 생성
- 감정 키워드 추출

## 설치 및 실행

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 추가하세요:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. 서비스 실행
```bash
cd ai-service
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API 엔드포인트

### 대화 관리 API
- `POST /api/v1/conversation-manager/decide` - 대화 관리 의사결정
- `GET /api/v1/conversation-manager/history/{user_id}` - 대화 히스토리 조회
- `POST /api/v1/conversation-manager/chat` - 기본 채팅
- `POST /api/v1/conversation-manager/chat-advanced` - 고급 채팅 (RAG 포함)

### 일기 분석 API - NEW!
- `POST /api/v1/diary-analyzer/analyze` - 일기 분석 및 코멘트 생성
- `GET /api/v1/diary-analyzer/health` - 서비스 상태 확인

## 일기 분석 API 사용 예시

### 요청
```json
{
  "user_id": "user123",
  "raw_diary": "오늘은 정말 힘든 하루였다. 회사에서 프로젝트 마감일이 다가와서 스트레스를 받았어. 하지만 팀원들과 함께 문제를 해결하면서 뿌듯함도 느꼈다."
}
```

### 응답
```json
{
  "processed_diary": "오늘은 정말 힘든 하루였다. 회사에서 프로젝트 마감일이 다가와서 스트레스를 받았지만, 팀원들과 함께 문제를 해결하면서 뿌듯함도 느꼈다.",
  "chunks": [
    "오늘은 정말 힘든 하루였다. 회사에서 프로젝트 마감일이 다가와서 스트레스를 받았어.",
    "하지만 팀원들과 함께 문제를 해결하면서 뿌듯함도 느꼈다."
  ],
  "advice": "스트레스 상황에서도 팀워크를 통해 성취감을 느끼는 것은 매우 소중한 경험입니다.",
  "comment": "사랑하는 제자님, 오늘의 기록을 읽으면서 정말 대견한 마음이 듭니다. 마감일이 다가오는 스트레스 속에서도 팀원들과 함께 문제를 해결해나가는 모습이 정말 아름답네요. 이런 경험들이 제자님을 더욱 성장시킬 거예요.",
  "quote": "\"함께하면 더 강해진다\" - 팀워크의 힘",
  "emotion_keywords": ["스트레스", "뿌듯함", "팀워크", "성취감"],
  "similar_past_diaries": [
    "지난주에도 비슷한 프로젝트 마감 스트레스를 겪었지만, 이번엔 더 잘 해결할 수 있었다."
  ]
}
```

## Spring Boot 연동

Spring Boot 백엔드에서는 다음과 같이 AI 서비스를 호출할 수 있습니다:

```java
@PostMapping("/api/diaries/analyze")
@ResponseBody
public ResponseEntity<ApiResponse<Map<String, Object>>> analyzeDiaryWithAI(
    @RequestParam Long userId,
    @RequestParam String content) {
    
    // AI 서비스 호출
    RestTemplate restTemplate = new RestTemplate();
    String aiServiceUrl = "http://localhost:8000/api/v1/diary-analyzer/analyze";
    
    Map<String, Object> requestData = new HashMap<>();
    requestData.put("user_id", String.valueOf(userId));
    requestData.put("raw_diary", content);
    
    HttpHeaders headers = new HttpHeaders();
    headers.setContentType(MediaType.APPLICATION_JSON);
    HttpEntity<Map<String, Object>> requestEntity = new HttpEntity<>(requestData, headers);
    
    ResponseEntity<Map> aiResponse = restTemplate.postForEntity(aiServiceUrl, requestEntity, Map.class);
    
    // 응답 처리...
}
```

## 데이터베이스

ChromaDB를 사용하여 다음 컬렉션들을 관리합니다:
- `diary_past_diaries` - 과거 일기 데이터
- `diary_advice` - 조언 데이터
- `diary_quotes` - 인용문 데이터

## 개발 환경

- Python 3.8+
- FastAPI
- ChromaDB
- OpenAI API
- LangChain
- PyTorch
- Sentence Transformers