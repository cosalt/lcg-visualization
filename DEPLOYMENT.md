# Deploying to Streamlit Community Cloud

## 📋 Prerequisites

1. A GitHub account
2. Your code pushed to a GitHub repository (already done! ✓)
3. A Streamlit Community Cloud account (free)

## 🚀 Deployment Steps

### Step 1: Sign Up for Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign up" and authenticate with your GitHub account
3. Grant Streamlit access to your repositories

### Step 2: Deploy Your App

1. Click "New app" button
2. Select your repository: `cosalt/lcg-visualization`
3. Choose branch: `main`
4. Set main file path: `app.py`
5. Click "Deploy!"

That's it! Your app will be live at: `https://[your-app-name].streamlit.app`

### Step 3: Customize Your Deployment (Optional)

In the app settings, you can:
- Set a custom subdomain
- Configure secrets (if needed)
- Adjust resource limits
- Set up auto-redeployment on push

## 🧪 Test Locally First

Before deploying, test your app locally:

```bash
# Navigate to your project directory
cd "/Users/raymartin/Linear Congruential Generator (LCG)"

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Files Required for Deployment

Your repository must contain:
- ✅ `app.py` - Your main Streamlit application
- ✅ `requirements.txt` - Python dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration (optional but recommended)
- ✅ `README.md` - Documentation (optional but nice to have)

## 🔄 Updating Your Deployed App

Once deployed, any push to your main branch will automatically redeploy your app!

```bash
# Make changes to app.py
# Then commit and push
git add .
git commit -m "Update: [describe your changes]"
git push origin main
```

Your app will automatically rebuild and redeploy (takes ~1-2 minutes).

## 🎨 App Features

Your deployed app includes:
- ✅ Interactive parameter controls (m, a, c, seed)
- ✅ Step-by-step animation of LCG calculations
- ✅ 2D pattern visualization (spectral view)
- ✅ Sequence quality analysis
- ✅ Parameter quality checks (Hull-Dobell Theorem)
- ✅ Educational content about LCGs
- ✅ Responsive design that works on mobile

## 🐛 Troubleshooting

### App Won't Start
- Check that `requirements.txt` has correct package versions
- View logs in Streamlit Cloud dashboard
- Ensure all imports are available

### Slow Performance
- Streamlit Community Cloud has resource limits
- Keep animations smooth by adjusting default speed
- Consider reducing max modulus value if needed

### Updates Not Showing
- Check GitHub to confirm push was successful
- Force redeploy from Streamlit Cloud dashboard
- Clear browser cache

## 📊 Monitoring Your App

In the Streamlit Cloud dashboard you can:
- View real-time logs
- Monitor resource usage
- See visitor analytics
- Configure domains and settings

## 🎯 Next Steps

1. Share your app URL on social media
2. Add it to your GitHub README
3. Gather feedback from users
4. Iterate and improve!

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Cloud Docs](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Forum](https://discuss.streamlit.io)

---

**Your app is ready to deploy! 🚀**

Just push these changes to GitHub and follow the deployment steps above.
