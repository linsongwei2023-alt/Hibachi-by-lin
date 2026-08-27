# English Notes Coach v2

Personal English diary + phrase notebook.

Persistence strategy:
1. Instant localStorage autosave on the current device.
2. Automatic Supabase cloud snapshot sync.
3. Recovery key for reconnecting cloud notes after browser data loss or on another device.
4. Manual JSON export/import backup.

Supabase backend uses `english_notes_save_snapshot` and `english_notes_load_snapshot`. The browser uses only the Supabase publishable key; the recovery key is hashed before it is stored in the database.

Production source is kept on the `english-notes-coach-v2` branch so future maintenance does not touch Hibachi production `main`.