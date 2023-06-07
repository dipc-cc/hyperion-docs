# Monitoring Jobs

## squeue

`squeue` provides information about jobs in Slurm scheduling queue, and is best used for viewing jobs and job step information for active jobs (PENDING, RUNNING, SUSPENDED). For more details on squeue refer to the [squeue manual](https://slurm.schedmd.com/squeue.html) or run `squeue --help`, man squeue.

```
squeue -u $USER
```

To view all running jobs for the current user:

```
squeue --me -t RUNNING
```

To view all pending jobs for current user:

```
squeue --me -t PENDING
```
## scancel 

Deletes your job. It takes the job identifier as a parameter.

```
scancel <jobid>
```

To cancel all the jobs for a user:

```
scancel -u <username>
```

To cancel all the running jobs for a user: 

```
scancel -t RUNNING -u <username>
```

## seff

SLURM provides a tool called `seff` to check the memory utilization and CPU efficiency for completed jobs. Note that for running and failed jobs, the efficiency numbers reported by `seff` are not reliable so please use this tool only for successfully completed jobs:

```
seff <job_id>
```

!!! tip
    It is recommended to use this command after launching some preliminary system work to see how many resources are being consumed, before launching a battery of calculations. Thus, in addition to reducing the waiting times for the reception of your work, you will help to maximize the resources of the calculation center

## sacct

`sacct` is used to report job or job step accounting information about active or completed jobs. For a complete list of sacct options please refer to the [sacct manual](https://slurm.schedmd.com/sacct.html) or run man sacct

Lists status info for a currently running job: 

```
sstat --format=JobID,Nodelist -j <jobid>
```

## Email notification

You may want to have SLURM send you email on certain events affecting your jobs. You can receive email to notify a job failure, completion, or if a job started. 

Add the following to your batch script to set the email address:

```
#SBATCH --mail-user=your@email.org
```

These are the different types of notifications:

```
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=ALL
```
