"use client";
import { useEffect, useState } from "react";
import { api } from '../../src/lib/api';

interface ApiResponse {
  message: string;
  graphql_playground: string;
  health_check: string;
}

export default function HomeTest() {
  const [data, setData] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Use api.get with just the endpoint - the base URL is handled automatically
        const result = await api.get<ApiResponse>('/');
        setData(result);
      } catch (err) {
        setError(err instanceof Error ? err : new Error('Unknown error'));
        console.error('API Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>Data from API:</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
