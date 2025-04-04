# task1-Aires


1] Arrow Detection & Rover Center Calculation
Find the offset value and add it to the y axis

2] Morse Code Decoder
We make a dictionary to map each letter of alphabet and other numeric values and symbols to their respective notations of morse code
then after breaking each message , converting it and then putting it back in english we get the required result

3] Letter pattern shifter :
Get the pattern and formulate it, also use for loop so that we dont have to make the code repitative / big
    {original_char = chr(ord(char) - (i + 1))} used to reverse the shift in the message characters

4] Sanchiko and Muchiko filter 
  Helps remove the nooise and improved the data accuracy
  MK Filter (Moving Average Filter)
  Computes the average of a sliding window (grp_size).
  Replaces each value with the mean of the neighboring values.
  Effect: Smoothes rapid variations but may lose sharp transitions.
  
  SK Filter (Median Filter)
  Takes a sliding window (grp_size) of values.
  Sorts the values and selects the middle one (median).
  Effect: Removes spikes (outliers) while preserving edges.



5] Change of Rotation (3D to 4D)
   What Are Euler Angles?
Euler angles represent 3D rotation using three values
Roll : Rotation about the X-axis
Pitch : Rotation about the Y-axis
Yaw : Rotation about the Z-axis

Quaternions
Provide stable 3D rotations without gimbal lock.
Q=(w,x,y,z)
where:
w : Scalar part
x, y, z : Vector part

First convert degrees to Radians : radians = degrees X pi / 180



Hard Dose :


1] Arena Generation and Path-finding : 
Took user input for the arena which will be then stored in a TXT file
The arena is represented as an n × n matrix where:
1 represents a safe position & 0 represents an obstacle
Used BFS for Pathfinding from the source to the goal in the arena , couldnt complete the code faced difficulties due to the arena not being generated due to out of bounds n value
First set all the values in the grid to 1
later reading from the previously stored txt file
2 3 4 5 : Add obstacles at positions:
North = 2 : Set arena[2][0] = 0
East = 3 : Set arena[0][3] = 0
South = 4 : Set arena[4][n-1] = 0
West = 5 : Set arena[n-1][5] = 0
and then use this new grid to find the shortest path.


2] Load and process the image and then convert the image to grayscale.
Apply Gaussian blur to reduce noise.
Use Canny edge detection to detect object edges.
Identify shapes in the image.
Approximate the shape using polygon detection.
If the detected shape has 5 to 8 edges, it is considered an arrow.
The bounding box width of the arrow is measured in pixels.
Using the pinhole camera model, the real-world distance of the arrow is estimated.

we set these constants in the code :
REAL_ARROW_WIDTH = 17.0  # cm
IMAGE_WIDTH = 1280  # pixels
DIAGONAL_FOV = 55  # degrees
HORIZONTAL_FOV = 47 

Use the distance formula for the pinhole camera (told in the pdf) : Distance =  Real Object Width X Focal Length / Perceived Width in Image  


3] Behaviour Tree :  learnt from 5min video provided in task1 pdf, done in canva.

