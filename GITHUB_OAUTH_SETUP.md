# GitHub OAuth Setup Guide

This guide will walk you through creating GitHub OAuth App credentials for the Odoo Partner Agent.

## What You'll Get

After completing this guide, you'll have:
- **Client ID**: Starts with `Iv1.` (e.g., `Iv1.1234567890abcdef`)
- **Client Secret**: A secret token for authenticating your application

## Step-by-Step Instructions

### 1. Access GitHub Developer Settings

1. Go to [GitHub.com](https://github.com)
2. Log in to your account
3. Click on your **profile picture** in the top-right corner
4. Select **Settings** from the dropdown menu
5. Scroll down the left sidebar to find **Developer settings** (near the bottom)
6. Click on **Developer settings**

### 2. Create a New OAuth App

1. In the Developer settings, click on **OAuth Apps** in the left sidebar
2. Click the **New OAuth App** button (or **Register a new application**)

### 3. Fill Out the Application Form

Provide the following information:

| Field | Value | Description |
|-------|-------|-------------|
| **Application name** | `Odoo Partner Agent` | The name users will see when authorizing |
| **Homepage URL** | `http://localhost:8069` | Your application's homepage (use localhost for development) |
| **Application description** | `Autonomous Odoo Partner Agent` | Optional description of your app |
| **Authorization callback URL** | `http://localhost:8069/auth/callback` | Where GitHub redirects after authorization |

**For Production:**
- Replace `http://localhost:8069` with your actual domain (e.g., `https://yourdomain.com`)
- Update the callback URL accordingly (e.g., `https://yourdomain.com/auth/callback`)

### 4. Register Your Application

1. Review the information you've entered
2. Click the **Register application** button
3. You'll be redirected to your new OAuth App's page

### 5. Get Your Client ID

On the OAuth App page, you'll immediately see:
- **Client ID**: This starts with `Iv1.` followed by alphanumeric characters
- Copy this value - you'll need it for your `.env` file

**Example Client ID:**
```
Iv1.1234567890abcdef
```

### 6. Generate a Client Secret

1. On the same OAuth App page, look for the **Client secrets** section
2. Click **Generate a new client secret**
3. GitHub will display your client secret **once**
4. **⚠️ CRITICAL:** Copy the secret immediately! You won't be able to see it again.

**Example Client Secret:**
```
1234567890abcdefghijklmnopqrstuvwxyzABCD
```

Note: GitHub OAuth App Client Secrets are random alphanumeric strings. They're different from Personal Access Tokens (which start with `ghp_`).

If you lose the secret, you'll need to generate a new one.

### 7. Configure Your Application

1. Navigate to your project directory:
   ```bash
   cd /path/to/odoo-partner-agent
   ```

2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

3. Edit the `.env` file:
   ```bash
   nano .env   # or use your preferred editor
   ```

4. Update the GitHub OAuth credentials:
   ```
   GITHUB_CLIENT_ID=Iv1.your-actual-client-id-here
   GITHUB_CLIENT_SECRET=your-actual-client-secret-here
   ```

5. Save the file

### 8. Verify Your Configuration

1. Make sure your `.env` file is in the project root directory
2. Ensure `.env` is listed in `.gitignore` (it should be by default)
3. **Never commit the `.env` file** to version control

### 9. Test Your Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   streamlit run app.py
   ```

3. The app should show "✅ GitHub OAuth is configured" if everything is set up correctly

## Security Best Practices

### Do's ✅
- Keep your Client Secret private and secure
- Use environment variables for credentials (never hardcode them)
- Add `.env` to `.gitignore`
- Rotate secrets regularly
- Use different OAuth Apps for development and production

### Don'ts ❌
- Never commit credentials to Git
- Don't share your Client Secret in public forums, issues, or documentation
- Don't use production credentials in development
- Don't expose your `.env` file publicly

## Updating Your OAuth App

If you need to change settings later:

1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Click on **OAuth Apps**
3. Select your application
4. Update the necessary fields
5. Click **Update application**

## Regenerating a Client Secret

If your secret is compromised:

1. Go to your OAuth App settings
2. Under **Client secrets**, click **Regenerate client secret**
3. Confirm the regeneration
4. Copy the new secret immediately
5. Update your `.env` file with the new secret
6. Restart your application

## Troubleshooting

### "GitHub OAuth is not configured" Warning

**Cause:** The app can't find your credentials.

**Solutions:**
- Verify `.env` file exists in the project root
- Check that credentials are correctly formatted
- Ensure there are no quotes around the values
- Restart the application after updating `.env`

### "Invalid client" Error

**Cause:** Client ID or Secret is incorrect.

**Solutions:**
- Double-check you copied the full Client ID and Secret
- Verify there are no extra spaces or characters
- Ensure you're using the correct OAuth App credentials
- Regenerate the client secret if needed

### Callback URL Mismatch

**Cause:** The redirect URL doesn't match the registered callback URL.

**Solutions:**
- Verify the callback URL in GitHub matches exactly
- Check for http vs https mismatch
- Ensure port numbers match (e.g., :8069)

## Additional Resources

- [GitHub OAuth Apps Documentation](https://docs.github.com/en/developers/apps/building-oauth-apps)
- [GitHub OAuth Flow](https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps)
- [Best Practices for OAuth Apps](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps#best-practices-for-creating-an-oauth-app)

## Support

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review the README.md file
3. Check GitHub's OAuth documentation
4. Open an issue in the repository

---

**Last Updated:** 2026-01-18
