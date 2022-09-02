# Motion Features:

### For each hour of the day, a set of 35 feature are computed to summaries the type of motion that occurred during that hour

##### Raw Motion signals are transformed into orientation independent signals to account for smartphones being positioned in different manners on peoples body:

Acceleration data, A<sub>x</sub>, A<sub>y</sub> and A<sub>z</sub> along with gyroscope data, G<sub>x</sub>, G<sub>y</sub> and G<sub>z</sub>, are recorded from the phone. A Kalman filter is used to calculate orientation angles $\theta$ and $\phi$ by measuring orientation from the gyroscope and utilizing the accelerometer to minimize any drift error that the gyroscope creates. The overall magnitude of the acceleration is calculated as $A_m=\sqrt{A^2_x+A^2_y+A^2_z}$ and the overall magnitude of the angular velocity is calculated as $G_m=\sqrt{G^2_x+G^2_y+G^2_z}$

Unconstrained sensor orientation results in the loss of useful information such as movement in a particular direction. In order to solve this problem, a measure of motion, independent of sensor orientation, is required. This is performed by computing a global reference frame in order to measure acceleration with respect to gravity as opposed to a local reference frame which measures acceleration with respect to the sensor device. A rotation matrix $R_\theta\phi$ is computed from the orientation quaternion and the global acceleration frame is defined as $\overline{A}=A \times R_\theta\phi$ where $A=\{A_x,A_y,A_z\}$. The acceleration vector $\overline{A}$ now represents acceleration relative to gravity. The vertical component of the acceleration $A^v$ can now be defined as $A^v = \overline{A}_y$. Yaw information is not utilized is this work due to the presence of noise in he yaw signal caused by ferromagnetic interference. We therefore have no representation of which direction the phone is pointing on the horizontal plane and therefore cannot disambiguate the remaining signals, $\overline{A}_x$ and $\overline{A}_z$, into dorsoventral and mediolateral (forward and sideward) directions. We must therefore combine these signals into a single horizontal acceleration component $A^h = \sqrt{\overline{A}^2_x + \overline{A}^2_z}$.

Rotational velocity relative to gravity is also computed using $\overline{G}=G \times R_\theta\phi$ where $G=\{G_x,G_y,G_z\}$. Vertical and Horizontal rotational velocity is then computed using $G^v = \overline{G}_y$ and $G^h = \sqrt{\overline{G}^2_x + \overline{G}^2_z}$ respectively.

#### For each hour, statistical summary features are computed from the raw signals $A_m$, $G_m$, $A^v$, $G^v$, $A^h$ and $G^h$ to compute 24 features f1 - f24: 

* f1: Mean of $A_m$
* f2: Variance of $A_m$
* f3: Kurtosis of $A_m$
* f4: Skewness of $A_m$
* f5: Min of $A_m$
* f6: Max of $A_m$
* f7: Mean of $G_m$
* f8: Variance of $G_m$
* f9: Mean of $A^h$ 
* f10: Variance of $A^h$
* f11: Mean of $A^v$ 
* f12: Variance of $A^v$
* f13: Mean of $G^h$ 
* f14: Variance of $G^h$
* f15: Mean of $G^v$ 
* f16: Variance of $G^v$
* f17: Correlation between $A^v$ and $A_m$
* f18: Correlation between $A^v$ and $A^h$
* f19: Inter Quartile Range $A_m$
* f20: Inter Quartile Range $G^v$
* f21: Inter Quartile Range $G^h$
* f22: Largest Rate of change from all zero crossings in  $A^v$
* f23: Mean orientation rate of change ($\theta$ and $\phi$)
* f24: Duration in seconds that device was moving during the 1 hour window

* f25: FFT frequency 1 computed from $A^v$
* f26: FFT frequency 2 computed from $A^v$
* f27: FFT frequency 3 computed from $A^v$
* f28: FFT frequency 4 computed from $A^v$
* f29: FFT frequency 5 computed from $A^v$

##### For hour h, there will be periods of inactivity where no motion is detected. The next 4 features are statistical summaries of the periods of inactivity
* f30: Variance of the durations of all periods of inactivity
* f31: Mean of the durations of all periods of inactivity
* f32: Inter Quartile Range (IQR) of the durations of all periods of inactivity
* f33: Variance/IQR ratio
* f34: NOT USED
* f35: NOT USED