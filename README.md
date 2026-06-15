# Number Klotski Detection

Real-time detection of a 15-puzzle (number Klotski / 16-puzzle) board from a
webcam. A fine-tuned [RF-DETR](https://github.com/roboflow/rf-detr) model reads
each frame, draws boxes and labels for the board, the empty slot, and tiles 1–15,
and pushes the annotated frame to a virtual camera you can use in Zoom, OBS, etc.

## Demo

<!-- TODO: replace with your own clip or screenshot.
     - GIF or screenshot: ![demo](docs/demo.gif)
     - MP4: drag the file into a GitHub release/issue and paste the URL GitHub gives you. -->

![demo](docs/demo.gif)

## Classes

`1`–`15`, `Empty`, and `Board` — 17 labels in all.

## Requirements

- Python 3.10+
- A webcam (the code reads device index `1`; change it in `main.py` if needed)
- A virtual camera backend for `pyvirtualcam`:
  - **Windows/macOS:** install [OBS Studio](https://obsproject.com/) once so its
    virtual camera is registered
  - **Linux:** `v4l2loopback`
- A GPU is recommended. `rfdetr` pulls in `torch`; install a CUDA build if you
  want real-time speed, otherwise it runs on CPU but slowly.

## Setup

```bash
python -m venv klotski-detection-venv
# Windows
klotski-detection-venv\Scripts\activate
# macOS/Linux
source klotski-detection-venv/bin/activate

pip install -r requirements.txt
```

## Getting the model weights

The trained weights aren't in the repo (the checkpoint is ~127 MB). Download
`checkpoint_best_total.pth` and place it here:

```
content/output/checkpoint_best_total.pth
```

Download it from the [latest release](../../releases) and drop it into
that path.

If you'd rather train your own, the dataset was annotated and exported from
Roboflow and the model was trained with RF-DETR Small for 50 epochs. See the
[training configuration](../../releases) for the full configuration.

## Run

```bash
python main.py
```

The console prints the virtual camera device it's sending to. Select that device
as your camera source in any app to see the live annotated feed.
