import "./App.css";
import { Link, Routes, Route, useLocation } from "react-router-dom";
import { Home } from "./pages/Home";
import { NotFound } from "./pages/NotFound";
import { BookRoutes } from "./routes/BookRoutes";
import { ZustandExample } from "./pages/ZustandExample/ZustandExample";

function App() {
	const location = useLocation();

	const showNav: boolean = location.pathname === "/";
	return (
		<div>
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
				<Route path='/' element={<Home />} />
				<Route path='/books/*' element={<BookRoutes />} />
				<Route path='/zustand-example' element={<ZustandExample />} />
				<Route path='*' element={<NotFound />} />
			</Routes>
		</div>
	);
}

export default App;
