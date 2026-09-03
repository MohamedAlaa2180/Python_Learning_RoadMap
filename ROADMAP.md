# AI Engineer Roadmap

Personal plan for a **senior Unity / C# engineer**, Python beginner, targeting **AI Engineer** (ship LLM systems). Middle East / Gulf optional later.

**Cadence:** ~8–12 hours/week → about **7–9 months** to a hireable portfolio.  
**Rule:** a phase is done when the **project ships**, not when a course hits 100%.

**Custom map (tick nodes here):** open [`progress/tracker.html`](progress/tracker.html) in a browser.  
Details: [`progress/ISSUES.md`](progress/ISSUES.md) · this week: [`progress/BOARD.md`](progress/BOARD.md) · roadmap.sh notes: [`progress/ROADMAP_SH.md`](progress/ROADMAP_SH.md).

---

## How to use this

```
Python → data literacy → enough ML to not be fake
    → LLMs → RAG → agents / evals / API
    → 2 portfolio products → apply
```

Skip: web frontend, competitive programming, Kaggle-as-a-lifestyle, TensorFlow-first, “100 Python exercises.”

**Weekly ritual (15 min):** mark a box here only if **Proof** exists (commit URL, demo, or notes file). Then mark the same skill **Done** on roadmap.sh. Watching videos does not count as Done.

---

## Stack

| Must | Later |
| --- | --- |
| Python, Git, FastAPI | Kubernetes |
| NumPy, Pandas, SQL | Spark |
| scikit-learn (lite), PyTorch (lite) | Training LLMs |
| Embeddings + Chroma or Qdrant | Fine-tuning (LoRA) after you have a job |
| One LLM API + Ollama | Multi-agent frameworks as a religion |
| Docker | LangChain-everything (use it as a tool, don’t become it) |

---

## Phase 0 — Python you’ll actually use (weeks 1–3)

You’re past “what is a variable.” Learn the dialect AI work uses.

**Skills**

- [ ] `venv` or `uv`, `pip`, project layout
- [ ] `list` / `dict` / comprehensions, functions, typing (`list[str]`, dataclasses)
- [ ] Files, JSON, pathlib, exceptions
- [ ] One script that is not a notebook

**Exit ticket**

- [ ] CLI: read a folder of `.txt` / `.json` → print counts, write a summary JSON

**Resources:** official Python tutorial (data structures + modules only), then stop.

---

## Phase 1 — Data literacy (weeks 4–6)

AI Engineering still lives on tables and messy text.

**Skills**

- [ ] NumPy: arrays, shapes, broadcasting
- [ ] Pandas: load CSV, filter, `groupby`, missing data
- [ ] SQL: `SELECT`, `JOIN`, `GROUP BY`
- [ ] Matplotlib: one honest chart

**Exit ticket**

- [ ] Analyze a real dataset (Steam reviews, Kaggle CSV, or your own logs)
- [ ] Notebook + 1-page “what I found”

**Skip:** advanced stats, A/B testing deep dive, Spark.

---

## Phase 2 — ML literacy, not ML career (weeks 7–10)

Vocabulary so “embedding” and “overfitting” aren’t magic. You will **not** job-hunt as ML Engineer yet.

**Skills**

- [ ] Train / val / test, leakage, precision / recall / F1
- [ ] scikit-learn Pipeline on a tiny dataset
- [ ] What a neural net is: tensors, loss, `backward()`
- [ ] 20-line PyTorch training loop on dummy data

**Exit ticket**

- [ ] Classify text with sklearn (`Tfidf` + logistic regression)

**Resources:** Google ML Crash Course (skim), [PyTorch 60-minute blitz](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html).

**Skip:** from-scratch transformers, CUDA kernels, Kaggle medals.

---

## Phase 3 — How LLMs actually work (weeks 11–14)

This is the start of the real job.

**Skills**

- [ ] Tokens, context window, temperature, system vs user vs tool messages
- [ ] Structured prompting (JSON schema, not “please be nice”)
- [ ] Chat APIs: OpenAI-compatible **and** one open model (Groq / Together / Ollama / Hugging Face)
- [ ] Cost and latency: tokens in/out, caching
- [ ] Safety: injection, PII, don’t trust the model

**Exit ticket**

- [ ] FastAPI `POST /chat` with system prompt, history, token/cost log
- [ ] Same prompt against two models, compared

