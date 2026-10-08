# FloodTrace AI – Reproduction Guide

## 1. Project Overview

FloodTrace AI is an AI-assisted flood search, human detection,
verification, and rescue prioritization system.

The system analyzes a flood image and follows this workflow:

Flood Image
↓
Detection Agent
↓
Verification Agent
↓
Priority Agent
↓
Final Rescue Decision

The system is designed to assist emergency response teams.
Final rescue decisions should always be reviewed by authorized
human personnel.

---

# 2. Requirements

Before running the project, install:

- Python 3.10 or later
- pip
- A stable internet connection for the first YOLO model download

---

# 3. Project Files

The project should contain:

```text
FloodTrace_AI/
│
├── app.py
├── detection_agent.py
├── verification_agent.py
├── priority_agent.py
├── requirements.txt
├── README.md
├── IMPROVEMENT_CHANGELOG.md
└── REPRODUCTION_GUIDE.md

---

# 4. Setup

Open a terminal inside the FloodTrace_AI project folder.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

---

# 5. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

The project uses the dependencies listed in `requirements.txt`.

---

# 6. Required Data

The application requires an image for testing.

Use:

- Public flood or emergency images that you are allowed to use, or
- Synthetic test images

Do not use private or sensitive personal data.

---

# 7. Run the Final Solution

From the project folder, run:

```bash
streamlit run app.py
```

The terminal should display a URL similar to:

```text
Local URL: http://localhost:8501
```

Open this URL in a browser.

Upload a test image and run the FloodTrace AI workflow.

---

# 8. Run the Baseline

The baseline performs direct person detection on the uploaded image.

The baseline output includes:

- People count
- Detection confidence
- Annotated image

Run the application using:

```bash
streamlit run app.py
```

Record the direct detection results before considering the additional verification and priority stages.

---

# 9. Evaluation

To evaluate the final system:

1. Use the same test image for comparison.
2. Record the baseline detection result.
3. Run the Detection Agent.
4. Run the Verification Agent.
5. Run the Priority Agent.
6. Compare the baseline output with the final multi-agent output.

The final system provides additional verification and structured rescue prioritization beyond direct detection.

---

# 10. Expected Output

The system should display:

- Uploaded image
- Detection result
- Possible people count
- Detection confidence
- Verification result
- Rescue priority
- Annotated image
- Mission history
- Final rescue recommendation

The final recommendation is reviewed by authorized human personnel before any real-world action.

---

# 11. Versions

Recommended environment:

- Python: 3.10 or later
- Streamlit: version specified in `requirements.txt`
- Ultralytics: version specified in `requirements.txt`
- OpenCV: version specified in `requirements.txt`

---

# 12. Approximate Runtime and Cost

Runtime depends on the computer hardware and image size.

Typical execution may take a few seconds after the model has loaded.

The first execution may take longer because the YOLO model may need to download.

## Cost

The core project runs locally and does not require a paid API key.

Approximate cost: no direct API cost for the core workflow.

Internet and local computing costs may vary depending on the user's environment.