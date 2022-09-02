# Motion Features:

### For each hour of the day, a set of 35 feature are computed to summarise the type of motion that occured during that hour
### Acceleration data, A<sub>x</sub>, A<sub>y</sub> and A<sub>z</sub> along with gyroscope data, G<sub>x</sub>, G<sub>y</sub> and G<sub>z</sub>, are recorded from the phone. A Kalman filter is used to calculate orientation angles $\theta$ and $\phi$ by measuring orientation from the gyroscope and utilizing the accelerometer to minimize any drift error that the gyroscope creates. The overall magnitude of the acceleration is calculated as A<sub>m</sub>=A<sup>2</sup><sub>x</sub>+A<sup>2</sup><sub>y</sub>+A<sup>2</sup><sub>z</sub> and the overall magnitude of the angular velocity is calculated as G<sub>m</sub>=G<sup>2</sup><sub>x</sub>+G<sup>2</sup><sub>y</sub>+G<sup>2</sup><sub>z</sub>

* f1:
* f2:
* f3:
* f4:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
* f1:
##### For hour h, there will be periods of inactivity where no motion is detected. The next 4 features are statistical summaries of the periods of inactivity
* f30: Variance of the durations of all periods of inactivity
* f31: Mean of the durations of all periods of inactivity
* f32: Inter Quartile Range (IQR) of the durations of all periods of inactivity
* f33: Variance/IQR ratio