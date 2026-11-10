import pytest

from fit import compare_garments, describe_diff


@pytest.mark.parametrize(
    ("diff", "expected"),
    [
        (0, "거의 비슷함"),
        (1.0, "거의 비슷함"),
        (-1.0, "거의 비슷함"),
        (1.5, "조금 큼"),
        (-3.0, "조금 작음"),
        (3.1, "많이 큼"),
        (-5, "많이 작음"),
    ],
)
def test_describe_diff(diff, expected):
    assert describe_diff(diff) == expected


def test_compare_garments_reports_diff_and_summary():
    reference = {"허리": 38.0, "총장": 105.0, "허벅지": 30.0}
    product = {"허리": 38.5, "총장": 106.0, "허벅지": 31.5}

    result = compare_garments(reference, product)

    assert result["허리"] == {"diff_cm": 0.5, "summary": "거의 비슷함"}
    assert result["총장"] == {"diff_cm": 1.0, "summary": "거의 비슷함"}
    assert result["허벅지"] == {"diff_cm": 1.5, "summary": "조금 큼"}


def test_compare_garments_ignores_unshared_items():
    result = compare_garments({"허리": 38.0, "밑위": 30.0}, {"허리": 38.0, "밑단": 22.0})

    assert list(result) == ["허리"]
