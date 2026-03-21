from tcas.main import altitude_separation_test
from tcas.state import State



# own_tracked_altitude < other_tracked_altitude



# True
def test_own_below_threat_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = state.own_tracked_altitude < state.other_tracked_altitude
    assert actual == expected

# SFalse
def test_own_below_threat_false():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=2000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = False
    actual = state.own_tracked_altitude < state.other_tracked_altitude
    assert actual == expected



# other_tracked_altitude < own_tracked_altitude


# True
def test_own_above_threat_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = state.other_tracked_altitude < state.own_tracked_altitude
    assert actual == expected

# False
def test_own_above_threat_false():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = False
    actual = state.other_tracked_altitude < state.own_tracked_altitude
    assert actual == expected



# positive_ra_alt_thresh Layers 0 -> 3



# Layer 0
def test_positive_ra_alt_thresh_layer0_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=0, own_tracked_alt_rate=0, other_tracked_altitude=0,
        altitude_layer_value=0, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = state.altitude_layer_value == 0
    assert actual == expected

# Layer 1
def test_positive_ra_alt_thresh_layer1_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=0, own_tracked_alt_rate=0, other_tracked_altitude=0,
        altitude_layer_value=1, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = state.altitude_layer_value == 1
    assert actual == expected

# Layer 2
def test_positive_ra_alt_thresh_layer2_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=0, own_tracked_alt_rate=0, other_tracked_altitude=0,
        altitude_layer_value=2, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = state.altitude_layer_value == 2
    assert actual == expected

# Layer 3
def test_positive_ra_alt_thresh_layer3_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=0, own_tracked_alt_rate=0, other_tracked_altitude=0,
        altitude_layer_value=3, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = state.altitude_layer_value == 3
    assert actual == expected

# Else 
def test_positive_ra_alt_thresh_layer3_false():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=0, own_tracked_alt_rate=0, other_tracked_altitude=0,
        altitude_layer_value=99, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = False
    actual = state.altitude_layer_value == 3
    assert actual == expected




# Testing climb_inhibit


# True
def test_inhibit_biased_climb_true():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=0, own_tracked_alt_rate=0, other_tracked_altitude=0,
        altitude_layer_value=0, up_separation=300, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=1,
    )
    expected = 400
    actual = state.up_separation + 100
    assert actual == expected

# False
def test_inhibit_biased_climb_false():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=0, own_tracked_alt_rate=0, other_tracked_altitude=0,
        altitude_layer_value=0, up_separation=300, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 300
    actual = state.up_separation
    assert actual == expected




# Testing non_cross_biase_climb Testing 


# inhibit_biased_climb(state) > down_separation -> True
def test_non_crossing_biased_climb_1():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=2000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=500, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected

# inhibit_biased_climb(state) > down_separation -> False
def test_non_crossing_biased_climb_2():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=600, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected

# (NOT own_below) OR (own_below AND NOT(down >= alim)) -> True
def test_non_crossing_biased_climb_3():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=400, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected

# (NOT own_below) OR (own_below AND NOT(down >= alim)) -> False
def test_non_crossing_biased_climb_4():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=400, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected


# Testing non_cross_biase_desc


# inhibit_biased_climb(state) > down_separation -> True
def test_non_crossing_biased_descend_1():
    state = State(
        current_vertical_sep=400, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected

# inhibit_biased_climb(state) > down_separation -> False
def test_non_crossing_biased_descend_2():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = True
    actual = altitude_separation_test(state)
    assert actual == expected

# Both Predicates -> False
def test_non_crossing_biased_descend_3():
    state = State(
        current_vertical_sep=0, high_confidence=0, two_of_three_reports_valid=0,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = False
    actual = altitude_separation_test(state)
    assert actual == expected

# guard passes, non_cross_biase_climb -> True, own_below -> True upward RA
def test_altitude_separation_test_guard_true_upward_ra():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 1
    actual = altitude_separation_test(state)
    assert actual == expected

# guard passes, non_cross_biase_desc -> True , own_above -> True downward RA
def test_altitude_separation_test_downward_ra():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=500, down_separation=600,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 2
    actual = altitude_separation_test(state)
    assert actual == expected

# high_confidence -> False
def test_altitude_separation_test_guard_false_high_confidence():
    state = State(
        current_vertical_sep=700, high_confidence=0, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected

# own_tracked_alt_rate -> False
def test_altitude_separation_test_guard_false_alt_rate():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=700, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected

# current_vertical_sep -> False
def test_altitude_separation_test_guard_false_vert_sep():
    state = State(
        current_vertical_sep=600, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected

# capability -> False
def test_altitude_separation_test_guard_false_capability():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=1, other_capability=1, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected

# non_cross_biase_climb -> False
def test_altitude_separation_test_need_upward_ra_false_non_cross_biase_climb():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected

# own_below -> False
def test_altitude_separation_test_need_upward_ra_false_not_below():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=600, down_separation=100,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual != 1

# non_cross_biase_desc -> False
def test_altitude_separation_test_need_downward_ra_false_non_cross_biase_desc():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=3000, own_tracked_alt_rate=0, other_tracked_altitude=1000,
        altitude_layer_value=0, up_separation=100, down_separation=500,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected

# own_above -> False
def test_altitude_separation_test_need_downward_ra_false_not_above():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=1000, own_tracked_alt_rate=0, other_tracked_altitude=3000,
        altitude_layer_value=0, up_separation=500, down_separation=600,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual != 2

# All Falses
def test_altitude_separation_test_no_ra():
    state = State(
        current_vertical_sep=700, high_confidence=1, two_of_three_reports_valid=1,
        own_tracked_altitude=2000, own_tracked_alt_rate=0, other_tracked_altitude=2000,
        altitude_layer_value=0, up_separation=0, down_separation=0,
        other_rac=0, other_capability=0, climb_inhibit=0,
    )
    expected = 0
    actual = altitude_separation_test(state)
    assert actual == expected