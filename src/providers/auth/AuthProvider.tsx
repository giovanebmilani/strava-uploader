import React, { createContext, FC, useContext, useEffect, useState } from 'react'
import * as Helper from './_helper'
import { AuthModel } from './_models'
import { exchangeToken, refresh } from './_requests'

type AuthContextProps = {
  code: string | undefined
  saveCode: (code: string) => void
  auth: AuthModel | undefined
  saveAuth: (auth: AuthModel | undefined) => void
  logout: () => void
}

const initAuthContextPropsState = {
  code: Helper.getCode(),
  saveCode: () => {},
  auth: Helper.getAuth(),
  saveAuth: () => {},
  logout: () => {}
}

const AuthContext = createContext<AuthContextProps>(initAuthContextPropsState)

const useAuth = () => {
  return useContext(AuthContext)
}

const AuthProvider: FC = ({children}) => {
  const [code, setCode] = useState('')
  const [auth, setAuth] = useState<AuthModel | undefined>(Helper.getAuth())
 
  const saveCode = (code: string) => {
    setCode(code)
    if(code) {
      Helper.setCode(code)
    }
  }

  const saveAuth = (auth: AuthModel | undefined) => {
    setAuth(auth)
    if(auth) {
      Helper.setAuth(auth)
    } else {
      Helper.removeAuth()
    }
  }

  const logout = () => {
    saveAuth(undefined)
  }

  const value = {
    code,
    saveCode,
    auth,
    saveAuth,
    logout
  }

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  )
}

const AuthInit: FC = ({children}) => {
  const { auth, saveAuth, logout } = useAuth()

  useEffect(() => {

    const exchange = async (code: string) => {
      try {
        const { data } = await exchangeToken(code)
        if(data) {
          saveAuth(data)
        }
      } catch (error) {
        console.log('Error trying to exchange code.', error)
      }
    }

    const refreshToken = async (refreshToken: string) => {
      try {
        const { data } = await refresh(refreshToken)
        if(data) {
          saveAuth(data)
        }
      } catch (error) {
        console.log('Error trying to refresh token.', error)
      }
    }

    if (auth) {
      if(auth.expiresAt < Date.now()) {
        refreshToken(auth.refreshToken)
      }
    } else {
      // exchange code here
      logout()
    }
  }, [])

  return (
    <>{children}</>
  )
}

export { AuthProvider, AuthInit, useAuth }