from aws_cdk import (
    Duration,
    RemovalPolicy,
    aws_backup as backup,
    aws_events as events,
)

from constructs import Construct

class Backup_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, instances: list, test: bool, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create backup vault
        self.backup_vault = backup.BackupVault(
            self, 'Backup-Vault',
            backup_vault_name='Backup-Vault',
            # access_policy=,
            )

        # Create backup plan
        self.backup_plan = backup.BackupPlan(
            self, 'Backup-Plan',
            backup_vault=self.backup_vault
            )

        # auto remove if project is in test state 
        if test:
            self.backup_vault.apply_removal_policy(RemovalPolicy.DESTROY)
            self.backup_plan.apply_removal_policy(RemovalPolicy.DESTROY)

        # Add instances to the backup plan resources
        for instance in instances:
            self.backup_plan.add_selection(
                'Instances',
                resources=[backup.BackupResource.from_ec2_instance(instance)],
                allow_restores=True,
            )
        
        # Add backup rules
        self.backup_plan.add_rule(backup.BackupPlanRule(
            enable_continuous_backup=True,
            delete_after=Duration.days(7),
            schedule_expression=events.Schedule.cron(
                hour="5",
                minute="0",
                ))
            )
