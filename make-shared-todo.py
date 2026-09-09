import re, datetime, io

src = open("Design-TODO.md", encoding="utf-8").read().split("\n")

HEADER = """# Design To-Do — Yuehui (shared view for Kelly)

Auto-generated from Yuehui's rolling `Design-TODO.md`. **Active work only** — paused and dropped items are filtered out, so this is shorter than her master list.

Status markers: no marker = Open · **Next** = up next this week · **Doing** = in progress · **Blocked** = waiting on someone. Date tag `(M/D)` = the meeting the task came from. Indented lines are sub-tasks of the line above; `⇢ parallel` runs alongside its parent rather than waiting on it.

Questions on any line — ask Yuehui, the longer context lives in her detail file.
"""

def indent(l):
    return len(l) - len(l.lstrip(" "))

def is_bullet(l):
    return l.lstrip(" ").startswith("- ")

def dead(l):
    return re.search(r"\*\*(Pause|Dropped)\b", l) is not None

out, skip_at, in_done = [], None, False
for line in src:
    if line.startswith("## "):
        in_done = line.strip() == "## Done"
        skip_at = None
        if in_done:
            continue
        out.append(line); continue
    if in_done:
        continue
    if is_bullet(line):
        ind = indent(line)
        if skip_at is not None and ind > skip_at:
            continue
        skip_at = None
        if dead(line):
            skip_at = ind
            continue
        out.append(line); continue
    if line.strip() == "":
        out.append(line); continue
    if skip_at is not None:
        continue
    out.append(line)

# carry Yuehui's current-state notes out of the preamble
pre = []
for l in src:
    if l.strip() == "---":
        break
    if l.startswith("**") or (l.strip() and not l.startswith("#") and not l.startswith("Rolling") and not l.startswith("Status:") and not l.startswith("`-`") and not l.startswith("Longer context") and not l.startswith("`design-todo.html`")):
        pre.append(l)
notes = ("## Where things stand\n\n" + "\n\n".join(pre) + "\n\n") if pre else ""

# strip the original preamble (everything before the first ---)
try:
    first = out.index("---")
    body = out[first+1:]
except ValueError:
    body = out

# drop sections that ended up with no bullets
blocks, cur = [], []
for l in body:
    if l.startswith("## "):
        blocks.append(cur); cur = [l]
    else:
        cur.append(l)
blocks.append(cur)
kept = []
for b in blocks:
    if any(is_bullet(x) for x in b) or not any(x.startswith("## ") for x in b):
        kept.append(b)

body = [l for b in kept for l in b]
# collapse 3+ blank lines
text = "\n".join(body)
text = re.sub(r"\n{3,}", "\n\n", text).strip()
text = re.sub(r"\n-{3,}\s*$", "", text).strip()

stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
footer = f"\n\n---\n\n_Generated {stamp} from Design-TODO.md. Yuehui's file is the source of truth; edits made here won't flow back._\n"

open("Design-TODO-Shared.md","w",encoding="utf-8").write(HEADER + "\n---\n\n" + notes + text + footer)
print("wrote Design-TODO-Shared.md")
