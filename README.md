# odoo-partner-agent

Skeleton structure for an Odoo partner agent project with a Streamlit UI and modular agents.

## Structure

- app.py - Streamlit UI
- orchestrator.py - Orchestrator / brain
- agents/
  - environment_agent.py
  - database_agent.py
  - core_apps_agent.py
- workspace/ - Auto-created workspace directory

## Setup Instructions

### 1. Create GitHub OAuth App

To integrate GitHub authentication, you need to create a GitHub OAuth App:

#### Step-by-Step Guide:

1. **Navigate to GitHub Developer Settings:**
   - Go to [GitHub.com](https://github.com)
   - Click on your profile picture (top right) → **Settings**
   - Scroll down to **Developer settings** (bottom of left sidebar)
   - Click **OAuth Apps** → **New OAuth App**

2. **Fill in the OAuth App Details:**
   - **Application name:** `Odoo Partner Agent` (or your preferred name)
   - **Homepage URL:** `http://localhost:8069` (for local development)
   - **Authorization callback URL:** `http://localhost:8069/auth/callback`
   - **Application description:** (Optional) "Autonomous Odoo Partner Agent"

3. **Register the Application:**
   - Click **Register application**

4. **Get Your Credentials:**
   - After registration, you'll see your **Client ID** (starts with `Iv1.`)
   - Click **Generate a new client secret** to get your **Client Secret**
   - **⚠️ Important:** Copy the Client Secret immediately - you won't be able to see it again!

5. **Configure Your Application:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your credentials:
     ```
     GITHUB_CLIENT_ID=Iv1.your-actual-client-id
     GITHUB_CLIENT_SECRET=your-actual-client-secret
     ```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

### Configuration Options

The `.env` file supports the following configuration options:

- **GitHub OAuth:**
  - `GITHUB_CLIENT_ID` - Your GitHub OAuth App Client ID (required)
  - `GITHUB_CLIENT_SECRET` - Your GitHub OAuth App Client Secret (required)

- **PostgreSQL:**
  - `POSTGRES_USER` - PostgreSQL superuser (default: postgres)
  - `POSTGRES_PASSWORD` - PostgreSQL password (default: postgres)
  - `POSTGRES_HOST` - Database host (default: localhost)
  - `POSTGRES_PORT` - Database port (default: 5432)

- **Odoo:**
  - `ODOO_DB_NAME` - Database name (default: odoo_db)
  - `ODOO_DB_USER` - Odoo database user (default: odoo_agent)
  - `ODOO_DB_PASSWORD` - Odoo database password (default: agent123)
  - `ODOO_ADMIN_PASSWORD` - Odoo admin password (default: admin123)

## Security Notes

- **Never commit your `.env` file** - it contains sensitive credentials
- The `.env` file is already listed in `.gitignore`
- Keep your Client Secret secure and rotate it if exposed
- For production, use environment variables or a secure secrets manager

## Next steps

- Implement the UI in app.py
- Flesh out each agent in agents/
- Add actual dependencies to requirements.txt
