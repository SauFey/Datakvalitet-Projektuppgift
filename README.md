# Bank Project - ETL och Analys - Automatiserat datakvalitetsflöde
### Individuellt arbete av SauFey

#### 📖 Projektbeskrivning
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

Utelämnade uppgifter:
- SCRUM
