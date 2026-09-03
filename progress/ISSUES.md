# Issues

One ticket per unit of work. Copy any block into GitHub Issues if you create a remote later.

Custom map: [`tracker.html`](tracker.html) (open in a browser).  
Optional roadmap.sh copy: [`roadmap.sh-prompt.txt`](roadmap.sh-prompt.txt)

**Labels:** `phase-0` … `phase-7` · `learn` · `build` · `ship`  
**Status:** `[ ]` Todo · `[~]` In progress · `[x]` Done

Update [`BOARD.md`](BOARD.md) when you change status.

---

## Phase 0 — Python (weeks 1–3)

### P0-01 · Project setup

- Status: [ ]
- Labels: `phase-0`, `learn`
- Weeks: 1

**Goal:** Isolated Python env and a folder you can grow.

**Acceptance**

- [ ] `venv` or `uv` created; packages install without touching system Python
- [ ] `src/` (or similar) + `.gitignore` ignoring `__pycache__` and `.venv`
- [ ] You can run a script from the project root

**Proof:** commit that adds the env workflow.

---

### P0-02 · Language you will use

- Status: [ ]
- Labels: `phase-0`, `learn`
- Weeks: 1–2

**Goal:** Lists, dicts, comprehensions, functions, type hints, dataclasses, exceptions.

**Acceptance**

- [ ] You can write a function with typed args and a dataclass without looking up syntax
- [ ] You handle a missing file with `try/except` and a clear message

**Proof:** small exercises file or notes with 3 examples you wrote yourself.

---

### P0-03 · Files, JSON, pathlib

- Status: [ ]
- Labels: `phase-0`, `learn`
- Weeks: 2

**Goal:** Read/write text and JSON on disk.

**Acceptance**

- [ ] Script walks a directory with `pathlib`
- [ ] Reads `.txt` and `.json`, writes a `.json` result

**Proof:** commit.

---

### P0-04 · Ship CLI file summarizer

- Status: [ ]
- Labels: `phase-0`, `build`, `ship`
- Weeks: 3
- **Exit ticket for Phase 0**

**Goal:** CLI that reads a folder of `.txt` / `.json`, prints counts, writes `summary.json`.

**Acceptance**

- [ ] `python -m` or `python path/to/cli.py <folder>` works
- [ ] Counts files, lines/keys, writes structured JSON
- [ ] README: how to run

**Proof:** repo folder + sample input + `summary.json`.

---

## Phase 1 — Data literacy (weeks 4–6)

### P1-01 · NumPy basics

- Status: [ ]
- Labels: `phase-1`, `learn`
- Weeks: 4

**Goal:** Arrays, shapes, broadcasting (think Unity `NativeArray`, not `List`).

**Acceptance**

- [ ] You can explain shape `(n, d)` and a broadcast multiply
- [ ] Short notebook or script with 5 NumPy ops you chose

**Proof:** file in repo.

---

### P1-02 · Pandas + one chart

- Status: [ ]
- Labels: `phase-1`, `learn`
- Weeks: 4–5

**Goal:** Load CSV, filter, `groupby`, missing data, one Matplotlib chart.

**Acceptance**

- [ ] Real CSV loaded (not a 5-row toy you typed by hand)
- [ ] `groupby` + missing-value report
- [ ] One chart that answers a question

**Proof:** notebook or script + chart image.

---

### P1-03 · SQL enough for interviews

- Status: [ ]
- Labels: `phase-1`, `learn`
- Weeks: 5

**Goal:** `SELECT`, `WHERE`, `JOIN`, `GROUP BY`.

**Acceptance**

- [ ] 5 queries on a sample DB (SQLite is fine)
- [ ] At least one `JOIN` and one aggregate

**Proof:** `.sql` file or notebook.

---

### P1-04 · Ship mini-analysis

- Status: [ ]
- Labels: `phase-1`, `build`, `ship`
- Weeks: 6
- **Exit ticket for Phase 1**

**Goal:** “What I found” on a real dataset.

**Acceptance**

- [ ] Dataset cited (source URL)
- [ ] Notebook + 1-page writeup (markdown is fine)
- [ ] 3 findings, each backed by a table or chart

**Proof:** writeup link in this ticket.

---

## Phase 2 — ML literacy (weeks 7–10)

### P2-01 · Core ML concepts

- Status: [ ]
- Labels: `phase-2`, `learn`
- Weeks: 7

**Goal:** Train/val/test, leakage, precision / recall / F1.

**Acceptance**

- [ ] You can explain leakage in one paragraph
- [ ] You can say when F1 beats accuracy

**Proof:** notes file (your words, not a paste).

---

