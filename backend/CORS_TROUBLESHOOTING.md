# 🔧 CORS Troubleshooting Guide

This guide helps you resolve CORS (Cross-Origin Resource Sharing) issues in production deployment.

## 🚨 Common CORS Issues

### 1. **"Access to fetch at '...' from origin '...' has been blocked by CORS policy"**

This is the most common CORS error. It means your frontend domain is not in the backend's allowed origins.

### 2. **"No 'Access-Control-Allow-Origin' header is present"**

The backend is not sending the proper CORS headers.

### 3. **"Request header field 'content-type' is not allowed"**

The backend is not allowing the required headers.

## 🔍 Debugging Steps

### Step 1: Check Current CORS Configuration

Visit your backend's CORS config endpoint:
```
https://your-backend.onrender.com/cors-config
```

This will show you:
- Current allowed origins
- Environment variables
- CORS settings

### Step 2: Check Environment Variables

In your Render dashboard, verify these environment variables:

```bash
ENVIRONMENT=production
FRONTEND_URL=https://your-frontend-domain.com
ADDITIONAL_CORS_ORIGINS=https://another-domain.com,https://third-domain.com
```

### Step 3: Test CORS with Browser DevTools

1. Open browser DevTools (F12)
2. Go to Network tab
3. Make a request to your backend
4. Check the response headers for CORS headers

## 🛠️ Fixing CORS Issues

### Option 1: Update Environment Variables

In your Render dashboard, set the correct `FRONTEND_URL`:

```bash
FRONTEND_URL=https://your-actual-frontend-domain.com
```

### Option 2: Add Multiple Origins

Use `ADDITIONAL_CORS_ORIGINS` for multiple domains:

```bash
ADDITIONAL_CORS_ORIGINS=https://domain1.com,https://domain2.com,https://domain3.com
```

### Option 3: Update render.yaml

Add the environment variables to your `render.yaml`:

```yaml
envVars:
  - key: FRONTEND_URL
    value: https://your-frontend-domain.com
  - key: ADDITIONAL_CORS_ORIGINS
    value: https://another-domain.com,https://third-domain.com
```

## 🔧 Advanced CORS Configuration

### Development vs Production

The application automatically switches CORS configuration based on environment:

- **Development**: Allows localhost origins
- **Production**: Only allows specified production domains

### Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `ENVIRONMENT` | Environment name | `production` |
| `FRONTEND_URL` | Primary frontend URL | `https://myapp.vercel.app` |
| `ADDITIONAL_CORS_ORIGINS` | Additional allowed origins | `https://staging.myapp.com,https://admin.myapp.com` |

### CORS Headers Explained

```python
# What the backend sends:
Access-Control-Allow-Origin: https://your-frontend-domain.com
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS, PATCH
Access-Control-Allow-Headers: *
Access-Control-Max-Age: 86400
```

## 🧪 Testing CORS

### 1. Test with curl

```bash
# Test preflight request
curl -X OPTIONS \
  -H "Origin: https://your-frontend-domain.com" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type" \
  https://your-backend.onrender.com/health

# Test actual request
curl -X GET \
  -H "Origin: https://your-frontend-domain.com" \
  https://your-backend.onrender.com/health
```

### 2. Test with JavaScript

```javascript
// Test from browser console
fetch('https://your-backend.onrender.com/health', {
  method: 'GET',
  credentials: 'include',
  headers: {
    'Content-Type': 'application/json',
  }
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));
```

## 🚀 Deployment Checklist

Before deploying, ensure:

- [ ] `ENVIRONMENT=production` is set
- [ ] `FRONTEND_URL` points to your actual frontend domain
- [ ] `ADDITIONAL_CORS_ORIGINS` includes all needed domains
- [ ] Frontend is configured to use the correct backend URL
- [ ] Test CORS configuration with the `/cors-config` endpoint

## 🔍 Common Frontend Domains

### Vercel
```
https://your-app.vercel.app
https://your-app.vercel.app/
```

### Netlify
```
https://your-app.netlify.app
https://your-app.netlify.app/
```

### Custom Domain
```
https://yourdomain.com
https://www.yourdomain.com
```

## 🆘 Still Having Issues?

1. **Check Render logs** for CORS-related errors
2. **Verify domain spelling** - even a typo will cause CORS to fail
3. **Test with different browsers** - some browsers handle CORS differently
4. **Check for redirects** - redirects can cause CORS issues
5. **Verify HTTPS** - mixed HTTP/HTTPS can cause issues

## 📞 Getting Help

If you're still experiencing CORS issues:

1. Check the `/cors-config` endpoint output
2. Review Render deployment logs
3. Test with the provided curl commands
4. Verify all environment variables are set correctly 