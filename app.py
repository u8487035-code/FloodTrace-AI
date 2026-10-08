
import streamlit as st
import numpy as np
import pandas as pd
import os
from PIL import Image
from datetime import datetime

from detection_agent import detect_people
from verification_agent import verify_detection
from priority_agent import calculate_priority


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="FloodTrace AI",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# FILE SETTINGS
# ==================================================

HISTORY_FILE = "mission_history.csv"


# ==================================================
# LOAD MISSION HISTORY
# ==================================================

def load_mission_history():

    if os.path.exists(HISTORY_FILE):

        try:

            history_df = pd.read_csv(HISTORY_FILE)

            return history_df.to_dict(
                orient="records"
            )

        except Exception:

            return []

    return []


# ==================================================
# SAVE MISSION HISTORY
# ==================================================

def save_mission_history():

    try:

        history_df = pd.DataFrame(
            st.session_state.mission_history
        )

        history_df.to_csv(
            HISTORY_FILE,
            index=False
        )

    except Exception as e:

        st.error(
            f"Unable to save mission history: {e}"
        )


# ==================================================
# GENERATE NEXT MISSION ID
# ==================================================

def generate_mission_id(history):

    highest_number = 0

    for mission in history:

        mission_id = str(
            mission.get("Mission ID", "")
        )

        if mission_id.startswith("FT-"):

            try:

                number_part = mission_id.replace(
                    "FT-",
                    ""
                )

                number = int(number_part)

                if number > highest_number:

                    highest_number = number

            except ValueError:

                continue

    return f"FT-{highest_number + 1:03d}"


# ==================================================
# INITIALIZE SESSION STATE
# ==================================================

if "mission_history" not in st.session_state:

    st.session_state.mission_history = (
        load_mission_history()
    )


if "current_mission_id" not in st.session_state:

    st.session_state.current_mission_id = (
        generate_mission_id(
            st.session_state.mission_history
        )
    )


if "save_message" not in st.session_state:

    st.session_state.save_message = ""


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🌊 FloodTrace AI")

    st.caption(
        "AI-Assisted Flood Search and Rescue System"
    )

    st.divider()

    st.subheader("📋 Mission Details")

    location = st.text_input(
        "📍 Rescue Location",
        placeholder="Enter flood location",
        key="location_input"
    )


    # AUTOMATIC MISSION ID

    mission_id = (
        st.session_state.current_mission_id
    )

    st.text_input(
        "🆔 Mission ID",
        value=mission_id,
        disabled=True
    )

    st.divider()

    st.subheader("🤖 System Information")

    st.write("⚙️ Multi-Agent AI System")

    st.write("👥 Person Detection")

    st.write("🔍 Detection Verification")

    st.write("🚨 Rescue Prioritization")

    st.divider()

    st.caption(
        "⚠️ AI results are decision-support "
        "information and should always be reviewed "
        "by authorized rescue personnel."
    )


# ==================================================
# MAIN HEADER
# ==================================================

st.title("🌊 FloodTrace AI")

st.subheader(
    "AI-Assisted Flood Search, Detection & Rescue Prioritization"
)

st.caption(
    "Multi-Agent AI System for supporting emergency response teams"
)

st.divider()


# ==================================================
# SYSTEM STATUS
# ==================================================

status_col1, status_col2, status_col3, status_col4 = (
    st.columns(4)
)

with status_col1:

    st.metric(
        "🆔 Current Mission",
        mission_id
    )

with status_col2:

    st.metric(
        "📍 Location",
        location if location else "Not Provided"
    )

with status_col3:

    st.metric(
        "🤖 Detection Agent",
        "ACTIVE"
    )

with status_col4:

    st.metric(
        "🔍 Verification Agent",
        "ACTIVE"
    )


st.divider()


# ==================================================
# FILE UPLOAD
# ==================================================

uploaded_file = st.file_uploader(
    "📤 Upload Flood Image",
    type=["jpg", "jpeg", "png"]
)


# ==================================================
# IMAGE ANALYSIS
# ==================================================

