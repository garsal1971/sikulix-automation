# Istruzioni per Claude Code — sikulix-automation

## Regola branch
- **Sviluppa sempre su un branch dedicato** (es. `claude/nome-fix`)
- **Al termine, unisci sempre su `main`** e fai push:
  ```bash
  git checkout main
  git merge <branch>
  git push origin main
  ```
- Non lasciare mai le modifiche solo sul branch di lavoro.

## Progetto
Script SikuliX per automazione app WeWard (raccolta carte, login/logout multi-account).

### Script principali
- `raccogli_sette_carte.sikuli/raccogli_sette_carte.py` — versione con login Google diretto
- `raccogli_sette_carte_no_google.sikuli/raccogli_sette_carte_no_google.py` — versione con flusso Gmail completo

### Note tecniche SikuliX
- SikuliX pre-scansiona **tutte** le stringhe `.png` nel file `.py` prima dell'esecuzione, **anche nei commenti**. Non usare mai nomi `.png` fittizi nei commenti.
- Le immagini devono risiedere nella stessa cartella `.sikuli` dello script.
