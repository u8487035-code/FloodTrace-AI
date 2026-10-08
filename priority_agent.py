
def calculate_priority(detection_result, verification_result):

    # ==================================
    # GET DETECTION VALUES
    # ==================================

    people_count = detection_result.get(
        "people_count",
        0
    )

    confidence = detection_result.get(
        "confidence",
        0
    )

    verified = verification_result.get(
        "verified",
        False
    )


    # ==================================
    # HIGH PRIORITY
    # Multiple people + strong confidence
    # ==================================

    if (
        people_count >= 3
        and confidence >= 0.70
        and verified
    ):

        priority = "HIGH"

        message = (
            "Multiple people detected with strong "
            "verification. Immediate rescue assessment "
            "recommended."
        )


    # ==================================
    # MEDIUM PRIORITY
    # One or two people detected
    # ==================================

    elif people_count >= 1:

        priority = "MEDIUM"

        if verified:

            message = (
                "Possible human presence verified. "
                "Rescue team review and assessment "
                "recommended."
            )

        else:

            message = (
                "Possible human presence detected, "
                "but additional human verification "
                "is recommended."
            )


    # ==================================
    # LOW PRIORITY
    # No people detected
    # ==================================

    else:

        priority = "LOW"

        message = (
            "No human presence detected. "
            "Continue monitoring the affected area."
        )


    # ==================================
    # RETURN RESULT
    # ==================================

    return {

        "priority": priority,

        "people_count": people_count,

        "confidence": confidence,

        "verified": verified,

        "message": message
    }