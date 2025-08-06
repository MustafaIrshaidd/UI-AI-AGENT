'use client';

import { useEffect, useState } from 'react';
import { config } from '../src/config/environment';

export default function EnvironmentStatus() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    // Only show in development
    setIsVisible(config.isDevelopment);
  }, []);

  if (!isVisible) return null;

  return (
    <div className="fixed bottom-4 right-4 bg-blue-500 text-white px-3 py-2 rounded-lg shadow-lg text-sm z-50">
      <div className="flex items-center gap-2">
        <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></span>
        <span>API: {config.apiUrl.replace('http://', '').replace('https://', '')}</span>
      </div>
    </div>
  );
} 