### P2-02 · scikit-learn Pipeline

- Status: [ ]
- Labels: `phase-2`, `build`
- Weeks: 7–8

**Goal:** Pipeline on a tiny dataset.

**Acceptance**

- [ ] `Pipeline` + train/test split
- [ ] Printed classification report

**Proof:** script.

---

### P2-03 · Tiny PyTorch loop

- Status: [ ]
- Labels: `phase-2`, `build`
- Weeks: 9

**Goal:** Tensors, loss, `backward()` — ~20 lines on dummy data.

**Acceptance**

- [ ] Loss goes down over steps
- [ ] You can explain what `backward()` does in one sentence

**Proof:** script + printed loss curve or log.

---

### P2-04 · Ship text classifier

- Status: [ ]
- Labels: `phase-2`, `build`, `ship`
- Weeks: 10
- **Exit ticket for Phase 2**

**Goal:** `Tfidf` + logistic regression on real-ish text (reviews, spam, etc.).

**Acceptance**

- [ ] Train/val split, metrics reported
- [ ] README: dataset, metric, 3 example predictions

**Proof:** public or local repo folder.

---

## Phase 3 — LLMs (weeks 11–14)

### P3-01 · LLM mental model

- Status: [ ]
- Labels: `phase-3`, `learn`
- Weeks: 11

**Goal:** Tokens, context window, temperature, message roles.

**Acceptance**

- [ ] Notes: what a token is, why context overflows, what temperature changes
- [ ] One prompt that returns valid JSON (schema or strict instructions)

**Proof:** notes + example prompt/output.

---

### P3-02 · Two model backends

- Status: [ ]
- Labels: `phase-3`, `build`
- Weeks: 12

**Goal:** One hosted API (OpenAI-compatible) and one local/open path (Ollama or Groq/HF).

**Acceptance**

- [ ] Same prompt, two models, side-by-side answers
- [ ] Tokens in/out logged for both

**Proof:** script output.

---

### P3-03 · Safety and cost

- Status: [ ]
- Labels: `phase-3`, `learn`
- Weeks: 13

**Goal:** Injection, PII, “don’t trust the model,” cost/latency.

**Acceptance**

- [ ] One injection example you tried and how you mitigated it
- [ ] Rough $ estimate for 1k requests of your chat endpoint

**Proof:** notes.

---

### P3-04 · Ship FastAPI chat

- Status: [ ]
- Labels: `phase-3`, `build`, `ship`
- Weeks: 14
- **Exit ticket for Phase 3**

**Goal:** `POST /chat` with system prompt, history, token/cost in the response.

**Acceptance**

- [ ] FastAPI app runs locally
- [ ] Conversation history works
- [ ] Response includes token and cost fields
- [ ] README: env vars, how to run, example `curl`

**Proof:** repo + example request/response.

---

## Phase 4 — RAG / Portfolio #1 (weeks 15–20)

### P4-01 · Chunking

- Status: [ ]
- Labels: `phase-4`, `learn`, `build`
- Weeks: 15

**Goal:** Chunk by size/overlap and by heading.

**Acceptance**

- [ ] Script chunks a markdown folder two ways
- [ ] You write which strategy you’d pick for docs vs chat logs

**Proof:** script + sample chunks.

---

### P4-02 · Embeddings + vector store

- Status: [ ]
- Labels: `phase-4`, `build`
- Weeks: 16

**Goal:** Embed chunks, store in Chroma or Qdrant, cosine search.

**Acceptance**

- [ ] Ingest + query by text returns nearest chunks
- [ ] You can change `top_k` and see the difference

**Proof:** script.

---

### P4-03 · Retrieve → generate → cite

- Status: [ ]
- Labels: `phase-4`, `build`
- Weeks: 17–18

**Goal:** Full RAG loop with sources.

**Acceptance**

- [ ] Answer uses retrieved context
- [ ] Response lists source chunk ids or filenames
- [ ] You document one failure (wrong retrieval or hallucination)

**Proof:** example Q/A JSON.

---

### P4-04 · RAG eval (20 questions)

- Status: [ ]
- Labels: `phase-4`, `build`
- Weeks: 19

**Goal:** Golden set, scored correct / partial / fail.

**Acceptance**

- [ ] 20 questions with expected facts or sources
- [ ] Script prints a score
- [ ] You change one chunking setting and record score delta

**Proof:** `evals/` folder + results.

---

### P4-05 · Ship Doc Q&A API

- Status: [ ]
- Labels: `phase-4`, `ship`
- Weeks: 20
- **Exit ticket for Phase 4 — Portfolio #1**

**Goal:** Public-quality Doc Q&A.

**Acceptance**

