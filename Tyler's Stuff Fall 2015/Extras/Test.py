'''
Created on Sep 3, 2015

@author: Tyler
'''
class myclass:
    def ramFreq(self):
        
        
        t_sec = (1/((1/2 * self * 10e6)))    #Calculates time in seconds of delay
        
        print("The Latency from your ram is {0} seconds.".format(t_sec))

def main():
    frequency = int(input("Enter the Frequency of your ram: ")) #Gets Frequency
    
    myclass.ramFreq(frequency)
        
main()