
not_used_operations = {
    'ec2': [
        'describe_load_balancer_policies',
        'describe_vpc_endpoint_services',
        'describe_aggregate_id_format',
        'describe_load_balancer_policy_types',
        'describe_endpoints',
        'describe_availability_zones',
        'describe_account_attributes',
        'describe_dhcp_options',
        'describe_fpga_images',
        'describe_host_reservation_offerings',
        'describe_id_format',
        'describe_instance_event_notification_attributes',
        'describe_instance_type_offerings',
        'describe_instance_types',
        'describe_managed_prefix_lists',
        'describe_prefix_lists',
        'describe_regions',
        'describe_launch_template_versions',
        'describe_principal_id_format',
        'describe_spot_price_history',
        'describe_flow_logs',
        ### The blow 2 require extra parameters.
        'describe_images',
        'describe_snapshots',
    ],
    'ecr': [
        'get_authorization_token',
    ],
    'ecs': [
        'describe_capacity_providers',
    ],
    'efs': [
        'describe_account_preferences',
    ],
    'acm': [
        'get_account_configuration',
    ],
    'athena': [
        'list_data_catalogs',
    ],
    'apigateway': [
        'get_account',
        'get_sdk_types',
    ],
    'xray': [
        'get_encryption_config',
        'get_sample_rules',
    ],
    'waf': [
        'get_change_token',
    ],
    'waf-regional': [
        'get_change_token',
    ],
    'sts': [
        'get_caller_identity',
        'get_session_token',
    ],
    'ssm': [
        'describe_available_patches',
        'describe_patch_baselines',
        'get_inventory_schema',
    ],
    'ses': [
        'get_account_sending_enabled',
        'get_send_quota',
    ],
    'sesv2': [
        'get_account',
        'get_deliverability_dashboard_options',
    ],
    'signer': [
        'list_signing_platforms',
    ],
    'shield': [
        'describe_attack_statistics',
        'get_subscription_state',
    ],
    'lex-models': [
        'get_builtin_intents',
        'get_builtin_slot_types',
    ],
    'dynamodb': [
        'describe_limits',
    ],
    'lightsail': [
        'get_blueprints',
        'get_container_service_powers',
        'get_container_api_metadata',
        'get_bundles',
        'get_relational_database_blueprints',
        'get_relational_database_bundles',
        'get_regions',
        'get_bucket_bundles',
    ],
    'inspector': [
        'describe_cross_account_access_role',
        'list_rules_packages',
    ],
    'lambda': [
        'get_account_settings',
    ],
    'kinesis': [
        'describe_limits',
    ],
    'kafka': [
        'list_kafka_versions',
        'get_compatible_kafka_versions',
    ],
    'iot': [
        'describe_account_audit_configuration',
        'describe_event_configurations',
        'get_indexing_configuration',
        'get_registration_code',
        'list_domain_configurations'
    ],
    'iotsitewise': [
        'describe_logging_options',
        'describe_storage_configuration'
    ],
    'guardduty': [
        'get_invitations_count',
    ],
    'gamelift': [
        'describe_ec2_instance_limits',
    ],
    'elb': [
        'describe_account_limits',
        'describe_load_balancer_policies',
    ],
    'elbv2': [
        'describe_account_limits',
        'describe_ssl_policies',
    ],
    'elasticache': [
        'describe_cache_parameter_groups',
        'describe_service_updates',
        'list_allowed_node_type_modifications',
        'describe_cache_security_groups',
        'describe_users',
    ],
    'elasticbeanstalk': [
        'describe_account_attributes',
        'list_available_solution_stacks'
    ],
    'clouddirectory': [
        'list_managed_schema_arns',
    ],
    'codebuild': [
        'list_builds',
        'list_curated_environment_images'
    ],
    'cloudtrail': [
        'list_public_keys',
        'get_event_selectors',
    ],
    'cloudwatch': [
        'describe_alarm_history',
        'list_metrics',
    ],
    'snowball': [
        'get_snowball_usage',
        'list_compatible_images'
    ],
    'sms': [
        'get_servers'
    ],
    'sagemaker': [
        'get_sagemaker_servicecatalog_portfolio_status',
    ],
    'transfer': [
        'list_security_policies'
    ],
    'schemas': [
        'list_registries',
    ],
    'securityhub': [
        'describe_standards',
    ],
    'secretsmanager': [
        'get_random_password',
    ],
    'service-quotes': [
        'list_services',
    ],
    'wellarchitected': [
        'list_lenses',
    ],
    'route53': [
        'get_checker_ip_ranges',
        'get_geo_location',
        'get_traffic_policy_instance_count',
        'get_hosted_zone_count',
        'get_health_check_count',
        'list_geo_locations',
    ],
    'resourcegroupstaggingapi': [
        'get_resources',
        'get_tag_keys',
    ],
    'events': [
        'describe_event_bus',
        'list_event_buses',
    ],
    'fis': [
        'list_actions',
    ],
    'frauddetector': [
        'get_kms_encryption_key',
    ],
    'glacier': [
        'get_data_retrieval_policy',
    ],
    'glue': [
        'get_catalog_import_status',
    ],
    'apprunner': [
        'list_auto_scaling_configurations',
    ],
    'rds': [
        'describe_account_attributes',
        'describe_certificates',
        'describe_source_regions',
    ],
    'ram': [
        'list_permissions',
    ],
    'redshift': [
        'describe_account_attributes',
        'describe_cluster_tracks',
        'describe_orderable_cluster_options',
        'describe_storage',
    ],
    'polly': [
        'describe_voices',
    ],
    'opsworks': [
        'describe_my_user_profile',
        'describe_operating_systems',
        'describe_user_profiles',
    ],
    'opsworkscm': [
        'describe_account_attributes',
    ],
    'emr': [
        'get_block_public_access_configuration',
        'list_release_labels',
    ],
    'elastictranscoder': [
        'list_presets',
    ],
    'dms': [
        'describe_account_attributes',
        'describe_applicable_individual_assessments',
        'describe_orderable_replication_instances',
    ],
    'docdb': [
        'describe_certificates',
        'describe_db_subnet_groups',
    ],
    'ds': [
        'get_directory_limits',
    ],
    'compute-optimizer': [
        'get_enrollment_status',
    ],
    'config': [
        'get_compliance_summary_by_config_rule',
        'get_compliance_summary_by_resource_type',
        'get_discovered_resource_counts',
    ],
    'dax': [
        'describe_parameter_groups'
    ],
    'codedeploy': [
        'list_deployment_configs',
    ],
    'backup': [
        'list_backup_plan_templates',
    ],
    'autoscaling': [
        'describe_account_limits',
    ],
    'auditmanger': [
        'get_account_status',
    ],
    'cloudformation': [
        'describe_account_limits',
    ],
    'nimble': [
        'list_eulas',
    ],
    'cloudfront': [
        'list_cache_polocies',
    ]
}
