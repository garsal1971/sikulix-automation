# -*- coding: utf-8 -*-
import sys
import math
sys.path.append(getBundlePath())   # trova i moduli nella stessa cartella .sikuli
from sikuli import *               # aggiunge tutte le funzioni SikuliX al modulo
import java.awt.Robot as Robot
import java.awt.event.InputEvent as InputEvent

# ================================================================
# CONFIGURAZIONE ACCOUNT
# ================================================================
_robot = Robot()
TARGET = (14, 129, 115)  # colore RGB del punto blu da cliccare sulle carte

ACCOUNT_CONFIG = {
    'garsal1971':          {'google': "1775290644794.png"},
    'adagarofalobognanni': {'google': "1775145979844.png"},
    'berros1974':          {'google': "1775217119680.png"},
    'gmx.salgar71':        {'google': "1775236822745.png"},
    'berros7426':          {'google': "1775237806527.png"},
    # aggiungi altri account qui sotto
}

# ================================================================
# UTILITY SCROLL
# ================================================================
def scroll_giu(volte=35, x=185, y=400, sposta_mouse=True):
    if sposta_mouse:
        _robot.mouseMove(x, y)
    for i in range(volte):
        _robot.mouseWheel(3)
        wait(0.05)

# ================================================================
# UTILITY GENERALI
# ================================================================
def cerca_con_tentativi(immagine, max_tentativi=5, attesa=0.5):
    # cerca immagine sullo schermo con N tentativi prima di rinunciare
    for t in range(1, max_tentativi + 1):
        if exists(immagine):
            return True
        print("    tentativo {0}/{1} fallito per [{2}], attendo {3}s...".format(t, max_tentativi, immagine, attesa))
        wait(attesa)
    print("  ERRORE: [{0}] non trovata dopo {1} tentativi.".format(immagine, max_tentativi))
    return False

def colore_vicino(c1, c2, soglia=20):
    return (abs(c1[0]-c2[0]) < soglia and
            abs(c1[1]-c2[1]) < soglia and
            abs(c1[2]-c2[2]) < soglia)

