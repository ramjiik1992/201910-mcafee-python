import threading as t;

def thread_info():
    print(f'current thread is {t.current_thread().name}')

def main():
    t1=t.Thread(target=thread_info)  #create a new thread to run thread_info
    t1.start()  #start the thread (execute thread_info)

    thread_info() #running thread_info on the main thread

    #thread_info() is called twice. on main thread and other thread
    

main()