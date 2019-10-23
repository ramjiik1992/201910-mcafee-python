import threading as t;

def count_down():
    name=t.current_thread().name
    print(f'{name} starts')    
    max=20
    while max>=0:
        print(f'{name} counts {max}')
        max-=1

    print(f'{name} ends')

def main():
    t1=t.Thread(target=count_down)
    t2=t.Thread(target=count_down)
    
    t1.start()
    t2.start()

    print('program ends')
    

main()