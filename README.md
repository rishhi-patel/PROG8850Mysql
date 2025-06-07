# PROG8850 - Assignment 2

**Automating Database Schema Changes and Implementing CI/CD for Database Deployment**
Total: 20 Points

---

## 🔹 Project Structure

```
├── create_projects.sql
├── execute_sql.py
├── add_departments.sql
├── run_add_departments.py
├── requirements.txt
└── .github
    └── workflows
        └── ci_cd_pipeline.yml
```

---

## 🔹 Question 1: Automating Database Schema Changes

### Files:

- `create_projects.sql` → Creates `projects` table.
- `execute_sql.py` → Runs `create_projects.sql` and adds `budget` column if it does not exist.

### How to run locally:

1️⃣ Set environment variables in `.env`:

```env
DB_HOST=your-server.mysql.database.azure.com
DB_USER=your-admin-user@your-server
DB_PASSWORD=your-password
DB_NAME=companydb
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Run:

```bash
python execute_sql.py
```

---

## 🔹 Question 2: CI/CD Pipeline for Database Deployment

### Files:

- `.github/workflows/ci_cd_pipeline.yml` → GitHub Actions workflow triggered on push to `main`.
- `add_departments.sql` → Creates `departments` table.
- `run_add_departments.py` → Script executed in GitHub Actions.

---

## 🔹 GitHub Actions Environment Variables (Secrets)

The following secrets are configured in GitHub:

| Secret Name   | Value                                |
| ------------- | ------------------------------------ |
| `DB_HOST`     | your-server.mysql.database.azure.com |
| `DB_USER`     | your-admin-user@your-server          |
| `DB_PASSWORD` | your-password                        |

---

## 🔹 Azure MySQL Configuration

✅ **Server:** Azure Database for MySQL Flexible Server
✅ **Database:** `companydb`
✅ **Networking:**

- ✅ Public access: **Enabled**
- ✅ Public access from Azure services: **Enabled**
- ✅ Local IP added to Firewall Rules

_Screenshot of Networking settings included in Documentation.pdf._

---

## 🔹 GitHub Actions Testing

- ✅ Pipeline triggers on push to `main`
- ✅ Runs `run_add_departments.py`
- ✅ Executes `add_departments.sql`
- ✅ Successful connection to Azure MySQL
- ✅ Successful pipeline run screenshot included in Documentation.pdf

---

## 🔹 How to run the pipeline:

```bash
git add .
git commit -m "Final - added pipeline for Assignment 2"
git push origin main
```
## 🔹 Screenshot:
![image](https://github.com/user-attachments/assets/a320ced3-bba8-422f-96af-189237c05dc1)

