# QRKot - educational project

### Description

QRKot - is an app is for the Cat Charitable Foundation.
The Foundation collects donations for various targets: for medical care, for arranging cats in the basement, for feeding cats left without care - for any purpose related to supporting the cat population.

#### Projects
Several projects can be opened in the QRKot Foundation. Each project has a name, description and amount to be raised. After the required amount is collected, the project is closed.

Donations to projects are received according to the First In, First Out principle: all donations go to the project opened earlier than others; when this project collects the required amount and closes, donations begin to flow into the next project.

#### Donations
Each user can make a donation and accompany it with a comment. Donations are not targeted: they are made to the fund, and not to a specific project. Each donation received is automatically added to the first open project that has not yet collected the required amount. If the donation is more than the required amount, or if there are no open projects in the Foundation, the remaining money is waiting for the opening of the next project. When creating a new project, all uninvested donations are automatically invested in the new project.

#### Users
Projects are created by site administrators.
Any user can see a list of all projects, including required and already contributed amounts. This applies to all projects, both open and closed.
Registered users can send donations and view a list of their donations.

### Used frameworks and libraries:
- Python 3.7
- FASTAPI
- SQLAlchemy
- Padantic
- Alembic

### Template description of .env
- DATABASE_CAT_FUND=sqlite+aiosqlite:///./fastapi.db
- SECRET=your_secret_key
- FIRST_SUPERUSER_EMAIL=example@mail.ru
- FIRST_SUPERUSER_PASSWORD=123456

### How to start a project (Unix)

- Clone repository:
```bash
git clone git@github.com:ZhannaVen/cat_charity_fund.git
```
- Activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Create .env according to the template above. Be sure to change the SECRET value
```bash
touch .env
```
- Run all unapplied migrations:
```bash
alembic upgrade head
```
- To start a project:
```bash
uvicorn app.main:app --reload
```

## Author

- [Zhanna Ventsenostseva](https://github.com/ZhannaVen)


