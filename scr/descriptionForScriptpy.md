### **Implementering av Dynamisk DNS med Domeneshop API**
For å sette opp dynamisk DNS med Domeneshop sitt API for å automatisk oppdatere DNS-registreringer når IP-adressen endrer seg, har jeg laget (implementert) et Python-script som kjører på vår VM i Azure. Dette scriptet vil overvåke IP-adressene til de tilkoblede RPi-enhetene og oppdatere DNS-oppføringene på Domeneshop for å peke til de riktige IP-adressene.

**Oppdatering av DNS-oppføringer for RPi-enheter**
Programmet vil bruke Domeneshop API til å oppdatere A-oppføringer (søk opp selv) for hver RPi med unike subdomener som rpi1.codexenmo.no, rpi2.codexenmo.no etc.

Koden er designet for å oppdatere DNS-oppføringer på Domeneshop for subdomener av hoveddomenet codexenmo.no, slik at hvert subdomene (f.eks.: tri.codexenmo.no tri2.codexenmo.no, rpi1.codexenmo.no) peker til en spesifikk IP-adresse. Dette er gunstig når man bruker flere enheter av Raspberry Pi-er og ønsker å tildele dem hver sin unike adresse (IP) på internett, slik at de kan nås via subdomener.

**Autentisering**
Koden bruker Domeneshop sitt API for å autentisere forespørsler med en API-token og secret (API_TOKEN og API_SECRET).

**Dynamisk DNS-oppdatering**
update_dns_record-funksjonen sender en POST-forespørsel til Domeneshop API for å opprette eller oppdatere DNS A-oppføringer. Hvert subdomene får sin egen IP-adresse oppdatert i DNS, slik at rpi1.codexenmo.no kan peke til IP-adressen 192.168.1.101 og rpi2.codexenmo.no til 192.168.1.102, eller til hvilke IP-er som er satt. IP-adressene over er kun eksempler.

**Eksempel-enhetskonfigurasjon**
I koden er det definert en ordbok devices som inneholder subdomener (rpi1, rpi2) og deres tilhørende IP-adresser. Når koden kjører, itererer den over denne ordboken og kaller update_dns_record-funksjonen for hver oppføring.

**Til senere?!?!?!: Tilpasning til Dynamisk Miljø**
Hvis Raspberry Pi-enhetene er på et nettverk med dynamiske IP-er, kan dette skriptet kjøres jevnlig (f.eks. ved hjelp av en cron-jobb) for å sikre at DNS-oppføringene alltid peker til de riktige IP-adressene.


### **Dynamisk DNS-oppdatering (DDNS) med update_ddns**
Denne funksjonen (update_ddns) bruker en enkel GET-forespørsel til et spesifikt DDNS-endepunkt for å oppdatere IP-adressen til et subdomene. Dette er en enklere metode for dynamiske DNS-tjenester, og den støtter kun oppdatering – ikke oppretting – av en DNS-oppføring. Funksjonen er enkel og rask, men er begrenset i funksjonalitet. Hvis DNS-oppføringen ikke eksisterer, vil denne metoden ikke opprette den.

Prosessen i update_ddns er:

Den bygger en URL med autentisering, subdomene og valgfri IP-adresse.
Den sender en GET-forespørsel til Domeneshops dynamiske DNS-endepunkt.
Den returnerer en suksessmelding hvis oppdateringen var vellykket, eller en feilmelding hvis den mislyktes.

### **Full DNS-administrasjon med PUT og POST**
Denne delen gir full fleksibilitet til å både oppdatere eksisterende oppføringer (med PUT) og opprette nye oppføringer (med POST). Her brukes Domeneshops generelle API-endepunkt for DNS-administrasjon, og autentisering skjer med HTTPBasicAuth.

Denne metoden er mer kompleks, men også kraftigere og bedre egnet for å håndtere situasjoner hvor DNS-oppføringen kanskje ikke finnes fra før:

Hvis en oppføring allerede finnes: Koden sender en PUT-forespørsel for å oppdatere IP-adressen.
Hvis oppføringen ikke finnes: Den sender en POST-forespørsel for å opprette en ny oppføring med det spesifiserte subdomene og IP-adresse.
Prosessen her er:

Den sjekker om oppføringen allerede eksisterer med get_existing_record-funksjonen (del 3).
Basert på resultatet:
Oppdaterer oppføringen med PUT hvis den finnes.
Oppretter en ny oppføring med POST hvis den ikke finnes.