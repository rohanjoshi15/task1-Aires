# Task 1 - Aires
 ---

 ### Light Dose

 ---

 ### 1 to 10. Linux Commands
 - Learnt from youtube "https://www.youtube.com/@NetworkChuck"
 - Screenshots uploaded

### Bash Scripting 
- It had to do battery check and Ping google to check connectivity and maintain a record
- syntax taken from google
- other than syntax - basic if else code logic implementation needed

---

### Medium Dose

--- 

## 1. Arrow Detection & Rover Center Calculation
- Find the offset value and add it to the Y-axis to negate the error.

---

## 2. Morse Code Decoder
- Create a dictionary mapping each letter, number, and symbol to Morse code.
- Break each message into parts, convert it using the dictionary, and then reassemble it to retrieve the English message.

---

## 3. Letter Pattern Shifter
- Extract the pattern and use a `for` loop to avoid repetitive or lengthy code.
- Logic used to reverse the shift in message characters:
  ```python
  original_char = chr(ord(char) - (i + 1))

## 4. Sanchiko and Muchiko Filter

- Helps remove noise and improve data accuracy.

### MK Filter (Moving Average Filter)
- Computes the average of a sliding window (`grp_size`).
- Replaces each value with the mean of its neighboring values.
- **Effect:** Smooths rapid variations but may lose sharp transitions.

### SK Filter (Median Filter)
- Takes a sliding window (`grp_size`) of values.
- Sorts the values and selects the middle one (median).
- **Effect:** Removes spikes (outliers) while preserving edges.

---

## 5. Change of Rotation (3D to 4D)

### Euler Angles
- Euler angles represent 3D rotation using three values:
  - **Roll**: Rotation about the X-axis
  - **Pitch**: Rotation about the Y-axis
  - **Yaw**: Rotation about the Z-axis

### Quaternions
- Provide stable 3D rotations without gimbal lock.
- Represented as: `Q = (w, x, y, z)`
  - `w`: Scalar part
  - `x, y, z`: Vector part

- **Convert degrees to radians**:
    - radians = degrees × π / 180
- Convert the Eulers angles to Quarternions by using the following python code / formulae
  ```python
  import math
  
  def euler_to_quaternion(roll, pitch, yaw):
      cy = math.cos(yaw * 0.5)
      sy = math.sin(yaw * 0.5)
      cp = math.cos(pitch * 0.5)
      sp = math.sin(pitch * 0.5)
      cr = math.cos(roll * 0.5)
      sr = math.sin(roll * 0.5)
  
      w = cr * cp * cy + sr * sp * sy
      x = sr * cp * cy - cr * sp * sy
      y = cr * sp * cy + sr * cp * sy
      z = cr * cp * sy - sr * sp * cy
  
      return w, x, y, z

---

# Hard Dose

---

## 1. Arena Generation and Pathfinding

- Took user input for the arena which is stored in a `.txt` file.
- Arena is represented as an `n × n` matrix where:
- `1` = Safe position
- `0` = Obstacle

- Used BFS (Breadth-First Search) to find the shortest path from source to goal.

- Arena initially set to all `1`s, then read from the `.txt` file and updated based on user directions.

### Obstacle Placement:
- Directions and updates:
- **North = 2** → `arena[2][0] = 0`
- **East  = 3** → `arena[0][3] = 0`
- **South = 4** → `arena[4][n-1] = 0`
- **West  = 5** → `arena[n-1][5] = 0`

- Faced difficulties completing the code due to out-of-bounds `n` value while generating the arena.

---

## 2. Arrow Distance Estimation via Image Processing

- Load and process the image.
- Convert to grayscale.
- Apply Gaussian blur to reduce noise.
- Use Canny edge detection to detect edges.
- Approximate detected shapes using polygons.
- If the shape has 5 to 8 edges, it is considered an arrow.
- Measure the bounding box width of the arrow in pixels.
- Estimate the real-world distance using the **pinhole camera model**.

### Constants:
   - ```python
     REAL_ARROW_WIDTH = 17.0  # cm
     IMAGE_WIDTH = 1280       # pixels
     DIAGONAL_FOV = 55        # degrees
     HORIZONTAL_FOV = 47      # degrees

### Distance : Distance = (Real Object Width X Focal Length) / Perceived Width in Image


### Behaviour Tree
 - Learned from the 5-minute video provided in the Task 1 PDF.
 - Designed the tree using Canva.