def distanza(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# ================================================================
# APERTURA APP
# ================================================================
def apri_weward(max_tentativi=5, attesa=0.5):
    # cerca e apre la icona della app WeWard
    print(">>> [apri_weward] cerco icona app...")
    if not cerca_con_tentativi("1775145501224.png", max_tentativi, attesa):
        print(">>> [apri_weward] ERRORE: icona app non trovata, uscita.")
        return False
    click(getLastMatch())
    print(">>> [apri_weward] app aperta OK")
    wait(0.5)
    return True

# ================================================================
# LOGIN ACCOUNT
# ================================================================
def apri_account(account='', max_tentativi=5, attesa=0.5):
    # esegue il login completo per account specificato (5 passi)
    print("\n>>> [apri_account] avvio login per: {0}".format(account))

    if account not in ACCOUNT_CONFIG:
        print(">>> [apri_account] ERRORE: account {0} non presente in ACCOUNT_CONFIG.".format(account))
        return False

    cfg = ACCOUNT_CONFIG[account]

    # passo 1: apri il menu di selezione account
    print("  [1/5] apertura menu account...")
    if not cerca_con_tentativi("1775145932354.png", max_tentativi, attesa):
        print("  [1/5] ERRORE: menu account non trovato.")
        return False
    click(getLastMatch())
    print("  [1/5] menu account aperto OK")
    wait(0.3)

    # passo 2: seleziona account tramite schermata bentornato (coordinate fisse)
    # TODO: sostituire con ricerca immagine se si cattura lo screenshot della schermata bentornato
    print("  [2/5] selezione account {0} tramite bentornato...".format(account))
    click(Location(185, 272))
    print("  [2/5] account selezionato OK")
    wait(0.5)

    # passo 3: avvia il login tramite Google
    print("  [3/5] avvio login Google...")
    click(Location(185, 172))
    if not cerca_con_tentativi(cfg['google'], max_tentativi, attesa):
        print("  [3/5] ERRORE: pulsante Google non trovato.")
        return False
    click(getLastMatch())
    print("  [3/5] login Google avviato, attendo caricamento pagina...")
    wait(10)

    # passo 4: conferma il login (immagine uguale per tutti gli account)
    print("  [4/5] conferma login...")
    if not cerca_con_tentativi(Pattern("1775293074174.png").targetOffset(29, 36), max_tentativi, attesa):
        print("  [4/5] ERRORE: pulsante conferma non trovato.")
        return False
    click(getLastMatch())
    print("  [4/5] login confermato OK")
    wait(0.5)

    # passo 5: imposta accesso aggiuntivo
    print("  [5/5] impostazione accesso aggiuntivo...")
    if not cerca_con_tentativi(Pattern("1775148172463.png").targetOffset(-62, -1), max_tentativi, attesa):
        print("  [5/5] ERRORE: opzione accesso aggiuntivo non trovata.")
        return False
    click(getLastMatch())
    scroll_giu(volte=15, x=185, y=400, sposta_mouse=True)
    if not cerca_con_tentativi("1775148488576.png", max_tentativi, attesa):
        print("  [5/5] ERRORE: conferma accesso aggiuntivo non trovata.")
        return False
    click(getLastMatch())
    print("  [5/5] accesso aggiuntivo impostato OK")
    wait(0.5)

    print(">>> [apri_account] login {0} completato OK".format(account))
    return True

# ================================================================
# NAVIGAZIONE SEZIONI
# ================================================================
def posizionati_su_carte(attesa_iniziale=5, max_tentativi=5, attesa=0.5):
    # naviga alla sezione Carte della app
    print("  [nav] apertura sezione Carte...")
    wait(attesa_iniziale)
    if not cerca_con_tentativi("1775294025267.png", max_tentativi, attesa):
        print("  [nav] ERRORE: icona sezione Carte non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] sezione Carte aperta OK")
    wait(0.5)
    return True

def posizionati_su_attivita(max_tentativi=5, attesa=0.5):
    # naviga alla sezione Attivita della app
    print("  [nav] apertura sezione Attivita...")
    if not cerca_con_tentativi("1775217437436.png", max_tentativi, attesa):
        print("  [nav] ERRORE: icona sezione Attivita non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] sezione Attivita aperta OK")
    wait(0.5)
    return True

def posizionati_su_menuutenza(max_tentativi=5, attesa=0.5):
    # apre il menu utente dal footer della app
    print("  [nav] apertura menu utente...")
    if not cerca_con_tentativi(Pattern("1775217620164.png").targetOffset(-2, 32), max_tentativi, attesa):
        print("  [nav] ERRORE: icona menu utente non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] menu utente aperto OK")
    wait(0.5)
    return True

def posizionati_su_menuutenza_ingranaggio(max_tentativi=5, attesa=0.5):
    # apre le impostazioni tramite icona ingranaggio
    print("  [nav] apertura impostazioni ingranaggio...")
    if not cerca_con_tentativi(Pattern("1775217843520.png").targetOffset(20, 19), max_tentativi, attesa):
        print("  [nav] ERRORE: icona ingranaggio non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] impostazioni aperte OK")
    wait(0.5)
    return True

# ================================================================
# LOGOUT
# ================================================================
def esci(max_tentativi=5, attesa=0.5):
    # esegue il logout dal account corrente (4 passi di conferma)

    # passo 1: clicca sul pulsante Esci
    print("  [logout 1/4] cerco pulsante Esci...")
    if not cerca_con_tentativi("1775218288286.png", max_tentativi, attesa):
        print("  [logout 1/4] ERRORE: pulsante Esci non trovato.")
        return False
    click(getLastMatch())
    print("  [logout 1/4] pulsante Esci cliccato OK")
    wait(0.5)

    # scroll senza mouseMove — evita "Mouse not useable (blocked)"
    scroll_giu(volte=35, x=185, y=400, sposta_mouse=False)

    # passo 2: prima conferma logout
    print("  [logout 2/4] prima conferma logout...")
    if not cerca_con_tentativi(Pattern("1775217958402.png").targetOffset(-141, 45), max_tentativi, attesa):
        print("  [logout 2/4] ERRORE: prima conferma non trovata.")
        return False
    click(getLastMatch())
    print("  [logout 2/4] prima conferma OK")
    wait(0.5)

    # passo 3: seconda conferma logout
    print("  [logout 3/4] seconda conferma logout...")
    if not cerca_con_tentativi(Pattern("1775218411391.png").targetOffset(111, 51), max_tentativi, attesa):
        print("  [logout 3/4] ERRORE: seconda conferma non trovata.")
        return False
    click(getLastMatch())
    print("  [logout 3/4] logout completato OK")
    wait(0.5)

    # passo 4: chiudi app WeWard
    print("  [logout 4/4] chiudi app WeWard...")
    if not cerca_con_tentativi(Pattern("1775296520334.png").targetOffset(14, -2), max_tentativi, attesa):
        print("  [logout 4/4] ERRORE: chiudi app non trovata.")
        return False
    click(getLastMatch())
    print("  [logout 4/4] app chiusa OK")
    wait(0.5)

    return True

def esci_weward(max_tentativi=5, attesa=0.5):
    # sequenza completa di logout da WeWard
    print(">>> [esci_weward] avvio sequenza logout...")
    ok = True
    ok = posizionati_su_attivita(max_tentativi, attesa) and ok
    ok = posizionati_su_menuutenza(max_tentativi, attesa) and ok
    ok = posizionati_su_menuutenza_ingranaggio(max_tentativi, attesa) and ok
    ok = esci(max_tentativi, attesa) and ok
    if ok:
        print(">>> [esci_weward] logout completato OK")
    else:
        print(">>> [esci_weward] ATTENZIONE: logout completato con errori.")
    return ok

# ================================================================
# CONTROLLO CARTE
# ================================================================
def controlla_carte(max_tentativi=5, attesa=0.5):
    """
    Ritorna:
      True  -> ci sono carte da raccogliere
      False -> nessuna carta disponibile
      None  -> errore tecnico (lista non trovata)
    """
    print("  [controlla_carte] cerco lista carte...")
    if not cerca_con_tentativi("1775384530118.png", max_tentativi, attesa):
        print("  [controlla_carte] ERRORE: lista carte non trovata.")
        return None
    click(getLastMatch())
    wait(0.5)

    print("  [controlla_carte] verifico carte disponibili...")
    nessuna = cerca_con_tentativi(Pattern("1775384584244.png").similar(0.91), 2, attesa)
    wait(0.5)

    print("  [controlla_carte] torno indietro...")
    if cerca_con_tentativi("1775385203175.png", max_tentativi, attesa):
        click(getLastMatch())
        print("  [controlla_carte] indietro OK")

    if nessuna:
        print("  [controlla_carte] nessuna carta disponibile.")
        return False

    print("  [controlla_carte] carte da raccogliere: SI")
    return True

# ================================================================
# RACCOLTA CARTE
# NOTA: questa cartella deve contenere anche i seguenti file PNG
#       copiati da raccogli_sette_carte_no_google.sikuli:
#         - angolo.png
#         - carta_apri.png
#         - carta_chiudi.png
#         - 1775501853376.png
# ================================================================
def cerca_angolo_piu_vicino():
    matches = list(findAll(Pattern("angolo.png").similar(0.80)))
    if not matches:
        print("Nessuna occorrenza di angolo trovata.")
        return None

    print("Trovate %d occorrenze di angolo." % len(matches))
    mouse = Env.getMouseLocation()
    piu_vicino = min(
        matches,
        key=lambda m: distanza(m.getCenter().x, m.getCenter().y, mouse.x, mouse.y)
    )
    centro = piu_vicino.getCenter()
    print("Scelto il piu vicino: (%d, %d)  distanza: %.1f px" % (
          centro.x, centro.y,
          distanza(centro.x, centro.y, mouse.x, mouse.y)))
    return piu_vicino

def gestisci_carta():
    if cerca_con_tentativi("carta_apri.png", 3, 0.5):
        click(getLastMatch())
        wait(0.5)
    if cerca_con_tentativi("carta_chiudi.png", 3, 0.5):
        click(getLastMatch())
        wait(0.5)
    if cerca_con_tentativi("1775501853376.png", 3, 0.5):
        click(getLastMatch())
        wait(0.5)

def raccogli_carte(max_tentativi=10, attesa=4):
    print("==> Cerco puntoblu...")
    if cerca_con_tentativi("1775501853376.png", 3, 0.5):
        click(getLastMatch())
        wait(0.5)

    cliccato = False

    for tentativo in range(1, max_tentativi + 1):
        print("--- Tentativo %d di %d ---" % (tentativo, max_tentativi))

        match = cerca_angolo_piu_vicino()
        if match is None:
            if tentativo < max_tentativi:
                print("Attendo %ds..." % attesa)
                wait(attesa)
            continue

        centro = match.getCenter()
        c = _robot.getPixelColor(centro.x, centro.y)
        trovato = (c.getRed(), c.getGreen(), c.getBlue())
        print("Pixel R:%d G:%d B:%d HEX:#%02x%02x%02x" % (
              trovato[0], trovato[1], trovato[2],
              trovato[0], trovato[1], trovato[2]))

        if colore_vicino(trovato, TARGET):
            print("Colore OK -> clicco!")
            click(Location(centro.x, centro.y))
            cliccato = True
            wait(0.5)
            gestisci_carta()
        else:
            print("Colore non corrisponde.")
            if tentativo < max_tentativi:
                print("Attendo %ds..." % attesa)
                wait(attesa)

    if cliccato:
        print("==> Completato con successo.")
    else:
        print("==> Terminati i tentativi senza click.")

    return cliccato

# ================================================================
# ESECUZIONE TUTTI GLI ACCOUNT
# ================================================================
def esegui_tutti(max_tentativi=5, attesa=0.5):
    # esegue login, raccolta carte e logout per ogni account in ACCOUNT_CONFIG
    print("\n==============================")
    print("AVVIO CICLO SU TUTTI GLI ACCOUNT")
    print("==============================")
    risultati = []
    for account in ACCOUNT_CONFIG:
        wait(1.5)
        if not apri_weward(max_tentativi, attesa):
            print("ERRORE: impossibile aprire WeWard, script interrotto.")
            return
        print("\n------------------------------")
        ok = apri_account(account, max_tentativi, attesa)
        if ok:
            if posizionati_su_carte(attesa_iniziale=5, max_tentativi=max_tentativi, attesa=attesa):
                stato = controlla_carte(max_tentativi, attesa)
                if stato is True:
                    raccogli_carte()
                elif stato is False:
                    print("  nessuna carta da raccogliere, passo al prossimo account.")
                else:
                    print("  ERRORE verifica carte, passo al prossimo account.")
        else:
            print("  account {0} saltato per errore login.".format(account))
        esci_weward(max_tentativi, attesa)
        risultati.append((account, 'OK' if ok else 'FAIL'))
    print("\n==============================")
    print("RIEPILOGO FINALE")
    print("==============================")
    for acc, esito in risultati:
        print("  {0}  {1}".format(esito, acc))

# ================================================================
# ESECUZIONE SINGOLO ACCOUNT
# ================================================================
def esegui_uno(account, max_tentativi=5, attesa=0.5):
    # esegue login, raccolta carte e logout per un singolo account
    print("\n==============================")
    print("AVVIO ACCOUNT: {0}".format(account))
    print("==============================")

    if not apri_weward(max_tentativi, attesa):
        print("ERRORE: impossibile aprire WeWard, script interrotto.")
        return

    ok = apri_account(account, max_tentativi, attesa)
    if ok:
        if posizionati_su_carte(attesa_iniziale=5, max_tentativi=max_tentativi, attesa=attesa):
            stato = controlla_carte(max_tentativi, attesa)
            if stato is True:
                raccogli_carte()
            elif stato is False:
                print("  nessuna carta da raccogliere.")
            else:
                print("  ERRORE verifica carte.")
    esci_weward(max_tentativi, attesa)

    print("\n==============================")
    print("RIEPILOGO: {0}  {1}".format('OK' if ok else 'FAIL', account))
    print("==============================")

# ================================================================
# AVVIO SCRIPT
# ================================================================
# esegui_uno('berros7426', 5, 0.5)
esegui_tutti(max_tentativi=5, attesa=0.5)
