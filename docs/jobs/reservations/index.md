# Reservations

Users can request a scheduled reservation of machine resources if their jobs have special needs that cannot be accommodated through the regular batch system. A reservation brings some portion of the machine to a specific user or project for an agreed upon duration. Typically this is used for interactive debugging at scale or real time processing linked to some experiment or event.

!!! failure "Note"
    It is not intended to be used to guarantee fast throughput for production runs.

## Fairshare

For normal batch jobs, fairshare modification is done on a per job basis. For scheduled reservations the entire block of reserved time is charged regardless of the number of nodes used or time spent running jobs.

## Requesting a reservation

To reserve compute nodes, please ask for the least amount of resources you need and try to schedule reservations so as to minimize impact on other users. 

## Viewing reservations

To view all reservations run 'scontrol show reservations', the output will consist of one entry per reservation name. Take a close look at the reservation fields such as `StartTime`, `EndTime`, `Duration`, `Nodes`, `Users`, `Accounts` to understand what the reservation.

## Using a reservation

Once your reservation request is approved and a reservation is placed on the system, to run jobs in the reservation, you can use the --reservation option on the submision script:

```
sbatch --reservation=<reservation_name>
```
