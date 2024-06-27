import pytest
from terminaltexteffects.utils.easing import in_out_cubic

def test_in_out_cubic():
    # Test the extremes and a couple of middle values
    assert in_out_cubic(0.0) == 0.0, "Failed at progress_ratio=0.0"
    assert in_out_cubic(1.0) == 1.0, "Failed at progress_ratio=1.0"

    # Test middle values to ensure the function transitions smoothly
    assert in_out_cubic(0.25) == 4 * 0.25**3, "Failed at progress_ratio=0.25"
    assert in_out_cubic(0.75) == 1 - (-2 * 0.75 + 2) ** 3 / 2, "Failed at progress_ratio=0.75"

    # Test the mid-point for symmetry
    mid_point = 0.5
    assert in_out_cubic(mid_point) == 0.5, "Failed at progress_ratio=0.5"

    # Additional tests for other values in the range
    assert pytest.approx(in_out_cubic(0.1), rel=1e-9) == 4 * 0.1**3, "Failed at progress_ratio=0.1"
    assert pytest.approx(in_out_cubic(0.9), rel=1e-9) == 1 - (-2 * 0.9 + 2) ** 3 / 2, "Failed at progress_ratio=0.9"

    # Boundary tests near the mid-point
    assert pytest.approx(in_out_cubic(0.499), rel=1e-9) == 4 * 0.499**3, "Failed at progress_ratio=0.499"
    assert pytest.approx(in_out_cubic(0.501), rel=1e-9) == 1 - (-2 * 0.501 + 2) ** 3 / 2, "Failed at progress_ratio=0.501"
