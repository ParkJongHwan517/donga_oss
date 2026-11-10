"""FIT: Reference outFit 기준으로 상품 실측을 비교하는 핵심 로직."""

from fit.compare import compare_garments, describe_diff, summarize_fit

__all__ = ["compare_garments", "describe_diff", "summarize_fit"]
__version__ = "0.2.0"
