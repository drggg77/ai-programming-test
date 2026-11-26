import pytest

from load_scores import load_scores


def test_loads_valid_rows_and_keeps_duplicate_names(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "\ufeffname,score\n Alice , 10 \nAlice,10\n",
        encoding="utf-8",
    )

    assert load_scores(path) == ([("Alice", 10), ("Alice", 10)], [])


@pytest.mark.parametrize("score", [0, 100])
def test_accepts_boundary_scores(tmp_path, score):
    path = tmp_path / "scores.csv"
    path.write_text(f"name,score\nStudent,{score}\n", encoding="utf-8")

    assert load_scores(path) == ([("Student", score)], [])


@pytest.mark.parametrize(
    ("row", "reason"),
    [
        ("Kim,80,extra", "열 개수가 2가 아님"),
        (",80", "이름이 비어 있음"),
        ("Kim,", "점수가 비어 있음"),
        ("Kim,abc", "점수가 정수가 아님"),
        ("Kim,-1", "점수가 0~100 밖"),
        ("Kim,101", "점수가 0~100 밖"),
    ],
)
def test_records_invalid_rows_as_skipped(tmp_path, row, reason):
    path = tmp_path / "scores.csv"
    path.write_text(f"name,score\n{row}\n", encoding="utf-8")

    assert load_scores(path) == ([], [(2, row, reason)])


def test_skips_blank_lines_without_recording_them(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("name,score\n\nKim,abc\n", encoding="utf-8")

    assert load_scores(path) == (
        [],
        [(3, "Kim,abc", "점수가 정수가 아님")],
    )


def test_header_only_file_returns_empty_lists(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("name,score\n", encoding="utf-8")

    assert load_scores(path) == ([], [])


def test_missing_file_raises_file_not_found_error(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores(tmp_path / "missing.csv")