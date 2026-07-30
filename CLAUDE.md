# Working rules for this repository

This repository sits outside the organisation-wide `CLAUDE.md`, so the rules it
needs are written here rather than inherited.

## Commits

**GR-013 (2026-07-30): do not put a `Co-Authored-By:` trailer in a commit
message.** Claude Code adds one by default, so it has to be removed explicitly
each time rather than merely not-added.

Use `NEWXUS <info@ouen-battle.com>` as the author:

```
git -c user.name=NEWXUS commit -m "..." --author="NEWXUS <info@ouen-battle.com>"
```

(`user.name` is unset in this working copy, so a bare `git commit` fails.)

History before 2026-07-30 carries `unknown <info@ouen-battle.com>` on 32
commits and `info@ouen-battle.com <info@ouen-battle.com>` on 14. Those are
published; **do not rewrite them.** The rule applies going forward, and
`tools/check_selfclaims.py` check H enforces it from a recorded baseline commit
rather than pretending the older ones comply.

`git push` is a manual gate held by HUMMER. Commit locally and report; do not
push.

### The guard, and what it does not do

`.githooks/commit-msg` rejects the trailer at commit time. Activate it once per
working copy:

```
git config core.hooksPath .githooks
```

It is a convenience, not a guarantee. It is **not carried by `git clone`**, it
is **skipped by `git commit --no-verify`**, and it **never looks at commits
that already exist**. All three are holes in the *path* it guards.

The guarantee is `tools/check_selfclaims.py` **check F**, which reads the
committed history and fails if any commit carries the trailer — whichever of
those three holes it arrived through. Constrain the result, not the route.

A fourth hole was found after the hook was first pushed: it went out as mode
`100644`. `chmod +x` had been run, but `core.filemode` is `false` in this
working copy, so git recorded nothing — and **git skips a non-executable hook
silently**, with no error. **Check G1** now verifies the mode recorded in the
index, so the guard cannot ship in a state where it never fires. If you ever
re-add the hook:

```
git update-index --chmod=+x .githooks/commit-msg
```

## Claims

Two checks exist because two claims here are easy to state and hard to keep
true. Run both before reporting work as done:

```
python tools/check_verbatim.py     # quotations trace to the verified corpus
python tools/check_selfclaims.py   # the repo's claims about itself hold
```

Each has a `--self-test` flag that injects a real defect and proves the check
goes red. Run it before trusting a green result.

Do not state a rule as enforced unless something enforces it. If a guard has
limits, write the limits next to the claim — that is what this file is doing
about its own hook.
