import numpy as np
import soundfile as sf
from scipy import signal
import sys
import argparse

def read_input(wavfile):
    """
    Reads in the wavfile as a numpy array and cleans and normalizes the signal.
    Returns the normalized signal and the sampling frequency.

    Args:
        wavfile: file path to .wav file

    Returns:
        signal: numpy array of the wavfile sampled at fs
        fs: sampling frequency
    """
    signal, fs = sf.read(wavfile)
    signal = signal.astype(np.float64)    # Cleaning
    signal = signal / np.abs(np.max(signal))    # Normalization

    return signal, fs

def fft_convolve(x, h):
    """
    Convolves the signal x with an impulse response h. Returns the convolved signal trimmed to the same length as the input.

    Args:
        x: input signal
        h: impulse response

    Returns:
        input signal convolved with the impulse response, trimmed to be the same length as the input signal
    """
    result = signal.fftconvolve(x, h, mode='full')

    # Find where the impulse response is strongest; this is the "start" of the impulse response
    # Accounts for impulse responses with a long pause before the actual response
    p_max = np.argmax(np.abs(h))

    # Compensate for impulse response delay by shifting the convolved signal
    output = np.empty_like(result)
    shift = -p_max
    if shift >= 0:
        output[:shift] = 0.0
        output[shift:] = result[:shift]
    else:
        output[shift:] = 0.0
        output[:shift] = result[-shift:]

    # Trim the convolved signal to be the same length as the original
    return output[0: x.shape[0]]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulates song in a venue described by its impulse response.')
    parser.add_argument('input', type=str, help='file path to input .wav sound file')
    parser.add_argument('imp_resp', type=str, help='file path to impulse response .wav sound file')
    parser.add_argument('output', type=str, help='file path to output .wav sound file')
    args = parser.parse_args()

    input_file = args.input
    ir_file = args.imp_resp
    output_file = args.output

    print("Reading song from {}...".format(input_file))
    sys.stdout.flush()
    sgnl, fs = read_input(input_file)
    print("Reading impulse response from {}...".format(ir_file))
    sys.stdout.flush()
    ir, fs_ir = read_input(ir_file)

    print("Generating reverberated signal...")
    sys.stdout.flush()
    signal_rev = fft_convolve(sgnl, ir)

    print("Writing song to {}...".format(output_file))
    sys.stdout.flush()
    sf.write(output_file, signal_rev, fs)
    print("Done!")
