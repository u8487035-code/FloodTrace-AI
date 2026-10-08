# 📈 FloodTrace AI – Improvement Changelog

## Project: FloodTrace AI

AI-Assisted Flood Search, Detection and Rescue Prioritization System

---

# Version 1 – Initial Prototype

## Initial System

The initial version of FloodTrace AI focused on detecting people from uploaded images.

### Features

- Image upload
- YOLOv8 person detection
- People count
- Detection confidence
- Annotated detection image

### Limitation

The initial system only provided object detection results.

It did not include:

- Detection verification
- Rescue prioritization
- Mission storage
- Rescue reports
- Analytics dashboard

---

# Version 2 – Multi-Agent System

The project was improved by introducing a multi-agent architecture.

## Detection Agent 🔎

The Detection Agent:

- Receives the uploaded image
- Uses YOLOv8 for person detection
- Counts detected people
- Calculates the highest detection confidence
- Generates an annotated image

### Output

- People detected
- Detection confidence
- Detection result
- Annotated image

---

## Verification Agent 🔍

A Verification Agent was added as a second decision layer.

The Verification Agent:

- Reviews the detection result
- Checks the detection confidence
- Determines whether the result should be trusted
- Recommends human review when required

### Benefit

This provides an additional verification stage instead of relying only on the object detection model.

---

## Priority Agent 🚨

A Priority Agent was added to classify rescue urgency.

### HIGH Priority

```text
People detected ≥ 1
AND
Detection confidence ≥ 50%