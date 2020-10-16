# oasis_camera_acquisition
OraVu camera uses `DirectShow`

### Dependency
- numpy
- matplotlib
- opencv-python
- comtypes

### Usage
1. Make sure Python packages are installed
2. Run main.py
3. Select a video device provide your choices

### DirectShow Introduction
`DirectShow` is a framework to write multimedia applications. The building block of a `DirectShow` is a filter

`DirectShow` provides an object called `FilterGraph` that is responsible to collect the filters

For this demo application, we have the following filters:
- A camera source filter, that reads the images from the camera.
- A `SampleGrabber` filter that allows us to do some operation on each frame provided by the camera
- A video render filter that displays the live streams of the camera on the GUI

#### Using the Class FilterGraph
`FilterGrpah` contained in the file `dshow_graph.py` as standalone. The class represent a `DirectShow` Filter Graph object


### License
```
Released under The MIT License (MIT)
Copyright 2020 Haopeng Tian
```
