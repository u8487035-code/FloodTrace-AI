
def verify_detection(detection_result):

    people_count = detection_result.get("people_count", 0)
    confidence = detection_result.get("confidence", 0)

    # High confidence
    if people_count > 0 and confidence >= 0.80:

        status = "High confidence - human presence likely"
        verified = True

    # Medium confidence
    elif people_count > 0 and confidence >= 0.50:

        status = "Medium confidence - needs human review"
        verified = False

    # Low confidence
    elif people_count > 0:

        status = "Low confidence - manual verification required"
        verified = False

    # No people
    else:

        status = "No human presence detected"
        verified = False

    return {
        "status": status,
        "verified": verified,
        "confidence": confidence
    }