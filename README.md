# HENNGE Admission Challenge

Solution to the [HENNGE](https://hennge.com) Admission Coding Challenge for the Global Internship Program.

## Mission 1 — Algorithm

**Problem:** Given N test cases, each with X integers, compute the sum of fourth powers of all non-positive numbers. Print `-1` if the count of integers doesn't match X.

**Constraints (Python):**
- No `for` or `while` loops
- No list/set/dictionary comprehensions
- No global variables
- Must include a `main()` function

**Approach:**
- Recursion replaces iteration — `solve(n)` calls `solve(n-1)` until base case
- Mutable list `pos = [0]` used as a closure to share state across nested functions without globals
- `filter()` and `map()` with lambdas for functional-style processing

## Mission 2 — Secret Gist

Source code published as a secret GitHub Gist named `main.py` as required.

## Mission 3 — Authenticated API Submission

Submitted the gist URL via HTTP POST to the HENNGE API with:
- **TOTP password** generated per RFC 6238 using HMAC-SHA-512 (not default SHA-1, per errata)
- **10-digit output** (`% 10^10`) with zero-padding
- **Time step:** 30 seconds, T0 = 0
- **Shared secret:** `email + "HENNGECHALLENGE004"` encoded as UTF-8
- **Auth header:** HTTP Basic Auth with Base64-encoded `email:totp`

## Files

| File | Purpose |
|------|---------|
| `main.py` | Challenge solution — submitted as secret gist |
| `submit.py` | TOTP generation + HTTP POST to HENNGE API |

## Result
