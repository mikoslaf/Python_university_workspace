
from dataclasses import dataclass

@dataclass(frozen=True)
class Job:
    id: int
    cpu: float
    mem_gb: float
    priority: int = 10 # higher is better

@dataclass
class Server:
    id: int
    free_cpu: int
    free_mem_gb: int

def schedule_jobs_on_server(server: Server, jobs: list[Job]) -> list[Job]:
    """
    Starting with the jobs of highest priority.... try to fit (schedule) them on server. 
    If possible -- subtract their requirements from server, and schedule next jobs. 
    If not possible -- skip the job, and try other, with lower priority. 
    Return scheduled jobs in order in which they were scheduled. 
    
    :param server: 
    :param jobs: 
    :return: 
    """

    jobs.sort(key=lambda job: job.priority, reverse=True)
    local_server = Server(id=server.id, free_cpu=server.free_cpu, free_mem_gb=server.free_mem_gb)
    result = []
    for job in jobs:
        if can_fit_on_server(local_server, job):
            local_server.free_cpu -= job.cpu
            local_server.free_mem_gb -= job.mem_gb
            result.append(job)
    return  result

        

def can_fit_on_server(s: Server, job: Job) -> bool:
    return job.cpu <= s.free_cpu and job.mem_gb <= s.free_mem_gb

if __name__ == '__main__':
    j1 = Job(1, cpu=4, mem_gb=2.5, priority=10)
    j2 = Job(2, cpu=2, mem_gb=5, priority=50)
    j3 = Job(3, cpu=6, mem_gb=10, priority=99)
    j4 = Job(4, cpu=2, mem_gb=2, priority=100)

    s1 = Server(1, free_cpu=12, free_mem_gb=9)

    #print(can_fit_on_server(s1, j1))
    #print(can_fit_on_server(s1, j2))

    print(schedule_jobs_on_server(server=s1, jobs=[j4, j1, j3, j2]))

    print(s1.free_cpu)