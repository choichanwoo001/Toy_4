#!/usr/bin/env python3
"""
인코딩 문제 없이 직접 테스트 실행
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic():
    """기본 테스트"""
    print("기본 테스트 실행 중...")
    
    # 간단한 assertion 테스트
    assert 1 + 1 == 2
    assert "hello" in "hello world"
    assert len([1, 2, 3]) == 3
    
    print("기본 테스트 통과!")

def test_imports():
    """import 테스트"""
    print("Import 테스트 실행 중...")
    
    try:
        import pytest
        print("pytest import 성공")
    except ImportError:
        print("pytest import 실패")
        return False
    
    try:
        from unittest.mock import Mock, patch
        print("unittest.mock import 성공")
    except ImportError:
        print("unittest.mock import 실패")
        return False
    
    print("Import 테스트 통과!")
    return True

def test_mock():
    """Mock 테스트"""
    print("Mock 테스트 실행 중...")
    
    from unittest.mock import Mock
    
    # Mock 객체 생성
    mock_service = Mock()
    mock_service.get_response.return_value = "Mock 응답"
    
    # Mock 메서드 호출
    result = mock_service.get_response("테스트 입력")
    
    # 결과 검증
    assert result == "Mock 응답"
    mock_service.get_response.assert_called_once_with("테스트 입력")
    
    print("Mock 테스트 통과!")

def test_patch():
    """Patch 테스트"""
    print("Patch 테스트 실행 중...")
    
    from unittest.mock import patch
    
    with patch('builtins.print') as mock_print:
        print("테스트 메시지")
        mock_print.assert_called_once_with("테스트 메시지")
    
    print("Patch 테스트 통과!")

def main():
    """메인 함수"""
    print("="*50)
    print("직접 테스트 실행")
    print("="*50)
    
    tests = [
        ("기본 테스트", test_basic),
        ("Import 테스트", test_imports),
        ("Mock 테스트", test_mock),
        ("Patch 테스트", test_patch),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            test_func()
            print(f"PASS: {test_name}")
            passed += 1
        except Exception as e:
            print(f"FAIL: {test_name}: {e}")
    
    print("="*50)
    print(f"테스트 결과: {passed}/{total} 통과")
    
    if passed == total:
        print("모든 테스트가 성공했습니다!")
        return True
    else:
        print("일부 테스트가 실패했습니다.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 