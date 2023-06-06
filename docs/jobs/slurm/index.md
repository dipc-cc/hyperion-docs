# SLURM

Slurm is an open source, fault-tolerant, and highly scalable cluster management and job batch system for large and small Linux clusters.

Batch jobs are typically submitted using a batch script which is a text file containing a number of job directives and GNU/linux commands or utilities. Batch scripts are submitted to the SLURM, where they are queued awaiting free resources. 

```
#!/bin/bash                                                          
#SBATCH --partition=test
#SBATCH --job-name=test_job
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:10:00
#SBATCH --mem=1Gb

echo "Hello DIPC!"
```

This batch script example can be read line by line as follows:

- `#SBATCH --partition=test`: send job to the test partition.
- `#SBATCH --job-name=test_job`: give a name to the job.
- `#SBATCH --cpus-per-task=1`: number of cpus/threads per task/process.
- `#SBATCH --nodes=1`: make a reservation of 1 node.
- `#SBATCH --ntasks-per-node=1`: number of tasks/processes per node.
- `#SBATCH --time=00:10:00`: requested walltime in DD-HH:MM:SS format.
- `#SBATCH --mem=1GB`: requested memory per node in GB.
- `echo "Hello DIPC!"`: actual piece of code we want to run.

!!! Tip

    If you do not know the amount of resources in terms of memory or time your jobs are going to need, you should overestimate this values in the first runs and tweak those values up as you learn how jobs behave. 

          
Once our batch script is prepared you can submit it as a batch job to the queue system.

!!! Tip

    If you do not redirect the output of your runs to a specific file, then the standard output will be redirected to a file that goes by the name `slurm-<job_id>.log`.


