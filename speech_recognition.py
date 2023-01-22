# code was inspired by the following resource, in porcupine documentation
# https://github.com/Picovoice/porcupine/issues/255#issuecomment-876974791

import os
import pyaudio
import pvporcupine
import struct

# load enviroment variables so key can be fetched
from dotenv import load_dotenv
load_dotenv()

# fetch access_key from environment variables
access_key = os.getenv('PICOVOICE_KEY')

# init listener
listener = pyaudio.PyAudio()

# init porcupine and import hotword samples
porcupine = pvporcupine.create(access_key = access_key, keyword_paths=["/home/pi/ArtOfSorting/hotword_detection/bubble_sort/bubble-sort_en_raspberry-pi_v2_1_0.ppn",
                                                                       "/home/pi/ArtOfSorting/hotword_detection/insertion_sort/insertion-sort_en_raspberry-pi_v2_1_0.ppn"])


def listen():

    # open audio stream
    stream = listener.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

    prev_amp = [0]*20   # buffer of size 20 to hold previous amplitude val's
                        # could experiment with increasing this to get more of
                        # the sound wave
                        # as it is it seems to catch at least the second word
                        # more experimentation might be needed

    output = ""

    while True:
        wave = stream.read(porcupine.frame_length)

        # convert to more managable form (byte to decimal)
        wave = struct.unpack_from("h" * porcupine.frame_length, wave)

        # generate value corresponding to what noise is detected (hotword or not, and if hotword then which hotword)
        hotword = porcupine.process(wave)
        
        # calculate amplitude of sound wave
        # amplitude is approximated as the furthest deviation from the zero line at any given point in the sound wave
        # could improve this to filter out peaks slightly with an average
        amp = abs(0 - wave[0])
        for i in range(1, len(wave)):
            if abs(0 - wave[i]) > amp:
                amp = abs(0 - wave[i])


        # if hotword is detected
        if hotword != -1:

            vol = max(prev_amp) # approximate volume as maximum value from the amplitude buffer

            # if hotword detected, then which hotword is detected?
            if hotword == 0:
                output = ["bubble", vol]
                stream.close()
                return(output)
            elif hotword == 1:
                output = ["insertion", vol]
                stream.close()
                return(output)

        # update the buffer with the new amplitude val
        prev_amp.pop(0)
        prev_amp.append(amp)


# TESTING  
#out = listen()
#print(out)
#listen()


# NEED TO GET AMPLITUDE OF WAVE AS VOLUME LEVEL, CAN USE THIS TO THRESHOLD WHEN HOTWORD DETECTION IS ACTIVE
# (REDUCING COMPUTATIONAL COST), AND ALSO AS ANOTHER MEANS OF INTERACTING WITH THE SYSTEM
# can't be used to reduce computational cost - since it's costly in and of itself