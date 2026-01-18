# Quick Reference: GitHub OAuth Configuration

## What You Need

### Client ID Format:
```
Iv1.[alphanumeric characters]
```
Example: `Iv1.1234567890abcdef`

### Client Secret Format:
```
ghp_[alphanumeric characters]
```
or other GitHub token format

Example: `ghp_1234567890abcdefghijklmnopqrstuvwxyz`

## How to Use

1. **Get credentials from GitHub:**
   - Go to: https://github.com/settings/developers
   - Click "OAuth Apps" → "New OAuth App"
   - Fill in the form (see GITHUB_OAUTH_SETUP.md for details)
   - Copy your Client ID (visible immediately)
   - Generate and copy your Client Secret (shown only once!)

2. **Configure your application:**
   ```bash
   cp .env.example .env
   ```
   
3. **Edit `.env` file:**
   ```
   GITHUB_CLIENT_ID=Iv1.your-actual-client-id
   GITHUB_CLIENT_SECRET=your-actual-client-secret
   ```

4. **Run the application:**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

## OAuth App Settings for Local Development

| Setting | Value |
|---------|-------|
| Application name | Odoo Partner Agent |
| Homepage URL | http://localhost:8069 |
| Callback URL | http://localhost:8069/auth/callback |

## Common Issues

### "GitHub OAuth is not configured" warning
- Check that `.env` file exists in project root
- Verify credentials are correctly formatted
- Remove quotes around values
- Restart the application

### Lost your Client Secret?
- Go to your OAuth App settings
- Generate a new client secret
- Update `.env` file immediately
- Restart the application

## Security Reminders

✅ **DO:**
- Keep `.env` file local (it's in .gitignore)
- Use different credentials for dev/production
- Rotate secrets regularly

❌ **DON'T:**
- Commit `.env` to Git
- Share secrets publicly
- Use production credentials in development

## Need More Help?

- 📖 Full guide: See `GITHUB_OAUTH_SETUP.md`
- 📋 Setup instructions: See `README.md`
- 🔗 GitHub Docs: https://docs.github.com/en/developers/apps/building-oauth-apps
