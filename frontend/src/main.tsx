import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom';
import { LogtoProvider, useHandleSignInCallback, type LogtoConfig } from '@logto/react';
import './index.css';
import App from './App.tsx';

declare global {
  interface Window {
    __APP_CONFIG__: {
      LOGTO_ENDPOINT: string;
      LOGTO_APP_ID: string;
      APP_URL: string;
      BACKEND_DOMAIN: string;
    };
  }
}

const config: LogtoConfig = {
  endpoint: window.__APP_CONFIG__.LOGTO_ENDPOINT,
  appId: window.__APP_CONFIG__.LOGTO_APP_ID,
  resources: [window.__APP_CONFIG__.BACKEND_DOMAIN],
};

function Callback() {
  const navigate = useNavigate();

  const { isLoading } = useHandleSignInCallback(() => {
    navigate('/');
  });

  if (isLoading) return <div>Redirecting...</div>;

  return null;
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <LogtoProvider config={config}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/callback" element={<Callback />} />
        </Routes>
      </BrowserRouter>
    </LogtoProvider>
  </StrictMode>,
);