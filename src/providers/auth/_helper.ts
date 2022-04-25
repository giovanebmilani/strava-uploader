import { AuthModel } from './_models'

const CODE_LOCAL_STORAGE_KEY = 'strava-app-code'
const AUTH_LOCAL_STORAGE_KEY = 'strava-auth'

const getCode = (): string | undefined => {
  if(!localStorage) {
    return
  }

  const code: string | null = localStorage.getItem(CODE_LOCAL_STORAGE_KEY)
  if(code) {
    return code
  }
}

const setCode = (code: string) => {
  if(!localStorage) {
    return
  }

  try {
    localStorage.setItem(CODE_LOCAL_STORAGE_KEY, code)
  } catch (error) {
    console.log('Error trying to save code at local storage.', error)
  }
}

const getAuth = (): AuthModel | undefined => {
  if(!localStorage) {
    return
  }

  const ls: string | null = localStorage.getItem(AUTH_LOCAL_STORAGE_KEY)
  if(!ls) {
    return
  }

  try {
    const auth: AuthModel = JSON.parse(ls) as AuthModel
    if(auth) {
      return auth
      // const expiresAt = new Date(auth.expiresAt)
      // if(expiresAt > new Date()) {
      //   return auth
      // }
    }
  } catch (error) {
    console.log('Error trying to parse the local storage auth.', error)
  }
}

const setAuth = (auth: AuthModel | undefined) => {
  if (!localStorage) {
    return
  }

  try {
    const ls = JSON.stringify(auth)
    localStorage.setItem(AUTH_LOCAL_STORAGE_KEY, ls)
  } catch (error) {
    console.log('Error trying to save auth at local storage.', error)
  }
}

const removeAuth = () => {
  if(!localStorage) {
    return
  }

  try {
    localStorage.removeItem(AUTH_LOCAL_STORAGE_KEY)
  } catch (error) {
    console.log('Error trying to remove auth at local storage.', error)
  }
}

export { getAuth, setAuth, removeAuth, getCode, setCode }
