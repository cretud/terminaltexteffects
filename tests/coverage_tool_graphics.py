import pytest
from terminaltexteffects.utils.graphics import Color
from terminaltexteffects.utils import hexterm

# Branch coverage dictionary
branch_coverage = {}

def track_coverage(branch_name):
    branch_coverage[branch_name] = True

# Initialize branch coverage with all branches set to False (not hit)
def initialize_branch_coverage():
    global branch_coverage
    branch_coverage = {
        "init_xterm_color_int": False,
        "init_xterm_color_str": False,
        "init_invalid_color": False,
    }

# Tests
def test_color_init_with_valid_xterm_color():
    # Mock the xterm_to_hex function to control its output
    hexterm.xterm_to_hex = lambda x: "ffffff" if x == 255 else "000000"
    
    color = Color(255)
    assert color.color_arg == 255
    assert color.xterm_color == 255
    assert color.rgb_color == "ffffff"
    track_coverage("init_xterm_color_int")
    
    color = Color(0)
    assert color.color_arg == 0
    assert color.xterm_color == 0
    assert color.rgb_color == "000000"

def test_color_init_with_invalid_color_value():
    # Test with an invalid color value
    with pytest.raises(ValueError, match=r"Invalid color value\. Color must be an XTerm-256 color code or an RGB hex color string\. Example: 255 or 'ffffff' or '#ffffff'"):
        Color("invalid_color")
    track_coverage("init_invalid_color")
        
    with pytest.raises(ValueError, match=r"Invalid color value\. Color must be an XTerm-256 color code or an RGB hex color string\. Example: 255 or 'ffffff' or '#ffffff'"):
        Color(256)
    track_coverage("init_invalid_color")

def test_color_init_with_valid_hex_color():
    color = Color("#ffffff")
    assert color.color_arg == "#ffffff"
    assert color.xterm_color is None
    assert color.rgb_color == "ffffff"
    track_coverage("init_xterm_color_str")

    color = Color("000000")
    assert color.color_arg == "000000"
    assert color.xterm_color is None
    assert color.rgb_color == "000000"
    track_coverage("init_xterm_color_str")

def print_coverage():
    method_branches = {
        "__init__": ["init_xterm_color_int", "init_xterm_color_str", "init_invalid_color"]
    }
    
    for method, branches in method_branches.items():
        hit_branches = sum(branch_coverage.get(branch, False) for branch in branches)
        total_branches = len(branches)
        coverage_percentage = (hit_branches / total_branches) * 100
        print(f"Coverage for {method}: {hit_branches}/{total_branches} branches hit ({coverage_percentage:.2f}%)")
        for branch in branches:
            print(f"  {branch} was {'hit' if branch_coverage.get(branch, False) else 'not hit'}")

def run_tests():
    initialize_branch_coverage()
    test_color_init_with_valid_xterm_color()
    test_color_init_with_invalid_color_value()
    test_color_init_with_valid_hex_color()

if __name__ == "__main__":
    run_tests()
    print_coverage()
