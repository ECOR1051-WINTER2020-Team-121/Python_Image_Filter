
from T121_P4_posterize import posterize


def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")


def test_posterize() -> None:
    """
    Tests function posterize

    >>> test_posterize()
    """
    # This test will involve a transformation from original -> Posterized (Decreased number of colours)

    # Quadrant definitions:
    #   I: 0-63
    #   II: 64-127
    #   III: 128-191
    #   IV: 192-255

    # ** Testing each combination would be too tiresome... Better to test if it transforms each case at the same time.

    # This function will test if function posterize() correctly transforms:
    # 0. (0, 0, 0) -> (31, 31, 31)  # Q1 Lower Boundary channel value
    # 1. (1, 1, 1) -> (31, 31, 31)  # Q1 non-boundary channel value
    # 2. (63, 63, 63) -> (31, 31, 31)   # Q1 Upper Boundary channel value
    # 3. (64, 64, 64) -> (95, 95, 95)   # Q2 Lower Boundary channel value
    # 4. (65, 65, 65) -> (95, 95, 95)   # Q2 non-boundary channel value
    # 5. (127, 127, 127) -> (95, 95, 95)    # Q2 Upper Boundary channel value
    # 6. (128, 128, 128) -> (
