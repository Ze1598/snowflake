--Select DB and Schema to run below

CREATE NETWORK RULE pypi_connection_rule
  TYPE = 'HOST_PORT'
  MODE = 'EGRESS'
  VALUE_LIST = ('pypi.org');

CREATE EXTERNAL ACCESS INTEGRATION pypi_access_integration
  ALLOWED_NETWORK_RULES = (pypi_connection_rule)
  ENABLED = true;
