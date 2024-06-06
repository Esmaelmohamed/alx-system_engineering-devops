# Postmortem: 504 Error / Site Outage

## Issue Summary
On September 11th, 2018, at midnight (PST), the server experienced an outage resulting in a 504 error for users attempting to access the website. The incident lasted 40 minutes, from 00:00 PST to 00:40 PST. During this period, most user requests resulted in 500 errors, reaching 100% at the peak of the issue. The root cause was a typo in the `wp-settings.php` file.

## Timeline
- **Timezone:** PST
- **00:00:** Outage began; users encountered a 500 error.
- **00:05:** Staff verified Apache and MySQL were operational.
- **00:10:** Website was still not loading correctly; server and database checks were performed.
- **00:12:** Apache server was restarted, resulting in a status 200 upon curling the website.
- **00:18:** Error logs were reviewed to identify the issue.
- **00:25:** Found Apache server was being prematurely shut down; no PHP error logs were present.
- **00:30:** PHP error logging was enabled in `php.ini`.
- **00:32:** Apache server was restarted, and PHP error logs were reviewed.
- **00:36:** PHP error logs indicated a mistyped file name causing the issue.
- **00:38:** The typo was corrected, and Apache server was restarted.
- **00:40:** Service was fully restored, and the website was operational.

## Root Cause
A typo in the `wp-settings.php` file, where a file extension was incorrectly written as `.phpp`, caused the server to respond with 500 errors. Initial diagnostics were hindered by disabled PHP error logging, delaying the identification of the root cause.

## Resolution and Recovery
- **00:12:** Restarted Apache server, status returned as 200 (OK).
- **00:18:** Began reviewing error logs.
- **00:25:** Noted the absence of PHP error logs.
- **00:30:** Enabled PHP error logging in `php.ini`.
- **00:32:** Restarted Apache server and reviewed PHP error logs.
- **00:36:** Identified and corrected the typo in `wp-settings.php`.
- **00:38:** Restarted Apache server.
- **00:40:** Verified the website was fully operational.

## Corrective and Preventative Measures
- Ensure error logging is always enabled on all servers.
- Conduct thorough local testing of server configurations and website functionality before deploying to a multi-server environment.
- Implement automated checks for common configuration errors to catch issues like typos before deployment.
- Regularly review and update server and application monitoring tools to ensure they capture all critical error logs.

