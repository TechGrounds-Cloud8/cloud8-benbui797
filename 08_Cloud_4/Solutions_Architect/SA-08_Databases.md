# Databases

# RDS
RDS runs on EC2 instances, you specify the instance when you launch RDS. By selecting a more powerful instance, you can vertically scale your database.

## Backups & Maintenance
**Automated Backups**
- You can select a backup window (e.g. every hour or every day)
- A snapshot is taken which is stored for 35 days
- You can do a point-in-time recovery for any snapshot taken within the retention period.
  
**Manual Backups**
- Backs up the entire DB instance, not just the individual database
- For single-AZ DB instances, there is a suspension of I/O operations
- For Multi-AZ SQL server; I/O is briefly suspensed on primary db
- For Multi-AZ MariaDB, MySQL, Oracle and PostgreSQL the snapshot is taken from the standby
- Snapshots do not expire (no retention period)
  
**Maintenance Windows**
- OS and Database patching can require taking the database online
- These tasks take place during a maintenance window
- By default a weekly maintenance window is configured
- You can select your own maintenance window