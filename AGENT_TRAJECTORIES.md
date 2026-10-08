# FloodTrace AI – Agent Trajectories

## Overview

FloodTrace AI uses three agents:

1. Detection Agent
2. Verification Agent
3. Priority Agent

The complete workflow is:

```text
Uploaded Image
      ↓
Detection Agent
      ↓
Verification Agent
      ↓
Priority Agent
      ↓
Human Review
      ↓
Final Rescue Action
```

The system provides decision support only. No rescue action is automatically performed.

---

# 1. Detection Agent Trajectory

## Agent Instruction

Analyze the uploaded image and detect people.

Return:

- Number of people detected
- Highest detection confidence
- Detection result
- Annotated image

## Input

A user uploads a JPG, JPEG, or PNG image through the Streamlit application.

## Action

The Detection Agent:

1. Receives the image as a NumPy array.
2. Sends the image to the YOLOv8 model.
3. Reviews detected bounding boxes.
4. Keeps detections where the COCO class is `person`.
5. Counts detected people.
6. Records the highest confidence score.
7. Draws bounding boxes and labels on the image.

## Tool / Component Response

The YOLOv8 model returns object detections containing:

- Class ID
- Confidence
- Bounding box coordinates

Example representative result:

```text
People detected: 1
Highest confidence: 0.78
Result: Possible human presence
```

## Feedback That Shapes the Next Step

The detection count and confidence are passed to the Verification Agent.

If no person is detected, the later agents receive a people count of zero.

## Retry / Limitation

Detection quality can vary depending on:

- Image quality
- Lighting
- Occlusion
- Distance from the camera
- Flood conditions

The application does not automatically retry detection with altered thresholds. Instead, uncertain results are surfaced for human review.

## Human Checkpoint

The detection result is not treated as a final rescue decision.

A qualified human reviewer must assess important cases before real-world action.

---

# 2. Verification Agent Trajectory

## Agent Instruction

Review the Detection Agent result and determine whether the detection should be considered sufficiently reliable or whether human review is recommended.

## Input

The Verification Agent receives information from the Detection Agent, including:

```text
People count
Detection confidence
Detection result
```

## Action

The Verification Agent evaluates the detection output according to its implemented verification logic.

It returns:

- Verification status
- Verified value
- Verification confidence

## Example Representative Result

```text
Status: VERIFIED
Verified: True
Verification confidence: 0.78
```

Or, for a less reliable result:

```text
Status: HUMAN REVIEW RECOMMENDED
Verified: False
Verification confidence: Lower confidence result
```

## Feedback That Shapes the Next Step

The Verification Agent sends its result to the Priority Agent.

This adds an additional decision-support stage between raw object detection and rescue prioritization.

## Retry / Human Checkpoint

When the result is uncertain, the system recommends human review rather than automatically treating the result as confirmed.

---

# 3. Priority Agent Trajectory

## Agent Instruction

Classify the situation as:

- HIGH
- MEDIUM
- LOW

based on the Detection Agent result.

## Input

The Priority Agent receives:

```text
People count
Detection confidence
Verification result
```

## Decision Process

### HIGH Priority

```text
People detected >= 1
AND
Detection confidence >= 0.50
```

### MEDIUM Priority

```text
People detected >= 1
AND
Detection confidence < 0.50
```

### LOW Priority

```text
No people detected
```

## Example Trajectory

### Input

```text
People detected: 1
Detection confidence: 0.78
```

### Decision

The people count is at least 1 and confidence is greater than or equal to 0.50.

### Output

```text
Priority: HIGH

Message:
Possible human presence detected.
Immediate rescue assessment recommended.
```

## Feedback and Final Result

The Priority Agent result is displayed in the FloodTrace AI interface as a recommendation.

The result is also included in:

- Mission Summary
- Visual Analytics Dashboard
- Rescue Report
- Mission History

## Human Checkpoint

HIGH, MEDIUM, and LOW are recommendations only.

The system does not automatically dispatch emergency services or initiate a rescue.

A qualified human reviewer must approve any consequential real-world action.
