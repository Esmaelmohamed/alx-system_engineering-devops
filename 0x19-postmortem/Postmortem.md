# Incident Report: 504 Error / Site Outage

## Summary
On September 11th, 2018, at midnight, the server experienced an outage resulting in a 504 error for users trying to access the website. The server is based on a LAMP stack.

## Timeline
- **00:00 PST:** Users encountered a 500 error when accessing the website.
- **00:05 PST:** Verification of Apache and MySQL status showed they were operational.
- **00:10 PST:** The website still wasn't loading correctly, although the server and database were functioning.
- **00:12 PST:** A quick restart of the Apache server returned a status 200 (OK) upon curling the website.
- **00:18 PST:** Initiated a review of error logs to identify the source of the error.
- **00:25 PST:** Found that Apache was being prematurely shut down. No PHP error logs were found in the expected location.
- **00:30 PST:** Checked `php.ini` settings and discovered error logging was disabled. Enabled error logging.
- **00:32 PST:** Restarted Apache server and checked the PHP error logs.
- **00:36 PST:** PHP error logs indicated a mistyped file name, causing improper loading and premature shutdown of Apache.
- **00:38 PST:** Corrected the file name and restarted the Apache server.
- **00:40 PST:** Server and website were operating normally.

## Root Cause and Resolution
The root cause was a typo in the `wp-settings.php` file, where a file extension was incorrectly written as `.phpp`. This led to a 500 error when accessing the server. Initial checks did not reveal much due to disabled PHP error logging. Upon enabling the logging in `php.ini` and restarting Apache, the logs showed the precise issue.

The solution involved:
1. Enabling PHP error logging.
2. Restarting Apache to capture the error in logs.
3. Identifying and fixing the typo in `wp-settings.php`.
4. Using Puppet to deploy the corrected file name across all servers.
5. Restarting servers to ensure the site loaded correctly.

## Corrective and Preventive Measures
- Ensure error logging is always enabled on all servers to facilitate quick troubleshooting.
- Conduct thorough testing of all server configurations and website functionality locally before deploying to a multi-server environment to minimize downtime and fix issues proactively.

