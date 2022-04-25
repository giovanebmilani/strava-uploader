import { Routes, Route, HashRouter } from 'react-router-dom'
import { PrivateRoutes } from './PrivateRoutes'
import { App } from '../App'
import { AuthPage } from '../pages/auth/AuthPage'
import { useAuth } from '../providers/auth/AuthProvider'


const AppRoutes = () => {
	const { auth } = useAuth()

	return (
		<HashRouter>
			<Routes>
				<Route path='/' element={<App/>}>
					{auth ? (
						<>
							<Route path='/' element={<PrivateRoutes/>}/>
						</>
					) : (
						<>
							<Route path='/' element={<AuthPage/>}/>
							<Route path='/code' />
						</>
					)}
				</Route>
			</Routes>
		</HashRouter>
	)
}

export { AppRoutes }