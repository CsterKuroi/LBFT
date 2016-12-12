from mpi4py import MPI

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

group = comm.Get_group()
group1 = group.Incl([0,4,5])
group2 = group.Incl([1,4,5])
group3 = group.Incl([2,4,5])
group4 = group.Incl([3,4,5])
#group5 = group.Incl([4,6])
#group6 = group.Incl([5,6])
#group7 = group.Incl([6,4,5])
#group8 = group.Incl([4,0,1,2,3])
#group9 = group.Incl([5,0,1,2,3])

comm_size = comm.Get_size()
comm1 = comm.Create(group1)
comm2 = comm.Create(group2)
comm3 = comm.Create(group3)
comm4 = comm.Create(group4)
#comm5 = comm.Create(group5)
#comm6 = comm.Create(group6)
#comm7 = comm.Create(group7)
#comm8 = comm.Create(group8)
#comm9 = comm.Create(group9)


if comm1 !=MPI.COMM_NULL:
#    print(comm_rank,comm1.Get_rank())
    if comm1.Get_rank() == 0:
        data= [1,1,1]
        comm1.bcast(data,root=0)
    else:
        data=comm1.bcast(None,root=0)
        print('rank %d (group1_rank %d)receive'%(comm_rank,comm1.Get_rank()),data)
        comm.send(data,dest=6)

if comm2 !=MPI.COMM_NULL:
#    print(comm_rank,comm1.Get_rank())
    if comm2.Get_rank() == 0:
        data= [2,2,2]
        comm2.bcast(data,root=0)
    else:
        data=comm2.bcast(None,root=0)
        print('rank %d (group2_rank %d)receive'%(comm_rank,comm1.Get_rank()),data)
        comm.send(data,dest=6)

if comm3 !=MPI.COMM_NULL:
#    print(comm_rank,comm1.Get_rank())
    if comm3.Get_rank() == 0:
        data= []
        comm3.bcast(data,root=0)
    else:
        data=comm3.bcast(None,root=0)
        print('rank %d (group3_rank %d)receive'%(comm_rank,comm1.Get_rank()),data)
        comm.send(data,dest=6)

if comm4 !=MPI.COMM_NULL:
#    print(comm_rank,comm1.Get_rank())
    if comm4.Get_rank() == 0:
        data= {"key","good"}
        comm4.bcast(data,root=0)
    else:
        data=comm4.bcast(None,root=0)
        print('rank %d (group4_rank %d)receive'%(comm_rank,comm1.Get_rank()),data)
        comm.send(data,dest=6)


if comm_rank == 6:
    data=comm.recv(source=4)
    print ('receive from rank4:',data)
    data=comm.recv(source=5)
    print ('receive from rank5:',data)

    data=comm.recv(source=4)
    print ('receive from rank4:',data)
    data=comm.recv(source=5)
    print ('receive from rank5:',data) 

    data=comm.recv(source=4)
    print ('receive from rank4:',data)
    data=comm.recv(source=5)
    print ('receive from rank5:',data)

    data=comm.recv(source=4)
    print ('receive from rank4:',data)
    data=comm.recv(source=5)
    print ('receive from rank5:',data)
