from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routers.conversation_manager_router import conversation_router
from app.api.v1.routers.diary_analyzer_router import diary_analyzer_router

# FastAPI 앱 생성
app = FastAPI(
    title="대화 관리 시스템 API",
    description="사용자 입력을 분석하고 ASK/REPLY를 결정하는 대화 관리 시스템",
    version="1.0.0",
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발용 - 운영에서는 특정 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(conversation_router, prefix="/api/v1")
app.include_router(diary_analyzer_router, prefix="/api/v1")

@app.get("/")
async def root():
    """루트 엔드포인트 - API 상태 확인"""
    return {"message": "대화 관리 시스템 API가 실행 중입니다.", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    """헬스 체크 엔드포인트"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 