**Resources:** OpenAI / Anthropic cookbooks, [Hugging Face LLM course](https://huggingface.co/learn) (using models, not pretraining).

---

## Phase 4 — RAG (weeks 15–20)

Most Gulf / enterprise AI Engineer jobs are this.

**Skills**

- [ ] Chunking (size, overlap, by heading)
- [ ] Embeddings, cosine similarity
- [ ] Vector store: Chroma or Qdrant
- [ ] Retrieve → (optional rerank) → generate
- [ ] Citations: answer + source chunks
- [ ] Failure modes: bad chunks, wrong top-k, stale docs

**Exit ticket — Portfolio #1 (public)**

- [ ] Doc Q&A API: ingest markdown/PDF, `/ingest` + `/ask`
- [ ] Returns answer + sources
- [ ] README with architecture diagram
- [ ] Eval of 20 questions (correct / partial / fail)
- [ ] Docker one-command run

---

## Phase 5 — Evals, agents, production (weeks 21–26)

What separates “I called the API” from “I can own the AI layer.”

**Skills**

- [ ] Evals: golden set, LLM-as-judge (with skepticism), prompt-change regression
- [ ] Agents / tools: function calling (search, calc, query vector DB)
- [ ] Structured output: Pydantic models, retries
- [ ] Observability: log prompts, retrievals, latency, cost
- [ ] Serving: FastAPI, secrets, rate limits, streaming
- [ ] Docker; optional one cloud deploy (Railway, Fly, Azure)

**Exit ticket — Portfolio #2**

- [ ] Tool-using agent (3+ tools)
- [ ] 30 eval cases; script fails if quality drops
- [ ] Cost number: $ per 100 queries

**Optional Gulf upgrade**

- [ ] Same RAG over Arabic + English docs

---

## Phase 6 — Unity specialty (weeks 27–28, optional)

Do this **after** RAG works. One project only.

- [ ] Screenshot / sprite classifier or detector **or**
- [ ] Unity ML-Agents small env **or**
- [ ] Synthetic Unity dataset → tiny detector
- [ ] Short video + public repo

---

## Phase 7 — Job package (weeks 27–30, overlap Phase 5)

- [ ] GitHub: 2 polished repos (RAG + agent/evals)
- [ ] LinkedIn: Senior Unity Engineer → AI Engineer, deployed links
- [ ] 1-page architecture writeup per project
- [ ] Interview drills: Python (medium), RAG system design, “how would you eval this?”
- [ ] Applications out (Egypt MNCs, remote GCC, UAE/KSA AI Engineer)

**Apply while Phase 5 is finishing.** Don’t wait for perfect.

---

## Week-by-week

| Weeks | Phase | Exit ticket | Done |
| --- | --- | --- | --- |
| 1–3 | Python | CLI file summarizer | [ ] |
| 4–6 | Data | Pandas + SQL mini-analysis | [ ] |
| 7–10 | ML literacy | sklearn text classifier + tiny PyTorch loop | [ ] |
| 11–14 | LLM APIs | FastAPI chat + cost log | [ ] |
| 15–20 | RAG | Portfolio #1 live | [ ] |
| 21–26 | Evals + agents | Portfolio #2 + eval script | [ ] |
| 27–30 | Polish + Unity optional | Applications out | [ ] |
| 31–36 | Buffer / interviews | No new courses | [ ] |

If you only have ~5h/week, stretch each block ~1.5× and **cut Phase 6**.

---

## Hire bar (you can do these without a tutorial open)

- [ ] Design RAG on a whiteboard (chunk → embed → retrieve → generate → cite)
- [ ] Explain a wrong answer (chunking vs retrieval vs prompt vs model)
- [ ] Add an eval set and catch a regression
- [ ] Expose an API with auth, logs, and a cost number
- [ ] Talk latency, failure modes, fallbacks like a senior engineer

---

## Tracking platforms

| Tool | Role |
| --- | --- |
| [`progress/tracker.html`](progress/tracker.html) | **Your custom map** + progress % |
| [roadmap.sh AI generator](https://roadmap.sh/ai/roadmap) | Optional mirror — prompt in [`progress/roadmap.sh-prompt.txt`](progress/roadmap.sh-prompt.txt) |
| This repo | Tickets, proof, projects |
| DeepLearning.AI / Coursera short courses | After Phase 3 only |
| [Hugging Face Learn](https://huggingface.co/learn) | Free, job-relevant modules |

Don’t optimize for roadmap.sh % or certificates. Hiring managers open **GitHub**.

---

## Anti-patterns

- Collecting 6 parallel courses
- Fine-tuning before RAG + evals
- Rebuilding LangChain instead of shipping
- Waiting until Python feels “finished”
- Calling yourself AI Engineer after a chatbot with no retrieval and no evals
