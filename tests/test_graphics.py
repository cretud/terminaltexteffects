import pytest
from terminaltexteffects.utils.graphics import Color
from terminaltexteffects.utils import hexterm

#Test suite made by Arber Gjigolli

def test_color_init_with_valid_xterm_color():
    # Mock the xterm_to_hex function to control its output
    hexterm.xterm_to_hex = lambda x: "ffffff" if x == 255 else "000000"
    
    color = Color(255)
    assert color.color_arg == 255
    assert color.xterm_color == 255
    assert color.rgb_color == "ffffff"
    
    color = Color(0)
    assert color.color_arg == 0
    assert color.xterm_color == 0
    assert color.rgb_color == "000000"

def test_color_init_with_invalid_color_value():
    # Test with an invalid color value
    with pytest.raises(ValueError, match=r"Invalid color value\. Color must be an XTerm-256 color code or an RGB hex color string\. Example: 255 or 'ffffff' or '#ffffff'"):
        Color("invalid_color")
        
    with pytest.raises(ValueError, match=r"Invalid color value\. Color must be an XTerm-256 color code or an RGB hex color string\. Example: 255 or 'ffffff' or '#ffffff'"):
        Color(256)

def test_color_init_with_valid_hex_color():
    color = Color("#ffffff")
    assert color.color_arg == "#ffffff"
    assert color.xterm_color is None
    assert color.rgb_color == "ffffff"

    color = Color("000000")
    assert color.color_arg == "000000"
    assert color.xterm_color is None
    assert color.rgb_color == "000000"
