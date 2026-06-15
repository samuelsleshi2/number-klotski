# Number Klotski Detection

Live object detection of a number Klotski/16-puzzle board from a webcam. 
A fine-tuned [RF-DETR](https://github.com/roboflow/rf-detr) model reads
each frame, draws boxes and labels for the board, the empty slot, and tiles 1–15,
and sends the annotated frames to a virtual camera device you can use in Zoom, OBS, etc.

## Demo
<img width="1920" height="1080" alt="Screenshot 2026-06-15 12-21-54" src="https://github.com/user-attachments/assets/cffcf5d9-2423-4b42-b036-abd565e52bb5" />

## Classes

`1`–`15`, `Empty`, and `Board`. 17 total labels.

## Requirements

- Python 3.10+
- A webcam (the script will read device index `1`. If needed, change the index in `main.py`)
- A virtual camera backend for `pyvirtualcam`:
  - **Windows/macOS:** install [OBS Studio](https://obsproject.com/), then
    clone [Unity Capture](https://github.com/schellingb/UnityCapture)
    and follow the instructions in that repo to set up your virtual camera device.
- A GPU is recommended. `rfdetr` uses `torch`. Install a CUDA build if you
  want faster speed or else it runs on CPU very slowly, around <10 FPS.

## Setup

```bash
python -m venv klotski-detection-venv

klotski-detection-venv\Scripts\activate # Windows
source klotski-detection-venv/bin/activate # macOS/Linux

pip install -r requirements.txt
```

## Getting the model weights

The trained weights aren't in the repo due to the checkpoint file with the
weights being about 127 MB. Instead, Download it from the 
[weights release](../../releases/tag/weights-v1) and drop it into
that path below.

```
content/output/checkpoint_best_total.pth
```

If you'd rather train your own, the dataset was annotated and exported from
Roboflow and the model was trained with RF-DETR Small for 50 epochs. See
[the config release](../../releases/tag/training-config-v1) for
the full configuration.

## Run

```bash
python main.py
```

The console prints the virtual camera device it's sending to. Select that device
as your camera source in your app of choice to see the live annotated feed.
