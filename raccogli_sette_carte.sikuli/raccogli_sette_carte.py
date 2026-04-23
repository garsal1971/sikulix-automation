import time
import sys
import math
sys.path.append(getBundlePath())   # trova i moduli nella stessa cartella .sikuli
from sikuli import *   # <-- aggiunge tutte le funzioni SikuliX al modulo
import java.awt.Robot as Robot
import java.awt.event.InputEvent as InputEvent

_robot = Robot()
TARGET = (14, 129, 115)
# lancia tutto



# ================================================================
# CONFIGURAZIONE ACCOUNTcerca_con_tentativi
# ================================================================
ACCOUNT_CONFIG = {
    'garsal1971': {
        'google':   "1775290644794.png"
    },
    'adagarofalobognanni': {
        'google':   "1775145979844.png"
    },
    'berros1974': {
        'google':   "1775217119680.png"
    },
     'gmx.salgar71': {
         'google':   "1775236822745.png"
     },
     'berros7426': {
         'google':   "1775237806527.png"
     }
    # aggiungi altri account qui sotto
}


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
def cerca_con_tentativi(immagine, max_tentativi=5, attesa=0.5):
    for t in range(1, max_tentativi + 1):
        if exists(immagine):
            return True
        print("    tentativo {0}/{1} fallito per [{2}], attendo {3}s...".format(
              t, max_tentativi, immagine, attesa))
        wait(attesa)
    print("  ERRORE: [{0}] non trovata dopo {1} tentativi.".format(immagine, max_tentativi))
    return False
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

# passo 2: seleziona account tramite schermata bentornato (uguale per tutti)
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
    if not cerca_con_tentativi(Pattern("1775293074174.png").targetOffset(29,36), max_tentativi, attesa):
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
    wheel(WHEEL_DOWN, 15)
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
def posizionati_su_carte():
    # naviga alla sezione Carte della app
    print("  [nav] apertura sezione Carte...")
    wait(5)
    if not cerca_con_tentativi("1775294025267.png", 5, 0.5):
        print("  [nav] ERRORE: icona sezione Carte non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] sezione Carte aperta OK")
    wait(0.5)
    return True

def posizionati_su_attivita():
    # naviga alla sezione Attivita della app
    print("  [nav] apertura sezione Attivita...")
    if not cerca_con_tentativi("1775217437436.png", 5, 0.5):
        print("  [nav] ERRORE: icona sezione Attivita non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] sezione Attivita aperta OK")
    wait(0.5)
    return True

def posizionati_su_menuutenza():
    # apre il menu utente dal footer della app
    print("  [nav] apertura menu utente...")
    if not cerca_con_tentativi(Pattern("1775217620164.png").targetOffset(-2, 32), 5, 0.5):
        print("  [nav] ERRORE: icona menu utente non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] menu utente aperto OK")
    wait(0.5)
    return True

def posizionati_su_menuutenza_ingranaggio():
    # apre le impostazioni tramite icona ingranaggio
    print("  [nav] apertura impostazioni ingranaggio...")
    if not cerca_con_tentativi(Pattern("1775217843520.png").targetOffset(20, 19), 5, 0.5):
        print("  [nav] ERRORE: icona ingranaggio non trovata.")
        return False
    click(getLastMatch())
    print("  [nav] impostazioni aperte OK")
    wait(0.5)
    return True

# ================================================================
# LOGOUT
# ================================================================
def esci():
    # esegue il logout dal account corrente (3 passi di conferma)

    # passo 1: clicca sul pulsante Esci
    print("  [logout 1/3] cerco pulsante Esci...")
    if not cerca_con_tentativi("1775218288286.png", 5, 0.5):
        print("  [logout 1/3] ERRORE: pulsante Esci non trovato.")
        return False
    click(getLastMatch())
    print("  [logout 1/3] pulsante Esci cliccato OK")
    wait(0.5)
    wheel(WHEEL_DOWN, 35)

    # passo 2: prima conferma logout
    print("  [logout 2/3] prima conferma logout...")
    if not cerca_con_tentativi(Pattern("1775217958402.png").targetOffset(-141, 45), 5, 0.5):
        print("  [logout 2/3] ERRORE: prima conferma non trovata.")
        return False
    click(getLastMatch())
    print("  [logout 2/3] prima conferma OK")
    wait(0.5)

    # passo 3: seconda conferma logout
    print("  [logout 3/3] seconda conferma logout...")
    if not cerca_con_tentativi(Pattern("1775218411391.png").targetOffset(111, 51), 5, 0.5):
        print("  [logout 3/3] ERRORE: seconda conferma non trovata.")
        return False
    click(getLastMatch())
    print("  [logout 3/3] logout completato OK")
    wait(0.5)

    # passo 4: chiudi aoo
    print("  [logout 4/4] chiudi app...")
    if not cerca_con_tentativi(Pattern("1775296520334.png").targetOffset(14,-2), 5, 0.5):
        print("  [logout 4/4] chiudi app..")
        return False
    click(getLastMatch())
    print("  [logout 4/4] logout completato OK")
    wait(0.5)
    
    return True

