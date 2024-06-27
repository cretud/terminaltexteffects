import pytest
from terminaltexteffects.utils.easing import in_out_cubic

# Branch coverage dictionary
branch_coverage = {}

def track_coverage(branch_name):
    branch_coverage[branch_name] = True

# Initialize branch coverage with all branches set to False (not hit)
def initialize_branch_coverage():
    global branch_coverage
    branch_coverage = {
        "less_than_half": False,
        "greater_than_or_equal_to_half": False,
    }

# Tests
def test_in_out_cubic():
    # Test the extremes and a couple of middle values
    assert in_out_cubic(0.0) == 0.0, "Failed at progress_ratio=0.0"
    track_coverage("less_than_half")

    assert in_out_cubic(1.0) == 1.0, "Failed at progress_ratio=1.0"
    track_coverage("greater_than_or_equal_to_half")

    # Test middle values to ensure the function transitions smoothly
    assert in_out_cubic(0.25) == 4 * 0.25**3, "Failed at progress_ratio=0.25"
    track_coverage("less_than_half")

    assert in_out_cubic(0.75) == 1 - (-2 * 0.75 + 2) ** 3 / 2, "Failed at progress_ratio=0.75"
    track_coverage("greater_than_or_equal_to_half")

    # Test the mid-point for symmetry
    mid_point = 0.5
    assert in_out_cubic(mid_point) == 0.5, "Failed at progress_ratio=0.5"
    track_coverage("greater_than_or_equal_to_half")

    # Additional tests for other values in the range
    assert pytest.approx(in_out_cubic(0.1), rel=1e-9) == 4 * 0.1**3, "Failed at progress_ratio=0.1"
    track_coverage("less_than_half")

    assert pytest.approx(in_out_cubic(0.9), rel=1e-9) == 1 - (-2 * 0.9 + 2) ** 3 / 2, "Failed at progress_ratio=0.9"
    track_coverage("greater_than_or_equal_to_half")

    # Boundary tests near the mid-point
    assert pytest.approx(in_out_cubic(0.499), rel=1e-9) == 4 * 0.499**3, "Failed at progress_ratio=0.499"
    track_coverage("less_than_half")

    assert pytest.approx(in_out_cubic(0.501), rel=1e-9) == 1 - (-2 * 0.501 + 2) ** 3 / 2, "Failed at progress_ratio=0.501"
    track_coverage("greater_than_or_equal_to_half")

# Function to print coverage results
def print_coverage():
    method_branches = {
        "in_out_cubic": ["less_than_half", "greater_than_or_equal_to_half"]
    }
    
    for method, branches in method_branches.items():
        hit_branches = sum(branch_coverage.get(branch, False) for branch in branches)
        total_branches = len(branches)
        coverage_percentage = (hit_branches / total_branches) * 100
        print(f"Coverage for {method}: {hit_branches}/{total_branches} branches hit ({coverage_percentage:.2f}%)")
        for branch in branches:
            print(f"  {branch} was {'hit' if branch_coverage.get(branch, False) else 'not hit'}")

# Function to run tests and print coverage
def run_tests():
    initialize_branch_coverage()
    test_in_out_cubic()
    print_coverage()

if __name__ == "__main__":
    run_tests()
    print_coverage()