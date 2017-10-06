
class Wavemanager():
    def __init__(self, frequency = 2500):
        self.folder = "../res/waves/"
        self.current = 0  # Current wave#.txt-file
        self.max = 3     # max amount of wave#.txt-files (must not exceed wave#.txt-files in folder "waves")
        self.frequency = frequency # spawn-tick-frequency 
        
        # current wave
        self.wavetime = 0
        self.wavetick = 0
        self.duration = 0
        self.queue = []
    
    def nextWave(self):
        self.wavetick = 0
        if self.current < self.max:
            self.current += 1
        elif self.current == self.max:
            self.current = 1
        file = open(self.folder+"wave"+str(self.current)+".txt")
        for line in file:
            content = line.strip().split(" ")
            if len(content) > 1:
                self.readLine(content)
        if len(self.queue) < self.duration:
            for i in range(self.duration-len(self.queue)):
                self.queue.append("hold")
        print("Queue loaded: ")
        print(self.queue)
            
    def readLine(self,content):
        order = content[0]
        amount = int(content[1])
        if order == "duration":
            self.duration = amount
        elif order == "delay":
            for i in range(amount):
                self.queue.append("hold")
        else:
            for i in range(amount):
                self.queue.append(order)

    def update(self,dt):
        if self.current == 0 or self.wavetick >= self.duration:
            self.nextWave()
            
        self.wavetime += dt
        if self.wavetime > 1000 and len(self.queue)>0:
            self.wavetime = 0
            self.wavetick += 1
            order = self.queue[0]
            del self.queue[0]
            if order != "Hold":
                print("Spawned: "+order)
                print(self.queue)
                print(str(self.duration)+" "+str(self.wavetick))
            return order
            
      
    