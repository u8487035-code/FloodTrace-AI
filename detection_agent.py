import cv2
import numpy as np
from ultralytics import YOLO


# ==========================================
# LOAD YOLO MODEL
# ==========================================

# yolov8s is more accurate than yolov8n
# It may be slightly slower.

model = YOLO("yolov8s.pt")


# ==========================================
# DETECT PEOPLE
# ==========================================

def detect_people(image):

    # --------------------------------------
    # MAKE SURE IMAGE IS NUMPY ARRAY
    # --------------------------------------

    if not isinstance(image, np.ndarray):
        image = np.array(image)


    # --------------------------------------
    # YOLO DETECTION
    # --------------------------------------

    results = model(

        image,

        # Detect only COCO class 0 = person
        classes=[0],

        # Ignore very weak detections
        conf=0.35,

        # IoU threshold for duplicate boxes
        iou=0.45,

        verbose=False
    )


    # --------------------------------------
    # INITIAL VALUES
    # --------------------------------------

    people_count = 0

    highest_confidence = 0.0

    annotated_image = image.copy()


    # --------------------------------------
    # PROCESS DETECTIONS
    # --------------------------------------

    for result in results:

        if result.boxes is None:

            continue


        for box in result.boxes:

            confidence = float(
                box.conf[0].item()
            )


            # Bounding box coordinates

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0].tolist()
            )


            # ----------------------------------
            # COUNT PERSON
            # ----------------------------------

            people_count += 1


            # ----------------------------------
            # HIGHEST CONFIDENCE
            # ----------------------------------

            if confidence > highest_confidence:

                highest_confidence = confidence


            # ----------------------------------
            # DRAW BOX
            # ----------------------------------

            cv2.rectangle(

                annotated_image,

                (x1, y1),

                (x2, y2),

                (0, 255, 0),

                3
            )


            # ----------------------------------
            # LABEL
            # ----------------------------------

            label = (
                f"Person "
                f"{confidence * 100:.0f}%"
            )


            cv2.putText(

                annotated_image,

                label,

                (x1, max(y1 - 10, 25)),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.7,

                (0, 255, 0),

                2
            )


    # ======================================
    # FINAL RESULT
    # ======================================

    if people_count == 0:

        result_text = (
            "No human presence detected"
        )

    elif people_count == 1:

        result_text = (
            "Possible human presence detected"
        )

    else:

        result_text = (
            f"{people_count} people detected"
        )


    # ======================================
    # RETURN RESULTS
    # ======================================

    return {

        "people_count": people_count,

        "confidence": round(
            highest_confidence,
            2
        ),

        "result": result_text,

        "annotated_image": annotated_image
    }
