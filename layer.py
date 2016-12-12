from mpi4py import MPI

print("hello world")  
print("my rank is: %d" %MPI.COMM_WORLD.Get_rank())  
