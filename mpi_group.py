from mpi4py import MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

group = comm.Get_group()
group = group.Excl([0,1,2])

new_comm = comm.Create(group)

if new_comm != MPI.COMM_NULL:
    print(comm_rank,new_comm.Get_rank())

