
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import ultralytics
except ImportError:
    install("ultralytics")
try:
    import roboflow
except ImportError:
    install("roboflow")



import roboflow
from roboflow import Roboflow
rf = Roboflow(api_key="isLsTzINU55umtJ2JAS9")
project = rf.workspace("volobuevs-workspace").project("transportdetection")
version = project.version(9)
dataset = version.download("yolov11")

'''
import ultralytics
from ultralytics.utils.benchmarks import benchmark
benchmark(model="yolo_transport_close.pt", data="TransportDetection-9\data.yaml", imgsz=640)

from ultralytics import YOLO
model = YOLO('yolo_transport_far.pt')
model.export(format="onnx")
model.export(format="tflite")
model.export(format="mnn")
model.export(format="ncnn")
model('TransportDetection-9/valid/images')
'''