if uploaded_file is not None:

    timestamp = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )


    # ----------------------------------------------
    # LOAD IMAGE
    # ----------------------------------------------

    try:

        image = Image.open(
            uploaded_file
        ).convert("RGB")

        image_array = np.array(image)

    except Exception as e:

        st.error(
            f"❌ Unable to read image: {e}"
        )

        st.stop()


    st.success("✅ Image uploaded successfully!")

    st.caption(
        f"🕒 Analysis Time: {timestamp}"
    )


    # ==================================================
    # RUN AI AGENTS
    # ==================================================

    try:

        # ----------------------------------------------
        # DETECTION AGENT
        # ----------------------------------------------

        detection_result = detect_people(
            image_array
        )


        # ----------------------------------------------
        # VERIFICATION AGENT
        # ----------------------------------------------

        verification_result = verify_detection(
            detection_result
        )


        # ----------------------------------------------
        # PRIORITY AGENT
        # ----------------------------------------------

        priority_result = calculate_priority(
            detection_result,
            verification_result
        )


    except Exception as e:

        st.error(
            f"❌ AI Analysis Error: {e}"
        )

        st.stop()


    # ==================================================
    # EXTRACT RESULTS SAFELY
    # ==================================================

    people_count = int(
        detection_result.get(
            "people_count",
            0
        )
    )

    confidence = float(
        detection_result.get(
            "confidence",
            0
        )
    )

    verification_status = (
        verification_result.get(
            "status",
            "Unknown"
        )
    )

    verified = bool(
        verification_result.get(
            "verified",
            False
        )
    )

    verification_confidence = float(
        verification_result.get(
            "confidence",
            0
        )
    )

    priority = (
        priority_result.get(
            "priority",
            "LOW"
        )
    )

    message = (
        priority_result.get(
            "message",
            "No decision available"
        )
    )


    # ==================================================
    # IMAGE RESULTS
    # ==================================================

    st.divider()

    st.header("🔍 AI Detection Result")

    image_col1, image_col2 = st.columns(2)


    with image_col1:

        st.subheader("📷 Original Image")

        st.image(
            image,
            use_container_width=True
        )


    with image_col2:

        st.subheader("🎯 AI Detected Image")

        annotated_image = detection_result.get(
            "annotated_image",
            image_array
        )

        st.image(
            annotated_image,
            use_container_width=True
        )


    # ==================================================
    # MULTI-AGENT ANALYSIS
    # ==================================================

    st.divider()

    st.header("🤖 Multi-Agent Analysis")

    agent_col1, agent_col2, agent_col3 = (
        st.columns(3)
    )


    # ----------------------------------------------
    # DETECTION AGENT
    # ----------------------------------------------

    with agent_col1:

        st.subheader("🔎 Detection Agent")

        st.metric(
            "People Detected",
            people_count
        )

        st.metric(
            "Highest Confidence",
            f"{confidence * 100:.0f}%"
        )

        st.info(
            detection_result.get(
                "result",
                "No result available"
            )
        )


    # ----------------------------------------------
    # VERIFICATION AGENT
    # ----------------------------------------------

    with agent_col2:

        st.subheader(
            "🔍 Verification Agent"
        )

        st.write(
            f"**Status:** {verification_status}"
        )

        st.write(
            f"**Confidence:** "
            f"{verification_confidence * 100:.0f}%"
        )

        if verified:

            st.success(
                "✅ Detection Verified"
            )

        else:

            st.warning(
                "⚠️ Human Review Recommended"
            )


    # ----------------------------------------------
    # PRIORITY AGENT
    # ----------------------------------------------

    with agent_col3:

        st.subheader(
            "🚨 Priority Agent"
        )

        st.metric(
            "Rescue Priority",
            priority
        )

        st.write(message)


    # ==================================================
    # FINAL RESCUE DECISION
    # ==================================================

    st.divider()

    st.header("🚨 Final Rescue Decision")


    if priority == "HIGH":

        st.error(
            "🚨 HIGH PRIORITY RESCUE REQUIRED"
        )

        st.write(message)


    elif priority == "MEDIUM":

        st.warning(
            "⚠️ MEDIUM PRIORITY - HUMAN REVIEW REQUIRED"
        )

        st.write(message)


    else:

        st.success(
            "✅ LOW PRIORITY - CONTINUE MONITORING"
        )

        st.write(message)


    # ==================================================
    # MISSION SUMMARY
    # ==================================================

    st.divider()

    st.header("📊 Mission Summary")

    summary_col1, summary_col2, summary_col3, summary_col4 = (
        st.columns(4)
    )


    with summary_col1:

        st.metric(
            "🆔 Mission ID",
            mission_id
        )


    with summary_col2:

        st.metric(
            "📍 Location",
            location if location else "Not Provided"
        )


    with summary_col3:

        st.metric(
            "👥 People Detected",
            people_count
        )


    with summary_col4:

        st.metric(
            "🚨 Priority",
            priority
        )


    # ==================================================
    # MISSION RECORD
    # ==================================================

    mission_record = {

        "Mission ID": mission_id,

        "Location": (
            location
            if location
            else "Not Provided"
        ),

        "People Detected": people_count,

        "Detection Confidence (%)": round(
            confidence * 100,
            1
        ),

        "Verification Status": verification_status,

        "Verified": verified,

        "Verification Confidence (%)": round(
            verification_confidence * 100,
            1
        ),

        "Priority": priority,

        "Analysis Time": timestamp
    }


    # ==================================================
    # SAVE MISSION
    # ==================================================

    st.divider()

    st.header("💾 Save Mission")

    if st.button(
        "💾 Save This Mission Permanently",
        use_container_width=True,
        type="primary"
    ):

        # Remove duplicate Mission ID

        st.session_state.mission_history = [

            mission

            for mission in
            st.session_state.mission_history

            if str(
                mission.get("Mission ID")
            ) != str(mission_id)

        ]


        # Add mission

        st.session_state.mission_history.append(
            mission_record
        )


        # Save CSV

        save_mission_history()


        # Success message

        st.session_state.save_message = (
            f"✅ Mission {mission_id} "
            f"saved permanently!"
        )


        # Generate NEXT mission ID

        st.session_state.current_mission_id = (
            generate_mission_id(
                st.session_state.mission_history
            )
        )


        st.success(
            f"✅ Mission {mission_id} saved permanently!"
        )


    # ==================================================
    # VISUAL ANALYTICS DASHBOARD
    # ==================================================

    st.divider()

    st.header("📊 Visual Analytics Dashboard")

    analytics_col1, analytics_col2, analytics_col3 = (
        st.columns(3)
    )


    # ----------------------------------------------
    # PEOPLE DETECTION
    # ----------------------------------------------

    with analytics_col1:

        st.subheader(
            "👥 People Detection"
        )

        st.metric(
            "Detected People",
            people_count
        )

        people_progress = min(
            people_count / 30,
            1.0
        )

        st.progress(
            people_progress
        )

        st.caption(
            f"{people_count} people identified "
            "in the image"
        )


    # ----------------------------------------------
    # DETECTION CONFIDENCE
    # ----------------------------------------------

    with analytics_col2:

        st.subheader(
            "🎯 Detection Confidence"
        )

        confidence_percent = int(
            confidence * 100
        )

        st.metric(
            "AI Confidence",
            f"{confidence_percent}%"
        )

        st.progress(
            min(
                confidence,
                1.0
            )
        )


    # ----------------------------------------------
    # VERIFICATION CONFIDENCE
    # ----------------------------------------------

    with analytics_col3:

        st.subheader(
            "🔍 Verification"
        )

        verification_percent = int(
            verification_confidence * 100
        )

        st.metric(
            "Verification Confidence",
            f"{verification_percent}%"
        )

        st.progress(
            min(
                verification_confidence,
                1.0
            )
        )


    # ==================================================
    # EMERGENCY PRIORITY STATUS
    # ==================================================

    st.divider()

    st.header(
        "🚦 Emergency Priority Status"
    )


    if priority == "HIGH":

        st.error(
            "🔴 HIGH PRIORITY — "
            "Immediate rescue assessment recommended"
        )


    elif priority == "MEDIUM":

        st.warning(
            "🟡 MEDIUM PRIORITY — "
            "Human review recommended"
        )


    else:

        st.success(
            "🟢 LOW PRIORITY — "
            "Continue monitoring"
        )


    # ==================================================
    # RESCUE REPORT
    # ==================================================

    st.divider()

    st.header("📄 Rescue Report")


    report = f"""
==================================================
        FLOODTRACE AI - RESCUE ANALYSIS REPORT
==================================================

MISSION INFORMATION
--------------------------------------------------

Mission ID: {mission_id}

Location: {location if location else "Not Provided"}

Analysis Time: {timestamp}


DETECTION AGENT
--------------------------------------------------

People Detected: {people_count}

Highest Confidence: {confidence * 100:.0f}%

Result: {detection_result.get("result", "Unknown")}


VERIFICATION AGENT
--------------------------------------------------

Status: {verification_status}

Verified: {verified}

Verification Confidence:
{verification_confidence * 100:.0f}%


PRIORITY AGENT
--------------------------------------------------

Rescue Priority: {priority}

Decision:
{message}


SYSTEM NOTICE
--------------------------------------------------

AI analysis is intended to assist rescue teams.

Final rescue decisions should always be confirmed
by authorized human personnel.

==================================================
"""


    st.text_area(
        "Generated Rescue Report",
        value=report,
        height=450
    )


    st.download_button(
        label="⬇️ Download Rescue Report",

        data=report,

        file_name=(
            f"{mission_id}_Rescue_Report.txt"
        ),

        mime="text/plain",

        use_container_width=True
    )


