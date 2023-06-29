import "./App.css";
import { Link, Routes, Route, useLocation } from "react-router-dom";
import { Home } from "./pages/Home";
import { NotFound } from "./pages/NotFound";
import { BookRoutes } from "./routes/BookRoutes";
import { ZustandExample } from "./pages/ZustandExample/ZustandExample";

import CssBaseline from "@mui/material/CssBaseline";
import { ThemeProvider } from "@mui/material/styles";
import theme from "./theme/theme";
import SignInSide from "./pages/SignInSide/SignInSide";
import Dashboard from "./pages/Dashboard/Dashboard";

function App() {
	const location = useLocation();

	const showNav: boolean = location.pathname === "/";
	return (
		<ThemeProvider theme={theme}>
			<div>
				{/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
				<CssBaseline />
				{showNav ? (
					<nav>
						<ul>
							<li>
								<Link to='/'>Home</Link>
							</li>
							<li>
								<Link to='/books'>Books</Link>
							</li>
							<li>
								<Link to='/zustand-example'>Zustand example</Link>
							</li>
						</ul>
					</nav>
				) : null}

				<Routes>
					<Route path='/' element={<SignInSide />} />
					<Route path='/dashboard' element={<Dashboard />} />
					<Route path='/books/*' element={<BookRoutes />} />
					<Route path='/zustand-example' element={<ZustandExample />} />
					<Route path='*' element={<NotFound />} />
				</Routes>
			</div>
		</ThemeProvider>
	);
}

export default App;
