import pyaudio
import struct
import audioop
import time

INITIAL_THRESHOLD = 0.010
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME) 
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
MAX_BLOCKS = 0.15/INPUT_BLOCK_TIME


class TEST(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_THRESHOLD
        self.noisycount = MAX_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )
        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
            channels = CHANNELS,
            rate = RATE,
            input = True,
            input_device_index = device_index,
            frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream


    def listen(self):
        start = -1
        while True: 
            try:
                chunk = self.stream.read(INPUT_FRAMES_PER_BLOCK)
            except IOError, e: 
                self.errorcount += 1
                print( "(%d) Error recording: %s"%(self.errorcount,e) )
                self.noisycount = 1
                return
            mx = audioop.max(chunk, 2)
            if mx > 2300:
                start = -1
                print "HIGH",mx

            elif mx < 2300: 
                print "LOW ",mx
                if start < 0:
                    start = time.time()
                elif time.time() - start >= 2:
                    break

        print("You're Done")
        self.stream.close()
        print("Stream Closed")
        return

if __name__ == "__main__":
    tt = TEST()

    for i in range(1000):
        tt.listen()
