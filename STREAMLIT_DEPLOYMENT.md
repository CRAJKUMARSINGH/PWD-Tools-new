# Streamlit Cloud Deployment Guide

This guide will help you deploy the PWD Tools Hub to Streamlit Community Cloud for easy access from anywhere.

## 🚀 Deployment Steps

### 1. Log in to Streamlit Cloud
1. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Click "Sign in" in the top right corner
3. Choose "Sign in with GitHub"
4. Authorize Streamlit Cloud to access your GitHub account

### 2. Create a New App
1. Once logged in, click the "New app" button
2. If this is your first time, you may need to connect your GitHub account:
   - Click "Connect to GitHub"
   - Install the Streamlit Cloud GitHub app on your account
   - Select the `CRAJKUMARSINGH/PWD-Tools-new` repository

### 3. Configure Your App
Fill in the following details:
- **Repository**: `CRAJKUMARSINGH/PWD-Tools-new`
- **Branch**: `main`
- **Main file path**: `app.py`
- **App name**: Choose a beautiful name like:
  - `pwd-tools-hub`
  - `infrastructure-management-suite`
  - `pwd-utilities`
  - `raj-pwd-tools`

### 4. Deploy
1. Click "Deploy!" button
2. Wait for the deployment to complete (usually takes 1-2 minutes)
3. Your app will be available at a URL like: `https://[your-app-name].streamlit.app`

## 🎨 Suggested Beautiful App Names

Here are some suggestions for your app name that would look great in the URL:

1. `pwd-tools-hub`
2. `infrastructure-suite`
3. `raj-pwd-utilities`
4. `pwd-management-tools`
5. `construction-tools-hub`
6. `public-works-suite`
7. `pwd-calculators`
8. `infrastructure-calculators`
9. `raj-infrastructure-tools`
10. `pwd-estimation-tools`

## ⚙️ Configuration Details

The app is already configured for Streamlit Cloud deployment:
- **Entry point**: [app.py](file://c:\Users\Rajkumar\PWD-Tools-new\app.py) (correctly set as main file)
- **Dependencies**: All listed in [requirements.txt](file://c:\Users\Rajkumar\PWD-Tools-new\requirements.txt)
- **Streamlit config**: Custom configuration in [.streamlit/config.toml](file://c:\Users\Rajkumar\PWD-Tools-new\.streamlit\config.toml)
- **Python version**: Specified in [runtime.txt](file://c:\Users\Rajkumar\PWD-Tools-new\runtime.txt)

## 🔧 Post-Deployment Configuration

After deployment, you can:

1. **Customize the URL**: In your app settings on Streamlit Cloud, you can change the app name which will update the URL

2. **Set secrets** (if needed): 
   - Go to your app dashboard
   - Click "Settings"
   - Go to "Secrets" tab
   - Add any environment variables your app might need

3. **Manage app settings**:
   - Update schedule
   - Access logs
   - Monitor usage
   - Manage permissions

## 🔄 Automatic Updates

The app will automatically redeploy when you push changes to the [main](file://c:\Users\Rajkumar\PWD-Tools-new\app.py#L29-L40) branch of your GitHub repository.

To update your app:
1. Make changes to your code
2. Commit and push to the [main](file://c:\Users\Rajkumar\PWD-Tools-new\app.py#L29-L40) branch
3. Streamlit Cloud will automatically detect the changes and redeploy

## 🔒 Security Notes

- The app is configured with appropriate security settings in [.streamlit/config.toml](file://c:\Users\Rajkumar\PWD-Tools-new\.streamlit\config.toml)
- CORS is disabled for security
- XSRF protection is configured
- File upload size is limited to 200MB

## 📞 Support

If you encounter any issues during deployment:
1. Check the build logs in your Streamlit Cloud dashboard
2. Ensure all dependencies in [requirements.txt](file://c:\Users\Rajkumar\PWD-Tools-new\requirements.txt) are correctly specified
3. Verify that [app.py](file://c:\Users\Rajkumar\PWD-Tools-new\app.py) is the correct entry point
4. Contact Streamlit support if needed