- [ ] `/ingest` and `/ask`
- [ ] Markdown and/or PDF ingest
- [ ] Answer + sources
- [ ] README architecture diagram
- [ ] Docker one-command run
- [ ] 20-question eval in repo

**Proof:** GitHub repo URL + screenshot or clip.

---

## Phase 5 — Evals, agents, production / Portfolio #2 (weeks 21–26)

### P5-01 · Eval harness

- Status: [ ]
- Labels: `phase-5`, `build`
- Weeks: 21

**Goal:** Golden set + regression when a prompt changes.

**Acceptance**

- [ ] Script compares current run to a baseline file
- [ ] Exit code ≠ 0 if score drops below a threshold

**Proof:** `eval.py` + baseline JSON.

---

### P5-02 · Tools / function calling

- Status: [ ]
- Labels: `phase-5`, `build`
- Weeks: 22

**Goal:** Model calls at least 3 tools.

**Acceptance**

- [ ] Tools: e.g. retrieve docs, one external or fake API, write a file or ticket
- [ ] Structured args (Pydantic or JSON schema)
- [ ] Retry or validation on bad tool args

**Proof:** logged tool-call trace.

---

### P5-03 · Observability + serving

- Status: [ ]
- Labels: `phase-5`, `build`
- Weeks: 23–24

**Goal:** Logs and a real service shape.

**Acceptance**

- [ ] Log prompt, retrieval, latency, cost (Langfuse / LangSmith / your tables)
- [ ] Secrets via env, not committed
- [ ] Rate limit or simple auth
- [ ] Optional: streaming tokens

**Proof:** log sample (redacted) + README.

---

### P5-04 · Docker + optional deploy

- Status: [ ]
- Labels: `phase-5`, `ship`
- Weeks: 24–25

**Goal:** Someone else can run it.

**Acceptance**

- [ ] `docker compose up` (or equivalent) documented
- [ ] Optional: live URL (Railway / Fly / Azure)

**Proof:** Dockerfile + run instructions; URL if deployed.

---

### P5-05 · Ship agent + 30 evals

- Status: [ ]
- Labels: `phase-5`, `ship`
- Weeks: 26
- **Exit ticket for Phase 5 — Portfolio #2**

**Goal:** Tool-using agent with evals and a cost number.

**Acceptance**

- [ ] 3+ tools
- [ ] 30 eval cases; harness fails on regression
- [ ] Documented $ per 100 queries
- [ ] README architecture + how to run evals

**Optional**

- [ ] Bilingual Arabic + English RAG (Gulf signal)

**Proof:** public repo URL.

---

## Phase 6 — Unity specialty (weeks 27–28, optional)

### P6-01 · One Unity-flavored demo

- Status: [ ]
- Labels: `phase-6`, `ship`
- Weeks: 27–28

**Pick one:** sprite/screenshot detector · ML-Agents env · Unity synthetic data → tiny detector.

**Acceptance**

- [ ] Public repo
- [ ] Short video
- [ ] README: what was learned, not a full game

**Proof:** repo + video link.

---

## Phase 7 — Job package (weeks 27–30)

### P7-01 · Portfolio polish

- Status: [ ]
- Labels: `phase-7`, `ship`
- Weeks: 27–28

**Acceptance**

- [ ] Two repos look hireable (README, architecture, how to run, evals)
- [ ] Dead tutorial forks removed or archived

**Proof:** two GitHub URLs.

---

### P7-02 · Public profile

- Status: [ ]
- Labels: `phase-7`, `ship`
- Weeks: 28–29

**Acceptance**

- [ ] LinkedIn headline: Senior Unity Engineer → AI Engineer
- [ ] Deployed or demo links on LinkedIn + GitHub profile

**Proof:** profile URLs.

---

### P7-03 · Interview drills

- Status: [ ]
- Labels: `phase-7`, `learn`
- Weeks: 29–30

**Acceptance**

- [ ] 5 medium Python problems you can talk through
- [ ] Whiteboard RAG once from memory
- [ ] Written answer: “How would you eval this chatbot?”

**Proof:** notes.

---

### P7-04 · Applications out

- Status: [ ]
- Labels: `phase-7`, `ship`
- Weeks: 30

**Acceptance**

- [ ] Applications started (Egypt MNCs, remote GCC, UAE/KSA AI Engineer)
- [ ] Do not wait for Phase 6

**Proof:** tracker of roles applied (private is fine).

---

## Copy-paste: GitHub Issue body

```markdown
## Goal


## Acceptance
- [ ]

## Proof

```

Suggested GitHub labels: `phase-0` … `phase-7`, `learn`, `build`, `ship`.
