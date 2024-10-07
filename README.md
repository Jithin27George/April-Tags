# April Tags

<p align="justify">
AprilTags are a type of fiducial marker used in computer vision applications for object detection and pose estimation. Similar to QR codes, they consist of a square black-and-white pattern designed to be robust and easily recognizable in different lighting conditions and angles. Each AprilTag contains a unique binary code, enabling individual identification.
</p>

### Key Features:

1. **Identification**: AprilTags can be identified uniquely from their encoded binary information, which makes them useful in distinguishing between multiple tags in a scene.
2. **Pose Estimation**: One of the primary uses of AprilTags is to determine the 6-DOF (Degrees of Freedom) pose of an object relative to a camera, including its position (x, y, z) and orientation (roll, pitch, yaw).
3. **Robustness**: AprilTags are designed to be detected even under challenging conditions such as partial occlusion, varied lighting, or at different angles.
4. **Low Latency Detection**: AprilTag detection algorithms are efficient and allow for real-time tracking in robotics and augmented reality (AR) applications.
   
### Applications:

1. **Robotics**: AprilTags are often used in autonomous systems to help robots identify objects, track positions, and localize themselves within an environment.
2. **Augmented Reality (AR)**: They serve as visual markers for overlaying digital content in AR applications.
3. **Drone Navigation**: AprilTags assist in navigation tasks where drones use the tags for precise location and landing.
4. **Calibration and Mapping**: In camera calibration or SLAM (Simultaneous Localization and Mapping) tasks, AprilTags are used to help estimate the position of the camera or robot within a space.

## Project Overview
<p align="justify">
This project provides code for generating these fiducial markers of the type 16h5, 25h9 and 36h11. The code is written in python and  has a tool folder containing a python file that can convert hex codes to binary lists which could be used to produce other types by appropriatly adjusting the any of the template provided (AprilTag_Generator(tag16h5)/ AprilTag_Generator(tag25h9)/ AprilTag_Generator(tag36h11)). A .txt file is provided along with AprilTag_Generator(tag36h11).py for applications involving creating a collage of 5x7 grid of april tags (type:36h11).
</p>

## SETUP

1. Clone this `AprilTag` repository to your local machine.

    ```bash
    $ cd [-->set the path to which you want the code to be downloaded to<--]
    $ git clone https://github.com/Jithin27George/April-Tags.git
    ```
2. Install required libraries to run the codes.

    ```bash
    $ pip install Pillow
    $ pip install numpy
    ```

## Future Development

- **April Tag Detector Code**
- **Camera caliberation**


## License

This project does not currently have an associated license.
