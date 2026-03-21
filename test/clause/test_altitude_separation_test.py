from tcas.main import altitude_separation_test
from tcas.state import State
 
def test_non_crossing_biased_climb_inner_false():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=600, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P9 | not own_below=not_below={not(state.own_tracked_altitude < state.other_tracked_altitude)} | not(down>=alim)=not(down>=alim)={not(state.down_separation >= 400)}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected
 
def test_non_crossing_biased_climb_inner_c1_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=2000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=600, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P9/not own_below | c1=not_below={not(state.own_tracked_altitude < state.other_tracked_altitude)} | not(down>=alim)=not(down>=alim)={not(state.down_separation >= 400)}")
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected
 
def test_non_crossing_biased_climb_inner_c3_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P9/not(down>=alim) | not own_below=not_below={not(state.own_tracked_altitude < state.other_tracked_altitude)} | not(down>=alim)=not(down>=alim)={not(state.down_separation >= 400)}")
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_climb_else_all_true():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=400, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P10 | own_above=own_above={state.other_tracked_altitude < state.own_tracked_altitude} | sep>=300={state.current_vertical_sep >= 300} | up>=alim={state.up_separation >= 400}")
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_climb_else_c1_false():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=400, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P10/own_above | own_above={state.other_tracked_altitude < state.own_tracked_altitude} | =sep>=300={state.current_vertical_sep >= 300} | up>=alim={state.up_separation >= 400}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_climb_else_c2_false():
    state = State(
        current_vertical_sep=200, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=400, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P10/sep>=300 | own_above={state.other_tracked_altitude < state.own_tracked_altitude} | sep>=300={state.current_vertical_sep >= 300} | up>=alim={state.up_separation >= 400}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_climb_else_c3_false():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=300, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P10/up>=alim | own_above={state.other_tracked_altitude < state.own_tracked_altitude} | sep>=300={state.current_vertical_sep >= 300} | up>=alim={state.up_separation >= 400}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected
 
def test_non_crossing_biased_descend_inner_all_true():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=600, down_separation=450,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P12 | own_below={state.own_tracked_altitude < state.other_tracked_altitude} | sep>=300={state.current_vertical_sep >= 300} | down>=alim={state.down_separation >= 400}")
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_descend_inner_c1_false():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=600, down_separation=450,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P12/own_below | own_below={state.own_tracked_altitude < state.other_tracked_altitude} | sep>=300={state.current_vertical_sep >= 300} | down>=alim={state.down_separation >= 400}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_descend_inner_c2_false():
    state = State(
        current_vertical_sep=200, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=600, down_separation=450,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P12/sep>=300 | own_below={state.own_tracked_altitude < state.other_tracked_altitude} | =sep>=300={state.current_vertical_sep >= 300} | down>=alim={state.down_separation >= 400}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected

def test_non_crossing_biased_descend_inner_c3_false():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P12/down>=alim | own_below={state.own_tracked_altitude < state.other_tracked_altitude} | sep>=300={state.current_vertical_sep >= 300} | down>=alim={state.down_separation >= 400}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected
 
def test_non_crossing_biased_descend_else_false():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P13 | not own_above={not(state.other_tracked_altitude < state.own_tracked_altitude)} | up>=alim={state.up_separation >= 400}")
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_descend_else_c1_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P13/not own_above | not own_above={not(state.other_tracked_altitude < state.own_tracked_altitude)} | up>=alim={state.up_separation >= 400}")
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected
 

def test_non_crossing_biased_descend_else_c3_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=500, down_separation=600,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P13/up>=alim | not_above={not(state.other_tracked_altitude < state.own_tracked_altitude)} | up>=alim={state.up_separation >= 400}")
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected
 
 


# Going over the True Falses 
def test_altitude_separation_test_guard_all_true():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=1, climb_inhibit=0,
    )
    print(f"\n[MCDC] P14 | c1={state.high_confidence} | c2={state.own_tracked_alt_rate<=600} | c3={state.current_vertical_sep>600} | c4={state.other_capability==1} | c5={state.two_of_three_reports_valid} | c6={state.other_rac==0}")
    expected = 1
    actual = altitude_separation_test(state)
    assert actual == expected
 
# First value is false
def test_altitude_separation_test_guard_c1_false():
    state = State(
        current_vertical_sep=700, high_confidence=0, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=1, climb_inhibit=0,
    )
    print(f"\n[MCDC] P14/c1 | c1={state.high_confidence} | c2={state.own_tracked_alt_rate<=600} | c3={state.current_vertical_sep>600} | c4={state.other_capability==1} | c5={state.two_of_three_reports_valid} | c6={state.other_rac==0}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected
 
# Second Value is false
def test_altitude_separation_test_guard_c2_false():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=700, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=1, climb_inhibit=0,
    )
    print(f"\n[MCDC] P14/c2 | c1={state.high_confidence} | c2={state.own_tracked_alt_rate<=600} | c3={state.current_vertical_sep>600} | c4={state.other_capability==1} | c5={state.two_of_three_reports_valid} | c6={state.other_rac==0}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected
 
# Third value is false
def test_altitude_separation_test_guard_c3_false():
    state = State(
        current_vertical_sep=600, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=1, climb_inhibit=0,
    )
    print(f"\n[MCDC] P14/c3 | c1={state.high_confidence} | c2={state.own_tracked_alt_rate<=600} | c3={state.current_vertical_sep>600} | c4={state.other_capability==1} | c5={state.two_of_three_reports_valid} | c6={state.other_rac==0}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected
 
# 4/5 value is false (Can be condensed into 1)
def test_altitude_separation_test_guard_c5_false():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=1, climb_inhibit=0,
    )
    print(f"\n[MCDC] P14/c5 | c4={state.other_capability==1} | c5={state.two_of_three_reports_valid} | c6={state.other_rac==0}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected
 
# Last value is false
def test_altitude_separation_test_guard_c6_false():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=1, other_capability=1, climb_inhibit=0,
    )
    print(f"\n[MCDC] P14/c6 | c4={state.other_capability==1} | c5={state.two_of_three_reports_valid} | c6={state.other_rac==0}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected
 
# non_cross_bias_climb=F, c2=T own_below
def test_altitude_separation_test_need_upward_c1_false():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P15/c1 | c1=non_cross_bias_climb=F | c2=own_below={state.own_tracked_altitude < state.other_tracked_altitude}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected
 
# own NOT below, c1=T non_cross_bias_climb=T
def test_altitude_separation_test_need_upward_c2_false():
    state = State(
        current_vertical_sep=400, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=400, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P15/c2 | c1=non_cross_bias_climb=T(via P10) | c2=own_below={state.own_tracked_altitude < state.other_tracked_altitude}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual != 1
 
#non_cross_bias_desc=F, own_above = T
def test_altitude_separation_test_need_downward_c1_false():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P16/c1 | c1=non_cross_bias_desc=F | c2=own_above={state.other_tracked_altitude < state.own_tracked_altitude}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected
 
# own NOT above, non_cross_bias_desc=T 
def test_altitude_separation_test_need_downward_c2_false():
    state = State(
        current_vertical_sep=400, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=600, down_separation=450,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    print(f"\n[MCDC] P16/c2 | c1=non_cross_bias_desc=T(via P12) | c2=own_above={state.other_tracked_altitude < state.own_tracked_altitude}")
    expected = 0
    actual = altitude_separation_test(state)
    assert actual != 2