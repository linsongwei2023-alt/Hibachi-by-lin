# Hibachi by Lin — maintenance and recovery guide

## Source of truth

- Production site: https://www.hibachibylin.com
- Canonical source repository: https://github.com/linsongwei2023-alt/Hibachi-by-lin
- Default branch: `main`
- Hosting: Vercel (automatic production deployment from the repository)

The repository and its Git history are the authoritative record. Chat conversations and assistant memory are helpful context, but they are not a backup system.

## Required workflow after every change

1. Pull or inspect the latest `main` branch before editing.
2. Make only the intended changes and test the affected pages.
3. Commit and push the complete change to `main` with a clear commit message.
4. Add a concise entry to `SITE_CHANGELOG.md`.
5. Confirm the Vercel production deployment succeeds.
6. Verify the affected URL on `https://www.hibachibylin.com`.
7. If ChatGPT Library is available, create a portable ZIP named `Hibachi-by-Lin-backup-YYYY-MM-DD-HHMMSS-UTC.zip`.

## What a portable backup must contain

- All website HTML, CSS, JavaScript, images, videos, configuration, and public assets.
- This guide and `SITE_CHANGELOG.md`.
- A backup manifest containing the UTC timestamp, branch, and exact Git commit SHA.
- No `.git` directory, credentials, environment secrets, customer information, or payment data.

## Restore or move the website

1. Create a new Git repository or hosting project.
2. Extract the newest portable ZIP into the project root.
3. Confirm `index.html`, `vercel.json`, `robots.txt`, and `sitemap.xml` are present.
4. Deploy as a static site.
5. Point the domain DNS to the new host only after the preview is verified.
6. Reconfigure any host-side environment variables separately; secrets are intentionally excluded from backups.

## Starting in another ChatGPT conversation or mode

Ask the assistant to inspect this repository and read `AGENTS.md` plus `SITE_MAINTENANCE.md` before making changes. This transfers the operational context without depending on cross-chat memory.
