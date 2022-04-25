import React from 'react'
import { Outlet } from 'react-router-dom'

import { GlobalStyle } from './styles/GlobalStyle'

const PrivateApp = () => {
  return (
    <>
      <GlobalStyle/>
      <Outlet/>
    </>
  )
}

export { PrivateApp }