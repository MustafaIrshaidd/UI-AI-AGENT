# UI AI Agent Frontend

This is a [Next.js](https://nextjs.org/) frontend application for the UI AI Agent project.

## 🚀 Quick Start

### 1. Environment Setup

Run the setup script to configure your environment:

```bash
./scripts/setup-env.sh
```

Or manually create a `.env.local` file:

```bash
# Local Development
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ENVIRONMENT=development
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## 🌍 Environment Configuration

The frontend automatically switches between local and production environments based on your configuration:

- **Development**: Uses `http://localhost:8000` for backend API
- **Production**: Uses your deployed backend URL (e.g., `https://your-backend.onrender.com`)

### Environment Variables

| Variable | Description | Development | Production |
|----------|-------------|-------------|------------|
| `NEXT_PUBLIC_API_URL` | Backend API URL | `http://localhost:8000` | `https://your-backend.onrender.com` |
| `NEXT_PUBLIC_ENVIRONMENT` | Environment name | `development` | `production` |

## 🔧 API Integration

The frontend includes a built-in API client that:

- Automatically uses the correct backend URL based on environment
- Handles CORS configuration
- Provides health check and configuration endpoints
- Supports GraphQL queries

### Usage Example

```typescript
import { api } from '@/src/lib/api';

// Health check
const health = await api.healthCheck();

// GraphQL query
const data = await api.graphql(`
  query {
    yourQuery {
      field
    }
  }
`);
```

## 🧪 Testing

The application includes an API Test component that:

- Shows current environment configuration
- Tests API connectivity
- Displays CORS configuration
- Provides debugging information

## 📦 Build and Deploy

### Build for Production

```bash
npm run build
```

### Deploy to Vercel

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Set environment variables in Vercel dashboard:
   - `NEXT_PUBLIC_API_URL`: Your production backend URL
   - `NEXT_PUBLIC_ENVIRONMENT`: `production`

### Deploy to Other Platforms

Set the same environment variables in your deployment platform. See `ENVIRONMENT_SETUP.md` for detailed instructions.

## 📁 Project Structure

```
frontend/
├── app/                    # Next.js app directory
├── components/             # React components
│   ├── ApiTest/           # API testing component
│   └── HomeTest/          # Home page component
├── src/
│   ├── config/            # Environment configuration
│   └── lib/               # Utility libraries
│       └── api.ts         # API client
├── scripts/               # Setup scripts
└── ENVIRONMENT_SETUP.md   # Detailed setup guide
```

## 🔍 Troubleshooting

### CORS Issues

1. Check that your frontend URL is in the backend's allowed origins
2. Verify environment variables are set correctly
3. Restart both frontend and backend after changing environment variables

### API Connection Issues

1. Verify the API URL is correct
2. Check that the backend is running
3. Use the API Test component to debug configuration

## 📚 Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [Environment Setup Guide](./ENVIRONMENT_SETUP.md)
- [API Client Documentation](./src/lib/api.ts)
