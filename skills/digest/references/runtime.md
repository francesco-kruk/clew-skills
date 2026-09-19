# Local PDF tooling

APM installs digest's instructions and references, not a PDF engine or Python
environment. No other skill supplies required runtime files. Choose a method
after probing the authorized PDF; use existing working tools first. Do not install
packages merely because they appear in this table.

| Chosen method | Runtime needed | Limits |
| --- | --- | --- |
| Coordinate-aware text extraction, page rendering, figure crops | Python and `pymupdf` | Useful first choice for selectable text and vector figures; extraction alone does not verify reading order or equations. |
| Existing Poppler text/render tools | `pdftotext` and, when rendering is needed, `pdftoppm` or `pdftocairo` | Text extraction is not OCR; confirm which executables are actually available. |
| Optional Markdown first pass | Python and `markitdown[pdf]` | An intermediate, not the fidelity authority; rendering/recovery may still require another tool. |
| Scanned text OCR with PyMuPDF | `pymupdf`, a local Tesseract installation and the required language data | Use `page.get_textpage_ocr(...)` and extract with that text page. Verify language/data paths. OCR is unreliable for math; inspect the source. |

For missing Python packages required by the selected method, create a task-local
virtual environment under the authorized external working directory, outside the
reader-facing bundle. Example PowerShell setup **only after choosing PyMuPDF**:

```powershell
python -m venv 'D:\Authorized Work\pdf-env'
& 'D:\Authorized Work\pdf-env\Scripts\python.exe' -m pip install pymupdf
& 'D:\Authorized Work\pdf-env\Scripts\python.exe' -c "import pymupdf; print(pymupdf.VersionBind)"
```

Replace the example path with the resolved authorized location. Use the environment's
interpreter explicitly for extraction and subsequent package installs; do not
assume shell activation persists. If MarkItDown was selected instead, install only
`"markitdown[pdf]"` initially and run:

```powershell
& 'D:\Authorized Work\pdf-env\Scripts\python.exe' -m markitdown `
  'D:\Authorized Sources\Book.pdf' -o 'D:\Authorized Work\raw.md'
```

Add PyMuPDF only if recovery/rendering calls for it and no suitable renderer is
already available. Keep raw extracts, caches, render probes, and the environment
outside the final bundle. Record actual versions and chosen methods in the report.
Do not downgrade or modify the user's global Python environment.

If a selected native renderer or OCR engine is missing, explain the requirement.
Use an authorized task-local installation and language data where supported; if
that cannot be provided, report the blocker rather than silently installing
system-wide software. A Python OCR wrapper alone does not install Tesseract.
Do not install all OCR languages or download document-linked resources.

Dependency downloads contact the configured package source but must not upload
the PDF. Do not add separate hosted OCR/vision services as a fallback. Ordinary
bounded Copilot task processing still applies as described in the skill.
If local extraction, OCR, and bounded visual transcription cannot recover a
region, retain a labeled page crop and report it as image-only/unreadable. If no
renderer can preserve it either, record the missing region and mark delivery
incomplete; never count a failed extraction as a blank page.
