# oasis_camera_acquisition
This is the camera acquisition 
This camera using DirectShow to capture, and this repo provide demonstration of how to 
acquire OraVu camera
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

`DirectShow` provides an object called `Filter Graph` that is responsible to collect the filters

#### Using the Class FilterGraph
`FilterGrpah` contained in the file `dshow_graph.py` as standalone. The class represent a `DirectShow` Filter Graph object


### License
The MIT License (MIT)
