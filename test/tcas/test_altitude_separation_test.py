from tcas.main import altitude_separation_test
from tcas.state import State
"""

ENABLE COVERAVGE 'uv add pytest-cov'
Test Requirements:
    - For positive_ra_alt_thresh:
        - Line 15: 
            - layer == 0 -> True
            - layer == 0 -> False
        - Line 17: 
            - layer == 1 -> True 
            - Layer == 1 -> False 
        - Line 19: 
            - layer == 2 -> True 
            - layer == 2 -> False 
        - Line 21: 
            - layer == 3 -> True 
            - layer == 3 -> False 
    - For non_crossing_biased_climb:
        - Line 35:
            - inhibit_biased_climb(state) > state.down_seperation -> True 
                - Line 36 -> 37 ?????
            - inhibit_biased_climb(state) > state.down_seperation -> False 
                - Line 40 -> 43
    - For non_crossing_biased_descend:
        - Line 48:
            - inhibit_biased_climb(state) > state.down_seperation -> True 
                - Line 49 -> 53 ?????
            - inhibit_biased_climb(state) > state.down_seperation -> False 
                - Line 55 -> 57
    - For altitude_seperation_test:
        - Line 63:
            - When:
                - state.high_confidence and (state.won_tracked_alt_rate <= 600) and (state.current_vertical_sep > 600) -> True
                - (state.other_capability == 1) and (state.two_of_three_reports_valid and state.other_rac == 0) -> True
                - or not (state.other_capability == 1) -> False 
            - Or when 1:
                - state.high_confidence and (state.won_tracked_alt_rate <= 600) and (state.current_vertical_sep > 600) -> False
                - (state.other_capability == 1) and (state.two_of_three_reports_valid and state.other_rac == 0) -> False
                - or not (state.other_capability == 1) -> True 
                - Sub Tests:
                    - Line 79: need_upward_RA and need_downward_RA -> True 
                    - Line 81: need_upward_RA -> True 
                    - Line 83: need_downward_RA -> True 
                    - Line 85: need_upward_RA and need_downward_RA -> False  
"""

def test():
    state = State(
        current_vertical_sep=0,
        high_confidence=0,
        two_of_three_reports_valid=0,
        own_tracked_altitude=0,
        own_tracked_alt_rate=0,
        other_tracked_altitude=0,
        altitude_layer_value=0,
        up_separation=0,
        down_separation=0,
        other_rac=0,
        other_capability=0,
        climb_inhibit=0,
    )

    expected = 0

    actual = altitude_separation_test(state)

    assert actual == expected
