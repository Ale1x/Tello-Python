# Controllo di Swarm di Drone Tello

Questo repository contiene script Python per il controllo di uno swarm di droni Tello utilizzando la libreria `djitellopy`. Lo swarm è sincronizzato per eseguire un volo coordinato.
Sono presenti due file:
1. il File `swarmThread.py` prevede due Thread ognuno che governa uno Swarm
2. Il file `swarmUnico.py` prevede un singolo swarm.

## Prerequisiti

Assicurati di avere installato quanto segue:

- Python 3.x
- La libreria `djitellopy`

Puoi installare le librerie richieste usando:

```bash
pip install djitellopy
```