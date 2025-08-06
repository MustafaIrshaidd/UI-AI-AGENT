'use client';

import { useState, useEffect } from 'react';
import { config, api } from '../../src/config/environment';

export default function TestConfigPage() {
  const [apiStatus, setApiStatus] = useState<string>('Testing...');
  const [corsStatus, setCorsStatus] = useState<string>('Testing...');

  useEffect(() => {
    // Test API connection
    api.healthCheck()
      .then(() => setApiStatus('✅ Connected'))
      .catch(() => setApiStatus('❌ Failed'));

    // Test CORS config
    api.corsConfig()
      .then(() => setCorsStatus('✅ Configured'))
      .catch(() => setCorsStatus('❌ Failed'));
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          🔧 Environment Configuration Test
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Environment Info */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">🌐 Environment</h2>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span className="text-gray-600">Environment:</span>
                <span className={`font-mono ${config.isDevelopment ? 'text-green-600' : 'text-blue-600'}`}>
                  {config.environment}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">API URL:</span>
                <span className="font-mono text-sm break-all">{config.apiUrl}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Node Env:</span>
                <span className="font-mono">{process.env.NODE_ENV}</span>
              </div>
            </div>
          </div>

          {/* API Status */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">📡 API Status</h2>
            <div className="space-y-2">
              <div className="flex justify-between">
                <span className="text-gray-600">Health Check:</span>
                <span className={apiStatus.includes('✅') ? 'text-green-600' : 'text-red-600'}>
                  {apiStatus}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">CORS Config:</span>
                <span className={corsStatus.includes('✅') ? 'text-green-600' : 'text-red-600'}>
                  {corsStatus}
                </span>
              </div>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">⚡ Quick Actions</h2>
            <div className="space-y-3">
              <button
                onClick={() => window.open(config.apiUrl + '/dashboard', '_blank')}
                className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition"
              >
                🚀 Open GraphQL Dashboard
              </button>
              <button
                onClick={() => window.open(config.apiUrl + '/docs', '_blank')}
                className="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-600 transition"
              >
                📚 Open API Docs
              </button>
              <button
                onClick={() => window.open('http://localhost:5050', '_blank')}
                className="w-full bg-purple-500 text-white py-2 px-4 rounded hover:bg-purple-600 transition"
              >
                🗄️ Open pgAdmin
              </button>
            </div>
          </div>

          {/* Environment Scripts */}
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">🔧 Environment Scripts</h2>
            <div className="space-y-2 text-sm">
              <div className="bg-gray-100 p-2 rounded font-mono">
                npm run env:dev
              </div>
              <div className="bg-gray-100 p-2 rounded font-mono">
                npm run env:prod
              </div>
              <div className="bg-gray-100 p-2 rounded font-mono">
                npm run env:status
              </div>
            </div>
          </div>
        </div>

        {/* Console Log */}
        <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">📋 Console Log</h2>
          <p className="text-gray-600 mb-2">
            Check your browser console for detailed environment configuration logs.
          </p>
          <div className="bg-gray-900 text-green-400 p-4 rounded font-mono text-sm">
            {`🔧 Environment Configuration: {
  apiUrl: "${config.apiUrl}",
  environment: "${config.environment}",
  isDevelopment: ${config.isDevelopment},
  isProduction: ${config.isProduction},
  nodeEnv: "${process.env.NODE_ENV}"
}`}
          </div>
        </div>
      </div>
    </div>
  );
} 