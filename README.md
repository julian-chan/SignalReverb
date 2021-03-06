# SignalReverb

Disclaimer: I started this project because I wanted to see what my favorite songs would sound like in various different concert halls, venues, stadiums, etc. This is purely an exploratory project and is by no means comprehensive.

## Dependencies
This was written with Python and tested with Python 3.6.

Dependencies:
* [soundfile](https://pypi.org/project/SoundFile/)

## Usage
To run the script, run:

`python reverb.py input_path imp_resp_path output_path`

Arguments:
* input_path: file path to input .wav sound file
* imp_resp_path: file path to impulse response .wav sound file
* output_path: file path to output .wav sound file

## Background
Indoor music venues can be thought of as Linear and Time Invariant (LTI) systems. LTI systems have 2 defining properties:
* Linearity: There is a linear mapping between the input and output
![](images/linearity.JPG)
* Time Invariance: Delaying an input by T delays the output by T
![](images/time_invariance.JPG)

The key advantage in being able to work with an LTI system is that it is characterized entirely by its impulse response. That is, the output of the system y(t) is the convolution (\*) of the input x(t) with the system's impulse response h(t)
![](images/convolution.JPG)

However, convolutions can get expensive as the lengths of the signal and impulse responses grow, requiring ![](images/conv_runtime.JPG) multiplication/addition operations. We can invoke the Convolution Theorem and make use of the fact that convolution in the time domain is multiplication (element-wise) in the frequency domain (and vice versa). So, our strategy is to compute the Fast Fourier Transform (FFT) in ![](images/fft_runtime.JPG) operations, do the element-wise multiplication in ![](images/mult_runtime.JPG) operations, and then compute the Inverse Fast Fourier Transform (IFFT) in ![](images/fft_runtime.JPG) operations.

Thus, by acquiring an impulse response (could be a balloon pop, gunshot sound, etc.) to determine the acoustic qualities of the venue, we can simulate how our favorite songs would sound in that venue!