# ==================================================
# NO IMAGE
# ==================================================

else:

    st.info(
        "👆 Upload a flood image to begin "
        "AI analysis."
    )


# ==================================================
# MISSION HISTORY
# ==================================================

st.divider()

st.header("📋 Mission History")


if len(
    st.session_state.mission_history
) > 0:

    history_df = pd.DataFrame(
        st.session_state.mission_history
    )


    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )


    # ----------------------------------------------
    # DOWNLOAD HISTORY
    # ----------------------------------------------

    csv_data = history_df.to_csv(
        index=False
    )


    st.download_button(
        label="⬇️ Download Mission History CSV",

        data=csv_data,

        file_name=(
            "FloodTrace_Mission_History.csv"
        ),

        mime="text/csv",

        use_container_width=True
    )


    # ----------------------------------------------
    # CLEAR HISTORY
    # ----------------------------------------------

    if st.button(
        "🗑️ Clear Mission History Permanently",
        use_container_width=True
    ):

        # Clear memory

        st.session_state.mission_history = []


        # Delete CSV

        if os.path.exists(HISTORY_FILE):

            try:

                os.remove(
                    HISTORY_FILE
                )

            except Exception as e:

                st.error(
                    f"Unable to delete history: {e}"
                )


        # Reset Mission ID

        st.session_state.current_mission_id = (
            "FT-001"
        )


        st.success(
            "🗑️ Mission History cleared!"
        )

        st.rerun()


else:

    st.info(
        "📭 No missions saved yet. "
        "Analyze an image and click "
        "'Save This Mission Permanently'."
    )