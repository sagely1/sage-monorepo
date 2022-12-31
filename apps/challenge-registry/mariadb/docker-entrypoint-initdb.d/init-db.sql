create database challenge;
create role challenge_role_admin;
grant all on challenge.* to challenge_role_admin;

-- maria
grant challenge_role_admin to maria;
set default role challenge_role_admin for maria;

-- Create the user for challenge-core-service
create user challenge_core_service identified by 'changeme';
grant challenge_role_admin to challenge_core_service;
set default role challenge_role_admin for challenge_core_service;

-- Create the user for challenge-user-service
create user challenge_user_service identified by 'changeme';
grant challenge_role_admin to challenge_user_service;
set default role challenge_role_admin for challenge_user_service;

-- Create the user for challenge-registry-organization-service
create user challenge_organization_service identified by 'changeme';
grant challenge_role_admin to challenge_organization_service;
set default role challenge_role_admin for challenge_organization_service;

-- Create the user for challenge-service
create user challenge_service identified by 'changeme';
grant challenge_role_admin to challenge_service;
set default role challenge_role_admin for challenge_service;