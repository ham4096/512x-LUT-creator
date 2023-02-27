# 512x-LUT-creator
Script that turns a 512 x 512 LUT (as can be produced by prod80's LUT Creator which can be obtained [here](https://github.com/prod80/prod80-ReShade-Repository).) into a 4096 x 64 LUT for use with tools such as ReShade. It is also possible to batch process multiple images at once to turn them into MultiLUTs.

The image can be of **any size** as long as the LUT is in the top left corner.

The only requirement for the script to run is **OpenCV2** which can be installed by the following command:
```
pip install opencv-python
```
