from mpi4py import MPI
import tx
import vote as v

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

"""
group = comm.Get_group()
group1 = group.Incl([0,4,5])
group2 = group.Incl([1,4,5])
group3 = group.Incl([2,4,5])
group4 = group.Incl([3,4,5])
group5 = group.Incl([4,6])
group6 = group.Incl([5,6])
group7 = group.Incl([6,4,5])
group8 = group.Incl([4,0,1,2,3])
group9 = group.Incl([5,0,1,2,3])

comm1 = comm.Create(group1)
comm2 = comm.Create(group2)
comm3 = comm.Create(group3)
comm4 = comm.Create(group4)
comm5 = comm.Create(group5)
comm6 = comm.Create(group6)
comm7 = comm.Create(group7)
comm8 = comm.Create(group8)
comm9 = comm.Create(group9)
"""

if 0<=comm_rank<=3:
    start = MPI.Wtime() 
    data = tx.create()
    comm.send(data,dest=4)
    comm.send(data,dest=5)

    data=comm.recv(source=4)
    data1=data
    data=comm.recv(source=5)

    flag =True
    if data == data1:
        pass
       #print ('rank %d :Get block'%comm_rank,data)
        for ctx in data:
            if not tx.validate(ctx):
                flag = False
        myvote=v.vote(flag)       
        comm.send(myvote,dest=4)
        comm.send(myvote,dest=5)

    data=comm.recv(source=4)
    data1=data
    data=comm.recv(source=5)
    if data == data1:
        pass
        #print ('rank %d :Get votes'%comm_rank,data)
        print('rank %d:'%comm_rank,v.election(comm_size,data))
    stop = MPI.Wtime()
    print("rank %d time:%lfs\n"%(comm_rank,stop-start))

if 4<=comm_rank<=5:
    data=comm.recv(source=0)
    comm.send(data,dest=6)
    data=comm.recv(source=1)
    comm.send(data,dest=6)
    data=comm.recv(source=2)
    comm.send(data,dest=6)
    data=comm.recv(source=3)
    comm.send(data,dest=6)

    data=comm.recv(source=6)
    comm.send(data,dest=0)
    comm.send(data,dest=1)
    comm.send(data,dest=2)
    comm.send(data,dest=3)

    flag = True
    for ctx in data:
        if not tx.validate(ctx):
            flag = False
    comm.send(v.vote(flag),dest=6)

    data=comm.recv(source=0)
    comm.send(data,dest=6)
    data=comm.recv(source=1)
    comm.send(data,dest=6)
    data=comm.recv(source=2)
    comm.send(data,dest=6)
    data=comm.recv(source=3)
    comm.send(data,dest=6)

    data=comm.recv(source=6)
    comm.send(data,dest=0)
    comm.send(data,dest=1)
    comm.send(data,dest=2)
    comm.send(data,dest=3)
    print('rank %d:'%comm_rank,v.election(comm_size,data))

if comm_rank == 6:
    ids = []
    votes = []
    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        ids.append(data)

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        ids.append(data)

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        ids.append(data)

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        ids.append(data)

    #print('block:',ids)
    comm.send(ids,dest=4)
    comm.send(ids,dest=5)
    flag = True
    for ctx in ids:
        if not tx.validate(ctx):
            flag = False
    votes.append(v.vote(flag))

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    votes.append(data1)
    votes.append(data)    

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        votes.append(data)

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        votes.append(data)

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        votes.append(data)

    data1=comm.recv(source=4)
    data=comm.recv(source=5)
    if data == data1 :
        votes.append(data)

    print('votes:',votes)
    comm.send(votes,dest=4)
    comm.send(votes,dest=5)
    print('rank %d:'%comm_rank,v.election(comm_size,votes))
