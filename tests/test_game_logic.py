from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

#tests added to test secret number bug by using Copilot
def test_numeric_comparison_not_string():
    """Test that secret number bug is fixed: uses numeric comparison, not string comparison."""
    # This test ensures we're doing numeric comparison, not string comparison
    # In string comparison, "9" > "10" is True (alphabetically)
    # In numeric comparison, 9 > 10 is False
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low", "9 should be too low compared to 10 (numeric, not string)"
    
    # In string comparison, "2" > "100" is True (alphabetically)
    # In numeric comparison, 2 > 100 is False
    outcome, _ = check_guess(2, 100)
    assert outcome == "Too Low", "2 should be too low compared to 100 (numeric, not string)"
    
    # Verify correct "too high" with single vs multi-digit
    outcome, _ = check_guess(15, 9)
    assert outcome == "Too High", "15 should be too high compared to 9"
