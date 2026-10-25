
from tray_inspection import classify_tray


def test_fail():
    """A high-confidence defect should fail."""
    detections = [
        {"class": "unsealed", "confidence": 0.90}
    ]
    assert classify_tray(detections) == "FAIL"


def test_review():
    """A medium-confidence defect requires review."""
    detections = [
        {"class": "wrinkle", "confidence": 0.60}
    ]
    assert classify_tray(detections) == "REVIEW"


def test_provisional_pass():
    """No detected defects gives provisional pass."""
    assert classify_tray([]) == "PROVISIONAL PASS"


def test_fail_threshold():
    """Exactly 75% confidence should fail."""
    detections = [
        {"class": "loose-meat", "confidence": 0.75}
    ]
    assert classify_tray(detections) == "FAIL"
