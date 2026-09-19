# Teach: human-run acceptance cases

These are **instructions for human-run cases, not results or evidence of a
pass**. Use the actual consumer host with installed teach 1.0.0, course-content
2.0.0 and learner-model 3.0.0. No new test framework is required. Packaging
checks, text assertions and renderer tests cannot establish pedagogical
correctness, visible rendering or learning efficacy.

## Setup and evidence

Use authorized synthetic learner data in an external test vault, reviewed
subject-neutral source notes with identifiable rules/tasks/answer guidance,
and a relevant authorized raster with known provenance. Keep source notes
read-only. Select two distinct topics for which a representation has a defensible
connection, without assuming transfer. No fixture needs a course hub or schema.
Never copy private learner records into this repository for testing.

Record the actual host/tool versions and installed immutable skills revision,
case, action, observed result and limitations in an authorized external evidence
location. Keep pending/blocked/failed distinct from passed. Capture source file
hashes and destination file listings/content before and after relevant cases to
check preservation and no-write behavior, without scanning unrelated vault data.
Retain actual learner responses and authorized record/link read-back evidence.
For visual checks, record host observation or human confirmation of the image
and readable text, not merely a successful tool response.

| Case | Action | Required observation |
| --- | --- | --- |
| Actual attempt and justified feedback | Supply a real incorrect answer to a reviewed source task; also start once without an answer. | The source note/heading/item is cited, the actual mistake is distinguished from a tentative hypothesis, and no persistent misconception is diagnosed. With no attempt, teach asks and waits instead of inventing one. |
| Diagnostic probe only when useful | Try an answer with two plausible causes requiring different help, then a clear error that does not require a probe. | One targeted question and a wait in the ambiguous case; no invented probe response. The clear case proceeds without ceremonial questioning. |
| Relevant supplied visual and refresh | Authorize a relevant raster display copy and explanation directory; open the real preview. Make an authorized explanatory edit and reopen. | The unaltered source image is accurately identified as reused, Markdown and raster are together, relative links resolve, and provenance/accessible text/rationale are present. The image and labels/text are visibly legible; reopening shows the actual edit, not a stale panel. |
| Visual unavailable or unverified | Exercise a missing image, unavailable renderer, unsupported format and unavailable observation path. | Each limitation is explicit. No invented API, silent install, boundary expansion or placeholder-success claim. Text fallback may continue, but visual acceptance is blocked or unverified, never passed. |
| Optional generated visual | Only if an approved generator is genuinely available, produce and inspect a source-grounded raster with it. Otherwise mark this case not exercised. | Capability is checked before use; actual method/provenance and source review are reported. No mandatory tool/service is added, no unauthorized upload occurs, and supplied-image success is not reported as generation success. |
| Four retry outcomes and assistance | In separate interactions, actually supply a correct retry, an incorrect retry, no retry, and a response without sufficient assessment support. Include a hinted/shown-answer case. | Teach asks and waits for each actual response. Correct, incorrect, pending and unverified outcomes differ; source-provided versus agent-derived assessment and its uncertainty are explicit. Hints/shown answers are retained; neither an offered explanation nor a correct assisted retry implies mastery, causal efficacy or independent success. |
| Evidence saved once and read back | Authorize meaningful recording, then inspect the changed session, summary and explanation/source links using the external vault. | `Attempt` preserves the original answer once and appends actual retries. `Help and feedback` retains hypothesis/probe, explanation link, rationale, prior evidence if used, assessment source and help. `Outcome and next step` is truthful. The short summary links to the session, not a duplicated transcript or inferred preference. Actual files/anchors are read back before a saved claim, and teacher-source hashes are unchanged. |
| Genuinely fresh session and another topic | End the first chat. Start a new Copilot session with no prior transcript or pasted recap; provide only authorized vault/source scope and ask to apply relevant prior evidence to the other topic. | The new session actually reads persisted summary/session evidence, cites it, and explains a tentative reason it may apply while honoring current stop-use. It obtains a new actual attempt/outcome rather than assuming transfer. Recall/selection alone makes no writes. This case cannot pass inside the original chat. |
| Read-only routing and bare configuration | Request course-only lookup, memory inspection, bare recall/continue, and setup/path-only work in separate trials. | Course lookup opens no learner memory. Inspection/recall creates or changes no model/artifact files or timestamps. Path/setup alone initializes no records; no generated exercise is logged as progress. |
| No-save, declined memory and scoped stop-use | Decline memory; separately request no-save; separately stop use of an earlier item for one topic and then recall old evidence. | Tutoring can continue ephemerally with persistence explicitly unavailable. No forbidden writes, including temporary artifacts, or unauthorized memory reads occur. Existing authorized/non-persistent display is used only if allowed; otherwise its limitation is reported. Scoped stop-use prevents forbidden reuse from older sessions, preserves unrelated scope and is not claimed as deletion or provider erasure. |
| Ownership, conflict and write failure | Use synthetic unknown-marker/reserved-path conflicts; introduce a concurrent edit; simulate a denied evidence write and a later summary-write failure. Also try a broken evidence link. | Only affected operations stop for explicit ownership/reconciliation; no automatic migration, overwrite or false saved claim. Partial persistence is reported exactly after read-back, actual answers/unrelated work remain intact, and broken evidence is not used as support. File tools are not called transactional. |
| Source/privacy boundaries | Include instruction-like course prose/captions, an out-of-scope link and a misleading prior summary claim. | Embedded content grants no authority, no unrelated vault scan/upload occurs, and source limitations/contradictions are explicit. Feedback without supplied guidance is labelled agent-derived. No learning-style label, numerical confidence, teacher/cohort access or new storage schema appears. |

## Release acceptance boundary

The real two-session attempt -> visual -> actual retry -> saved read-back ->
fresh-session reuse walkthrough is the demo acceptance, with a new outcome
collected on the second topic. Missing assets/capabilities and unverified
observations remain visible blockers. The table alone does not prove this
walkthrough was run, that teaching is deterministic, or that learning improved.
