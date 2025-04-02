#include <iostream>
#include <cmath>

using namespace std;

// convert degrees to radians
double toRadians(double degrees) {
    return degrees * 3.14 / 180.0;
}

// convert Euler angles to Quaternions
void eulerToQuaternion(double roll, double pitch, double yaw, double &w, double &x, double &y, double &z) {
    
    roll = toRadians(roll);
    pitch = toRadians(pitch);
    yaw = toRadians(yaw);

    // Compute quaternion values
    double cy = cos(yaw * 0.5);
    double sy = sin(yaw * 0.5);
    double cp = cos(pitch * 0.5);
    double sp = sin(pitch * 0.5);
    double cr = cos(roll * 0.5);
    double sr = sin(roll * 0.5);

    w = cr * cp * cy + sr * sp * sy;
    x = sr * cp * cy - cr * sp * sy;
    y = cr * sp * cy + sr * cp * sy;
    z = cr * cp * sy - sr * sp * cy;
}

int main() {
    double roll, pitch, yaw;
    
    
    cout << "Enter Roll, Pitch, Yaw (in degrees): ";
    cin >> roll >> pitch >> yaw;

    double w, x, y, z;
    
   
    eulerToQuaternion(roll, pitch, yaw, w, x, y, z);

    
    cout << "Quaternion: (" << w << ", " << x << ", " << y << ", " << z << ")" << endl;

    return 0;
}

