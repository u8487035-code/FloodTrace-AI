# 🌊 FloodTrace AI

## AI-Assisted Flood Search, Detection and Rescue Prioritization System

FloodTrace AI is a multi-agent AI system designed to assist emergency response teams during flood situations. The system analyzes uploaded images, detects possible human presence, verifies the detection result, and assigns a rescue priority level.

> ⚠️ This project is designed as an AI-assisted decision-support system. Final rescue decisions must always be made by authorized human personnel.

---
# 👤 Intended Users

FloodTrace AI is intended for:

- Emergency response teams
- Disaster management teams
- Search and rescue coordinators
- Human reviewers supporting rescue operations

---

# 🚧 Current Bottleneck

During floods and disasters, emergency teams may receive many images from affected locations.

Manually reviewing every image can be slow and difficult, especially when:

- There are many incoming images
- Lighting conditions are poor
- People are partially hidden
- Images are blurry
- Rescue teams need to prioritize their attention

This can delay the identification of images that may require urgent human review.

---

# ⭐ Why Solving This Is Valuable

FloodTrace AI helps organize image analysis by automatically detecting possible human presence and assigning a preliminary priority level.

This can help rescue teams:

- Review potentially important images sooner
- Reduce the amount of manual image screening
- Focus human attention on higher-priority cases
- Maintain mission records and reports

FloodTrace AI does not replace emergency personnel.

The system is designed as a decision-support tool, and qualified human personnel must review important rescue decisions.

# 📌 Problem Statement

During floods and other disasters, rescue teams may need to analyze a large number of images from affected areas.

Manually checking every image can be slow and may delay emergency response.

FloodTrace AI helps by:

- Detecting people in uploaded images
- Measuring detection confidence
- Verifying detection results
- Assigning a rescue priority
- Generating a rescue report
- Maintaining mission history

The goal is to help emergency response teams identify images that may require immediate human attention.

---

# 🎯 Project Objective

The objective of FloodTrace AI is to build a multi-agent system that can analyze flood-related images and provide rescue prioritization.

The system follows this workflow:

```text
Flood Image
     ↓
Detection Agent
     ↓
Verification Agent
     ↓
Priority Agent
     ↓
Final Rescue Decision
     ↓
Mission Report and History

# 🧪 Baseline vs Final Solution

## Baseline

The baseline system performs direct person detection on an uploaded image using YOLOv8.

The baseline output includes:

- People count
- Detection confidence
- Annotated image

## Final Solution

The final FloodTrace AI system extends the baseline with:

- Detection Agent
- Verification Agent
- Priority Agent
- HIGH / MEDIUM / LOW rescue prioritization
- Mission history
- Visual analytics
- Rescue report generation

### Main Improvement

The biggest improvement was converting raw object detection output into a structured multi-agent decision-support workflow.

Instead of only displaying detected objects, the system now passes results through verification and priority classification before presenting a recommendation for human review.