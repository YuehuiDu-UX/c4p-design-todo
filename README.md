# C4P Design To-Do

Rolling design task list for the Connect4Patients product work. Maintained by Yuehui Du.

## The files

| File | What it is | Who it's for |
|---|---|---|
| `Design-TODO.md` | **Source of truth.** Terse, one line per task, grouped by product area. Date tag `(M/D)` is the meeting the task came from. | Yuehui |
| `Design-TODO-Shared.md` | Active work only, generated from the above. Paused and dropped items filtered out. | Kelly and anyone syncing on the tasks |
| `Design-TODO-detail.md` | Longer context for each line: meeting background, open questions, related files. | Reference, when "what did I mean by this" comes up |
| `design-todo.html` | Clickable view of the list with status filters and a copy-as-markdown button. | Working view |
| `make-shared-todo.py` | Regenerates `Design-TODO-Shared.md` from `Design-TODO.md`. | Tooling |

## Status vocabulary

No marker = Open · **Next** = up next this week · **Doing** = in progress · **Pause** = not the priority right now · **Blocked** = waiting on someone · **Dropped** = decided against. `[x]` means done and overrides the status.

Indented lines are sub-tasks and ride along with their parent. A line prefixed `⇢ parallel` runs alongside its parent instead of waiting on it.

## Updating

Edit `Design-TODO.md`, then regenerate the shared view:

```
python3 make-shared-todo.py
```

Never hand-edit `Design-TODO-Shared.md`. It gets overwritten on every regeneration.
