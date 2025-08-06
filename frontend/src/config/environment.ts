// Environment configuration for different deployment environments

export interface EnvironmentConfig {
  apiUrl: string;
  environment: 'development' | 'production';
  isDevelopment: boolean;
  isProduction: boolean;
}

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
export const config: EnvironmentConfig = {
  apiUrl: getEnvVar('API_URL', 'http://localhost:8000'),
  environment: (getEnvVar('ENVIRONMENT', 'development') as 'development' | 'production'),
  isDevelopment: getEnvVar('ENVIRONMENT', 'development') === 'development',
  isProduction: getEnvVar('ENVIRONMENT', 'development') === 'production',
};

// Helper functions
export const getApiUrl = (): string => config.apiUrl;
export const isDevelopment = (): boolean => config.isDevelopment;
export const isProduction = (): boolean => config.isProduction;

// Log configuration in development
if (typeof window !== 'undefined' && config.isDevelopment) {
  console.log('🔧 Environment Configuration:', config);
} 