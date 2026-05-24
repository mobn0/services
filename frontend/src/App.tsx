import { useLogto } from '@logto/react';
import reactLogo from './assets/react.svg';
import viteLogo from './assets/vite.svg';
import heroImg from './assets/hero.png';
import './App.css';



function App() {
  const { signIn, signOut, isAuthenticated, getAccessToken } = useLogto();
  const appUrl = window.__APP_CONFIG__.APP_URL;
  async function showApiToken() {
    const token = await getAccessToken(window.__APP_CONFIG__.BACKEND_DOMAIN);
    console.log(token);
  }
  console.log(window.__APP_CONFIG__.BACKEND_DOMAIN);
  return (
    <>
      <section id="center">
        <div className="hero">
          <img src={heroImg} className="base" width="170" height="179" alt="" />
          <img src={reactLogo} className="framework" alt="React logo" />
          <img src={viteLogo} className="vite" alt="Vite logo" />
        </div>

        <div>
          <h1>{isAuthenticated ? 'Signed in' : 'Get started'}</h1>
          <p>
            {isAuthenticated
              ? 'You are logged in with Logto.'
              : 'Sign in to continue.'}
          </p>
        </div>

        <div>
          {isAuthenticated
            ? <button type="button" onClick={showApiToken}>
              Show API token
            </button>
            : ""}
        </div>

        {isAuthenticated ? (
          <button
            type="button"
            className="counter"
            onClick={() => signOut(appUrl)}
          >
            Sign out
          </button>
        ) : (
          <button
            type="button"
            className="counter"
            onClick={() => signIn(`${appUrl}/callback`)}
          >
            Sign in
          </button>
        )}
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  );
}

export default App;