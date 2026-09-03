# Custom roadmap

You wanted **your** plan as a clickable map you can tick — not the generic [AI Engineer](https://roadmap.sh/ai-engineer) chart.

## What we use (this is the custom map)

Open this file in a browser:

**[`tracker.html`](tracker.html)**

- Small cards on the left; **click** a card to open description, examples, and resources on the right
- **Right-click** a card → Todo / Learning / Done / Skipped
- Progress is saved in this browser (`localStorage`)
- **Done** only when you have proof (same rule as the repo)

Double-click `tracker.html`, or in a terminal:

```powershell
start e:\Python_Learning\progress\tracker.html
```

---

## Can this live on roadmap.sh?

**Partially.** I cannot create a roadmap inside *your* roadmap.sh account.

| Method | What happens |
| --- | --- |
| Official maps (Python, AI Engineer, …) | Community maps. Not this plan. Lots of nodes you should skip. |
| [Create custom roadmap](https://roadmap.sh/r/new) | Empty canvas. You drag boxes by hand. Progress tracking works after you build it. |
| [AI generator](https://roadmap.sh/ai/roadmap) | Closest match. You paste a prompt; it **rewrites** the graph. Free accounts are capped (often **2** AI roadmaps). Need to be logged in, then **Save**. |

If you still want a copy on roadmap.sh:

1. Sign up: https://roadmap.sh/signup
2. Open https://roadmap.sh/ai/roadmap
3. Format: **Roadmap**
4. Paste [`roadmap.sh-prompt.txt`](roadmap.sh-prompt.txt)
5. Generate → **Save** to account
6. Right-click nodes: Done / Learning / Skipped

Treat that as a **mirror**. `tracker.html` stays exact.

---

## Split of labor

| Place | Job |
| --- | --- |
| [`tracker.html`](tracker.html) | Custom map + % |
| [`ISSUES.md`](ISSUES.md) | Acceptance criteria |
| [`BOARD.md`](BOARD.md) | This week’s WIP |
| GitHub repos you will create | Proof hiring managers open |
