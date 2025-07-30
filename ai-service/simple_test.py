#!/usr/bin/env python3
"""
간단한 테스트 실행 스크립트
"""

import subprocess
import sys
import os

def run_simple_test():
    """간단한 테스트 실행"""
    try:
        # pytest가 설치되어 있는지 확인
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        
        result = subprocess.run(
            ["python", "-c", "import pytest; print('pytest available')"],
            capture_output=True,
            text=True,
            encoding='cp949',
            errors='replace',
            startupinfo=startupinfo
        )
        
        if result.returncode != 0:
            print("pytest가 설치되지 않았습니다. 다음 명령어로 설치하세요:")
            print("pip install pytest pytest-cov pytest-asyncio")
            return False
        
        # 간단한 테스트 실행
        print("테스트를 실행합니다...")
        result = subprocess.run(
            ["python", "-m", "pytest", "tests/test_example.py", "-v"],
            capture_output=True,
            text=True,
            encoding='cp949',
            errors='replace',
            startupinfo=startupinfo
        )
        
        print("테스트 결과:")
        print(result.stdout)
        
        if result.stderr:
            print("오류:")
            print(result.stderr)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"오류 발생: {e}")
        return False

if __name__ == "__main__":
    success = run_simple_test()
    if success:
        print("\n테스트가 성공적으로 완료되었습니다!")
        sys.exit(0)
    else:
        print("\n테스트가 실패했습니다.")
        sys.exit(1) 