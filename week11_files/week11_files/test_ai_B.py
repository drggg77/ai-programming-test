import pytest

from bug3_logic import find_max


@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        ([70, 85, 60, 95], 95),  # 마지막 원소가 최댓값
        ([95, 85, 70, 60], 95),  # 첫 원소가 최댓값
        ([10, 30, 20], 30),      # 중간 원소가 최댓값
        ([1], 1),                # 원소 하나
        ([1, 2], 2),              # 원소 둘
        ([-8, -2, -5], -2),      # 음수
        ([4, 4, 4], 4),          # 중복 최댓값
    ],
)
def test_find_max_returns_largest_score(scores, expected):
    assert find_max(scores) == expected


def test_find_max_raises_index_error_for_empty_list():
    with pytest.raises(IndexError):
        find_max([])