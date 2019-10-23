import threading as t;

def count_down(id,max):
    name=t.current_thread().name
    print(f'thread#{id} starts')    
    #max=20
    while max>=0:
        print(f'thread#{id} counts {max}')
        max-=1

    print(f'thread#{id} ends')

def main():
    t1=t.Thread(target=count_down,args=(1,50))
    t2=t.Thread(target=count_down,args=(2,30))
    
    t1.start()
    t2.start()

    print('program ends')
    

main()