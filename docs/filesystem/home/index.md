# Home 

Your home directory is where you arrive by default when you login to the cluster or any access/login node. It is mounted on `/dipc/username`. It is not intended for permanent file storage as it has short capacity (2GB per user). Your shell refers to it as “∼” (tilde), and its absolute path is also stored in the environment variable $HOME. Your home directory is shared across all the HPC Systems at DIPC. The data stored here should be relatively small since it is meant to permanently store the most relevant information for your research. Note that various kinds of configuration files are also stored here: `.bash_profile`, `.tcshrc`, `.vimrc`, etc.

!!! Warning 
    Remenber that `/dipc` filesystem is not exported to computing nodes, thus it is recomended to submit jobs from `/scratch`. 


## Quotas

information abour /home quotas

## Backups ??
