- Why use Coco Format (JSON) to export dataset?
    - COCO format is supported by a lot of modern
    computer vision frameworks including RF-DETR which is used in this
    project. 
    - COCO stores everything into a JSON file (_annotations.coco.json).
    That makes it easy for Python libraries to load and process the dataset
    without parsing text files
    - COCO format has a clean folder layout that can easily be recognized
    when you pass `dataset_dir` to `model.train()`

