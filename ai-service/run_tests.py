#!/usr/bin/env python3
"""
MainAgent 테스트 실행 스크립트

이 스크립트는 다양한 테스트 옵션을 제공합니다:
- 전체 테스트 실행
- 단위 테스트만 실행
- 통합 테스트만 실행
- 특정 테스트 파일 실행
- 커버리지 리포트 생성
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path

# 프로젝트 루트 디렉토리 설정
PROJECT_ROOT = Path(__file__).parent
TESTS_DIR = PROJECT_ROOT / "tests"


def run_command(cmd, description=""):
    """명령어 실행 및 결과 출력"""
    print(f"\n{'='*60}")
    if description:
        print(f"실행: {description}")
    print(f"명령어: {' '.join(cmd)}")
    print(f"{'='*60}")
    
    try:
        # Windows 환경에서 인코딩 문제 해결
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        
        result = subprocess.run(
            cmd, 
            cwd=PROJECT_ROOT, 
            check=True, 
            capture_output=True, 
            text=True, 
            encoding='cp949',
            errors='replace',
            startupinfo=startupinfo
        )
        print("성공!")
        if result.stdout:
            print("출력:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"실패 (종료 코드: {e.returncode})")
        if e.stdout:
            print("표준 출력:")
            print(e.stdout)
        if e.stderr:
            print("오류 출력:")
            print(e.stderr)
        return False


def run_all_tests():
    """전체 테스트 실행"""
    return run_command(
        ["python", "-m", "pytest", "tests/", "-v"],
        "전체 테스트 실행"
    )


def run_unit_tests():
    """단위 테스트만 실행"""
    return run_command(
        ["python", "-m", "pytest", "tests/", "-m", "unit", "-v"],
        "단위 테스트 실행"
    )


def run_integration_tests():
    """통합 테스트만 실행"""
    return run_command(
        ["python", "-m", "pytest", "tests/", "-m", "integration", "-v"],
        "통합 테스트 실행"
    )


def run_specific_test(test_file):
    """특정 테스트 파일 실행"""
    test_path = TESTS_DIR / test_file
    if not test_path.exists():
        print(f"테스트 파일을 찾을 수 없습니다: {test_path}")
        return False
    
    return run_command(
        ["python", "-m", "pytest", str(test_path), "-v"],
        f"특정 테스트 실행: {test_file}"
    )


def run_with_coverage():
    """커버리지와 함께 테스트 실행"""
    return run_command(
        ["python", "-m", "pytest", "tests/", "--cov=chatbot", "--cov-report=html", "--cov-report=term", "-v"],
        "커버리지 리포트와 함께 테스트 실행"
    )


def run_fast_tests():
    """빠른 테스트 실행 (느린 테스트 제외)"""
    return run_command(
        ["python", "-m", "pytest", "tests/", "-m", "not slow", "-v"],
        "빠른 테스트 실행 (느린 테스트 제외)"
    )


def check_dependencies():
    """의존성 확인"""
    print("\n의존성 확인 중...")
    
    required_packages = [
        "pytest",
        "pytest-cov",
        "pytest-asyncio",
        "unittest.mock"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"OK: {package}")
        except ImportError:
            print(f"MISSING: {package} (설치 필요)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n다음 패키지들을 설치해주세요:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("모든 의존성이 설치되어 있습니다.")
    return True


def show_test_info():
    """테스트 정보 출력"""
    print("\n테스트 정보")
    print("="*50)
    print(f"프로젝트 루트: {PROJECT_ROOT}")
    print(f"테스트 디렉토리: {TESTS_DIR}")
    
    # 테스트 파일 목록 출력
    test_files = list(TESTS_DIR.glob("test_*.py"))
    print(f"\n테스트 파일 ({len(test_files)}개):")
    for test_file in test_files:
        print(f"  - {test_file.name}")
    
    # pytest 설정 확인
    pytest_ini = PROJECT_ROOT / "pytest.ini"
    if pytest_ini.exists():
        print(f"\nOK: pytest.ini 설정 파일 존재")
    else:
        print(f"\nWARNING: pytest.ini 설정 파일 없음")


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(description="MainAgent 테스트 실행기")
    parser.add_argument(
        "--all", 
        action="store_true", 
        help="전체 테스트 실행"
    )
    parser.add_argument(
        "--unit", 
        action="store_true", 
        help="단위 테스트만 실행"
    )
    parser.add_argument(
        "--integration", 
        action="store_true", 
        help="통합 테스트만 실행"
    )
    parser.add_argument(
        "--file", 
        type=str, 
        help="특정 테스트 파일 실행 (예: test_main_agent.py)"
    )
    parser.add_argument(
        "--coverage", 
        action="store_true", 
        help="커버리지 리포트와 함께 실행"
    )
    parser.add_argument(
        "--fast", 
        action="store_true", 
        help="빠른 테스트 실행 (느린 테스트 제외)"
    )
    parser.add_argument(
        "--check-deps", 
        action="store_true", 
        help="의존성 확인"
    )
    parser.add_argument(
        "--info", 
        action="store_true", 
        help="테스트 정보 출력"
    )
    
    args = parser.parse_args()
    
    # 기본 동작: 전체 테스트 실행
    if not any([args.all, args.unit, args.integration, args.file, args.coverage, args.fast, args.check_deps, args.info]):
        args.all = True
    
    print("MainAgent 테스트 실행기")
    print("="*50)
    
    # 의존성 확인
    if not check_dependencies():
        sys.exit(1)
    
    success = True
    
    if args.info:
        show_test_info()
    elif args.check_deps:
        pass
    elif args.all:
        success = run_all_tests()
    elif args.unit:
        success = run_unit_tests()
    elif args.integration:
        success = run_integration_tests()
    elif args.file:
        success = run_specific_test(args.file)
    elif args.coverage:
        success = run_with_coverage()
    elif args.fast:
        success = run_fast_tests()
    
    if success:
        print("\n모든 테스트가 성공적으로 완료되었습니다!")
        sys.exit(0)
    else:
        print("\n일부 테스트가 실패했습니다.")
        sys.exit(1)


if __name__ == "__main__":
    main() 