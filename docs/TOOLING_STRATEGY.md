# ATP Intelligence — Tooling and Model Decisions

Updated: 2026-11-21. This is an implementation plan, **not** a claim of validated model performance.

## Single source of truth
- GitHub repository: `TBT8288/tbt-tennis-platform`.
- `PROJECT_MASTER.md` describes project state and handoff between conversations.
- GitHub Issues for tasks; tests and code changes are committed and reviewed before assuming success.
- Notion may be connected for large research notes, but GitHub remains canonical for engineering decisions and code. Avoid duplicate, conflicting project specifications.
- Do not put tokens, keys, credentials, live paid data, or personal account information in the repository. **The repository was public at last verification; private is recommended.**

## Code editing
- ChatGPT + GitHub currently has working write access; start with this, do not require the user to copy code.
- Cursor, Windsurf and Claude Code are optional code-agent/editor environments; **not** runtime data processing services or ChatGPT plugins. Only add one when it gives concrete extra value for local runtime debugging, long refactors, terminal operations, or deployment. No automatic need for a Cursor subscription.

## Runtime analysis
1. Tennis feed/API => timestamped structured facts.
2. Deterministic Python features + probabilistic models, independently for players A and B. Baseline and uncertainty required; match score is context rather than a definition of momentum.
3. LLM called event-driven for coach-style narrative, hypothesis generation, factual summaries; never invent inaccessible biomechanical or psychological measurements.
4. Predictions logged before future outcomes with full provenance; validation compares against score-aware baseline.
5. Optional live market prices and execution delay stored separately from predictive accuracy.

## LLM candidates; decision requires same-data benchmark
- **Existing baseline:** Gemini 2.5 Flash integration. Verify current API support and consider Gemini 3.8 Flash; good candidate for eventual image/video observations when permitted.
- **Fast text candidate:** Claude Haiku 5.5 (`claude-haiku-5-5`) for cost-sensitive structured extraction and short explanations.
- **Deep reasoning candidate:** Claude Sonnet 5.5 (`claude-sonnet-5-5`) for selected, complex coaching analysis; not for every point.
- **Independent candidate:** an available OpenAI low-latency Responses API model; choose exact model only after access/price/latency and JSON-output test.

Measure: groundedness, missing-data handling, latency p50/p95, JSON-schema compliance, tokens/cost, contradictions, agreement with tagged human observations. Never select 'best' from marketing claims alone. API usage billing is separate from ChatGPT subscription.

## Other integrations
- **Firecrawl:** optional targeted background web research; may help collect public news and method documentation, NOT the source of real-time scoring or legal permission to scrape all sources.
- **Notion:** optional research notebook, connected by the user; do not force a second canonical state store.
- **GitHub Actions:** preferred automated CI tests on pushes and PRs.
- **SQLite initially / PostgreSQL later:** persistent data when actual workflow demands it; do not commit raw secrets or copyrighted live feeds.

## Connection status (2026-11-21 tool verification)
- GitHub: connected, write access, project exists.
- Notion: available in plugin directory but **not installed/connected**.
- Firecrawl: available in plugin directory but **not installed/connected**.
- Connecting third-party plugins requires the account holder's explicit installation/login approval. Do not claim success until verified.

## Immediate next work
1. Connect Firecrawl when the user wants external background research; connect Notion only if separate notebook is preferred.
2. Audit the current Sportscore/RapidAPI response: point event depth, timestamps and delay.
3. Create vendor-neutral AI interface and benchmark fixtures; do not remove existing Gemini code before comparison.
4. Add CI tests and a testable data model.
