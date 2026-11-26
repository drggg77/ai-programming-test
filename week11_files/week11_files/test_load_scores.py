import pytest
from load_scores import load_scores

# --- STEP 1: 정상 케이스 (print를 assert로) ---
def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_빈_줄은_건너뛴다():
    kept, skipped = load_scores("scores.csv")
    # scores.csv 안에 빈 줄이 있어도 에러 없이 무시되는지 확인
    assert not any("빈 줄" in s[2] for s in skipped)

def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert ("최,네번", 77) in kept


# --- STEP 2: 예외 및 경계값 (raises, parametrize) ---
def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")

def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []

@pytest.mark.parametrize("점수, 유효한가", [
    (-1, False),   # 경계 아래 (예외)
    (0, True),     # 아래쪽 경계
    (1, True),     # 정상 범위 내
    (99, True),    # 정상 범위 내
    (100, True),   # 위쪽 경계
    (101, False)   # 경계 위 (예외)
])
def test_점수_경계값(tmp_path, 점수, 유효한가):
    # tmp_path를 써서 테스트용 임시 파일을 안전하게 생성
    test_csv = tmp_path / "임시.csv"
    test_csv.write_text(f"name,score\n학생,{점수}\n", encoding="utf-8")
    
    kept, skipped = load_scores(str(test_csv))
    assert (len(kept) == 1) == 유효한가