def esci_weward():
    # sequenza completa di logout da WeWard
    print(">>> [esci_weward] avvio sequenza logout...")
    posizionati_su_attivita()
    posizionati_su_menuutenza()
    posizionati_su_menuutenza_ingranaggio()
    esci()
    print(">>> [esci_weward] logout completato OK")

# ================================================================
# RACCOLTA CARTE
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



def raccogli_carte(max_tentativi=10, attesa=4):
    print("==> Cerco puntoblu...")
    doubleClick("1776370021625.png")    
    wait(0.5)
    doubleClick("1776370021625.png")
    wait(0.5)
    doubleClick("1776370021625.png")
    wait(0.5)   

    tentativo = 0
    prese = 0
    while prese < 7 and tentativo < max_tentativi:
        print("--- Tentativo %d di %d ---" % (tentativo, max_tentativi))

        if exists(Pattern("1776442897675.png").similar(0.90)):
            print("esiste carta clicco")
            click(Pattern("1776442897675.png").similar(0.90))

            if exists("1776443662760.png"):
                print("esiste carta da aprire")
                click("1776443662760.png")
                if exists("1776443756642.png"):
                     print("esiste chiudo carta presa")
                     click("1776443756642.png")
                     prese = prese + 1
        tentativo = tentativo + 1
    print("prese " + str(prese) + " - tentativo " + str(tentativo))
    return 

# ================================================================
# ESECUZIONE TUTTI GLI ACCOUNT
# ================================================================
def esegui_tutti(max_tentativi=5, attesa=0.5):
    # esegue login, raccolta carte e logout per ogni account in ACCOUNT_CONFIG
    print("\n==============================")
    print("AVVIO CICLO SU TUTTI GLI ACCOUNT")
    print("==============================")
    risultati = {}
    for account in ACCOUNT_CONFIG:
        wait(1.5)
        if not apri_weward(max_tentativi, attesa):
            print("ERRORE: impossibile aprire WeWard, script interrotto.")
            return
        print("\n------------------------------")
        ok = apri_account(account, max_tentativi, attesa)
        risultati[account] = 'OK' if ok else 'FAIL'
        if ok:
            posizionati_su_carte()
            if  controlla_carte():
                raccogli_carte(max_tentativi=21)
            else:
                print("  nessuna carta da raccogliere, passo al prossimo account.") 
            esci_weward()
        else:
            print("  account {0} saltato per errore login.".format(account))
    print("\n==============================")
    print("RIEPILOGO FINALE")
    print("==============================")
    for acc, esito in risultati.items():
        print("  {0}  {1}".format(esito, acc))
    return
# ================================================================
# ESECUZIONE SINGOLO ACCOUNT
# ================================================================

def controlla_carte():
    # controlla se ci sono carte disponibili da raccogliere
    flagexit = True

    # passo 1: cerca lista carte
    print("  [controlla_carte] cerco lista carte...")
    if not cerca_con_tentativi("1775384530118.png", 5, 0.5):
        print("  [controlla_carte] lista carte non trovata.")
        return False       # esce subito dalla funzione
    click(getLastMatch())  # clicca solo se trovata
    wait(0.5)

    # passo 2: verifica se ci sono carte disponibili
    print("  [controlla_carte] verifico carte disponibili...")
    if cerca_con_tentativi(Pattern("1775384584244.png").similar(0.91), 2, 0.5):
        print("  [controlla_carte] nessuna carta disponibile.")
        flagexit = False
    wait(0.5)

    # passo 3: torna indietro
    print("  [controlla_carte] torno indietro...".format(flagexit))
    if cerca_con_tentativi("1775385203175.png", 5, 0.5):
        click(getLastMatch())
        print("  [controlla_carte] indietro OK".format(flagexit))

    print("  [controlla_carte] carte da raccogliere: {0}".format(str(flagexit)))
    return flagexit
# ================================================================
# AVVIO SCRIPT
# ================================================================
# esegui_uno('berros7426', 5, 0.5)
esegui_tutti(max_tentativi=15, attesa=0.5)
#raccogli_carte(max_tentativi=15)