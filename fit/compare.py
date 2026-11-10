"""기준 옷(Reference outFit)과 상품의 실측 차이를 계산하고 문장으로 바꾼다.

문장 기준은 RFC #22의 결론을 따른다.
- 차이 1cm 이하: 거의 비슷함
- 1cm 초과 3cm 이하: 조금
- 3cm 초과: 많이
"""

from __future__ import annotations

NEAR_CM = 1.0
FAR_CM = 3.0


def describe_diff(diff_cm: float) -> str:
    """실측 차이(cm)를 사용자가 이해하기 쉬운 문장으로 바꾼다.

    양수는 상품이 기준 옷보다 크다는 뜻이다.
    """
    magnitude = abs(diff_cm)
    if magnitude <= NEAR_CM:
        return "거의 비슷함"
    degree = "조금" if magnitude <= FAR_CM else "많이"
    direction = "큼" if diff_cm > 0 else "작음"
    return f"{degree} {direction}"


def compare_garments(
    reference: dict[str, float],
    product: dict[str, float],
) -> dict[str, dict[str, float | str]]:
    """두 옷의 공통 측정 항목마다 차이(cm)와 설명을 돌려준다.

    한쪽에만 있는 항목은 비교할 수 없으므로 무시한다.
    """
    result: dict[str, dict[str, float | str]] = {}
    for name in reference.keys() & product.keys():
        diff = round(product[name] - reference[name], 1)
        result[name] = {"diff_cm": diff, "summary": describe_diff(diff)}
    return result
