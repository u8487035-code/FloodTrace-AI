# FloodTrace AI – Baseline and Evaluation

## 1. Problem

During flood situations, emergency teams may receive many images that need to be reviewed.

A simple object detection result can identify possible people, but raw detection output alone does not organize cases into an easy-to-review rescue priority.

FloodTrace AI adds verification and priority stages while keeping a qualified human reviewer responsible for consequential decisions.

---

# 2. Baseline

## Baseline Approach

The baseline approach uses YOLOv8 directly to detect people in an uploaded image.

### Baseline Workflow

```text
Flood Image
    ↓
YOLOv8 Person Detection
    ↓
People Count + Confidence + Annotated Image
```

### Baseline Output

The baseline provides:

- Number of people detected
- Detection confidence
- Annotated image

### Baseline Limitation

The baseline does not provide:

- A separate verification stage
- Rescue priority classification
- Structured HIGH / MEDIUM / LOW recommendations
- A multi-stage decision-support workflow

---

# 3. Final Solution

FloodTrace AI extends the baseline with three agents.

```text
Flood Image
    ↓
Detection Agent
    ↓
Verification Agent
    ↓
Priority Agent
    ↓
Human Review
```

### Additional Features

- Verification stage
- HIGH / MEDIUM / LOW priority
- Mission summary
- Mission history
- Rescue reports
- Visual analytics
- Explicit human review checkpoint

---

# 4. Evaluation Method

The same test image should be used when comparing the baseline and final workflow.

For each image, record:

1. People detected
2. Detection confidence
3. Baseline output
4. Verification result
5. Final priority

---

# 5. Representative Evaluation Results

## Test Case 1 – No Person Detected

### Baseline

```text
People detected: 0
Result: No human detected
```

### Final System

```text
Priority: LOW
Recommendation: Continue monitoring
```

### Observation

The final system converts the direct detection result into a structured recommendation for human review.

---

## Test Case 2 – Clear Person Detected

### Baseline

```text
People detected: 1 or more
Confidence: >= 50%
```

### Final System

```text
Priority: HIGH
Recommendation:
Possible human presence detected.
Immediate rescue assessment recommended.
```

### Observation

The final system adds verification and priority interpretation to the raw detection result.

---

## Test Case 3 – Lower Confidence Detection

### Baseline

```text
People detected: 1 or more
Confidence: < 50%
```

### Final System

```text
Priority: MEDIUM
Recommendation:
Possible human presence detected,
but confidence is low.
Manual verification recommended.
```

### Observation

This case demonstrates why a MEDIUM category was added: low-confidence detections should not automatically be treated as HIGH priority.

---

# 6. Comparison

| Feature | Baseline | FloodTrace AI |
|---|---|---|
| Person Detection | Yes | Yes |
| Detection Confidence | Yes | Yes |
| Annotated Image | Yes | Yes |
| Verification Stage | No | Yes |
| Priority Classification | No | Yes |
| MEDIUM Priority | No | Yes |
| Mission History | No | Yes |
| Rescue Report | No | Yes |
| Human Review Checkpoint | Implicit | Explicit |

---

# 7. Main Improvement

The main improvement is not a claim that the multi-agent system makes YOLO detect more people accurately.

Instead, the key improvement is that raw detection output is transformed into a structured decision-support workflow:

```text
Detection
    ↓
Verification
    ↓
Priority Recommendation
    ↓
Human Review
```

This makes the output easier to organize and review while retaining human control over consequential actions.

---

# 8. Evidence

Evidence for evaluation should include screenshots from actual FloodTrace AI runs showing:

- Original uploaded image
- Annotated detection image
- People count
- Detection confidence
- Verification result
- HIGH, MEDIUM, or LOW priority

The solution video should demonstrate at least one complete realistic execution.

---

# 9. Main Failure Mode

The main failure mode is inaccurate person detection in difficult scenes.

Examples include:

- Occluded people
- Small or distant people
- Poor lighting
- Blurry images
- Severe flooding
- Complex backgrounds

Because of this limitation, FloodTrace AI must not make autonomous rescue decisions.

---

# 10. Hot Take

A more complex AI system is not automatically safer.

For emergency decision-support, clearly exposing uncertainty and requiring qualified human review can be more valuable than presenting an automated decision as certain.