#run() -> loops through all algorithms in priorityQueue, and repeats this until interrupted
#interrupt() -> moves the pointer for the next algorithm in priorityQueue, allowing user to select next algorithm to run

import time
from init import generate_spectrum
import LED_controller

# import algorithms:
from algorithms import bubble_sort
from algorithms import insertion_sort
from algorithms import merge_sort
from algorithms import selection_sort
from algorithms import heap_sort
from algorithms import quick_sort
from algorithms import counting_sort
from algorithms import bucket_sort
from algorithms import radix_sort
from algorithms import cocktail_sort
from algorithms import tim_sort
from algorithms import binary_sort
from algorithms import shell_sort

class Main:
    def __init__(self):
        self.stripSize = 146
        self.defaultBrightness = 1

        #list to store all algorithms, will loop through this list to execute algorithms
        #allows changing of order of execution
        self.priorityQueue = ["bubble", "insertion", "merge", "selection",
                              "heap", "quick", "counting", "bucket", "radix",
                              "cocktail", "tim", "binary", "shell"]

        #get LED object from controller
        self.LED = LED_controller.LED(self.stripSize)
        #self.LED = None

        #counter for current algorithm being executed
        self.currAlg = 10

        #audio-output object
        self.AUDIO = None

        #temp variables to store
        self.swapSD = 0.0 # JUST USING RAW TIME AT THE MOMENT, WILL EXPERIMENT WITH LOOPING LATER
        self.compareSD = 0.0
        self.recursionSD = 0.0


    #def run(self, LED, audioBuff):
    def run(self, audioBuff):
        #self.LED = LED

        #generate spectrup of RGB colours
        generate_spectrum.initialize(self.LED,self.stripSize,self.defaultBrightness)

        #self.currAlg = 2
        #loop indefinitely
        while True:

            #refresh individual slowdowns:
            self.LED.swapSD = self.swapSD
            self.LED.compareSD = self.swapSD
            self.LED.recursionSD = self.recursionSD
 
            #randomize strip state
            self.LED.shake()
            #update physical strip
            self.LED.update()
            time.sleep(0.5)

            # loop around to start when necessary
            if self.currAlg >= len(self.priorityQueue):
                #reset curr
                self.currAlg = 0

            # execute relevant algorithm:
            if self.priorityQueue[self.currAlg] == "bubble":
                #execute bubble sort
                print("bubble sort")
                bubble_sort.sort(self.LED, audioBuff)
            elif self.priorityQueue[self.currAlg] == "insertion":
                #execute insertion sort
                print("insertion sort")
                insertion_sort.sort(self.LED, audioBuff)
            elif self.priorityQueue[self.currAlg] == "merge":
                #execute merge sort
                print("merge sort")
                merge_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "selection":
                #execute selection sort
                print("selection sort")
                selection_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "heap":
                #execute merge sort
                print("heap sort")
                heap_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "quick":
                #execute quick sort
                print("quick sort")
                quick_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "counting":
                #execute counting sort
                print("counting sort")
                generate_spectrum.initializeHalfSpectrum(self.LED,self.stripSize,self.defaultBrightness) # convert strip to random rg dist
                counting_sort.sort(self.LED)
                generate_spectrum.initialize(self.LED,self.stripSize,self.defaultBrightness) # return strip to standard rgb dist
            elif self.priorityQueue[self.currAlg] == "bucket":
                #execute bucket sort
                print("bucket sort")
                bucket_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "radix":
                #execute radix sort
                print("radix sort")
                radix_sort.sort(self.LED)
            elif self.priorityQueue[self.currAlg] == "cocktail":
                #execute cocktail shaker sort
                print("cocktail shaker sort")
                cocktail_sort.sort(self.LED, audioBuff)
            elif self.priorityQueue[self.currAlg] == "tim":
                # execute tim sort
                print("tim sort")
                tim_sort.sort(self.LED, audioBuff)
            elif self.priorityQueue[self.currAlg] == "binary":
                # execute binary sort
                print("binary sort")
                binary_sort.sort(self.LED, audioBuff)
            elif self.priorityQueue[self.currAlg] == "shell":
                # execute shell sort
                print("shell sort")
                shell_sort.sort(self.LED, audioBuff)

            #algorithm done so clear strip
            self.LED.clear()

            self.currAlg += 1
        
        self.LED.clear()

    def interrupt(self, interrupt_val):
        name = interrupt_val[0] # interrupt val contains, both the name of interupt alg, and the volume it was spoken at
        vol = interrupt_val[1]

        # need to do something with volume (use it to change the size of the array)

        try:
            #queue the spoken algorithm next
            self.currAlg = self.priorityQueue.index(name) - 1
            print("queuing: " + name + " sort")
        except:
            # could be slow or fast mode
            if name == "fast":
                print("entering fast mode!")
                self.LED.slowMode = False
            elif name == "slow":
                print("entering slow mode!")
                self.LED.slowMode = True
            else:
                print("Error, cannot find: " + name + " sort algorithm")

    #temporary (just for testing) will integrate with main interrupt method at a later date
    def interrupt2(self, interrupt_val):
        if interrupt_val == "slower":
            print("slowing")
            self.swapSD += 0.002
            self.compareSD += 0.002
            self.recursionSD += 0.002
        elif self.swapSD != 0:
            print("speeding-up")
            self.swapSD -= 0.002
            self.compareSD -= 0.002
            self.recursionSD -= 0.002
        

