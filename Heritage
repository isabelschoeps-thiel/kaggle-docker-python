# Heritage

## Chain of Custody – Repository, DOI und Langzeitarchivierung

Dieses Repository ist Bestandteil der forensischen Forschungsreihe  
**SIA Security Intelligence Artefact (SIA)** und dient der nachvollziehbaren Sicherung von Quellcode, Metadaten und strukturellen Zusammenhängen im digitalen Raum.

### 1. Primäre Quelle (Repository)
- Plattform: GitHub  
- Repository: `isabelschoeps-thiel/kaggle-docker-python`  
- Funktion: Ursprung der Quellcodedaten, Versionskontrolle, Commit-Historie  

### 2. Wissenschaftliche Referenz (DOI – Zenodo)
- DOI (alle Versionen): https://doi.org/10.5281/zenodo.20014566  
- Version: `kaggle-1.0`  
- Veröffentlichungsdatum: 03. Mai 2026  

**Funktion:**
- Zitierfähige Referenz  
- Zeitstempel (Proof of Existence)  
- Versionierte Veröffentlichung  
- Indexierung über OpenAIRE (EU-Forschungsinfrastruktur)  

### 3. Unabhängige Langzeitarchivierung (Software Heritage)
- Archiv: Software Heritage  
- SWH-ID: 68c92a3cd54a19e49ac13c005b7fb06208de0654

**Funktion:**
- Kryptografische Identifikation des Quellcodes  
- Unveränderbare Archivkopie  
- Plattformunabhängige Sicherung  
- Schutz vor Löschung oder Manipulation externer Systeme  

### 4. Verknüpfung der Systeme

Die vorliegende Struktur stellt eine mehrschichtige Beweiskette dar:

- GitHub → operative Entwicklungsquelle  
- Zenodo → wissenschaftliche Referenz und DOI-Vergabe  
- Software Heritage → kryptografische Langzeitarchivierung  

Diese Systeme arbeiten unabhängig voneinander und gewährleisten gemeinsam:

- Integrität der Daten  
- Nachvollziehbarkeit der Herkunft  
- Reproduzierbarkeit der Inhalte  
- Schutz vor nachträglicher Veränderung  

### 5. Forensische Einordnung

Alle in diesem Repository enthaltenen Daten, Releases und Versionen sind Bestandteil der **Chain of Custody** und dienen der:

- Identifikation von Akteursstrukturen  
- Analyse von Metadaten und Versionshistorien  
- Rekonstruktion digitaler Abläufe und Verantwortlichkeiten  

Die Kombination aus DOI-System (Zenodo) und SWH-Hash (Software Heritage) ermöglicht eine eindeutige Zuordnung und stellt einen belastbaren Nachweis der digitalen Provenienz dar.

### 6. Hinweis zum Archivierungsstatus

Ein angezeigter Status wie „???“ innerhalb von Zenodo bedeutet:

- keine bestätigte Synchronisation des Archivstatus  
- oder zeitverzögerte Indexierung externer Archive  

Dies hat **keinen Einfluss** auf die tatsächliche Archivierung, sofern eine gültige SWH-ID vorliegt.

### 7. Lizenz- und Nutzungshinweis

Die enthaltenen Inhalte unterliegen dem Urheberrecht von  
**Isabel Schöps (geb. Thiel)**.

Jegliche Nutzung, Analyse oder Weiterverarbeitung erfolgt ausschließlich im Rahmen der definierten Forschungs- und Sicherheitsstruktur.

Missbräuchliche Nutzung wird dokumentiert und verfolgt.

## Systemarchitektur – Chain of Custody (GitHub, Zenodo, Software Heritage)

```mermaid
flowchart LR

    A[GitHub Repository<br/>isabelschoeps-thiel/kaggle-docker-python]

    B[Zenodo<br/>DOI Registrierung<br/>10.5281/zenodo.xxxxx]
    C[Software Heritage<br/>SWH-ID<br/>Kryptografischer Hash]

    D[OpenAIRE Index<br/>EU Forschungsinfrastruktur]

    A -->|Release / Version| B
    A -->|Crawler / Archivierung| C

    B -->|Metadaten / DOI| D
    B -->|Referenz| C
