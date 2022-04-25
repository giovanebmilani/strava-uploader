import React from 'react'
import { useAuth } from '../../providers/auth/AuthProvider'

const STRAVA_AUTH_URL = 'https://www.strava.com/oauth/authorize?client_id=69535&response_type=code&redirect_uri=http://localhost:9000/code&approval_prompt=force&scope=read'

const AuthPage = () => {
  const { saveCode } = useAuth()

  const stravaAuth = () => {
    window.open(STRAVA_AUTH_URL);
  }

  return (
    <>
      <h1>Authenticate</h1>
      <button onClick={stravaAuth} >Authenticate</button>
    </>
  )
}

export { AuthPage }