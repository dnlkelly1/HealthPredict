# Motion Features:

### For each hour of the day, a set of 35 feature are computed to summaries the type of motion that occurred during that hour

##### Raw Motion signals are transformed into orientation independent signals to account for smartphones being positioned in different manners on peoples body:

Acceleration data, A<sub>x</sub>, A<sub>y</sub> and A<sub>z</sub> along with gyroscope data, G<sub>x</sub>, G<sub>y</sub> and G<sub>z</sub>, are recorded from the phone. A Kalman filter is used to calculate orientation angles $\theta$ and $\phi$ by measuring orientation from the gyroscope and utilizing the accelerometer to minimize any drift error that the gyroscope creates. The overall magnitude of the acceleration is calculated as $A_m=\sqrt{A^2_x+A^2_y+A^2_z}$ and the overall magnitude of the angular velocity is calculated as $G_m=\sqrt{G^2_x+G^2_y+G^2_z}$

Unconstrained sensor orientation results in the loss of useful information such as movement in a particular direction. In order to solve this problem, a measure of motion, independent of sensor orientation, is required. This is performed by computing a global reference frame in order to measure acceleration with respect to gravity as opposed to a local reference frame which measures acceleration with respect to the sensor device. A rotation matrix $R_\theta\phi$ is computed from the orientation quaternion and the global acceleration frame is defined as $\overline{A}=A \times R_\theta\phi$ where $A=\{A_x,A_y,A_z\}$. The acceleration vector $\overline{A}$ now represents acceleration relative to gravity. The vertical component of the acceleration $A^v$ can now be defined as $A^v = \overline{A}_y$. Yaw information is not utilized is this work due to the presence of noise in he yaw signal caused by ferromagnetic interference. We therefore have no representation of which direction the phone is pointing on the horizontal plane and therefore cannot disambiguate the remaining signals, $\overline{A}_x$ and $\overline{A}_z$, into dorsoventral and mediolateral (forward and sideward) directions. We must therefore combine these signals into a single horizontal acceleration component $A^h = \sqrt{\overline{A}^2_x + \overline{A}^2_z}$.

Rotational velocity relative to gravity is also computed using $\overline{G}=G \times R_\theta\phi$ where $G=\{G_x,G_y,G_z\}$. Vertical and Horizontal rotational velocity is then computed using $G^v = \overline{G}_y$ and $G^h = \sqrt{\overline{G}^2_x + \overline{G}^2_z}$ respectively.

#### For each hour, statistical summary features are computed from the raw signals $A_m$, $G_m$, $A^v$, $G^v$, $A^h$ and $G^h$ to compute 24 features f2 - f28: 

* f1: Percentage of day completed (e.g. 11am = (11/24) 0.458)

##### During a given hour, features f2-f27 are calculated during periods when the phone is not stationary. If the phone was stationary for the entire hour, f2-f29 will be NAN
* f2: Mean of $A_m$
* f3: Variance of $A_m$
* f4: Kurtosis of $A_m$
* f5: Skewness of $A_m$
* f6: Min of $A_m$
* f7: Max of $A_m$
* f8: Mean of $G_m$
* f9: Variance of $G_m$
* f10: Mean of $A^h$ 
* f11: Variance of $A^h$
* f12: Mean of $A^v$ 
* f13: Variance of $A^v$
* f14: Mean of $G^h$ 
* f15: Variance of $G^h$
* f16: Mean of $G^v$ 
* f17: Variance of $G^v$
* f18: Correlation between $A^v$ and $A_m$
* f19: Correlation between $A^v$ and $A^h$
* f20: Inter Quartile Range $A_m$
* f21: Inter Quartile Range $G^v$
* f22: Inter Quartile Range $G^h$
* f23: Largest Rate of change from all zero crossings in  $A^v$
* f24: Mean orientation rate of change ($\theta$ and $\phi$)
* f25: Duration in seconds that device was moving during the 1 hour window

* f26: FFT frequency 1 computed from $A^v$
* f27: FFT frequency 2 computed from $A^v$
* f28: FFT frequency 3 computed from $A^v$

##### For hour h, there will be periods of inactivity where no motion is detected. The next 4 features are statistical summaries of the periods of inactivity
##### During a given hour, features f29-f33 are calculated on the durations of peiods of inactivity

* f29: Percentage of time the phone was in a "moving" state (duration phone was not stationary). 1 = phone active for full hour, 0 = phone stationary for full hour
* f30: Variance of the durations of all periods of inactivity
* f31: Mean of the durations of all periods of inactivity (for an hour where no movement occured, and the sensor was ON for the entire hour, this value will be 3600 seconds)
* f32: Inter Quartile Range (IQR) of the durations of all periods of inactivity
* f33: Variance/IQR ratio

* f34: NOT USED
* f35: NOT USED