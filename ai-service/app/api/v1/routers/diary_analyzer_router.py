from fastapi import APIRouter, Depends, HTTPException
from app.models.diary import DiaryAnalysisRequest, DiaryAnalysisResponse
from app.services.diary_analyzer import DiaryAnalyzer

diary_analyzer_router = APIRouter(
    prefix="/diary-analyzer",
    tags=["diary-analyzer"],
)

def get_diary_analyzer() -> DiaryAnalyzer:
    """DiaryAnalyzer 의존성 주입"""
    return DiaryAnalyzer()

@diary_analyzer_router.post(
    "/analyze",
    response_model=DiaryAnalysisResponse,
    summary="일기 분석 및 코멘트 생성",
    description="사용자가 작성한 일기를 분석하여 전처리, 청크 분할, 감정/상황 추출, 조언 생성, AI 코멘트를 생성합니다.",
)
async def analyze_diary(
    request: DiaryAnalysisRequest,
    analyzer: DiaryAnalyzer = Depends(get_diary_analyzer),
):
    """
    일기 분석 및 코멘트 생성
    
    - 일기 전처리 (문법/문맥 정리)
    - 의미 단위 청크 분할
    - 감정/상황 추출 및 카테고리 매핑
    - 유사한 과거 일기 검색
    - 관련 조언 검색 및 통합
    - 관련 인용문 검색
    - AI 코멘트 생성
    - 감정 키워드 추출
    """
    try:
        result = await analyzer.analyze_diary(
            user_id=request.user_id,
            raw_diary=request.raw_diary
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"일기 분석 중 오류가 발생했습니다: {str(e)}"
        )

@diary_analyzer_router.get(
    "/health",
    summary="일기 분석 서비스 상태 확인",
    description="일기 분석 서비스의 상태를 확인합니다.",
)
async def health_check():
    """일기 분석 서비스 헬스 체크"""
    return {
        "status": "healthy",
        "service": "diary-analyzer",
        "message": "일기 분석 서비스가 정상적으로 실행 중입니다."
    } 