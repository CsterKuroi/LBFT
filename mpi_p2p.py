import mpi4py.MPI as MPI  
   
comm = MPI.COMM_WORLD  
comm_rank = comm.Get_rank()  
comm_size = comm.Get_size()  
   
# point to point communication  
data_send = [comm_rank]*5  
comm.send(data_send,dest=(comm_rank+1)%comm_size)  
data_recv =comm.recv(source=(comm_rank-1)%comm_size)  
print("my rank is %d, and Ireceived:" % comm_rank)  
print (data_recv)  
