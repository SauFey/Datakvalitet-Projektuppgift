# Projektuppgift - Bank-projekt -- Automatiserat Datakvalitetsflöde 

Detta projektuppgift heter "Bank Project" och handlar om att vi ska göra transaktioner och rollbacks vid fel, validera, analysera och importera data i en databas, logga tester och kvalitetssäkra på ett automatiserat sätt.

## 📖 Projektbeskrivning
Detta projekt implementerar ett **automatiserat workflow** för att:
- Ta emot dagliga transaktionsfiler (CSV).
- Validera och analysera datan (saknade värden, IBAN, felaktiga datum etc.).
- Ladda in validerad data i en **PostgreSQL-databas**.
- Använda **rollback** vid fel för att säkerställa datakvalitet.
- Hantera databasversioner med **Alembic**.
- Automatisera hela flödet med **Prefect**.
- Testa funktioner med **pytest**.

Verktyg för projektet:
- Python > För ETL, validering och logik
- PostgreSQL > Relationsdatabas för kunder, konton, transaktioner
- SQLAlchemy + Alembic > Databasmodellering och migrationer
- Jupyter Notebook > Dataanalys och rapporter
- Pytest > För testning
- Prefect > Workflow-automatisering
- Git > Versionshantering


Projektet är versionerat i GitHub och följer en tydlig mappstruktur för enkel vidareutveckling.
