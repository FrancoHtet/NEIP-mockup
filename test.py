# --- WRITE YOUR CODE HERE ---
def filter_critical_errors(logs):
    return list(filter(lambda log: log["resolved"] == False and log["level"] == "CRITICAL", logs))


# --- AUTOMATED TEST CASES ---
def run_tests():
    # Test Case 1: Standard mixed logs
    mixed_logs = [
        {"id": 1, "level": "INFO", "resolved": True},
        {"id": 2, "level": "CRITICAL", "resolved": False}, # Match
        {"id": 3, "level": "CRITICAL", "resolved": True},
        {"id": 4, "level": "WARN", "resolved": False},
        {"id": 5, "level": "CRITICAL", "resolved": False}  # Match
    ]
    result_1 = filter_critical_errors(mixed_logs)
    assert len(result_1) == 2, f"Expected 2 matches, got {len(result_1)}"
    assert result_1[0]["id"] == 2, "First match should be log ID 2"
    assert result_1[1]["id"] == 5, "Second match should be log ID 5"

    # Test Case 2: No matches present
    safe_logs = [
        {"id": 1, "level": "INFO", "resolved": False},
        {"id": 2, "level": "CRITICAL", "resolved": True}
    ]
    assert filter_critical_errors(safe_logs) == [], "Expected empty list when no matches exist"

    # Test Case 3: Empty input list
    assert filter_critical_errors([]) == [], "Expected empty list for empty input"

    print("🎉 All test cases passed successfully!")

# Execute the tests
run_tests()
