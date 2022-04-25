import React from 'react'
import { Outlet } from 'react-router-dom'
import { AuthInit } from './providers/auth/AuthProvider'

import { GlobalStyle } from './styles/GlobalStyle'

const App = () => {
  return (
    <>
      <AuthInit>
        <GlobalStyle/>
        <Outlet/>
      </AuthInit>    
    </>
  )
}

export { App }