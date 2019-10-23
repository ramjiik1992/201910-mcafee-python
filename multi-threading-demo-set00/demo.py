import threading as t;

class CountDown(t.Thread):
    def __init__(self,id,max):
        super().__init__()
        self._id=id
        self._max=max

    def run(self):
        id=self._id
        max=self._max
        print(f'thread#{id} starts')    
        while max>=0:
            print(f'thread#{id} counts {max}')
            max-=1

        print(f'thread#{id} ends')

def main():
    t1=CountDown(1,50)
    t2=CountDown(2,30)
    
    t1.start()
    t2.start()

    print('program ends')
    

main()