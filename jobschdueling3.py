# Get number of jobs
n = int(input("Enter number of jobs: "))

jobs = []
profit = []
deadline = []

# Input job details
print("Enter job details (JobID Profit Deadline):")
for i in range(n):
    jobId, p, d = input().split()
    jobs.append(jobId)
    profit.append(int(p))
    deadline.append(int(d))

# Combine and sort by profit descending
profitNJobs = list(zip(profit, jobs, deadline))
profitNJobs = sorted(profitNJobs, key=lambda x: x[0], reverse=True)

# Initialize slots
max_deadline = max(deadline)
slot = [0] * (max_deadline + 1)
ans = ['null'] * (max_deadline + 1)
total_profit = 0

# Schedule jobs
for i in range(n):
    job = profitNJobs[i]
    for j in range(job[2], 0, -1):
        if slot[j] == 0:
            ans[j] = job[1]
            total_profit += job[0]
            slot[j] = 1
            break

# Output results
print("Jobs scheduled buddy:", [job for job in ans[1:] if job != 'null'])
print("Total Profit:", total_profit)


output :

tanishka@tanishka-Latitude-5490:~$ python3 job3.py
Enter number of jobs: 5
Enter job details (JobID Profit Deadline):
j1 15 2
j2 27 3
j3 10 3
j4 100 3
j5 150 4
Jobs scheduled buddy: ['j1', 'j2', 'j4', 'j5']
Total Profit: 292
tanishka@tanishka-Latitude-5490:~$ 
