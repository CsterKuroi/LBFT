import mpi4py.MPI as MPI  
   
comm = MPI.COMM_WORLD  
comm_rank = comm.Get_rank()  
comm_size = comm.Get_size()  
   
if comm_rank == 0:  
   data = range(comm_size)  
data = comm.bcast(data if comm_rank == 0else None, root=0)  
print ('rank %d, got:' % (comm_rank))  
print (data)  
