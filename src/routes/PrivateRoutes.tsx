import { Route, Routes, Navigate } from 'react-router-dom'
import { PrivateApp } from '../PrivateApp'
import { Homepage } from '../pages/home/Homepage'

const PrivateRoutes = () => {
	
	return (
		<Routes>
			<Route path='/' element={<PrivateApp/>}>
				<Route path='/' element={<Homepage />} />
			</Route>		
		</Routes>
	)
}

export { PrivateRoutes }