import time
import threadpool  
def sayhello(str):
    print("Hello ",str)
    time.sleep(1)

name_list =['xiaozi','aa','bb','cc']
start_time = time.time()
pool = threadpool.ThreadPool(100) 
requests = threadpool.makeRequests(sayhello, name_list) 
[pool.putRequest(req) for req in requests] 
pool.wait() 
print('%d second'% (time.time()-start_time))