import axios from 'axios'
import { AuthModel } from './_models'

const EXCHANGE_TOKEN_URL = 'http://127.0.0.1:4000/auth'
const REFRESH_TOKEN_URL = 'http://127.0.0.1:4000/refresh'

export const exchangeToken = (code: string) => {
  return axios.get<AuthModel>(EXCHANGE_TOKEN_URL, {
    data: { code }
  })
} 

export const refresh = (refreshToken: string) => {
  return axios.post<AuthModel>(REFRESH_TOKEN_URL, {
    data: { refreshToken }
  })
}
