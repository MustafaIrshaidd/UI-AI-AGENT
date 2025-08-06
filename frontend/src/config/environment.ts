// Environment configuration for different deployment environments

export interface EnvironmentConfig {
  apiUrl: string;
  environment: 'development' | 'production';
  isDevelopment: boolean;
  isProduction: boolean;
}

// Automatically detect environment based on hostname and NODE_ENV
const detectEnvironment = (): 'development' | 'production' => {
  if (typeof window !== 'undefined') {
    // Check hostname for localhost/development environments
    const hostname = window.location.hostname;
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
      return 'development';
    }
  }
  
  // Check NODE_ENV (Vercel sets this to 'production')
  if (process.env.NODE_ENV === 'production') {
    return 'production';
  }

  // Default to development
  return 'development';
};

// Get environment variables with fallbacks
const getEnvVar = (key: string, fallback: string): string => {
  if (typeof window !== 'undefined') {
    // Client-side: use NEXT_PUBLIC_ prefixed variables
    return (window as { __NEXT_DATA__?: { props?: { env?: Record<string, string> } } }).__NEXT_DATA__?.props?.env?.[key] || 
           process.env[`NEXT_PUBLIC_${key}`] || 
           fallback;
  }
  // Server-side: use environment variables directly
  return process.env[`NEXT_PUBLIC_${key}`] || fallback;
};

// Environment configuration
const detectedEnv = detectEnvironment();
console.log('detectedEnv :', detectedEnv);
export const config: EnvironmentConfig = {
  apiUrl: getEnvVar('API_URL', detectedEnv === 'development' ? 'http://localhost:8000' : 'https://your-backend.onrender.com'),
  environment: detectedEnv,
  isDevelopment: detectedEnv === 'development',
  isProduction: detectedEnv === 'production',
};

// Helper functions
export const getApiUrl = (): string => config.apiUrl;
export const isDevelopment = (): boolean => config.isDevelopment;
export const isProduction = (): boolean => config.isProduction;

// Enhanced logging for debugging
if (typeof window !== 'undefined') {
  console.log('🔧 Environment Configuration:', {
    apiUrl: config.apiUrl,
    environment: config.environment,
    isDevelopment: config.isDevelopment,
    isProduction: config.isProduction,
    nodeEnv: process.env.NODE_ENV,
  });
} 