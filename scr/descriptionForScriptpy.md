For å sette opp dynamisk DNS med Domeneshop sitt API for å automatisk oppdatere DNS-registreringer når IP-adressen endrer seg, 
har jeg laget (implementert) et python-script som kjører på vårres VM i Azure. 
Dette scriptet vil overvåke IP-adressene til de tilkoblede RPi-enhetene og oppdatere DNS-oppføringene på Domeneshop for å peke til de riktige IP-adressene.

programmet vil bruke Domeneshop API til å oppdatere A-oppføringer (søk opp selv) for hver RPi med unike subdomener som rpi1.codexenmo.no, rpi2.codexenmo.no etc.

Koden er designet for å oppdatere DNS-oppføringer på Domeneshop for subdomener av hoveddomenet codexenmo.no, 
slik at hvert subdomene (ex: rpi1.codexenmo.no, rpi2.codexenmo.no) peker til en spesifikk IP-adresse. 
gunstig når man bruker flere enheter av RPier, og ønsker å tildele dem hver sin unike adresse (IP) på internett, slik at de kan nås via subdomener.

Autentisering: Koden bruker Domeneshop sitt API for å autentisere forespørsler med en API-token og secret (API_TOKEN og API_SECRET).

Dynamisk DNS-oppdatering: update_dns_record-funksjonen sender en POST-forespørsel til Domeneshop API for å opprette eller oppdatere DNS A-oppføringer.
Hvert subdomene får sin egen IP-adresse oppdatert i DNS, slik at rpi1.codexenmo.no kan peke til IP-adressen 192.168.1.101 og rpi2.codexenmo.no til 192.168.1.102, eller til hvilke IP-er som er satt. IP over er bare eksempler

Eksempel-enhetskonfigurasjon: I koden er det definert en ordbok devices som inneholder subdomener (rpi1, rpi2) og deres tilhørende IP-adresser. Når koden kjører, itererer den over denne ordboken og kaller update_dns_record-funksjonen for hver oppføring.

Til senere?!?!?!: Tilpasning til Dynamisk Miljø: Hvis Raspberry Pi-enhetene er på et nettverk med dynamiske IP-er, kan dette skriptet kjøres jevnlig (f.eks. ved hjelp av en cron-jobb) for å sikre at DNS-oppføringene alltid peker til de riktige IP-adressene.