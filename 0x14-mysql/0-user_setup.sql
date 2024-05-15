-- Create the replication user if it does not already exist
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'password';

-- Assign replication and select privileges to the user
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON *.* TO 'replica_user'@'%';

-- Refresh the privilege table to ensure changes take effect
FLUSH PRIVILEGES;

-- Verify the user and its privileges
SELECT user, host, Repl_slave_priv, Select_priv 
FROM mysql.user 
WHERE user = 'replica_user';

